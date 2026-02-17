from src.browser import init_browser, close_browser
from src.scraper import open_indeed


def main():
    browser = init_browser()
    open_indeed(browser)
    close_browser(browser)


if __name__ == "__main__":
    main()
