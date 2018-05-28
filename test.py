from Crypto.Cipher import Blowfish
from struct import pack

f = open("blowfish_secret", "r")
bs = Blowfish.block_size 
key = b'bsprak2018'
ciphertext = b'142a8d893a453dfc8400943bae3f4708d2b65ac030d3de0a682fcc4f5f2ef070afe0fe0f6f85fafdd06efad30966f25c6f0c2198c1c31cb0e547db67e2241b17d3d6eaea6570e5c6b437d1020959b3504b050cc049b68b8d'
iv = ciphertext[:bs]
ciphertext = ciphertext[bs:]

cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
msg = cipher.decrypt(ciphertext)

last_byte = msg[-1]
msg = msg[:- (last_byte if type(last_byte) is int else ord(last_byte))]
print(repr(msg))
