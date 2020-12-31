"""
GoogleのWebサイトを使って、Seleniumを動かすサンプル
"""

import time

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By


GOOGLE_URL = "https://www.google.com/"


def search_chromedriver():
    """
    Googleにアクセスし、'ChromeDriver'というクエリで検索を実行するサンプル.
    """
    with Chrome() as driver:
        print("Googleへアクセス中...")
        driver.get(GOOGLE_URL)
        # time.sleep(2)
        print("検索実行...")
        search_box = driver.find_element_by_name("q")
        search_box.send_keys('ChromeDriver')
        # time.sleep(2)
        search_box.submit()
        # time.sleep(2)
        driver.quit()
        print("終了しました.")


def exec_headless_mode():
    """
    headlessモードで動かすサンプル
    """
    # WebDriverのオプション
    options = ChromeOptions()
    options.add_argument("--headless")

    with Chrome(options=options) as driver:
        print("Googleにアクセス中...")
        driver.get(GOOGLE_URL)
        print("検索前タイトル: " + driver.title)
        print()

        print("検索BOXに入力中...")
        search_box = driver.find_element_by_name("q")
        search_box.send_keys("ChromeDriver")
        search_box.submit()
        print("検索後タイトル: " + driver.title)
        print()

        print("検索結果を取得")
        for g_h3 in driver.find_elements_by_css_selector(".g h3"):
            print(g_h3.text)
        print()

        print("検索件数を取得")
        stats = driver.find_element(by=By.ID, value="result-stats").text
        print("取得件数: " + stats)
        print()

        print("クラス名やタグ名で取得")
        for i, g in enumerate(driver.find_elements_by_class_name("g")):
            if len(g.find_elements_by_class_name("r")) != 0:
                print("------ " + str(i+1) + " ------")
                r = g.find_elements_by_class_name("r")[0]
            else:
                continue
            print(r.text)
            print("\t" + r.find_element_by_tag_name("a").get_attribute("href"))
            s = g.find_element_by_class_name("s")
            print("\t" + s.find_element_by_class_name("st").text)
            print()

        driver.quit()


def main():
    # search_chromedriver()
    exec_headless_mode()


if __name__ == "__main__":
    main()
