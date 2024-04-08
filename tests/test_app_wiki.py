from qa_guru_python_22.models.pages.search_page import search_page


def test_should_getting_started():
    search_page.should_getting_started()


def test_search():
    search_page.skip()
    search_page.search('Appium')
    search_page.should_results('Appium')


def test_open_page():
    search_page.skip()
    search_page.search('Python')
    search_page.open_page()
