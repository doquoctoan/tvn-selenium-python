from project.pages.search import GoogleSearchPage


def test_google_search(browser):
    search_page = GoogleSearchPage(browser)
    search_page.load()
    search_page.search("panda\n")