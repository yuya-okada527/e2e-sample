"""
GoogleのWebサイトを使って、Seleniumを動かすサンプル
"""

import time

from selenium.webdriver import Chrome, ChromeOptions


def search_chromedriver():
    """
    Googleにアクセスし、'ChromeDriver'というクエリで検索を実行するサンプル.
    """
    with Chrome() as driver:
        print("Googleへアクセス中...")
        driver.get('https://www.google.com/')
        time.sleep(2)
        print("検索実行...")
        search_box = driver.find_element_by_name("q")
        search_box.send_keys('ChromeDriver')
        time.sleep(2)
        search_box.submit()
        time.sleep(2)
        driver.quit()
        print("終了しました.")


def exec_headless_mode():
    """
    headlessモードで動かすサンプル
    """
    pass


def main():
    search_chromedriver()


if __name__ == "__main__":
    main()
