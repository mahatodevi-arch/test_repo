# Date Adder Script

A simple Python utility to prepend today's date (YYYY-MM-DD) to the beginning of every filename in a specified directory.

## Objective
The goal is to automate the organization of files by adding a standardized date prefix to their names.

## Features
- Automatically fetches today's date in `YYYY-MM-DD` format.
- Prepends the date to all files in the target directory.
- Skips the script itself to prevent accidental renaming.
- Simple and easy to use.

## Usage
1. Place `add_date_to_filenames.py` in the folder containing the files you want to rename.
2. Run the script:
   ```bash
   python3 add_date_to_filenames.py
   ```

## Prompt Source
This project was created based on the following prompt:
> Create a python script to add today's date (YYYY-MM-DD) to the beginning of every filename in a folder.
