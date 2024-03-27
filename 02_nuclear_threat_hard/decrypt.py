# We first obtain the first 6 chars of the used key by XOR-ing the cyphertext with "From: ", then we obtain the randomly generated values of A and C by solving the related modular algebra system.

ct_file = open("captured_ct.txt", "rb")
ciphertext = ct_file.read()

start = [70, 114, 111, 109, 58, 32]

key = []
key += [a ^ b for (a, b) in zip(start, ciphertext[0:6])]
print(f"Key[0-6]: ", key)

# system:
# key[1] = (A * key[0] + C) % 256
# key[2] = (A * key[1] + C) % 256
A = 0
C = 0
for A in range(2**128):
    C = (key[1] - key[0]*A) % 256
    if (key[1]*A + C) % 256 == key[2]:
        print(f"Modular Algebra System's Solutions: A = {A}, C = {C}")
        break

#Once we have A and C, we can generate the entire used key and finally XOR-ing the entire key with the cyphertext to get the plaintext

pt = []
ki = key[0]
for i in range(len(ciphertext)):
    pt.append(ki ^ ciphertext[i])
    ki = (A * ki + C) % 256

ascii_characters = [chr(num) for num in pt]
pt = "".join(ascii_characters)
print(f'Plaintext: "{pt}"')
