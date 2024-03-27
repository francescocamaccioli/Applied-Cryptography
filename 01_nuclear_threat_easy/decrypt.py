A = 1103515245
C = 12345
n = 2 ** 31

ct_file = open("captured_ct_easy.txt", "rb")
ciphertext = ct_file.read()

start = [70, 114, 111, 109]

key = []
key += [a ^ b for (a, b) in zip(start, ciphertext[0:4])]

pt = []
pt += [a ^ b for (a, b) in zip(key, ciphertext[0:4])]

ki = 0
for i in range(3, -1, -1):
    ki += key[i]
    if i != 0: ki = ki << 8
ki_p = (A * ki + C) % n

pt = []
for i in range(1, int(len(ciphertext) / 4)):
    ki_b = [ki_p % 256, (ki_p >> 8) % 256, (ki_p >> 16) % 256, (ki_p >> 24) % 256]
    pt += [a ^ b for (a, b) in zip(ki_b, ciphertext[i * 4:i * 4 + 4])]
    ki_p = (A * ki_p + C) % n

result_string = ''.join([chr(int_val) for int_val in pt])
print(f'"From {result_string}"')
