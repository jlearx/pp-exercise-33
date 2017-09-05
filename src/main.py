'''
Created on Aug 31, 2017

@author: jlearx
'''

def loadBdays():
    birthdays = {
        'Albert Einstein': '03/14/1879',
        'Benjamin Franklin': '01/17/1706',
        'Ada Lovelace': '12/10/1815',
        'Donald Trump': '06/14/1946',
        'Rowan Atkinson': '01/6/1955'}
    
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
    