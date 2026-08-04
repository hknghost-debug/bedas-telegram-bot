from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        page = browser.new_page(viewport={"width": 1366, "height": 768})

        page.goto(
            "https://www.bedas.com.tr/elektrik-kesintisi-sorgulama",
            wait_until="networkidle",
            timeout=60000,
        )

        print("Sayfa başlığı:", page.title())

        page.screenshot(path="bedas.png", full_page=True)

        browser.close()

if __name__ == "__main__":
    main()
