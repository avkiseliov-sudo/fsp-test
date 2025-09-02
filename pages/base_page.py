from playwright.sync_api import Page
from typing import Literal

class BasePage:
    """Base class for all page objects"""

    def __init__(self, page: Page):
        self.page = page

    def pause_test(self) -> None:
        """Pause execution for debugging"""
        self.page.pause()

    def input_by_placeholder(self, placeholder: str, value: str) -> None:
        """Fill input field by its placeholder text"""
        self.page.get_by_placeholder(placeholder).fill(value)

    def click_button(self, name: str) -> None:
        """Click button by exact accessible name"""
        self.page.get_by_role("button", name=name, exact=True).click()

    def wait_loaded(
            self,
            state: Literal["domcontentloaded", "load", "networkidle"] = "domcontentloaded",
            timeout: int = 20000
    ) -> None:
        """
        Wait until the page is fully loaded.

        Args:
            state: Load state to wait for.
                - "domcontentloaded" → DOM content is loaded (but CSS/JS/images may still be loading).
                - "load" → 'load' event fired (all static resources are loaded).
                - "networkidle" → no network requests for at least 500 ms (recommended for SPAs).
            timeout: Maximum waiting time in milliseconds (default 20s).
        """
        self.page.wait_for_load_state(state=state, timeout=timeout)