import time
import logging
import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Configura o logger para exibir mensagens de INFO ou superior
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class InstagramScraper:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = self._setup_driver()

    def _setup_driver(self):
        """Configura e inicializa o WebDriver do Chrome."""
        options = Options()
        # options.add_argument("--headless") # Descomente caso queira executar sem interface gráfica
        options.add_argument("--disable-gpu") # Desativa o uso da GPU para evitar possíveis problemas de renderização
        options.add_argument("--window-size=1920,1080") # Define o tamanho da janela do navegador para 1920x1080
        options.add_argument("--no-sandbox") # Desativa o modo sandbox para evitar restrições de execução (necessário em alguns ambientes)
        options.add_argument("--disable-dev-shm-usage") # Impede o uso de /dev/shm, útil para evitar erros em ambientes com pouca memória compartilhada
        
        service = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=options)

    def _login(self):
        """Realiza login no Instagram."""
        logging.info("🔑 Acessando página de login...")
        self.driver.get("https://www.instagram.com/accounts/login/")

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(self.username)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(self.password)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
            time.sleep(5)

            if "login" in self.driver.current_url:
                logging.error("❌ Falha no login. Verifique suas credenciais.")
                self.driver.quit()
                return

            self.driver.refresh()
            time.sleep(3)
            self._fechar_popups()

            logging.info("✅ Login realizado com sucesso.")

        except Exception as e:
            logging.error(f"❌ Erro ao tentar fazer login: {e}")
            self.driver.quit()
            raise

    def _fechar_popups(self):
        """Fecha pop-ups que aparecem após o login."""
        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Agora não')]"))
            ).click()
            logging.info("🔄 Pop-up fechado.")
        except Exception:
            logging.info("⚠️ Nenhum pop-up para fechar.")

    def _acessar_lista(self, tipo):
        """Acessa a lista de seguidores ou de quem o usuário está seguindo."""
        perfil_url = f"https://www.instagram.com/{self.username}/"
        self.driver.get(perfil_url)
        logging.info(f"📌 Acessando perfil: {perfil_url}")

        xpath = "//a[contains(@href, '/followers/')]" if tipo == "followers" else "//a[contains(@href, '/following/')]"

        try:
            botao_lista = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            botao_lista.click()
            logging.info(f"📂 Abrindo lista de {tipo}...")
        except Exception as e:
            logging.error(f"❌ Não foi possível abrir a lista de {tipo}: {e}")
            self.driver.quit()
            raise

    def _rolar_modal(self):
        """Rola o modal de seguidores/seguidos para carregar todos os itens."""
        logging.info("⏳ Rolando a lista...")
        modal_xpath = "//div[contains(@class, 'xyi19xy x1ccrb07 xtf3nb5 x1pc53ja x1lliihq x1iyjqo2 xs83m0k xz65tgg x1rife3k x1n2onr6')]"

        try:
            modal = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, modal_xpath))
            )
        except Exception as e:
            logging.error(f"❌ Modal não encontrado: {e}")
            self.driver.quit()
            raise

        last_height = self.driver.execute_script("return arguments[0].scrollHeight", modal)
        tentativas = 0

        while tentativas < 3:
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)
            new_height = self.driver.execute_script("return arguments[0].scrollHeight", modal)

            if new_height == last_height:
                tentativas += 1
            else:
                tentativas = 0
                last_height = new_height

            logging.info("🔄 Rolando para carregar mais itens...")

        logging.info("✅ Rolagem concluída.")

    def _obter_lista(self):
        """Obtém a lista de usuários carregada no modal."""
        lista_xpath = "//div[contains(@class, 'x1dm5mii x16mil14 xiojian x1yutycm x1lliihq x193iq5w xh8yej3')]"
        time.sleep(2)

        elementos = self.driver.find_elements(By.XPATH, lista_xpath)

        lista = set()
        for el in elementos:
            partes = el.text.strip().split("\n")
            if partes:
                lista.add(partes[0])

        return list(lista)

    def _capturar_lista(self, tipo):
        """Captura a lista completa de seguidores ou seguidos."""
        self._acessar_lista(tipo)
        self._rolar_modal()
        return self._obter_lista()

    def _comparar_listas(self, seguidores, seguindo):
        """Compara listas para encontrar quem não segue de volta."""
        return sorted([user for user in seguindo if user not in seguidores])

    def _salvar_resultados(self, lista):
        """Salva os usuários que não seguem de volta em um arquivo."""
        with open("nao_seguem_de_volta.txt", "w", encoding="utf-8") as f:
            for user in lista:
                f.write(user + "\n")
        logging.info("📝 Resultados salvos em 'nao_seguem_de_volta.txt'.")

    def executar(self):
        """Executa todo o processo de análise."""
        try:
            self._login()

            seguidores = self._capturar_lista("followers")
            seguindo = self._capturar_lista("following")
            nao_seguem_de_volta = self._comparar_listas(seguidores, seguindo)

            logging.info("\n📊 Resumo da análise:")
            logging.info(f"👥 Seguidores: {len(seguidores)}")
            logging.info(f"➡️ Seguindo: {len(seguindo)}")
            logging.info(f"❌ Não seguem de volta: {len(nao_seguem_de_volta)}\n")

            self._salvar_resultados(nao_seguem_de_volta)

            return seguidores, seguindo, nao_seguem_de_volta

        finally:
            self.driver.quit()
            logging.info("🛑 Navegador fechado.")

def obter_credenciais():
    """Solicita as credenciais ao usuário."""
    username = input("Usuário: ")
    password = getpass.getpass("Senha: ")
    return username, password

if __name__ == "__main__":
    print("📥 Informe suas credenciais do Instagram")
    username, password = obter_credenciais()
    scraper = InstagramScraper(username, password)
    scraper.executar()
