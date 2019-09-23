#Jesse "McCree" Chen and Michael Zhang
#SoftDev1 pd1
#K10 -- Jinja Tuning
#2019-09-21

from flask import Flask, render_template
import random

# CSV Script ----------------------------------------------------------
filehandle = open('occupations.csv', 'r')
csv_list = filehandle.readlines()
list_of_percents = list()
list_of_jobs = list()
#open the csv file
file=open("occupations.csv","r")

#read the file and split on new lines to get each line of the csv table as an element in the list
job=file.read().split("\n")

#function to iterate through the list and split each line of the csv table on the right-most comma, separating the occupation and the percentage
def splitCategory(l):
    #splits occupations and percentages
    for x in range(0,len(l)):
        #loop through list
        l[x]=l[x].rsplit(",",1)
        #split at the last comma of each item (becomes 2d array with occupation and percentage)
    return l
job=splitCategory(job)

#function for taking out the quotation marks in the occupation
def takeOutQuotes(l):
    for x in range(0,len(l)):
        #loop through the list
        for i in range(0,len(l[x])-1):
            #loop through the occupation and then the percentage
            l[x][i]=l[x][i].strip("\"")
            #strip the quotes
    return l
job=takeOutQuotes(job)

#take out the first item(category titles) and last two items (total percentage and an extra empty list)
job=job[1:len(job)-2]

#function to update each percentage to be a sum of all previous percentages
def rangePercent(l):
    #make the first string percentage a float
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

#function that will pick a random occupation based on the percentage
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
print (randomPick(job))


#Make list of jobs and list of percents
for pair in csv_list:
	rev_pair = pair[::-1]
	rev_percentage = ''
	rev_job = ''
	index_of_comma = 0
	for char in rev_pair:
		if char != ',':
			rev_percentage += char
			index_of_comma += 1
		elif char == ',':
			break
	for char in rev_pair[(index_of_comma + 1):]:
		rev_job += char
	list_of_percents.append(rev_percentage[:0:-1])
	list_of_jobs.append(rev_job[::-1])


#Random generation of a job


# End of CSV Script ---------------------------------------------------

app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign following fxn to run when run route requested
def hello_word():
    print(__name__) #where will this go? the console aka the terminal
    return "Hello World"

@app.route("/occupyflaskst") #assign following fxn to run when run route requested
def occ_table():
    return render_template('/occ_template.html',
    	tab_title = "Occupation Table and Generator",
		random_job = randomPick(job),
    	pair_list = zip(list_of_jobs, list_of_percents))

if __name__ == "__main__":
    app.debug = True #When this is false, the website no longer able to update authomatically when you make a change in the code
    app.run() #If this is commented out, the webstie is just not hosted