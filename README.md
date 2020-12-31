# E2E テスト検証

WEB アプリケーションの E2E テスト自動化のための検証リポジトリ

## 検証ツール

- selenium

## インストール

- selenium

  - python

  ```bash
  # poetryの場合
  poetry add selenium

  # pipの場合
  pip install selenium
  ```

- webdriver

  - Chrome

  ```bash
  # Homebrewを使用（Mac）
  # 念のためHomebrewをUpdate
  brew tap homebrew/cask

  # chromedriverのインストール
  brew install --cask chromedriver

  # 確認(Chromeのバージョンと対応していることを確認)
  brew info --cask chromedriver
  chromedriver: 87.0.4280.20
  ...
  ```
