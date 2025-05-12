from stats import get_words 

import sys

def get_book_text(filePath):
    with open(filePath) as f:
        redFile = f.read()
    get_words(redFile)
    #print(redFile)




def main(filePath):
    get_book_text(filePath)


if len(sys.argv) < 2 :
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    filePath = sys.argv[1]
    main(filePath)
    #print(sys.argv)