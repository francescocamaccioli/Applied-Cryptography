# Decrypting the message
M = 837779756984826573847982

# Convert the decrypted message to ASCII
combination = str(M)

# Convert ASCII to characters
combination_ascii = ''.join(chr(int(combination[i:i+2])) for i in range(0, len(combination), 2))

print("Decrypted combination (ASCII):", combination_ascii)
