from pathlib import Path
import shutil

folder_path = Path.home() / 'Downloads'  # You can change this

file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Videos': ['.mp4', '.mkv', '.avi'],
    'Music': ['.mp3', '.wav'],
}

for file in folder_path.iterdir():
    if file.is_file():
        ext = file.suffix.lower()
        moved = False

        for folder_name, extensions in file_types.items():
            if ext in extensions:
                target_folder = folder_path / folder_name
                target_folder.mkdir(exist_ok=True)
                shutil.move(str(file), target_folder / file.name)
                print(f"Moved: {file.name} → {folder_name}/")
                moved = True
                break
        if not moved:
            other_folder = folder_path / 'Others'
            other_folder.mkdir(exist_ok=True)
            shutil.move(str(file), other_folder / file.name)
            print(f"Moved: {file.name} → Others/")
