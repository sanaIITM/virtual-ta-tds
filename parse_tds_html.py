from bs4 import BeautifulSoup

# Load the saved HTML file
with open("tds_course_page.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# This depends on the structure of the HTML — we try to find modules and topics
# Let's print some sample text to see what's extractable
all_text = soup.get_text(separator="\n", strip=True)

# Save to file
with open("tds_plain_text.txt", "w", encoding="utf-8") as out:
    out.write(all_text)

print("✅ Extracted text saved to tds_plain_text.txt")

