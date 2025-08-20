import word_unscrambler
from src import wordler

def main():
    """
    Main function to select and run tools.
    """
    while True:
        print("\nSelect a tool:")
        print("1: Word Unscrambler")
        print("2: Wordler")
        print("q: Quit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            word_unscrambler.run()
        elif choice == '2':
            wordler.run()
        elif choice.lower() == 'q':
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
