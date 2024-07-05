import traceback
from bs4 import BeautifulSoup
from pyvirtualdisplay import Display
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


with Display(visible=0, size=[800, 600]) as display:
    driver = uc.Chrome(headless=False, driver_executable_path='/home/danil/PycharmProjects/price_tracker/chromedriver')
    try:

        driver.get(
            'https://www.ozon.ru/product/komplekt-noskov-shop-layn-igra-5-par-1426082663/?asb=iNVd3xz8qT%252B%252BHKzZ70my%252Bb99IkCLTPnENEAXPjFohXk%253D&asb2=TeMZHCRMhcY22gYggsZy9iWAzE2UO0n7lkz6XrWoKeOWoAy11bYvm0lI9QZdegJ5oehm4_WFOQvXxDZQ4A8yOQ&avtc=1&avte=2&avts=1720181116&keywords=%D0%BF%D1%80%D0%BE%D0%B3%D1%83%D0%BB%D0%BA%D0%B8+%D1%81+%D1%81%D0%BE%D0%B1%D0%B0%D0%BA%D0%B0%D0%BC%D0%B8+%D0%B8%D0%B3%D1%80%D0%B0'
            )

        element = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-widget="webPrice"]')))
        soup = BeautifulSoup(driver.page_source)
        price_tag = soup.select_one('[data-widget="webPrice"]')
        
        print(price_tag)
        original_price = price_tag.find(string="без Ozon Карты").parent.parent.parent.select('span')[1]
        discount_price = price_tag.find(string="c Ozon Картой").parent.find_previous('span')
        print(original_price, discount_price)

    except Exception as error:
        print(traceback.format_exc())
        print(driver.page_source)
    finally:
        driver.quit()
