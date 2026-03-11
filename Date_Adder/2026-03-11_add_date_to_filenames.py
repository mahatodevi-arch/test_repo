import os
import sys
from datetime import datetime

def add_date_to_filenames(directory='.'):
    """
    Prepends today's date (YYYY-MM-DD) to all filenames in the specified directory.
    """
    # Get today's date in YYYY-MM-DD format
    today = datetime.now().strftime('%Y-%m-%d')
    prefix = f"{today}_"

    # Get the name of this script to avoid renaming it
    script_name = os.path.basename(__file__)

    # List files in the directory
    try:
        if not os.path.exists(directory):
            print(f"Directory '{directory}' does not exist.")
            return
            
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    except Exception as e:
        print(f"Error accessing directory '{directory}': {e}")
        return

    count = 0
    for filename in files:
        # Skip this script
        if filename == script_name:
            continue
        
        # Avoid prepending if the date already exists at the start
        if filename.startswith(prefix):
            print(f"Skipping '{filename}' (already prefixed)")
            continue

        # Construct new filename
        new_filename = prefix + filename
        
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_filename)

        try:
            os.rename(old_path, new_path)
            print(f"Renamed: '{filename}' -> '{new_filename}'")
            count += 1
        except Exception as e:
            print(f"Error renaming '{filename}': {e}")

    print(f"\nCompleted! Total files renamed: {count}")

if __name__ == "__main__":
    target_dir = sys.argv[1] if len(sys.argv) > 1 else '.'
    add_date_to_filenames(target_dir)
