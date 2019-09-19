"""
Author: Ariella Cohen
Date: 09/19/2019
Project: Pickle Robot Python Challenge

"""

import itertools
import random

num2letters = {0:["0","0","0"],1:["1","1","1"],2:["A","B","C"],3:["D","E","F"],4:["G","H","I"],5:["J","K","L"],
        6:["M","N","O"],7:["P","Q","R","S"],8:["T","U","V"],9:["W","X","Y","Z"]}

def read_words(filename):
    """
    This function reads in a file line by line getting rid of the last two characters
    on each line (\n)
    """
    words = open(filename, 'r')
    word_list = []
    for word in words:
        word_list.append(word[0:len(word)-1].upper())
    return word_list

def number_to_words(phone_number):
    """
    This function reads in a phone number of type string and returns a single 
    "wordified" version of the phone number
    """
    #read in list of all English words
    all_words = read_words("words_alpha.txt")
    possible_letters = []
    combo_words = []
    word_idx = []
    
    #go through all of the numbers and create a list of the letters that go
    #with each number
    for i in range (5,len(phone_number)):
        try:
            possible_letters.append(num2letters[int(phone_number[i])])
        #for a dash
        except ValueError:
            continue 
    #create all possible combinations of letters related to each number
    inputdata = possible_letters
    combos = list(itertools.product(*inputdata))
    #convert each tuple to a string
    combos = [''.join(i) for i in combos]
    
    area_code = phone_number[0:6]
    #get rid of the dash in the phone number
    new_phone = phone_number[0:9]+phone_number[10:]
    
    #create list of all words that are found within a phone number and the index
    #at which they are found
    for word in all_words:
        for combo in combos:
            if word in combo and word not in combo_words:
                word_idx.append(combo.find(word))
                combo_words.append(word)
    
    random_idx = random.randint(0,len(combo_words))
    
    #create the final wordified phone number
    if word_idx[random_idx] != 0:
        final_number = area_code + new_phone[6:(word_idx[random_idx]+6)] + "-" + combo_words[random_idx] + \
        "-" + new_phone[word_idx[random_idx]+6+len(combo_words[random_idx]):]     
    else:
        final_number = area_code + new_phone[6:(word_idx[random_idx]+6)] + combo_words[random_idx] + "-" + \
        new_phone[word_idx[random_idx]+6+len(combo_words[random_idx]):]     
    
    if final_number[-1] == "-":
        final_number = final_number[0:len(final_number)-1]
    return final_number       
    
def words_to_number(phone_number):
    """
    This function reads in a "wordified" phone number of type string and
    returns the phone number in all numbers
    """
    letters_list = []
    new_numbers = ""
    #create main list including lists of letters corresponding to numbers
    for i in range(2,len(num2letters)):
        letters_list.append(num2letters[int(i)])

    #add each number to a string    
    for character in phone_number:
        for i in range (len(letters_list)):
            if character in letters_list[i]:
                new_numbers += str(i+2)
        #add the character to the string of numbers if it is already an int
        try:
            char = int(character)
            new_numbers += character
        except ValueError:
            continue
    #create final phone number after all letters have been changed to numbers        
    final_number = new_numbers[0] + "-" + new_numbers[1:4] + "-" + new_numbers[4:7] + "-" + new_numbers[7:]
    return final_number
 
def all_wordifications(phone_number):
    """
    This function reads in a phone number of type string and returns a list of
    all English "wordified" versions of this phone number
    """
    #read in list of all English words
    all_words = read_words("words_alpha.txt")
    possible_letters = []
    combo_words = []
    word_idx = []

    #go through all of the numbers and create a list of the letters that go
    #with each number
    for i in range (5,len(phone_number)):
        try:
            possible_letters.append(num2letters[int(phone_number[i])])
        #for a dash
        except ValueError:
            continue 
        
    #create all possible combinations of letters related to each number
    inputdata = possible_letters
    combos = list(itertools.product(*inputdata))
    #convert each tuple to a string
    combos = [''.join(i) for i in combos]
    
    area_code = phone_number[0:6]
    #get rid of the dash in the phone number
    new_phone = phone_number[0:9]+phone_number[10:]
    
    #create list of all words that are found within a phone number and the index
    #at which they are found
    for word in all_words:
        for combo in combos:
            if word in combo and word not in combo_words:
                word_idx.append(combo.find(word))
                combo_words.append(word)
    all_numbers = []
    #create the final wordified phone number
    for i in range (len(word_idx)):
        if word_idx[i] != 0:
            final_number = area_code + new_phone[6:(word_idx[i]+6)] + "-" + combo_words[i] + "-" + \
            new_phone[word_idx[i]+6+len(combo_words[i]):]     
        else:
            final_number = area_code + new_phone[6:(word_idx[i]+6)] + combo_words[i] + \
            "-" + new_phone[word_idx[i]+6+len(combo_words[i]):]     
        if final_number[-1] == "-":
            final_number = final_number[0:len(final_number)-1]
        #add all possible wordified phone numbers to a list
        all_numbers.append(final_number)
    return all_numbers
    
if __name__ == '__main__':
    wordification = number_to_words('1-800-407-2563')
    print(wordification)
    print(words_to_number(wordification))
    all_wordifications('1-800-407-2563')

    