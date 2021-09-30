const { test, expect } = require("@playwright/test");
test("test", async ({ page }) => {
  // Googleのトップ画面に遷移
  await page.goto("https://www.google.com/");
  // 検索ボックスにPlaywrightと入力
  await page.fill('[aria-label="検索"]', "playwright");
  // エンターキーを謳歌
  await Promise.all([
    page.waitForNavigation(),
    page.press('[aria-label="検索"]', "Enter"),
  ]);
  // PlaywrightのGithubリポジトリへのリンクをクリック
  await page.click("text=microsoft/playwright: Node.js library");
  // 想定通りのURLに遷移していることを確認
  await expect(page).toHaveURL("https://github.com/microsoft/playwright");
  // すぐ閉じると、わかりにくいので、10秒ほど、待機する
  await new Promise((resolve) => setTimeout(resolve, 10_000));
});
