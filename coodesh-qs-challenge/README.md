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
   pip install -r requirements.txt
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

**Ferramentas analisadas:**

- **Selenium WebDriver (Escolhida):**
  - **Vantagens:** Open source, suporta múltiplos navegadores, integração com várias linguagens, grande comunidade, flexível para automação web realista.
  - **Desvantagens:** Scripts podem ser mais verbosos, manutenção pode ser trabalhosa em aplicações muito dinâmicas.

- **Ghost Inspector:**
  - **Vantagens:** Interface amigável, fácil de criar testes sem código, integração com CI/CD.
  - **Desvantagens:** É uma ferramenta paga para uso avançado, menos flexível para customizações complexas, dependência de nuvem.

- **Cypress:**
  - **Vantagens:** Muito rápido, fácil de configurar, ótima experiência para testes front-end, excelente para aplicações modernas.
  - **Desvantagens:** Suporte limitado a navegadores (principalmente Chrome/Edge), não suporta múltiplas abas/janelas facilmente, não cobre todos os cenários de automação web.

- **Robot Framework:**
  - **Vantagens:** Sintaxe simples baseada em palavras-chave, fácil de ler e escrever, integração com Selenium.
  - **Desvantagens:** Menos flexível para fluxos complexos, depende de bibliotecas externas para automação web, pode ser mais difícil de debugar.

- **Cucumber (Behave para Python):**
  - **Vantagens:** Permite escrita de cenários em linguagem natural (Gherkin), facilita comunicação entre áreas técnicas e de negócio, integração com várias linguagens.
  - **Desvantagens:** Exige estruturação de arquivos .feature e steps, pode ser mais trabalhoso para fluxos simples.

**Por que escolhi Selenium?**
- Permite automação realista e flexível, cobrindo todos os requisitos do desafio.
- Suporta diferentes navegadores e sistemas operacionais.
- Possui grande comunidade e documentação.
- Integra-se facilmente com Python, facilitando a manutenção e evolução dos testes.

## Exemplos para outras ferramentas

O início do arquivo `automacao_magento.py` contém exemplos de como rodar o mesmo fluxo com Robot Framework e Cucumber (Behave para Python).

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
