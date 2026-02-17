from selenium import webdriver
from src.logger import init_logger

logger = init_logger()


def init_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    logger.info("Iniciando o navegador")

    browser = webdriver.Chrome(options=options)
    return browser


def close_browser(browser):
    if browser:
        logger.info("Fechando o navegador")
        browser.quit()
