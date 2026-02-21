from src.logger import init_logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
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


def get_card_jobs(browser):
    logger.info("Buscando vagas")

    wait = WebDriverWait(browser, 10)

    cards = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".resultContent"))
    )
    logger.info(f"Encontrados {len(cards)} vagas")

    return cards


def extract_job_data(card):
    try:
        title = card.find_element(By.CSS_SELECTOR, ".jobTitle").text
    except NoSuchElementException:
        title = "Não informado"

    try:
        company = card.find_element(
            By.CSS_SELECTOR, "[data-testid='company-name']"
        ).text
    except NoSuchElementException:
        company = "Não informado"

    try:
        location = card.find_element(
            By.CSS_SELECTOR, "[data-testid='text-location']"
        ).text
    except NoSuchElementException:
        location = "Não informado"

    return {
        "title": title,
        "company": company,
        "location": location,
    }


def collect_jobs(cards):
    jobs = []
    for card in cards:
        jobs.append(extract_job_data(card))
    return jobs


def save_to_csv(jobs):
    import pandas as pd

    df = pd.DataFrame(jobs)
    df.to_csv("vagas.csv", index=False)

    logger.info("Vagas salvas em vagas.csv")

    print(df)
