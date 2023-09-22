from selene import be, have, browser

def test_first_less1(browser_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))

def test_second_less2(browser_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('11223344qqwweerraaazzzxxxcccppp').press_enter()
    browser.element('[id="search"]').should(have.text('текст 11223344qqwweerraaazzzxxxcccppp не найден'))