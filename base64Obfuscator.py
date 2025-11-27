import base64

input = input("Enter the string to be obfuscated: ").encode()

obfuscated = base64.b64encode(input).decode()
print("Obfuscated string:", obfuscated)

