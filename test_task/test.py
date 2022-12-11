import time
import random

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from urllib.request import urlopen
from PIL import Image


options = webdriver.ChromeOptions()
options.add_argument('User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 '
                     '(KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36')
driver = webdriver.Chrome(
    executable_path='D:\\TradingBot\\test_task\\chromedriver.exe',
    options=options)


def get_data(pair='BTCUSDT'):
    """Fills input fields"""

    try:
        driver.get('https://paper-trader.frwd.one/')
        time.sleep(2)

        # entry field pair
        pair_input = driver.find_element(By.NAME, 'pair')
        pair_input.clear()
        pair_input.send_keys(pair)
        time.sleep(1)

        # entry field timeframe
        time_frame_input = driver.find_element(By.NAME, 'timeframe')
        time_frame_input.clear()
        lst_time_frame = ['5m', '15m', '1h', '4h', '1d', '1w', '1M']
        time_frame_input.send_keys(random.choice(lst_time_frame))
        time.sleep(1)

        # entry field candles
        candles_input = driver.find_element(By.NAME, 'candles')
        candles_input.clear()
        candles_input.send_keys(random.randint(1, 1000))
        time.sleep(1)

        # entry field period
        period_input = driver.find_element(By.NAME, 'ma')
        period_input.clear()
        period_input.send_keys(random.randint(1, 100))
        time.sleep(1)

        # entry field take-profit
        tp_input = driver.find_element(By.NAME, 'tp')
        tp_input.clear()
        tp_input.send_keys(random.randint(1, 1000))
        time.sleep(1)

        # entry field stop-loss
        sl_input = driver.find_element(By.NAME, 'sl')
        sl_input.clear()
        sl_input.send_keys(random.randint(1, 1000))
        time.sleep(1)

        sl_input.send_keys(Keys.ENTER)
        time.sleep(5)

        get_soup(driver)

    except Exception as ex:
        print(ex)


def get_soup(driver):
    """Downloading the generated image"""
    soup = BeautifulSoup(driver.page_source, 'lxml')
    result = [f"https://paper-trader.frwd.one{url.find_next('img').get('src')[1:]}" for url in soup.find_all('body')]
    image = Image.open(urlopen(*result))
    image.save('D:\\TradingBot\\test_task\\media\\image.png')


def main():
    get_data()


if __name__ == '__main__':
    main()

