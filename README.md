# E2E テスト検証

WEB アプリケーションの E2E テスト自動化のための検証リポジトリ

## 検証ツール

- selenium

## インストール

- selenium

  - python

  ```bash
  # poetryの場合
  $ poetry add selenium

  # pipの場合
  $ pip install selenium
  ```

- webdriver

  - Chrome

  ```bash
  # Homebrewを使用（Mac）
  # 念のためHomebrewをUpdate
  $ brew tap homebrew/cask

  # chromedriverのインストール
  $ brew install --cask chromedriver

  # 確認(Chromeのバージョンと対応していることを確認)
  $ brew info --cask chromedriver
  >> chromedriver: 87.0.4280.20
  ...
  ```

## 参考サイト

- Selenium for Python
  - https://qiita.com/memakura/items/20a02161fa7e18d8a693
- Selenium 公式(日本語)
  - https://www.selenium.dev/documentation/ja/
- e2e テストツール
  - http://var.blog.jp/archives/82577944.html
- puppeteer github
  - https://github.com/puppeteer/puppeteer
- puppeteer 参考
  - https://qiita.com/bezeklik/items/c6448d50ff0efb45829e
- puppeteer スクリーンショット
  - https://qiita.com/103ma2/items/89f9fefca46f072f43e8
- selenide
  - https://qiita.com/tatesuke/items/589e30ab9b3dc7037e26
- cypress.io
  - https://www.cypress.io/
