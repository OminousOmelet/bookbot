import sys
from stats import get_word_count, get_char_count, sorted_char_list
def get_book_text(file):
    with open(file) as f:
        return f.read()

def main():
    args_list = sys.argv
    if len(args_list) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {args_list[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(args_list[1])} total words")
    print("-------- Character Count --------")
    sorted_dict = sorted_char_list(args_list[1])
    for item in sorted_dict:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")

main()
