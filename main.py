import sys
from collections import Counter
import nltk

def find_possible_words(letters, word_list):
    """
    Finds all words from a word_list that can be formed using the given letters.
    """
    letters_lower = letters.lower()
    letter_counts = Counter(letters_lower)
    required_char = letters_lower[0]
    possible_words = []

    for word in word_list:
        word = word.strip().lower()
        if not word or len(word) <= 4 or required_char not in word:
            continue
        
        word_counts = Counter(word)
        is_possible = all(letter_counts[char] >= count for char, count in word_counts.items())

        if is_possible:
            possible_words.append(word)
            
    return possible_words

def main():
    """
    Main function to run the word finder.
    """
    # Use NLTK's word corpus instead of a local file.
    try:
        from nltk.corpus import words
        word_list = words.words()
    except LookupError:
        print("NLTK 'words' corpus not found. Downloading...")
        try:
            nltk.download('words')
            from nltk.corpus import words
            word_list = words.words()
        except Exception as e:
            print(f"Error downloading 'words' corpus: {e}")
            print("Please ensure you have an internet connection or download it manually.")
            sys.exit(1)
    except ImportError:
        print("Error: NLTK library not found. Please install it using 'pip install nltk'")
        sys.exit(1)

    while True:
        input_letters = input("Enter 7 letters (or 'quit' to exit): ")
        if input_letters.lower() == 'quit':
            break
        if len(input_letters) != 7 or not input_letters.isalpha():
            print("Invalid input. Please enter exactly 7 alphabetic characters.")
            continue

        found_words = find_possible_words(input_letters, word_list)

        if found_words:
            print(f"\nFound {len(found_words)} possible words:")
            # Sort by length, then alphabetically
            found_words.sort(key=lambda x: (len(x), x))
            for word in found_words:
                print(word)
        else:
            print("No words could be formed from those letters.")
        print("-" * 20)

if __name__ == "__main__":
    main()
