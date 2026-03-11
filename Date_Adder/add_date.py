import os
import sys
from datetime import datetime

def add_date_to_filenames(directory_path='.'):
    """
    Prepends today's date (YYYY-MM-DD) to all files in the given directory.
    """
    # Get today's date in YYYY-MM-DD format
    today_prefix = datetime.now().strftime('%Y-%m-%d') + "_"
    
    # Get the basename of this script to avoid renaming it
    script_name = os.path.basename(__file__)
    exclude_files = [script_name, "Gemini.md", "Readme.md"]

    if not os.path.exists(directory_path):
        print(f"Directory '{directory_path}' not found.")
        return

    # Counter for renamed files
    renamed_count = 0

    # Iterate through all files in the directory
    for filename in os.listdir(directory_path):
        file_full_path = os.path.join(directory_path, filename)

        # Check if it's a file and not this script
        if os.path.isfile(file_full_path) and filename not in exclude_files:
            # Skip if already prefixed
            if filename.startswith(today_prefix):
                print(f"Skipping '{filename}' (already has date prefix)")
                continue

            # Construct new name
            new_filename = today_prefix + filename
            new_full_path = os.path.join(directory_path, new_filename)

            # Perform rename
            try:
                os.rename(file_full_path, new_full_path)
                print(f"Successfully renamed: {filename} -> {new_filename}")
                renamed_count += 1
            except Exception as e:
                print(f"Error renaming {filename}: {e}")

    print(f"\nTask completed. Total files renamed: {renamed_count}")

if __name__ == "__main__":
    # Use the first argument as target directory if provided, otherwise Use current directory
    target = sys.argv[1] if len(sys.argv) > 1 else '.'
    add_date_to_filenames(target)
