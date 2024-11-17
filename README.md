A Python script to extract multiple bytecode arrays from a C file and automatically save them as binary files with correct extensions. This tool uses regex to identify unsigned char arrays in the source code, processes the bytecode, and utilizes file type detection to name files appropriately. Perfect for analyzing or extracting embedded resources like images, fonts, or other binary data.

Features:
- Handles multiple `unsigned char` arrays in a single C file.
- Saves each array as a separate binary file.
- Automatically detects and assigns the correct file extension (e.g., .png, .jpg, .ttf, etc.).
- Easy to use on Windows or Linux.
