def number_of_words(text):
    words_list = text.split()
    num_words = len(words_list)
    print(f"Found {num_words} total words")

def number_of_chars(text):
    chars = list(text.lower())
    chars_dict = {}
    for char in chars:
        if char.isalpha():
            if char not in chars_dict:
                chars_dict[char] = 1
            else:
                chars_dict[char] += 1
    sorted_chars = sorted(chars_dict.items(), key=lambda item: item[1], reverse=True)
    for char, count in sorted_chars:
        print(f"{char}: {count}")


