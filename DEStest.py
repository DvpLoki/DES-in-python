from StdDES import DES
plaintext=b'thisiste'
key=b'mysecret'
d=DES(key)
c=d.encrypt(plaintext)
de=d.decrypt(c)
print(f'plaintext:{plaintext}\nkey:{key}\nciphertext:{c}\nDecrypted text:{de}')