import base64

encrypted = 'HlUeFAgME10FUkVITUYMHRNPAlJJUkoCBAMaSxcSEBdKQVFPUUsFAQAXAAQPSFoOURADFAITHxxR DkxVQhsDAhkKEkcUGQBVQUFMDhVGHxATFwAEBRtRDkxVQgcDDQQMHUsSUklSShMKDRRHAgZCUldB TBwXSBNSSVJKBwQAUQ5MVUIFBA9KSAs='
my_eyes=str.encode("ermakov.vu")
decoded=base64.b64decode(encrypted)
decrypted=""
for i in range(0,len(decoded)):
    decrypted+=chr((my_eyes[i%len(my_eyes)] ^ decoded[i]))
print(decrypted)