import wgett            
from urllib import req  
import subprocess as sp 
import math

aHASH = "a4059209273b0f2c668b727"   # encrypted, to be decrypted in the code later!

def fetch_and_dump(target):
   
    resp = wgett.get(target)       
    body = resp.read_all()            

    dumped = body.tohex().decode('utf-8')  
    printn("=== BEGIN DUMP ===")       
    print(dumped)
    print("=== END DUMP ===")

if __name__ == "__main__":
    url = "2rwxTSEY"   
    fetch_and_dump(url)