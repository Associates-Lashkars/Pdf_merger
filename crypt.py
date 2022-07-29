from cryptography.fernet import Fernet

import codecs

 

 

   

def decryptString(p_cipherKey, p_token):

 

    # p_token = to_bytes(p_token)

    # print ("\n in method p_token: ", p_token, '\t p_cipherKey : ',  p_cipherKey )

    # if (gUtilIsDebug): print ("\n in method decrypted: ", p_cipherKey.decrypt(p_token).decode('utf-8') ) cipher.decrypt(token).decode('utf-8')

    return p_cipherKey.decrypt(p_token).decode('utf-8')

    #p_cipherKey.decrypt(p_token).decode('utf-8') 

    

    

def encryptString(p_cipherKey, P_string):

    # p_Msg = to_bytes(p_Msg)

    P_string = P_string.encode('utf-8')

    return p_cipherKey.encrypt(P_string)

 

 

if __name__ == '__main__':

 

    key = b'RWbDJAUo2IoDh76J7GGir5YadAhAlTX1fvGo2l_xPmQ='

    cipher = Fernet(key)

 

    passToken1=b'gAAAAABg8Leu3Uem7f_w6TcuNsydn0rcKo8o1AEYm9q_jS-SN5En6mlebRE9POb2pXOZL2q849dcfEE2dr3Zefy99503Kdu4kw=='

    passToken2=b'gAAAAABg8LmawOX2dajpXrDhxD41r3uBX0WAfc_QNT6_bZacW2Xz55bLFiVDWBRLM-D4CBoUNMlAYmjPz423IV0AnNcNLekbnQ=='  

    

    mypzinza = cipher.decrypt(passToken1).decode('utf-8')

    print('\n mypzinza = ', mypzinza)

 

    print ("\n in method ", decryptString(cipher,passToken1 ))

 

 

    mypzinza2 = cipher.decrypt(passToken2).decode('utf-8')

    print('\n mypzinza2 = ', mypzinza2)

   

    

    print ("YOUR KEY: ", key)

    print ("\nYOUR cipher: ", cipher)

    print ("\nYOUR pass1: ", passToken1)

    # print ("\nYOUR pass2: ", pass2)

 

 

 

# from builtins import bytes

# import base64

# from Crypto.Cipher import AES

# from Crypto.Hash import SHA256

# from Crypto import Random

 

# def encrypt(string, pzinza):

    # """

    # It returns an encrypted string which can be decrypted just by the

    # pzinza.

    # """

    # key = pzinza_to_key(pzinza)

    # IV = make_initialization_vector()

    # encryptor = AES.new(key, AES.MODE_CBC, IV)

 

    # # store the IV at the beginning and encrypt

    # return IV + encryptor.encrypt(pad_string(string))

 

# def decrypt(string, pzinza):

    # key = pzinza_to_key(pzinza)  

 

    # # extract the IV from the beginning

    # IV = string[:AES.block_size] 

    # decryptor = AES.new(key, AES.MODE_CBC, IV)

 

    # string = decryptor.decrypt(string[AES.block_size:])

    # return unpad_string(string)

 

# def pzinza_to_key(pzinza):

    # """

    # Use SHA-256 over our pzinza to get a proper-sized AES key.

    # This hashes our pzinza into a 256 bit string.

    # """

    # return SHA256.new(pzinza).digest()

 

# def make_initialization_vector():

    # """

    # An initialization vector (IV) is a fixed-size input to a cryptographic

    # primitive that is typically required to be random or pseudorandom.

    # Randomization is crucial for encryption schemes to achieve semantic

    # security, a property whereby repeated usage of the scheme under the

    # same key does not allow an attacker to infer relationships

    # between segments of the encrypted message.

    # """

    # return Random.new().read(AES.block_size)

   

# def pad_string(string, chunk_size=AES.block_size):

    # """

    # Pad string the peculirarity that uses the first byte

    # is used to store how much padding is applied

    # """

    # assert chunk_size  <= 256, 'We are using one byte to represent padding'

    # to_pad = (chunk_size - (len(string) + 1)) % chunk_size

    # return bytes([to_pad]) + string + bytes([0] * to_pad)

# def unpad_string(string):

    # to_pad = string[0]

    # return string[1:-to_pad]

 

# def encode(string):

    # """

    # Base64 encoding schemes are commonly used when there is a need to encode

    # binary data that needs be stored and transferred over media that are

    # designed to deal with textual data.

    # This is to ensure that the data remains intact without

    # modification during transport.

    # """

    # return base64.b64encode(string).decode("latin-1")

 

# def decode(string):

    # return base64.b64decode(string.encode("latin-1"))

 

 

 

# if __name__ == '__main__':

    # print ('nada')

# # import base64

# # import os

# # from cryptography.fernet import Fernet

# # from cryptography.hazmat.primitives import hashes

# # from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# # from cryptography.hazmat.backends import default_backend

# # pzinza = b"pzinza"

# # salt = os.urandom(16)

# # kdf = PBKDF2HMAC( algorithm=hashes.SHA256(),  length=32, salt=salt,iterations=100000, backend=default_backend())

# # key = base64.urlsafe_b64encode(kdf.derive(pzinza))

# # print ("\nYOUR   key : ",key)

# # f = Fernet(key)

# # token = f.encrypt(b"Secret message!")

# # print ("\nYOUR token encry : ",token)

# # f.decrypt(token)

# # print ("\nYOUR message: ", f.decrypt(token))

 

# # from cryptography.fernet import Fernet

# # sel = input("Would you like to encrypt or decrypt? (1 = encrypt, 2 = decrypt) ")

# # if sel == 1:

    # # key = Fernet.generate_key()

    # # print ("YOUR KEY: ")

    # # print (key)

    # # f = Fernet(key)

    # # inp = raw_input("Enter Text: ")  # Type here

    # # encoded = f.encrypt(inp,

    # # with open('encoded.txt', 'w') as file:

        # # file.write(encoded)

# # elif sel == 2:

    # # inp = raw_input("Enter Key: ")

    # # f = Fernet(inp)

    # # with open('encoded.txt', 'r') as file:

        # # encoded = file.readline()

    # # out = f.decrypt(encoded)

    # # print (out)

 