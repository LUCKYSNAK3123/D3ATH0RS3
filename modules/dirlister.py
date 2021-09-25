import os 
import base64


def run(**args):
    print("[*] In dirlister module.")
    files = os.listdir(".")
    return str(files)


