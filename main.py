# The excuse reframes the miss as policy: the cat outranks the cleaning
# schedule, and the vacuum knows its place in the household hierarchy.
"""Writes one robot vacuum excuse to /output/entry.txt."""
import os

TEXT = "That spot was under the cat, and I have a strict no-disturbing-management policy."

# Rule: the excuse must be a single line of 1 to 140 characters.
assert "\n" not in TEXT and 1 <= len(TEXT) <= 140, f"entry must be one line, 1-140 chars (got {len(TEXT)})"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT + "\n")
