import random
import time

ct_file = open("deepest_secrets.txt", "rb")
ciphertext = ct_file.read()
print(ciphertext)

actual_seed = str(time.time()).encode('ASCII')
len_seed = len(actual_seed)

msg_len = len(ciphertext) - len_seed
print (f"Ciphertext length: {len(ciphertext)}; Seed length: {len_seed}; Message length: {msg_len}")

# We know that the seed is at the end of the message, and that it was encrypted by xoring it with 0x88.
# I reverse the ciphertext so that in rev_ciphertext I have the encrypted seed in the reverse order;
# I decrypt each of its byte with 0x88; then, I reverse it to find the seed used to generate the key.
rev_ciphertext = ciphertext[::-1]
decription_seed = [c ^ k for (c, k) in zip(rev_ciphertext[0:len_seed], [0x88] * len_seed)]
decription_seed = decription_seed[::-1]
str_seed = ''.join([chr(i) for i in decription_seed])
print(f"Seed used to encrypt: {str_seed}")

# Now I use the seed to generate the encryption key
seed = float(str_seed)
random.seed(seed)
key = []
for i in range(msg_len):
    key+=[random.randrange(256)]
print(f"The key used to encrypt was: {key}")

# Obtain the plaintext computing the XOR of the ciphertext with the key.
plaintext = [c ^ k for (c,k ) in zip(ciphertext[0:msg_len], key)]
print(''.join([chr(i) for i in plaintext]))
