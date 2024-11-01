alphabets=["a","b","c","d","e","f","g"
           ,"h","i","j","k","l","m","n"
           ,"o","p","q","r","s","t","u",
           "v","w","x","y","z","a","b","c","d","e","f","g"
           ,"h","i","j","k","l","m","n"
           ,"o","p","q","r","s","t","u",
           "v","w","x","y","z"]


direction=input("Enter the 'encode' to encode your message or 'decode' to decode your message: \n")
text=input("Enter your message: \n")
shift=int(input("Enter the number of shift you want: \n"))

def encrypt(plain_text,shift_amount):
    cipher=""
    for letter in plain_text:
        position=alphabets.index(letter)
        new_position=position+shift_amount
        new_letter=alphabets[new_position]
        cipher+= new_letter
    print(f" the encoded message will be {cipher}")
 
def decrypt(cipher,shift_amount):
    plain_text=""

    for letter in cipher:
        position=alphabets.index(letter)
        new_position= position-shift_amount
        plain_text += alphabets[new_position]
    print(f"the decoded text is {plain_text}")



if direction=="encode":
 encrypt(plain_text=text,shift_amount=shift)
elif direction=="decode":
   decrypt(cipher=text,shift_amount=shift)