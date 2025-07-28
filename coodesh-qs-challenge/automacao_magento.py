# Para rodar este fluxo com Robot Framework:
# 1. Instale o Robot Framework e a biblioteca SeleniumLibrary:
#    pip install robotframework robotframework-seleniumlibrary
#
# 2. Exemplo de estrutura de um teste Robot Framework para este fluxo:
#
# *** Settings ***
# Library    SeleniumLibrary
#
# *** Variables ***
# ${URL}    https://magento.softwaretestingboard.com
#
# *** Test Cases ***
# Fluxo Completo Magento
#     Open Browser    ${URL}    chrome
#     Maximize Browser Window
#     # Pausa para cadastro manual
#     Pause Execution    Crie a conta manualmente e clique em OK para continuar.
#     Input Text    id=search    shirt
#     # Aguarde sugestões e clique no último, ou submeta a busca
#     # (Robot Framework não tem suporte nativo para sugestões dinâmicas, pode ser necessário customizar)
#     Press Keys    id=search    RETURN
#     Wait Until Page Contains Element    class=products
#     Click Element    css=.product-item-link
#     # Se necessário, selecione tamanho/cor
#     # Click Element    xpath=//div[@option-label='S']
#     # Click Element    xpath=//div[contains(@option-label, 'Blue')]
#     Click Button    id=product-addtocart-button
#     # Tentar adicionar review (pode ser customizado)
#     # Click Element    xpath=//a[contains(@href, '#reviews')]
#     # Input Text    id=nickname_field    TestUser
#     # Input Text    id=summary_field     Ótimo produto!
#     # Input Text    id=review_field      Produto testado via automação. Recomendo!
#     # Click Element    css=.review-control-vote label:last-child
#     # Click Button    css=button.action.submit.primary
#     Click Element    css=.showcart
#     Click Button    id=top-cart-btn-checkout
#     Pause Execution    Complete o checkout manualmente e clique em OK para finalizar.
#     Close Browser
#
# 3. Salve o fluxo acima em um arquivo .robot e execute com:
#    robot nome_do_arquivo.robot
#
# Para rodar este fluxo com Cucumber (Behave para Python):
# 1. Instale o Behave e Selenium:
#    pip install behave selenium
#
# 2. Exemplo de estrutura de um teste Behave (Cucumber) para este fluxo:
#
# features/magento.feature
# ---------------------------------
# Feature: Fluxo completo no Magento Demo
#   Scenario: Usuário realiza busca, adiciona produto ao carrinho e faz checkout
#     Given que estou na home do Magento Demo
#     And crio uma conta manualmente
#     When busco por "shirt" e clico no último resultado sugerido
#     And seleciono um produto aleatório e adiciono ao carrinho
#     And tento adicionar um comentário/review
#     Then inicio o checkout
#
# features/steps/magento_steps.py
# ---------------------------------
# from behave import given, when, then
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import random, time
#
# @given('que estou na home do Magento Demo')
# def step_impl(context):
#     context.driver = webdriver.Chrome()
#     context.wait = WebDriverWait(context.driver, 10)
#     context.driver.get("https://magento.softwaretestingboard.com")
#
# @given('crio uma conta manualmente')
# def step_impl(context):
#     print("Crie a conta manualmente e pressione Enter...")
#     input()
#
# @when('busco por "shirt" e clico no último resultado sugerido')
# def step_impl(context):
#     # ...similar ao Python...
#
# @when('seleciono um produto aleatório e adiciono ao carrinho')
# def step_impl(context):
#     # ...similar ao Python...
#
# @when('tento adicionar um comentário/review')
# def step_impl(context):
#     # ...similar ao Python...
#
# @then('inicio o checkout')
# def step_impl(context):
#     # ...similar ao Python...
#
# 3. Execute com:
#    behave
#
# Observação: O Behave usa arquivos .feature para descrever cenários e arquivos Python para implementar os passos.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import sys

def iniciar_driver():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    return driver, wait

def acessar_home(driver, wait, report):
    driver.get("https://magento.softwaretestingboard.com")
    try:
        assert driver.find_element(By.ID, "store.menu")
        print("Home page carregada com sucesso.")
        report.append("Home page carregada com sucesso.")
    except Exception as e:
        print("Erro ao carregar home page:", e)
        report.append("Erro ao carregar home page.")
        driver.quit()
        sys.exit(1)

def criar_conta_manual():
    print("Acesse a tela de cadastro (clique em 'Create an Account').")
    print("Preencha os dados fictícios do https://randomuser.me e resolva o captcha manualmente.")
    input("Após criar a conta e estar logado, pressione Enter para continuar...")

def buscar_produto(wait, report, termo="shirt"):
    search = wait.until(EC.presence_of_element_located((By.ID, "search")))
    search.clear()
    search.send_keys(termo)
    try:
        suggestions = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".autocomplete-suggestions li")))
        if suggestions:
            suggestions[-1].click()
            print("Clicou no último resultado sugerido.")
            report.append("Clicou no último resultado sugerido.")
        else:
            search.submit()
            print("Sugestões não encontradas, buscou por 'shirt'.")
            report.append("Sugestões não encontradas, buscou por 'shirt'.")
    except:
        search.submit()
        print("Sugestões não encontradas, buscou por 'shirt'.")
        report.append("Sugestões não encontradas, buscou por 'shirt'.")
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "products")))
    print("Página de resultados carregada.")
    report.append("Página de resultados carregada.")

def selecionar_produto_aleatorio(driver, report):
    products = driver.find_elements(By.CSS_SELECTOR, ".product-item-link")
    if products:
        product = random.choice(products)
        product_name = product.text
        product.click()
        print(f"Produto aleatório selecionado: {product_name}")
        report.append(f"Produto aleatório selecionado: {product_name}")
    else:
        raise Exception("Nenhum produto encontrado.")

def selecionar_tamanho_cor(wait, report, tamanho='S', cor='Blue'):
    try:
        size = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[@option-label='{tamanho}']")))
        size.click()
        print(f"Tamanho {tamanho} selecionado.")
        report.append(f"Tamanho {tamanho} selecionado.")
    except:
        pass
    try:
        color = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(@option-label, '{cor}')]")))
        color.click()
        print(f"Cor {cor} selecionada.")
        report.append(f"Cor {cor} selecionada.")
    except:
        pass

def adicionar_ao_carrinho(wait, report):
    add_to_cart = wait.until(EC.element_to_be_clickable((By.ID, "product-addtocart-button")))
    add_to_cart.click()
    print("Produto adicionado ao carrinho.")
    report.append("Produto adicionado ao carrinho.")

def adicionar_review(driver, wait, report):
    try:
        review_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '#reviews')]")))
        review_tab.click()
        time.sleep(1)
        nickname = wait.until(EC.presence_of_element_located((By.ID, "nickname_field")))
        summary = driver.find_element(By.ID, "summary_field")
        review = driver.find_element(By.ID, "review_field")
        nickname.send_keys("TestUser")
        summary.send_keys("Ótimo produto!")
        review.send_keys("Produto testado via automação. Recomendo!")
        stars = driver.find_elements(By.CSS_SELECTOR, ".review-control-vote label")
        if stars:
            stars[-1].click()
        driver.find_element(By.CSS_SELECTOR, "button.action.submit.primary").click()
        print("Comentário enviado para o produto.")
        report.append("Comentário enviado para o produto.")
    except Exception as e:
        print("Não foi possível adicionar comentário/review:", e)
        report.append("Não foi possível adicionar comentário/review.")

def realizar_checkout(wait, report):
    cart = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".showcart")))
    cart.click()
    checkout = wait.until(EC.element_to_be_clickable((By.ID, "top-cart-btn-checkout")))
    checkout.click()
    print("Checkout iniciado. Complete os dados manualmente se necessário.")
    report.append("Checkout iniciado.")

def salvar_relatorio(report):
    with open("relatorio_teste.txt", "w", encoding="utf-8") as f:
        for linha in report:
            f.write(linha + "\n")

if __name__ == "__main__":
    driver, wait = iniciar_driver()
    test_report = []
    try:
        acessar_home(driver, wait, test_report)
        criar_conta_manual()
        buscar_produto(wait, test_report)
        selecionar_produto_aleatorio(driver, test_report)
        selecionar_tamanho_cor(wait, test_report)
        adicionar_ao_carrinho(wait, test_report)
        adicionar_review(driver, wait, test_report)
        realizar_checkout(wait, test_report)
        input("Pressione Enter para finalizar e fechar o navegador...")
    finally:
        salvar_relatorio(test_report)
        driver.quit()
