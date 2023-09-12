#!/usr/bin/env python3

import os
import sys

def remove_first_byte(src_dir, dest_dir):
    # Check if source directory exists
    if not os.path.exists(src_dir):
        print("Error: Source directory does not exist!")
        sys.exit(1)

    # Create destination directory if it doesn't exist
    os.makedirs(dest_dir, exist_ok=True)

    # Process each file in the source directory
    for filename in os.listdir(src_dir):
        src_file = os.path.join(src_dir, filename)
        dest_file = os.path.join(dest_dir, filename)

        if os.path.isfile(src_file):
            with open(src_file, 'rb') as f:
                data = f.read()[1:]  # Read all data from the file, excluding the first byte

            with open(dest_file, 'wb') as f:
                f.write(data)

    print("Processing complete.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: script.py <source_directory> <destination_directory>")
        sys.exit(1)

    remove_first_byte(sys.argv[1], sys.argv[2])
