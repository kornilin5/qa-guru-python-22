from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class SearchPage:

    with step('Getting started'):

        def should_getting_started(self):
            browser.element((
                AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
                    have.text('The Free Encyclopedia\n…in over 300 languages'))
            browser.element(
                (AppiumBy.ID,
                 'org.wikipedia.alpha:id/fragment_onboarding_forward_button'
                 )).click()
            browser.element((AppiumBy.ID,
                             'org.wikipedia.alpha:id/primaryTextView')).should(
                                 have.text('New ways to explore'))
            browser.element(
                (AppiumBy.ID,
                 'org.wikipedia.alpha:id/fragment_onboarding_forward_button'
                 )).click()
            browser.element((AppiumBy.ID,
                             'org.wikipedia.alpha:id/primaryTextView')).should(
                                 have.text('Reading lists with sync'))
            browser.element(
                (AppiumBy.ID,
                 'org.wikipedia.alpha:id/fragment_onboarding_forward_button'
                 )).click()
            browser.element((AppiumBy.ID,
                             'org.wikipedia.alpha:id/primaryTextView')).should(
                                 have.text('Data & Privacy'))

    with step('Type search'):

        def search(self, text):
            browser.element(
                (AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
            browser.element(
                (AppiumBy.ID,
                 "org.wikipedia.alpha:id/search_src_text")).type(text)

    with step('open page'):

        def open_page(self):
            browser.element(
                (AppiumBy.ID,
                 "org.wikipedia.alpha:id/page_list_item_title")).click()

    with step('Check results'):

        def should_results(self, text):
            results = browser.all(
                (AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
            results.should(have.size_greater_than(0))
            results.first.should(have.text(text))

    with step('skip'):

        def skip(self):
            browser.element(
                (AppiumBy.ID,
                 'org.wikipedia.alpha:id/fragment_onboarding_skip_button'
                 )).click()


search_page = SearchPage()
