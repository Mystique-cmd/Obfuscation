import random
def insert_random_whitespace(text, insertions_number=5):
    whitespace_char = [" ", "\t", "\n"]
    text_list = list(text)

    for _ in range(insertions_number):
        pos = random.randint(0, len(text_list)) #random position
        ws = random.choice(whitespace_char) #random whitespace
        text_list.insert(pos, ws)
    return "".join(text_list)

original = input( "Enter YOur Text:")
modified = insert_random_whitespace(original, num_insertions=10)
print("Modified:", repr(modified))