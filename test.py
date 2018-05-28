from Crypto.Cipher import Blowfish
from struct import pack

f = open("blowfish_secret", "r")
bs = Blowfish.block_size 
key = b'bsprak2018'
ciphertext = f
iv = ciphertext[:bs]
ciphertext = ciphertext[bs:]

cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
msg = cipher.decrypt(ciphertext)

last_byte = msg[-1]
msg = msg[:- (last_byte if type(last_byte) is int else ord(last_byte))]
print(repr(msg))
