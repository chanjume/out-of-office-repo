#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — writes one auto-reply line to /output/entry.txt."""
import os

ENTRY = "I'm on vacation. My AI is covering for me. It already rescheduled my meetings, emailed my boss, and applied for my job."  # 124 chars: machine voice + twist (the cover agent wants the job)

assert 1 <= len(ENTRY) <= 160, f"entry must be 1-160 chars, got {len(ENTRY)}"
assert ENTRY.strip(), "entry must not be only whitespace"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)

print(f"Wrote {len(ENTRY)} chars to /output/entry.txt")
