from playwright.sync_api import Page
from pages.base_page import BasePage
from config.settings import settings


class HomePage(BasePage):
    """Home page objects"""
    URL = settings.BASE_URL
    MAIN_BANNER_XPATH = "//div[@class='main-banner']"
    SERVICES_XPATH = "//div[@class='services']"
    PRE_FOOTER_XPATH = "//div[@class='pre-footer-form']"
    EMAIL_XPATH = "//input[@type='email']"
    DOWNLOAD_BUTTON_XPATH = "//button[contains(@class,'downloadButton')]"

    def __init__(self, page: Page):
        super().__init__(page)

    def open(self) -> "HomePage":
        self.page.goto(self.URL)
        self.wait_loaded()
        return self

    def enter_email(self, section: str, email: str) -> "HomePage":
        """Enter email inside given section"""
        self.page.locator(section).locator(self.EMAIL_XPATH).fill(email)
        return self

    def click_download_button(self, section: str) -> "HomePage":
        """Click button by name inside given section"""
        self.page.locator(section).locator(self.DOWNLOAD_BUTTON_XPATH).click()
        return self

    def is_email_valid(self, section: str) -> bool:
        """Check if email input inside section is valid via JS"""
        email_input = self.page.locator(section).locator(self.EMAIL_XPATH)
        return email_input.evaluate("el => el.checkValidity()")
