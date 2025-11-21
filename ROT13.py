import codecs

text = input("Enter text to encode/decode with ROT13: ")
rot13_text = codecs.encode(text, 'rot_13')
print("ROT13 result:", rot13_text)

decoded_text = codecs.decode(rot13_text, 'rot_13')
print("Decoded back to original:", decoded_text)
