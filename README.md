# 📸 Instagram Scraper

Este projeto é um **Web Scraper** para o **Instagram** que coleta a lista de seguidores e seguidos de um usuário, identifica quem não segue de volta e apresenta um resumo da análise. Ele utiliza a biblioteca **Selenium** para automação do navegador. O script foi desenvolvido para fins educativos e visa demonstrar como utilizar o **Selenium** para coleta de dados.

---

## 📌 Funcionalidades

✅ **Login Automático** no Instagram.  
✅ **Captura de Lista** de seguidores e seguidos.  
✅ **Rolagem Automática** para carregar todos os itens.  
✅ **Identificação de Usuários** que não seguem de volta.  
✅ **Mensagens de Log** detalhadas para acompanhamento.     
✅ **Execução via Terminal** com entrada segura de credenciais.

### Customização:
Este script foi projetado para ser fácil de customizar. Se você deseja coletar outras informações além de seguidores e seguidos (como postagens, curtidas, comentários, etc.), o código pode ser facilmente modificado para acessar essas informações. Basta alterar a função **_acessar_lista()** ou adicionar novas funções para capturar diferentes elementos na página do Instagram.

---

## ⚙️ Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/fernandes-everton/ig-analyzer.git
    cd ig-analyzer
    ```

2. Instale as dependências:
    ```bash
    pip install selenium
    pip install webdriver-manager
    ```

---

## 🚀 Como Usar

### 1️⃣ Executar o Script

Execute o script `.py` diretamente pelo terminal:

```bash
python instagram_scraper.py
```
Você será solicitado a informar seu **usuário** e **senha** diretamente no terminal.    
    **Nota de segurança:** A senha é solicitada de forma segura (não aparece na tela enquanto você digita).

### 2️⃣ Processo

O script irá automaticamente:
1. Fazer login no Instagram.
2. Capturar a lista de seguidores e seguidos.
3. Identificar usuários que não seguem de volta.
4. Gerar um arquivo chamado `nao_seguem_de_volta.txt` com o resultado.
5. Exibir um resumo da análise no terminal.

---

## 🛠 Tecnologias Utilizadas

- **Python**
- **Selenium**
- **WebDriver Manager**
- **Logging**

---

## 📜 Estrutura do Código

### 📂 **InstagramScraper Class**

- 📌 `__init__()` → Inicializa o WebDriver e define as credenciais do usuário.
- 📌 `_setup_driver()` → Configura o navegador Chrome para a automação.
- 📌 `_login()` → Realiza login no Instagram.
- 📌 `_fechar_popups()` → Fecha pop-ups iniciais.
- 📌 `_acessar_lista(tipo)` → Abre a lista de seguidores ou seguidos. 
- 📌 `_rolar_modal()` → Rola o modal para carregar todos os usuários.
- 📌 `_obter_lista()` → Extrai os nomes dos usuários carregados.
- 📌 `_capturar_lista(tipo)` → Captura a lista completa conforme o tipo. 
- 📌 `_comparar_listas(seguidores, seguindo)` → Identifica quem não segue de volta.
- 📌 `_salvar_resultados(lista)` → Salva os resultados em um arquivo `.txt`.
- 📌 `executar()` → Executa todo o processo de login, coleta, análise e salvamento.

---

## ⚠️ Avisos Importantes

🔹 Este projeto é apenas para fins educativos.  
🔹 Automação em redes sociais pode violar os termos de uso da plataforma. Use com responsabilidade.     
🔹 Evite executar o script repetidamente em um curto intervalo para não ser bloqueado pelo Instagram.   
🔹 O script pode parar de funcionar se o Instagram alterar sua estrutura.

---

## 📢 Contribuição

Sinta-se à vontade para contribuir! Faça um **fork** do repositório, crie um **branch** com suas alterações e envie um **pull request**.  

---

🔗 **Desenvolvido por [Everton Fernandes](https://github.com/fernandes-everton)**
