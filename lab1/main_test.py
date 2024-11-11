from playwright.sync_api import sync_playwright


def test_registration(page):
    # Перейти на сторінку реєстрації
    page.goto("https://parabank.parasoft.com/parabank/register.htm")
    
    # Заповнити форму реєстрації
    page.fill('input[name="customer.firstName"]', 'Тест')
    page.fill('input[name="customer.lastName"]', 'Користувач')
    page.fill('input[name="customer.address.street"]', '123 Головна вулиця')
    page.fill('input[name="customer.address.city"]', 'Будь-де')
    page.fill('input[name="customer.address.state"]', 'CA')
    page.fill('input[name="customer.address.zipCode"]', '12345')
    page.fill('input[name="customer.phoneNumber"]', '555-555-5555')
    page.fill('input[name="customer.ssn"]', '123-45-6789')
    page.fill('input[name="username"]', 'TestUser123')  # Ввести унікальне ім'я користувача
    page.fill('input[name="password"]', '1234qwert')
    page.fill('input[name="repeatedPassword"]', '1234qwert')
    
    # Відправити форму реєстрації
    page.click('input[type="submit"]')
    
    # Зачекати на повідомлення про підтвердження або перейти на сторінку огляду рахунків
    page.wait_for_selector('text=Огляд рахунків')
    assert page.is_visible('text=Огляд рахунків'), 'Реєстрація не вдалася'


def test_login(page):
    # Перейти на сторінку логіну
    page.goto('https://parabank.parasoft.com/parabank/index.htm')
    
    # Заповнити форму логіну
    page.fill('input[name="username"]', 'TestUser123')  # Використати те ж ім'я користувача
    page.fill('input[name="password"]', '1234qwert')
    page.click('input[type="submit"]')
    
    # Зачекати на завантаження сторінки огляду рахунків
    page.wait_for_selector('text=Огляд рахунків')
    assert page.is_visible('text=Огляд рахунків'), 'Логін не вдалася'


def run_tests():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Запустити тест реєстрації
        test_registration(page)

        # Запустити тест логіну
        test_login(page)

        context.close()
        browser.close()


if __name__ == "__main__":
    run_tests()
