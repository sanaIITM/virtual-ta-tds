from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Headless browser setup
options = Options()
options.add_argument("--headless")  # run without opening browser
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Set up the Chrome WebDriver with service manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Load the course site
driver.get("https://tds.s-anand.net/#/2025-01/")
time.sleep(5)  # wait for JS to load

# Grab the HTML
html = driver.page_source

# Save to file
with open("tds_course_page.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ HTML saved to tds_course_page.html")

driver.quit()

