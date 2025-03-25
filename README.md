# 📸 Instagram Scraper

Este projeto é um **Web Scraper** para o **Instagram** que coleta a lista de seguidores e seguidos de um usuário, identifica quem não segue de volta e apresenta um resumo da análise. Ele utiliza a biblioteca **Selenium** para automação do navegador. O script foi desenvolvido para fins educativos e visa demonstrar como utilizar o **Selenium** para coleta de dados.

---

## 📌 Funcionalidades

✅ **Login Automático** no Instagram.  
✅ **Captura de Lista** de seguidores e seguidos.  
✅ **Rolagem Automática** para carregar todos os itens.  
✅ **Identificação de usuários** que não seguem de volta.  
✅ **Mensagens de Log** detalhadas para acompanhamento.

### Customização:
Este script foi projetado para ser fácil de customizar. Se você deseja coletar outras informações além de seguidores e seguidos (como postagens, curtidas, comentários, etc.), o código pode ser facilmente modificado para acessar essas informações. Basta alterar a função **acessar_lista()** ou adicionar novas funções para capturar diferentes elementos na página do Instagram.

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

### 1️⃣ Configurar Usuário e Senha

Abra o notebook `.ipynb` e altere as variáveis `USERNAME` e `PASSWORD` com suas credenciais do Instagram:

```python
USERNAME = "seu_username_aqui" 
PASSWORD = "sua_senha_aqui"
```

**Aviso de segurança:** 

Evite deixar sua senha em texto simples no código. Para uma abordagem mais segura, você pode armazenar a senha em uma variável de ambiente. Por exemplo:

```bash
export INSTAGRAM_PASSWORD="sua_senha_aqui"
```

No código Python, você pode acessar a variável de ambiente usando:

```python
import os
PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
```

### 2️⃣ Executar o Script

No Jupyter Notebook, execute as células do código sequencialmente. A execução será feita em partes. O código irá:
1. Fazer login no Instagram.
2. Capturar a lista de seguidores e seguidos.
3. Identificar usuários que não seguem de volta.
4. Exibir um resumo no console.

---

## 🛠 Tecnologias Utilizadas

- **Python**
- **Selenium**
- **WebDriver Manager**
- **Logging**

---

## 📜 Estrutura do Código

### 📂 **InstagramScraper Class**

- 📌 `__init__()` → Inicializa o WebDriver e define as credenciais do usuário
- 📌 `_setup_driver()` → Configura e retorna uma instância do WebDriver do Chrome
- 📌 `login()` → Realiza login no Instagram 
- 📌 `fechar_popups()` → Fecha pop-ups desnecessários  
- 📌 `acessar_lista()` → Acessa seguidores ou seguidos do perfil do usuário 
- 📌 `rolar_modal()` → Rola a lista até carregar todos os itens 
- 📌 `obter_lista()` → Extrai os nomes da lista  
- 📌 `executar()` → Executa todas as etapas

---

## ⚠️ Observações

🔹 O Instagram pode bloquear automações repetidas, então use com moderação.  
🔹 Considere rodar o script em um ambiente seguro e com conta de testes.  
🔹 O script pode parar de funcionar se o Instagram alterar sua estrutura.

---

## 📢 Contribuição

Sinta-se à vontade para contribuir! Faça um **fork** do repositório, crie um **branch** com suas alterações e envie um **pull request**.  

---

🔗 **Desenvolvido por [Everton Fernandes](https://github.com/fernandes-everton)**
