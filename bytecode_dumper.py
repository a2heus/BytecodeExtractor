import re
import os
import magic  

source_file = "fonts.h"

try:
    with open(source_file, "r") as f:
        content = f.read()

    matches = re.findall(r"unsigned char (\w+)\[[^\]]+\] = \{([^\}]+)\};", content, re.DOTALL)

    if not matches:
        print("Aucun tableau 'unsigned char' trouvé.")
        exit()

    for name, data in matches:
        byte_values = re.findall(r"0x[0-9A-Fa-f]{2}", data)
        byte_values = [int(b, 16) for b in byte_values]

        temp_file = f"{name}.bin"

        with open(temp_file, "wb") as f:
            f.write(bytearray(byte_values))

        file_type = magic.Magic(mime=True).from_file(temp_file)

        if "image/png" in file_type:
            extension = ".png"
        elif "image/jpeg" in file_type:
            extension = ".jpg"
        elif "font" in file_type:
            extension = ".ttf"
        elif "application/pdf" in file_type:
            extension = ".pdf"
        elif "text/plain" in file_type:
            extension = ".txt"
        elif "application/zip" in file_type:
            extension = ".zip"
        else:
            extension = ".bin"  

        output_file = f"{name}{extension}"
        os.rename(temp_file, output_file)

        print(f"Fichier créé : {output_file} ({len(byte_values)} octets, type : {file_type})")

except Exception as e:
    print(f"Erreur : {e}")
