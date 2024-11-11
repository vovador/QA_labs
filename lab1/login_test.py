from playwright.sync_api import sync_playwright


def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        # Перейти на сторінку логіну
        page.goto('https://parabank.parasoft.com/parabank/index.htm')
        
        # Заповнити форму логіну
        page.fill('input[name="username"]', 'TestUser123')  # Використати те ж ім'я користувача
        page.fill('input[name="password"]', '1234qwert')
        page.click('input[type="submit"]')
        
        # Зачекати на завантаження сторінки огляду рахунків
        page.wait_for_selector('text=Огляд рахунків')
        assert page.is_visible('text=Огляд рахунків'), 'Логін не вдалася'

        context.close()
        browser.close()


if __name__ == "__main__":
    test_login()
