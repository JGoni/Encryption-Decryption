#!/usr/bin/python3
import math
text = input('Type here: ')
shift = int(input ('Shift? : '))
text_List = list(text)

# # Encrytion method 
def Encrypt (t, s) :
        encrypt = list()
        n = shift % 26
        for i in range(0, len(text)):
                char = text[i]
                # if character is uppercase letter
                if(char.isupper()):
                        encrypt += chr((ord(char)-65+n)%26+65) 
                # if character is in lower case
                else :
                        encrypt += chr((ord(char)-97+n)%26+97)
                
        return encrypt   

# Decrytion method
def Decrypt (t, s) :
        decrypt = list()
        n = shift % 26
        for i in range(0, len(text)):
                char = text[i]
                # if character is uppercase letter
                if(char.isupper()):
                        decrypt += chr((ord(char)-65-n)%26+65) 
                # if character is in lower case
                else :
                        decrypt += chr((ord(char)-97-n)%26+97)
        return decrypt   

# Collecting User choice to select Encrytion or Cryption
choose = int(input ( 'Press \n 1 to Encrypt text \n 2 to Decrypt text \n => '))
if (choose == 1) :
        print ('Encrypting : ')
        result = Encrypt(text,shift)
        
elif (choose == 2) :
        print ('Decrypting : ')
        result = Decrypt(text,shift)

else :
        print ('Unknown Input')
print(result)

# Columnar Transposition

key_length = int(input('Key length: '))

# Columnar Decryption
x= math.ceil(len(text)/key_length)
def columnar (t, K) :
        for i in range(0, len(t), K):
                yield t[i:i+K]
list_using_key = list(columnar(result, x))

print(*(list_using_key), sep = "\n")
Columnar_decrypted_list = list()
for j in range (0, len(list_using_key[0])) :
        for i in list_using_key :
                 Columnar_decrypted_list += i[j]        
                                     
        j+=1
print(*Columnar_decrypted_list)

l = list(columnar(Columnar_decrypted_list, key_length))  
print(*(l), sep='\n') 

# print(*list(columnar(result, x)), sep = "\n")          

