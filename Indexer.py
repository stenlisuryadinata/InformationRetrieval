import sys,os,re
import time
import math

# define global variables used as counters
tokens = 0
documents = 0
terms = 0
termindex = 0
docindex = 0 

# initialize list variable
#
alltokens = []
alldocs = []

#
# Capture the start time of the routine so that we can determine the total running
# time required to process the corpus
#
t2 = time.localtime()   


# set the name of the directory for the corpus

dirname = "/Users/stenlisuryadinata/cacm"

# For each document in the directory read the document into a string
#
all = [f for f in os.listdir(dirname)]
for f in all:
    documents+=1
    with open(dirname+'/'+f, 'r') as myfile:
        alldocs.append(f)
        data=myfile.read().replace('\n', '')  
        for token in data.split():
            alltokens.append(token)
            tokens+=1


# Open for write a file for the document dictionary

documentfile = open(dirname+'/'+'documents.dat', 'w')
alldocs.sort()
for f in alldocs:
  docindex += 1
  documentfile.write(f+','+str(docindex)+os.linesep)
documentfile.close()

#
# Sort the tokens in the list
alltokens.sort()

#
# Define a list for the unique terms  
g=[]

#
# Identify unique terms in the corpus
for i in alltokens:    
    if i not in g:
       g.append(i)
       terms+=1

terms = len(g)

# Output Index to disk file. As part of this process we assign an 'index' number to each unique term.  
# 
indexfile = open(dirname+'/'+'index.dat', 'w')
for i in g:
  termindex += 1
  indexfile.write(i+','+str(termindex)+os.linesep)
indexfile.close()


# Print metrics on corpus
#
print ('Processing Start Time: %.2d:%.2d' % (t2.tm_hour, t2.tm_min))
print ("Documents %i" % documents)
print ("Tokens %i" % tokens)
print ("Terms %i" % terms)

t2 = time.localtime()   
print ('Processing End Time: %.2d:%.2d' % (t2.tm_hour, t2.tm_min))

# size of vocabulary (M) in Heap's law, k=40, peta=0.5
#T is terms/tokens?
print("============================================")
M = 40*math.pow(tokens, 0.5)
print("size of vocabulary (M) in Heap's law, k=40, peta=0.5")
print("size of vocabulary %i" %M)