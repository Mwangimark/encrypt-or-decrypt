import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

def encrypt(text,shift):
  encoded_text = []

  for i in range (0,len(text)):
    if text[i] in alphabet:
      alphabet_index = alphabet.index(text[i])
      alphabet_index += shift
      
      if alphabet_index > 26 :
        alphabet_index -= 26
        
      encodedtxt = (alphabet[alphabet_index])
      encoded_text.append(encodedtxt)
    else:
      encoded_text.append(text[i])
  encoded_joined_text = ''.join(encoded_text)
  print("The coded message is : "+encoded_joined_text)



def dencrypt(text,shift):
  encoded_text = []

  for i in range (0,len(text)):
    if text[i] in alphabet:
      alphabet_index = alphabet.index(text[i])
      alphabet_index -= shift
  
      if alphabet_index < 0 :
        alphabet_index += 26
  
      encodedtxt = (alphabet[alphabet_index])
      encoded_text.append(encodedtxt)
    else :
      encoded_text.append(text[i])
  encoded_joined_text = ''.join(encoded_text)
  print("The decoded message is : "+encoded_joined_text)

gaming = True

while gaming:
    direction = input("Type 'encode' to encrypt, 'decode' to decrypt :").lower()

    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    if shift > 26:
        shift = shift % 26

    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        dencrypt(text, shift)
    else:
        print("Wrong input")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "no":
        gaming = False
        print("Goodbye!")


