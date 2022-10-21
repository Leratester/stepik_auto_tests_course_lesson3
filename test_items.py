import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
# link = "https://ya.ru/"


def test_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(10)

    button = len(browser.find_elements_by_css_selector("button.btn-add-to-basket"))
    assert button > 0, "Button not found"



