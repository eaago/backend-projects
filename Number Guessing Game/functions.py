import os

def clear_screen(attempt):
    if os.name == 'nt':
        _ = os.system('cls')
        print("===============================================================")
        print("=     _  _ _  _ _  _ ___  ____ ____    ____ ____ _  _ ____    =")
        print("=     |\ | |  | |\/| |__] |___ |__/    | __ |__| |\/| |___    =")     
        print("=     | \| |__| |  | |__] |___ |  \    |__] |  | |  | |___    =")                                    
        print("=                                                             =")
        print("===============================================================")
        if attempt == 0:
            print(f"\nWelcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 10.")
        else:
            print(f"\nWelcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 10.\nYou'll have {attempt} chances to guess the correct number.")

def select_difficulty():
    message = ""
    choice = 0
    while True:
        clear_screen(0)
        print(message)
        try:
            choice = int(input("Please select the difficulty level.\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)\n\nEnter your choice: "))
            if choice < 1 or choice > 3:
                message = "\nInvalid input. Please try again.\n"
            else:
                if choice == 1:
                    print("Easy difficulty selected.")
                elif choice == 2:
                    print("Medium difficulty selected")
                elif choice == 3:
                    print("Hard difficulty selected.")
                return choice
        except:
            message = "\nInvalid input. Please try again.\n"