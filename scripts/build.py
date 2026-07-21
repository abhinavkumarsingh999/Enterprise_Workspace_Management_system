from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
required_folders = [
    "src",
    "tests",
    "docs",
    "scripts",
]

print("Enterprise Workspace Scaffolding - Build Script")

for folder in required_folders:
    folder_path = PROJECT_ROOT / folder
    if folder_path.exists():
        print(f"{folder} exists")
    else:
        folder_path.mkdir(parents=True)
        print(f"created folder {folder}")
        
print("\nBuild complete. Check the project root for the required folder structure.")