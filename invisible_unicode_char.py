import re
from typing import Iterable

INVISIBLE_CHARS = {
	"\u200B",	#Zero width space
	"\u200C",	#Zero width non-joiner
	"\u200D",	#Zero width joiner
	"\u2060",	#Word joiner
	"\uFEFF",	#Zero width no-break space /BOM
}

INVISIBLE_RE = re.compile(f"[{".join(INVISIBLE_CHARS)"}]")

def has_invisible(text:str, targets: Iterable[str] = INVISIBLE_CHARS) -> bool:
	patttern = re.compile(f"[{".join(targets)"}]")
	return bool(patttern.search(text))
	
def remove_invisible(text: str, targets: Iterable[str] = INVISIBLE_CHARS) -> str:
	pattern = re.compile(f"[{".join(targets)"}]")
	return pattern.sub("", text)
	
def replace_invisible(text: str, repl: str = "[ZW]", targets: Iterable[str] = INVISIBLE_CHARS) -> str:
	pattern = re.compile(f"[{".join(targets"}]")
	return pattern.sub(repl, text)
	
def insert_zero_width_space(text: str, interval: int = 3) -> str:
	if interval <= 0 :
		raise ValueError ("intervals must be >= 1")
	
	zws = "\u200B"
	out = []
	for i , ch in enumerate(text):
		out.append(ch)
		if( i+1)% interval == 0 and (i+1) != len(text):
			out.append(zws)
	return "".join(out)
	
def inject_invisible_watermark(text: str, key:str = "01") -> str:
	bit_map = {"0": "\u200b", "1" : "\u200C"}
	bits = [bit_map.get(b, "\u200B") for b in key]
	if not bits:
		return text
		
	out = []
	bi = 0
	for ch in text:
		out.append(ch)
		if ch.isalnum():
			out.append(bits[bi])
			bi = (bi + 1)% len(bits)
	return "".join(out)

if __name__ == "__main__":
	user_input = input("Enter a string: ")
	
	# Example: Insert zero-width spaces
	obfuscated_text = insert_zero_width_space(user_input, interval=3)
	print(f"Obfuscated with ZWS: {obfuscated_text}")
	
	# Example: Check for invisible characters
	if has_invisible(obfuscated_text):
		print("The obfuscated text contains invisible characters.")
	
	# Example: Remove invisible characters
	cleaned_text = remove_invisible(obfuscated_text)
	print(f"Cleaned text: {cleaned_text}")
	
	# Example: Inject watermark
	watermarked_text = inject_invisible_watermark(user_input, key="0101")
	print(f"Watermarked text: {watermarked_text}")
	
	# Example: Replace invisible characters
	replaced_text = replace_invisible(watermarked_text)
	print(f"Replaced invisible chars: {replaced_text}")
