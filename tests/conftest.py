import pytest
from playwright.sync_api import sync_playwright, Playwright, Page, APIRequestContext
from config.settings import settings
from pages.base_page import BasePage


@pytest.fixture(scope="session")
def playwright() -> Playwright:
    """Start Playwright once for the whole test session"""
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright):
    """Launch browser once per session"""
    browser = playwright.chromium.launch(
        headless=settings.HEADLESS,
        args=["--start-maximized"] if not settings.HEADLESS else []
    )
    yield browser
    browser.close()


@pytest.fixture
def page(browser) -> Page:
    """Create new isolated page, maximizing window when not headless."""
    if settings.HEADLESS:
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
    else:
        context = browser.new_context(no_viewport=True)
    page = context.new_page()
    yield page
    if settings.PAUSE_TEST:
        # Only pause for debugging, not in normal test runs
        base_page = BasePage(page)
        base_page.pause_test()
    context.close()

@pytest.fixture(scope="session")
def api(playwright) -> APIRequestContext:
    """API client using Playwright's request context"""
    request_context = playwright.request.new_context()
    yield request_context
    request_context.dispose()