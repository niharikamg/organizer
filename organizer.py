import os
import shutil

# Define file categories and their corresponding extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx", ".csv"],
    "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Code": [".py", ".java", ".cpp", ".js", ".html", ".css"],
    "Executables": [".exe", ".sh", ".bat"],
    "Others": []  # Any files not categorized
}

def organize_files(directory):
    """Organizes files in the given directory into categorized subfolders."""
    if not os.path.exists(directory):
        print("Directory not found!")
        return

    # Create subfolders if they don’t exist
    for category in FILE_CATEGORIES.keys():
        category_path = os.path.join(directory, category)
        os.makedirs(category_path, exist_ok=True)

    # Move files into respective folders
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):  # Ignore folders
            file_ext = os.path.splitext(filename)[1].lower()

            moved = False
            for category, extensions in FILE_CATEGORIES.items():
                if file_ext in extensions:
                    shutil.move(file_path, os.path.join(directory, category, filename))
                    print(f"Moved: {filename} → {category}/")
                    moved = True
                    break

            # If no category matched, move to "Others"
            if not moved:
                shutil.move(file_path, os.path.join(directory, "Others", filename))
                print(f"Moved: {filename} → Others/")

if __name__ == "__main__":
    target_directory = input("Enter the folder path to organize: ")
    organize_files(target_directory)
    print("✅ File organization complete!")
