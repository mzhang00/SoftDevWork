filehandle = open('occupations.csv', 'r')
csv_list = filehandle.readlines()
list_of_percents = list()
list_of_jobs = list()

job=filehandle.read().split("\n")
print (job)
def splitCategory(l):
    #splits occupations and percentages
    for x in range(0,len(l)):
        #loop through list
        l[x]=l[x].rsplit(",",1)
        #split at the last comma of each item (becomes 2d array with occupation and percentage)
    return l
job=splitCategory(job)

def takeOutQuotes(l):
    for x in range(0,len(l)):
        #loop through the list
        for i in range(0,len(l[x])-1):
            #loop through the occupation and then the percentage
            l[x][i]=l[x][i].strip("\"")
            #strip the quotes
    return l
job=takeOutQuotes(job)

job=job[1:len(job)-2]

def randomPick(l):
    #generates a random percentage between 0 and 100%
    rand=random.randint(0,1000)
    rand=rand/10.0

    #counters for looping through the list
    counta=0
    countb=len(l)-1

    #the case where none of the occupations are selected
    if rand>99.8:
        return "unemployed"
    #loop through the list both from the front and the back until the randomly generated percentage is within one of the sections
    while l[counta][1]<rand and l[countb][1]>rand:
        #loop through both front and back; front loop till find something greater, back loop till find something smaller
        counta=counta+1
        #advance front loop
        countb=countb-1
        #push back back loop
    #this is the case that the randomly generated percentage was exactly one of the percentages
    if  l[countb][1]==rand:
        #deals with edge case for back loop
        return l[countb][0]
    if l[counta][1]>=rand:
        #front loop returns whatever item it counted up to
        return l[counta][0]
    else:
        #back loop returns the next item
        return l[countb+1][0]

def rangePercent(l):
    #make the first string percentage a float
    print (l)
    l[0][1]=float(l[0][1])
    for x in range(1,len(l)):
        #update each following percentage to be a float
        l[x][1]=round(float(l[x][1])+l[x-1][1],1)
        #make the current percentage the sum of the previous and current such that if the first item has 6.1 percent and second one has 10.2 %
        #we will modify the second number to be 16.3 so that when we generate a random number we can use binary search to find which two items it is between
        #if our random number is 5.3, since its less than the 6.1, the first item is returned
        #if 11.4 is generated, second item is returned because it is greater than 6.1 but less than 16.3
    return l
job=rangePercent(job)

def randomPick(l):
    #generates a random percentage between 0 and 100%
    rand=random.randint(0,1000)
    rand=rand/10.0

    #counters for looping through the list
    counta=0
    countb=len(l)-1

    #the case where none of the occupations are selected
    if rand>99.8:
        return "unemployed"
    #loop through the list both from the front and the back until the randomly generated percentage is within one of the sections
    while l[counta][1]<rand and l[countb][1]>rand:
        #loop through both front and back; front loop till find something greater, back loop till find something smaller
        counta=counta+1
        #advance front loop
        countb=countb-1
        #push back back loop
    #this is the case that the randomly generated percentage was exactly one of the percentages
    if  l[countb][1]==rand:
        #deals with edge case for back loop
        return l[countb][0]
    if l[counta][1]>=rand:
        #front loop returns whatever item it counted up to
        return l[counta][0]
    else:
        #back loop returns the next item
        return l[countb+1][0]
