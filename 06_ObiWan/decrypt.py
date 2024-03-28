#!/usr/bin/env python3
import binascii
import sys
import math

# since n is huge, the x mod n always returns x
# we can exploit this by reversing the encryption y[i] = x[i]^e mod n = x[i]^e
# x[i] = n ^ (1/e)

c_file = open("Secret_msg.txt","r")
c = c_file.read()

int_arr = list(map(int, c.split()))
x = []
for i in range(len(int_arr)):
    x.append(math.ceil(pow(int_arr[i],1/17)))

chars = [chr(num) for num in x]
pt = "".join(chars)
print(pt)
