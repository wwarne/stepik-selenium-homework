import time


def test_add_to_cart_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    add_button = browser.find_elements_by_css_selector('button.btn-add-to-basket')
    assert len(add_button) == 1
