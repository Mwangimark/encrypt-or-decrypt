alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

def encrypt(text,shift):
  encoded_text = []

  for i in range (0,len(text)):
    alphabet_index = alphabet.index(text[i])
    alphabet_index += shift
    
    if alphabet_index > 26 :
      alphabet_index -= 26
      
    encodedtxt = (alphabet[alphabet_index])
    encoded_text.append(encodedtxt)
  encoded_joined_text = ''.join(encoded_text)
  print(f"The coded message is : {encoded_joined_text}")



def dencrypt(text,shift):
  encoded_text = []

  for i in range (0,len(text)):
    alphabet_index = alphabet.index(text[i])
    alphabet_index -= shift

    if alphabet_index < 0 :
      alphabet_index += 26

    encodedtxt = (alphabet[alphabet_index])
    encoded_text.append(encodedtxt)
  encoded_joined_text = ''.join(encoded_text)
  print(f"The decoded message is : {encoded_joined_text}")

# =================/////////================
if direction == "encode":
  encrypt(text,shift)
elif direction == "decode":
  dencrypt(text,shift)
else:
  print("Wrong input")
# =================//////================

