def get_words(text):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    word_list = text.split()
    print(f"Found { len(word_list) } total words")
    print("--------- Character Count -------")
    get_char_count(text)
    print("============= END ===============")

def get_char_count(text):
    dict_char = {}
    for i in text.lower():
        if not dict_char.get(i):
            dict_char[i] = 1
        else:
            dict_char[i] += 1
    sorted_dict(dict_char)


def sorted_dict(charDict):
    sorted_Dict = []
    for i in charDict:
        if i.isalpha():
            sorted_Dict.append({
                "char" : i,
                "num" :  charDict[i]

            })
    sorted_Dict.sort(reverse=True, key=sort_on)

    for i in sorted_Dict:
        print(f"{i['char'] }: {i['num']}")
    #print(sorted_Dict)


def sort_on(dict):
    return dict["num"]





