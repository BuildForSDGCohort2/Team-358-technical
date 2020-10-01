#!/usr/bin/env python

# Importing the necessary modules
import os
from cryptography.fernet import Fernet


# Creating a class to load the encrypted password, token, and secret keys.
class Encryption:
    def __init__self(self):
        pass

    # Creating a method for decrypting the cloudinary passwords, e.t.c
    def CloudinaryDecrypt(self):
        email_password = 'gAAAAABfbod1QYLp3CWJkDDpCxzKmWiHp11fwW77nkfRSwQnM3pg4jqpKLaWKJcPiGYK_EhVpK9Boz7WVMPZVNAJTsRgqaqeQg=='.encode()
        api_key = 'gAAAAABfboVawrtrZf9bxC-hG6fCKdkU0L0oD1WqQ61L4WSfFmPfv0b4N8Q56d0lt9Z-ptMOsfIMN1opSsGgJPB2vlOgw7k-Sw=='.encode()
        api_secret = 'gAAAAABfbocOwTygC_D11rNT6B2BO8ubyasd8uCYJIqVGnROqW0-6FaoEAX6NYaeRJW-4HCKSifswv2Wcge_aO-hAvqXxS27NHZbUMSU4N0mxPAvt3Lhx_o='.encode()

        # Setting the path to the key gen pem file
        key_gen_path = os.path.sep.join(["key", "key_gen.pem"])

        # loading the key gen pem file
        with open(key_gen_path, "rb") as file:
            key_gen = file.read()

        # Creating an instance of the fernet object
        f = Fernet(key_gen)

        # Decrypting the keys
        decrypted_email_password = f.decrypt(email_password).decode()
        decrypted_api_key = f.decrypt(api_key).decode()
        decrypted_api_secret = f.decrypt(api_secret).decode()

        # Returning the decrypted values
        return decrypted_email_password, decrypted_api_key, decrypted_api_secret

    # Creating a method for decrypting the twilio passwords.
    def TwilioDecrypt(self):
        account_sid = "gAAAAABfdPGuRe6RcnEeq67HeaUtERC_WXAGkMQYguirG-tsk59l1u57W6EooXcik9LsQRBA5xLoGn-oJOgb_HjwHWbpMPSUJ3k84m7tVbDIpZjmVraYjWhGm3a3n34Jbn6n4W9l-Scl".encode()
        auth_token = "gAAAAABfdPK5uNImbeVAhSEihAfoMRtWEQ8SIHV0i08Vu6SpG9uvLFkUtUfmImAF9Xn5t2eQ39nIlsKOzFrPBnbq8yebjg0CIRRtHaV1IZJIPp4eyvq7DjbM1_rSCC1p_9ga6i_v1JpD".encode()

        # Setting the path to the key gen pem file
        key_gen_path = os.path.sep.join(["key", "key_gen.pem"])

        # loading the key gen pem file
        with open(key_gen_path, "rb") as file:
            key_gen = file.read()

        # Creating an instance of the Fernet object
        f = Fernet(key_gen)

        # Decrypting the keys
        decrypted_account_sid = f.decrypt(account_sid).decode()
        decrypted_auth_token = f.decrypt(auth_token).decode()

        # Returning the decrypted values
        return decrypted_account_sid, decrypted_auth_token

    def Decrypt(self):
        pass
