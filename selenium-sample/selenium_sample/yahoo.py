"""
Yahoo不動産をSeleniumで操作するサンプル
"""
import argparse
import os
from time import sleep
from pathlib import Path

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

# 引数の解析
PARSER = argparse.ArgumentParser(description="Yahoo不動産をSeleniumで操作するサンプルスクリプト")
PARSER.add_argument("--headless", action="store_true", help="headlessモードで動かすかどうかを指定します.")
ARGS = PARSER.parse_args()

# Yahoo不動産トップURL
YAHOO_REALESTATE = "https://realestate.yahoo.co.jp/"

# スクリーンショット画像ディレクトリ
IMAGE_DIR = os.path.join(
    Path(__file__).resolve().parents[0],
    "images"
)

def new_mansion():
    """
    新築マンションをSeleniumで操作するサンプル
    """
    print("新築ブラウズ開始")
    options = ChromeOptions()
    if ARGS.headless:
        options.add_argument("--headless")
    with Chrome(options=options) as driver:
        # デフォルトのタイムアウト時間を設定
        wait = WebDriverWait(driver, 10)
        
        # Yahoo!不動産に遷移
        driver.get(YAHOO_REALESTATE)
        screenshot(driver, "yahoo_realestate_top.png")

        # 新築マンションの検索画面に遷移
        new_mansion_link = driver.find_element_by_css_selector(".maNew a")
        new_mansion_link.click()
        ## 新築マンションの検索画面が出てくるまで待つ
        wait.until(EC.element_to_be_clickable((By.ID, "lc")))

        # 近畿の西宮で検索
        ## 近畿を選択
        local_select = Select(driver.find_element_by_id("lc"))
        local_select.select_by_visible_text("近畿")

        ## 検索BOXに入力
        input_box = driver.find_element_by_id("dta")
        input_box.send_keys("西宮")

        ## 検索実行
        search_button = driver.find_element_by_class_name("AreaSearchIn__button")
        search_button.click()

        sleep(3)

        screenshot(driver, "yahoo_realestate_after_search.png")

        driver.quit()
    print("新築ブラウズ終了")


def screenshot(driver, file_name):
    """
    スクリーンショットを取得する.
    headlessモード出ない場合、きれいに取れません.
    """
    # 作成ディレクトリを作成
    os.makedirs(IMAGE_DIR, exist_ok=True)

    # 画面のサイズを設定
    w = driver.execute_script("return document.body.scrollWidth")
    h = driver.execute_script("return document.body.scrollHeight")
    driver.set_window_size(w, h)

    # スクリーンショットを保存
    driver.save_screenshot(os.path.join(IMAGE_DIR, file_name))


def main():
    new_mansion()


if __name__ == "__main__":
    main()
