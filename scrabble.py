
from curses.ascii import isalpha


print("Please, choose one name ")
name = input()
while name.isalpha() != True:
    print("Error: name must contain only letters")
    print("Please, choose one name ")
    name = input()

#scrabble score
score = 0

# Dictionary with value for each letter
letter = {"a":1,"b":3,"c":3,"d":2,"e":1,"f":4,"g":2,"h":4,"i":1,"j":8,"k":5,"l":1,"m":3,"n":1,"o":1,"p":3,
"q":10,"r":1,"s":1,"t":1,"u":1,"v":4,"w":4,"x":8,"y":4,"z":10}

def sum_dict_val(str:str, dic:dict):
    """Given a string, it will sum of the value of each character and return the total amount
    
    str -- a string
    dict -- a dictionary
    """
    total = 0
    for ltr in str:
        ltr = ltr.lower()
        total += dic[ltr]
    return total

score = sum_dict_val(name, letter)
print("The total is:", score)


# Testing

def scrabble_test():
    assert sum_dict_val("cabbage",letter) == 14, 'The word cabbage should score 14'
    assert sum_dict_val("Carrot",letter) == 8, 'The word cabbage should score 14'
