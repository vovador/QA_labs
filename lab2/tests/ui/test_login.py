from pages.login_page import LoginPage

def test_login(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    login_page.navigate("http://localhost:3000/login")
    login_page.login("test_user", "test_password")
    assert page.url == "http://localhost:3000/dashboard"
