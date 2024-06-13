from random import shuffle
import time
import string

#------CONSTANTS---------
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHABET = string.ascii_uppercase
NUM_COL = 4
NUM_ROW = 2

def display_table(visible):
    """
    Displays a string printed in a form of a table.
    
    Args:
        visible - a dictionary.
    Prints:
        A string table of the values of visible.
    """
    #iterating through the dictionary and printng values
    for key, val in visible.items():
        
        #left aligns with 2 spaces
        print(val.ljust(2), end = ' ')
        
        #print a new row.
        if key % NUM_COL == 0:
            print(end='\n')


def flip(visible, secret, num1, num2):
    """
    Updates a dictionary with letter strings
    at the keys of num1 and num2
    
    Args:
        visible - dictionary of number strings as values.
        secret - dictionary of letter strings as values.
        num1 - integer to identify key of a letter.
        num2 - integer to identify key of a letter.
    Return:
        a dictionary with letters shown.
    
    """
    visible[num1] = secret.get(num1)
    visible[num2] = secret.get(num2)
    return visible


def flip_back(visible, num1, num2):
    """
    Updates a dictionary with number strings at the
    keys of num1 and num2
    
    Args:
        visible - dictionary of mixed letter strings as values.
        num1 - integer to identify key of a letter.
        num2 - integer to identify key of a letter.
    Return:
        a dictionary with number strings shown.
    
    """
    visible[num1] = str(num1)
    visible[num2] = str(num2)
    return visible


def similarity(visible, secret, num1, num2):
    """
    Flips dictionaries back and forth between letter
    and number strings changing only
    the specified num1 and num2 keys.
    
    Args:
        visible - dictionary of number strings as values.
        secret - dictionary of letter strings as values.
        num1 - integer to identify key of a letter.
        num2 - integer to identify key of a letter.
    Return:
        a dictionary with letters  if the letters
        at the specified num1 and num2 keys else flip back
        after 2 seconds.
    
    """ 
    #flipping visible before checking.
    correct = flip(visible, secret, num1,num2)
    
    #if value of num1 == value of num2, then display
    # for 2 seconds then flip back.
    #else keep it flipped.
    if visible.get(num1) != secret.get(num2):
        display_table(flip(visible, secret, num1,num2))
        
        time.sleep(2) #sleep and clear screen then flip back.
        print ('\n' * 100)
        return (flip_back(visible,num1, num2))
    
    else:
        return correct


def invalid_guess(visible, secret, num1, num2):
    """
    Checks if num1 and num2 are valid keys in the dictionaries
    and are not equal.
    
    Args:
        visible - dictionary of number strings as values.
        secret - dictionary of letter strings as values.
        num1 - integer to identify key of a letter.
        num2 - integer to identify key of a letter.
    Return:
        a boolean of whether num1 and num2 are valid or not.
    
    """
    guessed = []
    for key, val in visible.items():
        
        #if value is in secret, then append its key to guessed
        if val in secret.values():
            guessed.append(key)
    return (num1 in guessed) or (num2 in guessed) or (num1 not in visible) or (num2 not in visible) or (num1 == num2)
            

def str_to_lst(alphabet):
    """
    Converts strings to lists.
    
    Args:
        alphabet: string of letters
    Return:
        a list of letters.
    
    """
    lst = []
    for letter in alphabet:
        lst.append(letter)
    return lst

def visible_dict(lst):
    """
    Converts list to dictionary.
    
    Args:
        lst: list of letters
    Return:
        a dictionary of string letters as values.
    
    """
    visible = {}
    for i in range (len(lst)):
        visible[i+1] = str(i+1)
    return visible

def make_dict(strings):
    """
    Converts string to dictionary.
    
    Args:
        strings: string of letters
    Return:
        a dictionary of string letters as values.
    
    """
    dictionary = {}
    lst = str_to_lst(strings)
    for i in range(len(lst)):
        
        #key is index+1 mapping to letters.
        dictionary[i+1] = lst[i]
    return dictionary


def play_game():
    """
    Prints board of numbers and asks for use input that
    is used to play the game.
    
    Args:
        no arguments
    Prints board using the game loop of requesting for input
    then flips numbers back and forth,
    checks if they are the same and take correct action.
    
    """
    #return suffled letters
    LETTERS = str_to_lst(ALPHABET[: NUM_COL * (NUM_ROW//2)] * 4)
    shuffle(LETTERS)
    
    #append letters to dictionary of letters.
    SECRET= make_dict(LETTERS)
    
    #make visible dictionary with numbers
    VISIBLE = visible_dict(LETTERS)
    
    #display table
    display_table(VISIBLE)
    
    #take the start time and start game loop.
    guesses = 0
    start = time.time()
    
    while True:
        x, y = map(int, input("Guess two squares: ").split())
        
        #track number of valid guesses
        guesses += 1
        #checking valid input
        while invalid_guess(VISIBLE, SECRET, x, y):
            print('Invalid number(s).')
            x, y = map(int, input("Guess two squares: ").split())
            
        #use similarity to flip and flip back.
        if similarity(VISIBLE, SECRET, x,y) != SECRET:
           
           #don't play if total number of letters
           # duplicated is more than 25
            if len(LETTERS) > 50:
                print('You can only duplicate 25 letters.')
                break
            else:
                display_table(VISIBLE)
        
        else:
            print('You win!')
            display_table(VISIBLE)
            break

    duration = time.time() - start
    print ('It took you '+ str(guesses) + ' guesses and ' + str(int(duration)) + ' seconds.')         

        
if __name__ == "__main__":
    
    play_game()
