

# Building a Cipher in FreeCodeCamp
# Loop allows you to systematically go through a sequence of elements and execute actions on each one.

# Variables 
## SHIFT shifts which letter is read in the alphabet by '3' to the right
# .find() returns the index of the matching character insid the string

# !!!!! CAESAR CIPHEERRR!!!!!!
text = 'Hello Zaira'
shift = 3
def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_message = ''
    for char in message.lower(): # 'for' loop, 'char' is a variable that sequentially takes the value of the elements in text
        if char == ' ': # Adds a space to the cipher if there is a space in the text str
            encrypted_message += char 
        else:
            index = alphabet.find(char) # Value is what is RETURNED BY alphabet.find(char) 
            new_index = (index + offset) % len(alphabet) # mod lets the loop returnt he remainder of the the two numbers.
            encrypted_message += alphabet[new_index] 
    print('plain message:', message)
    print('encrpyted message:', encrypted_message)
caesar(text, shift)
caesar(text, 10)

# THIS IS ALL DELETED IN FAVOR FOR A LOOP 
# HIDING IN COMMENT
# index = alphabet.find(text[0].lower()) 
# print(index)
# print(text.lower())  # .lower() - Prints Hello World in all LOWER CASE
# shifted = alphabet[index + shift] # accesses the value of 'alphabet' at 'index' and adds the shift var. 
# print(shifted)
# This print shows 'h' is at index '7' in the 'alphabet' string



#TRANSFORMING INTO VIGENERE CIPHER !!!!!

text = 'Goodmorning Dave'
text2 = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding' # 'python'

def vigenere(message, key, direction = 1): # offset to key, added direction for encryption
    key_index = 0 # since the key is shorter then the text I am encrypting, this will help repeat it. 
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''
    for char in message.lower(): # 'for' loop, 'char' is a variable that sequentially takes the value of the elements in text
        if not char.isalpha(): # Appends any non letter character to the message
            final_message += char 
        else:
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1 
            
            # define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char) 
            index = alphabet.find(char) # Value is what is RETURNED BY alphabet.find(char) 
            new_index = (index + offset * direction) % len(alphabet) # mod lets the loop return the remainder of the the two numbers.
            final_message += alphabet[new_index] 
            
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
def decrypt(message, key):
    return vigenere(message, key, -1)
# CANT FIGURE OUT HOW TO GET NORMAL ENCRYTION TO RUN AFTER CHANGING DECRYPTION AND ADDING ENCRYPT/DECRYPT FUNCS
encryption = encrypt(text, custom_key) # no need to call ,1 after custom_key as 1 is the default in direction parameter
print(encryption)
decryption1 = vigenere(text, custom_key, -1)
print(decryption1)  

decryption = decrypt(text2, custom_key)

print(f'\nEncrypted text: {text2}') # \n adds a new line/line break
print('Key: ' + custom_key)
print(f'\nDecrypted text: {decryption}\n')

