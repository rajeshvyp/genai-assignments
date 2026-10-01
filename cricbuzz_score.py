from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.cricbuzz.com/")
    page.get_by_text("IND vs SL - IND won", exact=True).click()
    page.wait_for_selector("div.flex.flex-col.gap-2")
    score = page.inner_text("div.flex.flex-col.gap-2")
    print(score)
    page.screenshot(path="score.png")
    browser.close()