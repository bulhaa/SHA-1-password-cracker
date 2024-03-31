import hashlib
import base64

def crack_sha1_hash(hash, use_salts = False):
    
    with open("top-10000-passwords.txt", "r") as f:
        for password in f:
            strippedPassword = password.strip()
            if use_salts:
                with open("known-salts.txt", "r") as f2:
                    for salt in f2:
                        m = hashlib.sha1()
                        strippedSalt = salt.strip()
                        m.update((strippedSalt + strippedPassword).encode())
                        # print(f'm.hexdigest(): {m.hexdigest()} line: {strippedSalt + strippedPassword}')
                        if m.hexdigest() == hash:
                            return strippedPassword
                        
                        m = hashlib.sha1()
                        m.update((strippedPassword + strippedSalt).encode())
                        # print(f'm.hexdigest(): {m.hexdigest()} line: {strippedPassword + strippedSalt}')
                        if m.hexdigest() == hash:
                            return strippedPassword
            else:
                m = hashlib.sha1()
                m.update(strippedPassword.encode())
                # print(f'm.hexdigest(): {m.hexdigest()} line: {line}')
                if m.hexdigest() == hash:
                    return strippedPassword

    return "PASSWORD NOT IN DATABASE"
    
# r = crack_sha1_hash(
#             "5d70c3d101efd9cc0a69f4df2ddf33b21e641f6a")
# print('r: ', r)