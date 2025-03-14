def get_num_words(text):
    words = text.split()
    return len(words)


def get_character_counts(text):
    counts = {}
    for character in text:
        if character == " ":
            continue
        lower = character.lower()
        if lower not in counts:
            counts[lower] = 0
        counts[lower] += 1
    return counts


COUNT_KEY = "count"


def convert_to_sorted_list(counts):
    list = []
    for key in counts:
        list.append({"character": key, COUNT_KEY: counts[key]})
    list.sort(reverse=True, key=sort_on)
    return list


def sort_on(dict):
    return dict[COUNT_KEY]

