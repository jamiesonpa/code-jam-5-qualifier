import random
import string


lowercase = ["a", "b", "c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
uppercase = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def generate_password(password_length: int = 8, has_symbols: bool = False, has_uppercase: bool = False, ignored_chars = None, allowed_chars = None) -> str: 
    symbolChoice = "!"

    if password_length < 999998:
        if ignored_chars != None and allowed_chars == None:
            for char in ignored_chars:
                charindex = lowercase.index(char)
                lowercase.remove(char)
                del uppercase[charindex]
                if "!" in ignored_chars:
                    symbolChoice = "@"
            upperCaseChar =  random.randint(0,password_length-1)
            symbolInsertion =  upperCaseChar - 1
            password = ''
            counter = 0
            while counter < password_length:
                if counter == upperCaseChar:
                    nextChar = random.choice(uppercase)
                elif counter == symbolInsertion:
                    nextChar = symbolChoice
                else:
                    nextChar = random.choice(lowercase)
                password = password + nextChar
                counter += 1
            return str(password)
        elif allowed_chars != None:
            if ignored_chars != None:
                raise UserWarning
            password = ''
            counter = 0
            while counter < password_length:
                nextChar = random.choice(allowed_chars)
                password = password + nextChar
                counter += 1
                return str(password)
        else:
            upperCaseChar = random.randint(0,password_length-1)
            symbolInsertion = upperCaseChar - 1
            password = ''
            counter = 0
            while counter < password_length:
                if counter == upperCaseChar:
                    nextChar = random.choice(uppercase)
                elif counter == symbolInsertion:
                    nextChar = symbolChoice
                else:
                    nextChar = random.choice(lowercase)
                password = password + nextChar
                counter += 1
            counter = 0
            return str(password)
    else:
        password = ("A@" + 999997 * "a")
        return str(password)
        
