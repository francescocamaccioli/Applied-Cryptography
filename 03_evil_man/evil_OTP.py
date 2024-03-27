#!/usr/bin/env python3
import random
import sys
import time
#I take the time in which i am encrypting
seed = time.time()
random.seed(seed)
seed_enc = str(seed).encode('ASCII')

#I want to encrypt a very secret message...
msg = input('Your message: ').encode('ASCII')

#Therefore i generate a key with length equal to the message!
key = [random.randrange(256) for _ in msg]

#OTP is PERFECTLY SECURE when len(m)==len(k)! No Way somebody will decrypt my message!
c = [m ^ k for (m,k ) in zip(msg + seed_enc, key + [0x88]*len(seed_enc))]

#Saving my cyphertext as bytes!
with open("deepest_secrets.txt", "wb") as f:
    f.write(bytes(c))

