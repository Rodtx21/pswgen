import random

def main():
    password = []
    
    #upc letters
    for x in range(2):
        upc = random.randint(65, 91)
        password.append(upc)

    #lwc letters
    for y in range(2):
        lwc = random.randint(97, 123)
        password.append(lwc)

    #digits
    for z in range(2):
        dg = random.randint(48, 58)
        password.append(dg)
    
    #punctuation
    for z in range(2):
        p = random.randint(33, 48)
        password.append(p)

    for b in range(4):
        any = random.randint(33, 124)
        password.append(any)


    #randomize it
    random.shuffle(password)

    #create final list
    passw = ''

    #char it
    for a in range(len(password)):
        passw += chr(password[a])
    
    print(passw)



main()