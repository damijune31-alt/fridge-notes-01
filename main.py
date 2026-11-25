import os
import sys
from pathlib import Path

# One passive-aggressive note from a smart fridge: the door log never lies,
# and the yogurt has opinions too.
NOTE = "Door opened 14 times today. Items taken: none. The yogurt and I are starting to think I'm a television."

if not 1 <= len(NOTE) <= 200:
    sys.exit(f"note must be 1-200 characters, got {len(NOTE)}")
if "\n" in NOTE:
    sys.exit("note must be a single line")

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
entry_path = out_dir / "entry.txt"
entry_path.write_text(NOTE, encoding="utf-8")

if entry_path.read_text(encoding="utf-8") != NOTE:
    sys.exit("entry.txt does not match the note")
print(f"wrote {len(NOTE)} characters to entry.txt")
