#!/usr/bin/env python

# Importing the necessary modules
import os
from cryptography.fernet import Fernet


# Creating a class to load the encrypted password, token, and secret keys.
class Encryption:
    def __init__self(self):
        pass

    # Creating a method for decrypting the passwords, e.t.c
    def Decrypt(self):
        email_password = 'gAAAAABfbod1QYLp3CWJkDDpCxzKmWiHp11fwW77nkfRSwQnM3pg4jqpKLaWKJcPiGYK_EhVpK9Boz7WVMPZVNAJTsRgqaqeQg=='.encode()
        api_key = 'gAAAAABfboVawrtrZf9bxC-hG6fCKdkU0L0oD1WqQ61L4WSfFmPfv0b4N8Q56d0lt9Z-ptMOsfIMN1opSsGgJPB2vlOgw7k-Sw=='.encode()
        api_secret = 'gAAAAABfbocOwTygC_D11rNT6B2BO8ubyasd8uCYJIqVGnROqW0-6FaoEAX6NYaeRJW-4HCKSifswv2Wcge_aO-hAvqXxS27NHZbUMSU4N0mxPAvt3Lhx_o='.encode()

        # Setting the path to the key gen pem file
        key_gen_path = os.path.sep.join(["key", "key_gen.pem"])

        # loading the key gen pem file
        with open(key_gen_path, "rb") as file:
            key_gen = file.read()

        #
        f = Fernet(key_gen)

        # Decrypting the keys
        decrypted_email_password = f.decrypt(email_password).decode()
        decrypted_api_key = f.decrypt(api_key).decode()
        decrypted_api_secret = f.decrypt(api_secret).decode()

        # Returning the decrypted values
        return (decrypted_email_password, decrypted_api_key, decrypted_api_secret)
