
import binascii
import re
name = "Hex"

def check(result):
    if("charset" in result):
        if(not result["charset"]==r"[0-9a-fA-F ]" and not result["charset"]==r"[0-9 ]"):
            return False
    
    if("entropy" in result):
        if(result["entropy"]<=1.95 or result["entropy"]>=4):
            return False
    
    return True


def decrypt(text, key=''):
    text = text.replace(' ', '')
    res = binascii.unhexlify(text).decode()
    #print(res)
    if(re.match(r'^[ -~]*$',res)):
        return res
    else:
        return False