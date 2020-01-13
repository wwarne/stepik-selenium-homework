import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Choose a language for a browser')


@pytest.fixture()
def browser(request):
    browser_lang = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_lang})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
