#!/usr/bin/python3
from Crypto.Cipher import AES
from Crypto.Util import Padding
iv_hex_string  = 'aabbccddeeff00998877665544332211'
iv  = bytes.fromhex(iv_hex_string)
expected_ciphertext = '3879c71b232cd0d2fc6f5ffcc1d76f074c0fcbe007d9cc53939fdeebf1d6ffd2'
data = b'This is a top secret.'
word_file = open("words.txt", "r")
content = word_file.read()
lst = content.split("\n")
word_file.close()
new=[]
for i in range(len(lst)):
        word = lst[i]
        if len(word) <= 16 :
                new.append(word)
key_list = []              
for i in range(len(new)):
        length = 16
        padding = '#'
        item = new[i].ljust(length,padding)
        key_list.append(item)
        key = bytes.fromhex(key_list[i].encode('utf-8').hex())
        # Encrypt the entire data
        cipher = AES.new(key, AES.MODE_CBC, iv)                   
        ciphertext = cipher.encrypt(Padding.pad(data, 16))       
        cipher_hex=ciphertext.hex()
        if cipher_hex == expected_ciphertext :
                print(key)
