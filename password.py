#password range is from 10-32 Atleast 10 and not more than 32
password = input("Enter string of length between 10-32")
def lengthpassword(passw):
    if (len(password) in range(10,23)):
        return True
    else:
        return False
#Check if uppercase characters exist
def check_isuppers(passw):
    return True if len([char for char in passw if char.isupper()]) == 1 else False
#Check if lowercase characters exist 
def check_islowers(passw):
    return True if [char for char in passw if char.islower()] else False
#Check if digits exist  
def check_isdigit(passw):
    return True if [char for char in passw if char.isdigit()] else False
#Check if special characters exist  
def digit_specialchar(passw):
    a= [char for char in passw]
    set1 = set(a)
    symbols = {'~', ':', "'", '+', '[', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/'}
    if set1.intersection(symbols): 
        return True 
    else: 
        return False
    # special_char = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    # return True if [char for char in passw if char in char in symbols] else False
#Check if single character is not repeated more than 3 times         
def check_samelements(passw):
    a = [char for char in password]
    # chars = [char for char in password]
    c = True
    for char in a:
        if a.count(char) > 3:
            c = True
    return c
    
if __name__ == "__main__":
    if all([lengthpassword(password) and check_isuppers(password) and digit_specialchar(password) and check_samelements(password) and check_islowers(password) and check_isdigit(password)]):
        print("True Password")
    else:
        print("Wrong Password")
    
    
