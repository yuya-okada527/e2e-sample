const { test, expect } = require("@playwright/test");
test("test", async ({ page }) => {
  // Googleのトップ画面に遷移
  await page.goto("https://www.google.com/");
  // 検索欄に「エクサ」と入力
  await page.fill('[aria-label="検索"]', "エクサ");
  // エンターキーを押下
  await Promise.all([
    page.waitForNavigation(),
    page.press('[aria-label="検索"]', "Enter"),
  ]);
  // エクサのホームページリンクをクリック
  await page.click("text=株式会社エクサ");
  // ちゃんとリンクに遷移できているか確認
  await expect(page).toHaveURL("https://www.exa-corp.co.jp/");
  // 実行後、わかりやすいように10秒ほど待機
  await new Promise((resolve) => setTimeout(resolve, 10_000));
});
