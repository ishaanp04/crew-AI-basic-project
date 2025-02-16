import re

with open("output_log_raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Regex to remove ANSI escape codes
clean_text = re.sub(r"\x1b\[[0-9;]*[mK]", "", text)

with open("output_log_clean.txt", "w", encoding="utf-8") as f:
    f.write(clean_text)

print("Clean output saved to output_log_clean.txt")
