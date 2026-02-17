from src.browser import init_browser, close_browser
from src.scraper import open_indeed, accept_cookies, get_card_jobs


def main():
    browser = init_browser()
    open_indeed(browser)
    accept_cookies(browser)
    cards = get_card_jobs(browser)
    close_browser(browser)


if __name__ == "__main__":
    main()
