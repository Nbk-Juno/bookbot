def get_book_words(text):
    words = text.split()
    return len(words)

def get_book_char(text):
    char_stats = {}
    text = text.lower()
    for char in text:
        if char not in char_stats:
            char_stats[char] = 1
        else:
            char_stats[char] += 1
    return char_stats



def sort_char(char_stats):
    def sort_on(items):
        return items["num"]
    
    char_list = []
    for char, count in char_stats.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})

    char_list.sort(key=sort_on, reverse=True)
    return char_list
