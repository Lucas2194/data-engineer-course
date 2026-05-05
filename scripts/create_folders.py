from pathlib import Path

folders = [
    "data/raw",
    "data/processed",
    "data/external",
    "logs",
    "reports",
]

for folder in folders:
    Path(folder).mkdir(parents=True, exist_ok=True)
    print(f"Folder gotowy: {folder}")