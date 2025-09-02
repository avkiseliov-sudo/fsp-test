from pages.home_page import HomePage


def test_invalid_email(page):
    home = HomePage(page).open()
    home.enter_email(HomePage.MAIN_BANNER_XPATH, "wrong_email")
    home.click_download_button(HomePage.MAIN_BANNER_XPATH)
    assert not home.is_email_valid(HomePage.MAIN_BANNER_XPATH)
