def unique_ordered(seq):
    seen = set()
    result = []
    for item in seq:
        item_lower = item.lower()
        if item_lower not in seen:
            seen.add(item_lower)
            result.append(item)
    return result

def contains_cyrillic(text):
    return any('а' <= ch <= 'я' or 'А' <= ch <= 'Я' for ch in text)
