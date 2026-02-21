from src.browser import init_browser, close_browser
from src.scraper import (
    open_indeed,
    accept_cookies,
    get_card_jobs,
    collect_jobs,
    save_to_csv,
)


def main():
    browser = init_browser()

    try:
        open_indeed(browser)
        accept_cookies(browser)

        cards = get_card_jobs(browser)
        jobs = collect_jobs(cards)

        save_to_csv(jobs)

    finally:
        close_browser(browser)


if __name__ == "__main__":
    main()
