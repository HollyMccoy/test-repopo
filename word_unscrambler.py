import sys
from collections import Counter
import nltk

def find_possible_words(letters, word_list):
    """
    Return words from word_list that can be formed from the provided letters.
    
    The comparison is case-insensitive. A candidate word is included only if:
    - it is non-empty,
    - its length is greater than 4,
    - it contains the first character of `letters` (after lowercasing),
    - and every character in the candidate appears no more times than it does in `letters`.
    
    Parameters:
        letters (str): Source letters used to form words (case-insensitive).
        word_list (iterable[str]): Iterable of candidate words (strings).
    
    Returns:
        list[str]: Matching words from word_list (lowercased and stripped).
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

def run():
    """
    Run an interactive word-unscrambler REPL using the NLTK words corpus.
    
    This function loads the NLTK word list (attempting to download the 'words' corpus if missing), then enters a loop prompting the user to enter exactly seven alphabetic characters or 'quit' to exit. For each valid input it calls find_possible_words to compute all candidate words that can be formed from the letters, prints a count and the matching words sorted by length then alphabetically, and repeats. If the NLTK library or corpus cannot be loaded/downloaded, the function prints an explanatory message and returns.
    
    Side effects:
    - Reads from standard input and writes messages to standard output.
    - May attempt to download the NLTK 'words' corpus if it is not available.
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
            return
    except ImportError:
        print("Error: NLTK library not found. Please install it using 'pip install nltk'")
        return

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
