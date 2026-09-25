from comp import *
import timeit
from encoder import *
from huffman import *

filePathList = ["txtfiles/1.txt", "txtfiles/2.txt", "txtfiles/3.txt", "txtfiles/4.txt","txtfiles/5.txt"]


def read(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        file_content = file.read()
    return file_content

def amount(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        file_content = file.read()

    binary_data = file_content.encode("utf-8")

    bit_length = len(binary_data) * 8
    return bit_length

def main():

    tidlzw = []
    tidhuff = []
    
    for x in range(len(filePathList)):

        huff = HuffmanCoding(filePathList[x])
        tidhuff.append(timeit.timeit(stmt = lambda: huff.compress(), number = 100))
        tidlzw.append(timeit.timeit(stmt = lambda: enc(filePathList[x], amount(filePathList[x])), number = 100))
        
        
    tidlzw = [x / 100 for x in tidlzw]
    tidhuff= [x / 100 for x in tidhuff]

    
    print(tidlzw)
    print(tidhuff)


main()