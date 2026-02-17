from src.logger import init_logger

logger = init_logger()


def open_indeed(browser):
    url = "https://br.indeed.com/jobs?q=&l=Brasil&from=searchOnHP%2Cwhereautocomplete&vjk=e2b04a667ea7ec82"
    logger.info(f"Acessando {url}")
    browser.get(url)
