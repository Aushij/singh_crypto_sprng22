#!/usr/bin/python3

# XOR two bytearrays
def xor(first, second):
   return bytearray(x^y for x,y in zip(first, second))

MSG   = "This is the known message!"
HEX_1 = "de03e4f2f3f5e1afde53a1db602d883d23913b91b04a64e3362b6e"
HEX_2 = "de03e4f2f3f5e1afcb1bb79e6831823e6ddc3387b05862e159"

# Convert ascii string to bytearray
D1 = bytes(MSG, 'utf-8')

# Convert hex string to bytearray
D2 = bytearray.fromhex(HEX_1)
D3 = bytearray.fromhex(HEX_2)

r1 = xor(D1, D2)
r2 = xor(D2, D3)
r3 = xor(r1, D2)
print(r1.hex())
print(r2.hex())
print(r3.hex())
