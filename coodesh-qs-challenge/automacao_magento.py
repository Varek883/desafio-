from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
test_report = []

try:
    # 1. Home page
    driver.get("https://magento.softwaretestingboard.com")
    assert driver.find_element(By.ID, "store.menu")
    print("Home page carregada com sucesso.")
    test_report.append("Home page carregada com sucesso.")

    # 2. Criar conta manualmente (Diferencial 2)
    print("Acesse a tela de cadastro (clique em 'Create an Account').")
    print("Preencha os dados fictícios do https://randomuser.me e resolva o captcha manualmente.")
    input("Após criar a conta e estar logado, pressione Enter para continuar...")  # Pausa para criação manual

    # 3. Buscar por 'shirt' e clicar no último resultado sugerido (Diferencial 1)
    search = wait.until(EC.presence_of_element_located((By.ID, "search")))
    search.clear()
    search.send_keys("shirt")
    try:
        suggestions = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".autocomplete-suggestions li")))
        if suggestions:
            suggestions[-1].click()
            print("Clicou no último resultado sugerido.")
            test_report.append("Clicou no último resultado sugerido.")
        else:
            search.submit()
            print("Sugestões não encontradas, buscou por 'shirt'.")
            test_report.append("Sugestões não encontradas, buscou por 'shirt'.")
    except:
        search.submit()
        print("Sugestões não encontradas, buscou por 'shirt'.")
        test_report.append("Sugestões não encontradas, buscou por 'shirt'.")

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "products")))
    print("Página de resultados carregada.")
    test_report.append("Página de resultados carregada.")

    # 4. Adicionar produto aleatório do catálogo de moda masculina (Diferencial 3)
    products = driver.find_elements(By.CSS_SELECTOR, ".product-item-link")
    if products:
        product = random.choice(products)
        product_name = product.text
        product.click()
        print(f"Produto aleatório selecionado: {product_name}")
        test_report.append(f"Produto aleatório selecionado: {product_name}")
    else:
        raise Exception("Nenhum produto encontrado.")

    # Se necessário, selecione tamanho/cor aqui (exemplo para tamanho S)
    try:
        size = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@option-label='S']")))
        size.click()
        print("Tamanho S selecionado.")
        test_report.append("Tamanho S selecionado.")
    except:
        pass

    try:
        color = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@option-label, 'Blue')]")))
        color.click()
        print("Cor Blue selecionada.")
        test_report.append("Cor Blue selecionada.")
    except:
        pass

    add_to_cart = wait.until(EC.element_to_be_clickable((By.ID, "product-addtocart-button")))
    add_to_cart.click()
    print("Produto adicionado ao carrinho.")
    test_report.append("Produto adicionado ao carrinho.")

    # 5. Adicionar comentário/review ao produto (Diferencial 4)
    try:
        # Aguarda link para reviews ou navega até a aba de reviews
        review_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '#reviews')]")))
        review_tab.click()
        time.sleep(1)
        # Preenche o formulário de review
        nickname = wait.until(EC.presence_of_element_located((By.ID, "nickname_field")))
        summary = driver.find_element(By.ID, "summary_field")
        review = driver.find_element(By.ID, "review_field")
        nickname.send_keys("TestUser")
        summary.send_keys("Ótimo produto!")
        review.send_keys("Produto testado via automação. Recomendo!")
        # Seleciona 5 estrelas
        stars = driver.find_elements(By.CSS_SELECTOR, ".review-control-vote label")
        if stars:
            stars[-1].click()
        driver.find_element(By.CSS_SELECTOR, "button.action.submit.primary").click()
        print("Comentário enviado para o produto.")
        test_report.append("Comentário enviado para o produto.")
    except Exception as e:
        print("Não foi possível adicionar comentário/review:", e)
        test_report.append("Não foi possível adicionar comentário/review.")

    # 6. Realizar checkout
    cart = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".showcart")))
    cart.click()
    checkout = wait.until(EC.element_to_be_clickable((By.ID, "top-cart-btn-checkout")))
    checkout.click()
    print("Checkout iniciado. Complete os dados manualmente se necessário.")
    test_report.append("Checkout iniciado.")

    input("Pressione Enter para finalizar e fechar o navegador...")

finally:
    # Diferencial 5 - Gerar relatório simples do teste
    with open("relatorio_teste.txt", "w", encoding="utf-8") as f:
        for linha in test_report:
            f.write(linha + "\n")
    driver.quit()
