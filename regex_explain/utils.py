def tokenize_pattern(pattern: str):
    tokens = []
    i = 0
    while i < len(pattern):
        if pattern[i] == "\\":
            tokens.append(pattern[i:i+2])
            i += 2
        else:
            tokens.append(pattern[i])
            i += 1

    return tokens