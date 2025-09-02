from playwright.sync_api import Page

class BasePage:
    """Base class for all page objects"""

    def __init__(self, page: Page):
        self.page = page

    def pause_test(self) -> None:
        """Pause execution for debugging"""
        self.page.pause()
