import sys

def main():
    word = input("word: ")
    character_count = dict() #using a dict. placing the word in dict then iterating through it

    for letter in word:
        character_count[letter] = word.count(letter)

        print(type(word))
        print(f"character_count: {character_count}")
    return 0

if __name__ == "__main__":
    sys.exit(main())