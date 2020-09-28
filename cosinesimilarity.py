import math
import operator

#These two functions are for calculating cosine similarity
def dot_product2(v1, v2):
    return sum(map(operator.mul, v1, v2))
def cosineSimilarity(v1, v2):
    #v1請放入doc，v2請放入query
    prod = dot_product2(v1, v2)
    len1 = math.sqrt(dot_product2(v1, v1))
    len2 = math.sqrt(dot_product2(v2, v2))
    return prod / (len1 * len2)

# N is for controling how many document can be input
# alldoc for storing input
# setalldoc can store all non-repeated words

N = int(input())

alldoc = []
setalldoc = []
for i in range (1,N+1):
    word=(input().split(':'))[1] #all input format is "doc1:······", so capturing string after ":"
    word=word.replace(',','').replace('.','').lower() #replace all "," and "." to blank, and tranfer all letters to be lowercase
    alldoc += [word]
    word=word.split()
    setword=set(word)
    setalldoc += setword
setsetalldoc = set(setalldoc)

# make the words of each input to be separate 
DocList = []
for each in alldoc:
    DocList.append(each.split())

# generate inputs' vector
EachDocVec = []
for each in DocList:
    vec = dict(zip(setalldoc,[0]*len(setalldoc)))
    for word in each:
        vec[word]+=1
    EachDocVec.append(vec)

# input keywords as query
query = input().lower() 
set_query = []
query = query.split()
setquery=set(query)
set_query += setquery

#generate keywords' vector
queryvector = []
vec = dict(zip(setalldoc,[0]*len(setalldoc)))
for qword in set_query:
    vec[qword] += 1
queryvector.append(vec)
V3 = list(queryvector[0].values())

#Using cosine similarity formula to evaluate it and storing into result list 
result = []
for j in range (len(EachDocVec)):
    vectornum = list(EachDocVec[j].values())
    result += [cosineSimilarity(vectornum,V3)]

for z in range (len(result)):
    print('doc{}'.format(z+1),round(result[z],4))
for x in range (len(result)):
    if result[x] == max(result):
        print('best:doc{}'.format(x+1))
