from .utils import tokenize_pattern


REGEX_MAP = {
    "^" : "start of string",
    "$" : "end of string",
    "." : "wildcard, can match any character",
    "*" : "zero or more of the preceding element",
    "?" : "zero or one of the preceding element",
    "+" : "one or more of the preceding element",
    "\\d" : "digit",
    "\\w" : "word character (letter, number, underscore)",
    "|" : "or operator, match the element on either side"
}



def explain_regex (pattern: str) -> str:
    tokens = tokenize_pattern(pattern)
    explanation = []
    
    for token in tokens:
        meaning = REGEX_MAP.get(token, f"(no explanation for {token})")
        explanation.append(f"{token:8} -> {meaning}")

    return "\n".join(explanation)
