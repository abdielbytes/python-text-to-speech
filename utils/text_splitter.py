def split_text(text, max_length=4096):
    return [text[i:i+max_length] for i in range(0, len(text), max_length)]
