# read from file the encrypted message that contains the code
ct_file = open("./captured/cap_transaction.enc", "rb")
ct = ct_file.read()

print(f"Captured ciphertext: {ct}")

print(f"ct lenght = {len(ct)}")

# I have to switch block 2 with block 5
new_ciphertext = ct[0:16] + ct[64:80] + ct[32:64] + ct[16:32] + ct[80:]

print(f"Modified ciphertext: {new_ciphertext}")

# I write the modified ciphertext in the transaction.enc file
with open("transaction.enc", "wb") as f:
    f.write(bytes(new_ciphertext))
