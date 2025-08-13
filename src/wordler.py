import nltk
from nltk.corpus import words

try:
    words.words()
except LookupError:
    nltk.download('words')

# Get all 5-letter words from the NLTK words corpus, and ensure they are lowercase.
WORD_LIST = [word.lower() for word in words.words() if len(word) == 5]

def wordler(clues):
    """
    Finds possible 5-letter words based on given letters and their positions.
    :param clues: A list of strings representing clues.
                  Format "l-p": letter 'l' is at position 'p' (1-5).
                  Format "l-0": letter 'l' is in the word, but position is unknown.
                  Format "l-0-p": letter 'l' is in the word, but not at position 'p'.
    :return: A list of possible 5-letter words.
    """
    known_positions = [None] * 5
    present_letters = []
    misplaced_letters = {} # letter -> list of excluded 0-indexed positions

    for clue in clues:
        parts = clue.split('-')
        letter = parts[0].lower()
        position = int(parts[1])

        if len(parts) == 2: # e.g. "w-1" or "e-0"
            if 1 <= position <= 5:
                known_positions[position - 1] = letter
            elif position == 0:
                present_letters.append(letter)
        elif len(parts) == 3: # e.g. "e-0-1"
            if position == 0:
                excluded_pos = int(parts[2]) - 1
                if letter not in misplaced_letters:
                    misplaced_letters[letter] = []
                if excluded_pos not in misplaced_letters[letter]:
                    misplaced_letters[letter].append(excluded_pos)

    possible_words = []
    for word in WORD_LIST:
        valid = True
        # Rule 1: Check for letters in known positions.
        for i in range(5):
            if known_positions[i-1] and word[i-1] != known_positions[i-1]:
                valid = False
                break
        if not valid:
            continue

        # Rule 2: Check for presence of letters with unknown positions.
        for letter in present_letters:
            if letter not in word:
                valid = False
                break
        if not valid:
            continue

        # Rule 3: Check for misplaced letters (present, but not in specific spots)
        for letter, excluded_indices in misplaced_letters.items():
            if letter not in word:
                valid = False
                break
            for i in excluded_indices:
                if 0 <= i < 5 and word[i] == letter:
                    valid = False
                    break
            if not valid:
                break
        if not valid:
            continue
        
        possible_words.append(word)

    return possible_words

def run():
    """
    Interactively asks user for clues and finds possible Wordle words.
    """
    print("\n--- Wordler ---")
    print("Enter clues one by one. Format: letter-position.")
    print("  - Use position 1-5 if you know the exact location (e.g., 'w-1').")
    print("  - Use position 0 if the letter is present but in an unknown location (e.g., 'e-0').")
    print("  - To specify a wrong position for a present letter, add it after a second dash (e.g., 'e-0-1').")
    print("  - Press Enter without typing anything to finish entering clues.")
    
    clues = []
    while True:
        clue = input(f"Enter clue {len(clues) + 1}: ")
        if not clue:
            break
        # Basic validation could be added here
        clues.append(clue)

    if not clues:
        print("No clues entered. Returning to main menu.")
        return

    possibilities = wordler(clues)

    print(f"\nBased on clues: {', '.join(clues)}")
    if possibilities:
        print(f"Found {len(possibilities)} possible words:")
        print(', '.join(possibilities))
    else:
        print("Found no possible words with the given clues.")

