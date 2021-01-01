const puppeteer = require("puppeteer");

const headless = false;
const slowMo = 10;
const width = 1280;
const height = 800;
const dumpio = true;
const args = ["--start-fullscreen", "--disable-infobars", "--hide-scrollbars"];

const google_url = "https://www.google.com/";

const screenshot_dir = "images/";

(async () => {
  // ブラウザを起動
  const browser = await puppeteer.launch({ headless, slowMo, dumpio, args });
  const page = (await browser.pages())[0];
  await page.setViewport({ width, height });

  // Googleに遷移
  await page.goto(google_url);
  await save(page, "google_top.png");

  // 検索実行
  await page.type("input[name='q']", "puppeteer");
  await page.click("input[name='btnK']");
  await page.waitForNavigation({
    timeout: 60000,
    waitUntil: "domcontentloaded",
  });
  await save(page, "searche_puppeteer.png");

  browser.close();
})();

const save = async (page, fileName) => {
  await page.screenshot({
    path: screenshot_dir + fileName,
    fullPage: true,
  });
};
