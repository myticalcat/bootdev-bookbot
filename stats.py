def get_num_words(txt : str) -> int:
    return len(txt.split())

def get_characters_count(txt : str) -> dict[str, int]:
    txt = txt.lower()
    count = {}
    for c in txt:
        if c not in count:
            count[c] = 0
        count[c] += 1

    return count