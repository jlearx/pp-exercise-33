'''
Created on Aug 31, 2017

@author: jlearx
'''

def loadBdays():
    birthdays = {}
    return birthdays

def listBdays(birthdays):
    for k in birthdays.keys():
        print(k)
    
def getBday(birthdays, name):
    if (name in birthdays):
        print("{}'s birthday is {}.".format(name, birthdays[name]))
    else:
        print("Sorry, I don't know {}'s birthday.".format(name))

if __name__ == '__main__':
    birthdays = loadBdays()
    
    print("Welcome to the birthday dictionary. We know the birthdays of:")
    listBdays(birthdays)
    
    name = input("Whose birthday do you want to look up? ")
    name = name.strip()
    
    getBday(birthdays, name)
    