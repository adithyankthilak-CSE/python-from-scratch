import random
import string

characters = string.ascii_letters + string.digits + string.punctuation
characters = list(characters)
keys = characters.copy()

random.shuffle(keys)

#print(f"characters are {characters}")
#print(f"keys are {keys}")

#encription
plain_text = input("Enter the text to be encrypted: ")
encrypted_text = " "
for letter in plain_text:
    index=characters.index(letter)
    encrypted_text += keys[index]
print(f"encrypted text is :{encrypted_text}")

#decription
print("**************************************")
encrypted_text = input("Enter the text to be decrypted: ")
plain_text = " "
for letter in encrypted_text:
    index=keys.index(letter)
    plain_text += characters[index]
print("**************************************")
print(f"decripted text is :{plain_text}")
print(f"encripted text is :{encrypted_text}")
print("**************************************")