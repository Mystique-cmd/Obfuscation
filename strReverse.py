def reverse_obfuscate(text:str) ->str:
	return text[::-1]

if __name__ == "__main__":
	original = input ( "Enter  the string to reverse:")
	reversed = reverse_obfuscate(original)
	print(reversed)
