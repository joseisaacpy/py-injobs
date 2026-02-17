from src.logger import init_logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = init_logger()


def open_indeed(browser):
    url = "https://br.indeed.com/jobs?q=&l=Brasil&from=searchOnHP%2Cwhereautocomplete&vjk=e2b04a667ea7ec82"
    logger.info(f"Acessando {url}")
    browser.get(url)


def accept_cookies(browser):
    wait = WebDriverWait(browser, 10)
    wait.until(
        EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
    ).click()
    logger.info("Aceitando cookies")
