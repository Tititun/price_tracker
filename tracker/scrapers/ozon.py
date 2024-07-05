import pathlib
from typing import Optional, Tuple
import traceback

from bs4 import BeautifulSoup
from pyvirtualdisplay import Display
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc

chromedriver_path = pathlib.Path(__file__).parent / 'chromedriver'


def parse_price_text(text: str) -> float:
    """convert price text to float"""
    return float(text.strip('₽').replace(' ', ''))


def parse_price_from_url(url: str) -> Optional[Tuple[float]]:
    """return original price and discounted price"""
    with Display(visible=0, size=[800, 600]):
        driver = uc.Chrome(headless=False,
                            driver_executable_path=chromedriver_path)
        try:
            driver.get(url)

            WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, '[data-widget="webPrice"]')))
            
            soup = BeautifulSoup(driver.page_source)
            price_tag = soup.select_one('[data-widget="webPrice"]')
            
            original_price = parse_price_text(
                price_tag.find(string="без Ozon Карты")
                         .parent.parent.parent.select('span')[1].text)
            discount_price = parse_price_text(
                price_tag.find(string="c Ozon Картой")
                         .parent.find_previous('span').text)
            
            return original_price, discount_price

        except Exception:
            print(traceback.format_exc())
        finally:
            driver.quit()


if __name__ == '__main__':
    url = 'https://www.ozon.ru/product/gel-dlya-ukrepleniya-zubov-r-o-c-s-medical-minerals-remineralizuyushchiy-45-g-203756949/?avtc=1&avte=4&avts=1720182615'
    print(parse_price_from_url(url))
