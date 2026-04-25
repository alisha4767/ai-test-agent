from playwright.sync_api import sync_playwright

def run_steps(steps):
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=False)
        page = browser.new_page()

        for step in steps:
            print("Executing:", step)

            try:
                if step["action"] == "open":
                    page.goto(step["url"])

                elif step["action"] == "type":
                    page.fill(step["target"], step["value"])

                elif step["action"] == "click":
                    page.click(step["target"])

                elif step["action"] == "assertion":
                    if step["contains"].lower() not in page.content().lower():
                        print("❌ Assertion failed")
                        browser.close()
                        return False

            except Exception as e:
                print("❌ Step failed:", e)
                browser.close()
                return False

        browser.close()
        return True