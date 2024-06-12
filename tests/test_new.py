import allure
from selenium.webdriver.common.by import By

@allure.title("Просмотр перехода на Вакансии")
def test_has_title(driver, base_url):
    driver.get(base_url + "hr/vacancies/")
    driver.find_element(By.CLASS_NAME, "mb-9")
    driver.find_element(By.LINK_TEXT, "Вакансии")


@allure.title("Просмотр перехода на Вакансии_2222222")
def test_has_title_222222(driver, base_url):
    driver.get(base_url + "hr/vacancies/")
    driver.find_element(By.CLASS_NAME, "mb-9")
    driver.find_element(By.LINK_TEXT, "Вакансии")
