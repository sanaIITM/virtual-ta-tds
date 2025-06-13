import re
import json

with open("tds_plain_text.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

content = {}
current_module = ""
current_topic = ""

for line in lines:
    # Example pattern for module headings
    if re.match(r'^Module \d+:', line):
        current_module = line
        content[current_module] = {}
    elif line.startswith("Video") or line.startswith("Lecture") or re.match(r'^\d+\.', line):
        current_topic = line
        if current_module:
            content[current_module][current_topic] = ""
    else:
        # Add description to the current topic
        if current_module and current_topic:
            content[current_module][current_topic] += line + " "

# Save as JSON
with open("tds_structured.json", "w", encoding="utf-8") as f:
    json.dump(content, f, indent=2)

print("✅ Structured content saved to tds_structured.json")

