from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=True,
        args=[
            "--disable-dev-shm-usage",
            "--no-sandbox",
            "--disable-gpu"
        ]
    )

    page = browser.new_page()

    page.goto(
        "https://www.bedas.com.tr/elektrik-kesintisi-sorgulama",
        wait_until="domcontentloaded",
        timeout=180000
    )

    print(page.title())

    browser.close()
