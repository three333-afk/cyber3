from cryptography.fernet import Fernet

key = open ("mykey.key","rb").read()

enc = Fernet(key) 
def decrypted_file(file_name):

    with open(file_name, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = enc.decrypt(encrypted_data)
        

    with open(file_name.replace(".t3_enc",".t3_dec") , "wb") as file:
        file.write(decrypted_data)


file = input("plz inter the name of file within directory to decrypt : ")

decrypted_file(file)
