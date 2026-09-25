from encoder import * 


file_path = "C_labben/txtfiles/1.txt"

with open(file_path, "r", encoding="utf-8") as file:
    file_content = file.read()

binary_data = file_content.encode("utf-8")

bit_length = len(binary_data) * 8

enc(file_path, bit_length)