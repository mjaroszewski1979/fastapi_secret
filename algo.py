from random import randint

# Random multiplier generator
mltplr = randint(99, 999)

# Random key generator
key = randint(99, 999)

# Data dictionary of lowercase or uppercase letters, numbers and special characters: 
# '.', '(', ')', '-', '>', '<', '?', '!', ';', ':', '{', '}', '[', ']', ',', '"', tab, new line and space
chars = {

    'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4,

    'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8,

    'i' : 9, 'j' : 10, 'k' : 11, 'l' : 12,

    'm' : 13, 'n' : 14, 'o' : 15, 'p' : 16,

    'q' : 17, 'r' : 18, 's' : 19, 't' : 20,

    'u' : 21, 'v' : 22, 'w' : 23, 'x' : 24,

    'y' : 25, 'z' :26, ' ' : 100, 'A' : 101,

    'B' : 102, 'C' : 103, 'D' : 103, 'E' : 104,

    'F' : 105, 'G' : 106, 'H' : 107, 'I' : 108,

    'J' : 109, 'K' : 110, 'L' : 111, 'M' : 112,

    'N' : 113, 'O' : 114, 'P' : 115, 'Q' : 116,

    'R' : 117, 'S' : 118, 'T' : 119, 'U' : 120,

    'V' : 121, 'W' : 122, 'X' : 123, 'Y' : 124,

    'Z' : 125, '.' : 200, '(' : 201, ')' : 202,

    '-' : 203, '>' : 204, '<' : 205, '?' : 206, 
    
    ';' : 207, ':' : 208, '{' : 209, '}' : 210, 
    
    '[' : 211, ']' : 212, '`' : 213, '!' : 214, 
    
    ',' : 215, '"' : 216, '\n' : 217, '\t' : 218,
    
    '0' : 300, '1' : 301, '2' : 302, '3' : 303, 
    
    '4' : 304, '5' : 306, '6' : 307, '7' : 308, 
      
    '8' : 309, '9' : 310 }

# Defining encryption algorithm
def enc_algo(password, key=key):
    num = randint(99, 999)

# Creating a list of numbers corresponding to individual characters in the password
    enc_list= list(chars[i] for i in str(password))
    my_cipher = [num]

# Applying encryption to each character 
    for i in enc_list:
        my_cipher.append((mltplr * i) + int(num + key))

# Returning encrypted string
    my_cipher = "" + ",".join((map(str, my_cipher))) + ""
    return my_cipher
    

# Defining decryption algorithm
def dec_algo(my_cipher, key=key):
    enc_list = eval(my_cipher, {"__builtins__": {'list' : list}})

# Getting first item from encrypted list
    read_num = enc_list[0]

# Reversing encryption process
    dec_items = list(int((i - int(read_num + key)) / mltplr) for i in enc_list)

# Creating a list of characters
    decrypted = list(k for i in dec_items for k,v in chars.items() if v == i)

# Returning decrypted string
    decrypted_str = "".join((map(str, decrypted))) + ""
    return decrypted_str