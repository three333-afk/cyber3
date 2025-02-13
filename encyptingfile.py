from cryptography.fernet import Fernet

key = Fernet.generate_key()
enc = Fernet(key)
with open("mykey.key","wb") as k:
    k.write(key)
def encrypted_file(file_name):

    with open(file_name, 'rb') as file:
        file_data = file.read()

        encrypted_data = enc.encrypt(file_data)
        

    with open(file_name + ".t3_enc" , 'wb') as file:
        file.write(encrypted_data)


file = input("plz inter the name of file within directory to encrypt : ")

encrypted_file(file)

