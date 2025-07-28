# Magento Automation Challenge

Automação de testes caixa preta para o site [Magento Demo](https://magento.softwaretestingboard.com).

## Descrição

Este projeto realiza testes automatizados de fluxo de compra, busca, cadastro e comentários em produtos no Magento Demo, utilizando Selenium WebDriver e Python.

## Tecnologias Utilizadas

- Python 3.x
- Selenium WebDriver
- ChromeDriver

## Como instalar e usar

1. **Clone o repositório**  
   Faça o download ou clone este repositório.

2. **Instale as dependências**  
   No terminal, execute:
   ```
   pip install selenium
   ```

3. **Baixe o ChromeDriver**  
   Baixe o ChromeDriver compatível com a versão do seu navegador Chrome e coloque-o no PATH do sistema ou na mesma pasta do script.

4. **Execute o script**  
   No terminal, execute:
   ```
   python automacao_magento.py
   ```

5. **Siga as instruções do terminal**  
   Algumas etapas (como cadastro e checkout) exigem interação manual devido ao captcha e segurança do site.

## Justificativa da Ferramenta

**Ferramenta escolhida:** Selenium WebDriver

**Por que Selenium?**
- Suporta múltiplos navegadores e sistemas operacionais.
- Permite automação realista, simulando ações de um usuário.
- Ampla documentação e comunidade ativa.
- Fácil integração com Python e outras linguagens.

**Vantagens sobre outras ferramentas:**
- Cypress: Muito bom para front-end, mas limitado a Chrome/Electron e não suporta múltiplas abas facilmente.
- Playwright: Poderoso e moderno, mas menos maduro e com comunidade menor que Selenium.
- Puppeteer: Focado em Chrome/Chromium, menos flexível para outros navegadores.

## .gitignore sugerido

```
__pycache__/
*.pyc
chromedriver.exe
.env
dist/
build/
relatorio_teste.txt
```

## Challenge

Challenge by coodesh.
