"""
Yahoo不動産をSeleniumで操作するサンプル
"""
from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

YAHOO_REALESTATE = "https://realestate.yahoo.co.jp/"

def new_mansion():
    """
    新築マンションをSeleniumで操作するサンプル
    """
    print("新築ブラウズ開始")
    with Chrome() as driver:
        # デフォルトのタイムアウト時間を設定
        wait = WebDriverWait(driver, 10)
        
        # Yahoo!不動産に遷移
        driver.get(YAHOO_REALESTATE)

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

        driver.quit()
    print("新築ブラウズ終了")
    

def main():
    new_mansion()


if __name__ == "__main__":
    main()
