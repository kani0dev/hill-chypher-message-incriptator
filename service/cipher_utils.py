import re
import unicodedata


def clean_text(text: str) -> str:
    clean = unicodedata.normalize("NFKD", text.lower()).encode("ascii", "ignore").decode("utf-8")
    return re.sub(r"[^a-z]", "", clean)


def pad_text(text: str, block_size: int, pad_char: str = "x") -> list[str]:
    tokens = [text[i:i+block_size] for i in range(0, len(text), block_size)]
    if len(tokens[-1]) < block_size:
        tokens[-1] = tokens[-1].ljust(block_size, pad_char)
    return tokens


def chars_to_nums(tokens: list[str]) -> list[list[int]]:
    return [[ord(c) - ord("a") for c in token] for token in tokens]


def nums_to_chars(nums: list[list[int]]) -> str:
    return "".join("".join(chr(num + ord("a")) for num in triplet) for triplet in nums)
