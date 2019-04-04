def hangman(word):
    """starts hangman game.

    Args:
        word(str): a word that player the 2 wants to find.
      """

    # counts how many times the player 2 gets a wrong answer.
    wrong = 0
    
    # As the player 2 makes a mistake, each line of this image will show up.
    stages = ["",
         "________        ",
         "|               ",
         "|        |      ",
         "|        0      ",
         "|       /|\     ",
         "|       / \     ",
         "|               "
          ]

    # separates the given word into letters and put them to a list.
    rletters = list(word)

    # makes a hint for the player 2.
    # an initial board for "cat" is ["_", "_", "_"]
    board = ["_"] * len(word)

    # boolen variable to indicate whether the player 2 wins.
    win = False

    # initial announcement.
    print("Welcome to HANGMAN")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Predict one letter."
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
   
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break

  if not win:
    print("\n".join(stages[0:wrong+1]))
    print("You lose. The answer is {}.".format(word))

hangman("sofisticated")
