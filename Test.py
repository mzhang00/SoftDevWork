import random

def randStudent(l):
    firstRand = random.randint(0,2);
    if (firstRand == 0):
        firstRand = 'orpheus'
    elif (firstRand == 1):
        firstRand = 'rex'
    else:
        firstRand = 'endymion'
    print (l.get(firstRand)[random.randint(0, len(l.get(firstRand)) - 1)])

KREWES = {'orpheus': ['12','as','ad','sadf'], 'rex': ['132','asds','adfgfdgd','sdsgsfadf'], 'endymion': ['2','a','aasdfadf','sad']}

randStudent(KREWES)
