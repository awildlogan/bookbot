def main(): #we start with function calls and print statements
    book_path = "books/frankenstein.txt"
    text = word_reading_function(book_path)
    word_count = word_counting_function(text)
    chars_ina_dict = character_counting_function(text)
    sorted_chars = char_dict_sorted_list(chars_ina_dict)
    
    
    print(f"--- Begin report of {book_path} --- ")
    print(f"There are {word_count} words in this file")
    
    for entry in sorted_chars:
        if entry['char'].isalpha():
            print(f"{entry['char']}: {entry['num']}")
    
    print("End Report")
    
       
    
def word_reading_function(book_path): #this function opens and reads the file
    with open (book_path) as f:
        return f.read()

def word_counting_function(text): # this function splits the text and returns the word count
    words = text.split()
    return len(words)
    
def character_counting_function(text): # this function counts characters and returns a count via dictionary
    char_dict = {}
    for char in text:
        lowered = char.lower()
        if lowered in char_dict:
            char_dict[lowered] += 1
        else:
            char_dict[lowered] = 1
    return char_dict

def character_sorting(char_dict): # this function takes the char_dict and returns the value of the num key
    return char_dict["num"]

def char_dict_sorted_list(char_dict):
    sorted_list = []
    for ch in char_dict:
        sorted_list.append({"char": ch, "num": char_dict[ch]})
    sorted_list.sort(reverse=True, key=character_sorting)
    return sorted_list

main()