import math
"""Frequency of words in each Document"""
documents=      [[1,0,5,5,3],
               [0,1,2,5,5],
               [1,3,0,3,4],
               [3,2,1,4,5],
               [4,0,1,5,0]]
query=[4,2,1,3,0]
"""TF"""
temp_documents=documents
temp_query=query
for i in range(0,5):
    sum=0
    for j in range(0,5):
        sum=sum+temp_documents[i][j]
    for k in range(0,5):
        temp_documents[i][k]=temp_documents[i][k]/sum
"""for query"""
sum=0
for i in range(0,5):
    sum=sum+temp_query[i]    
for i in range(0,5):
    temp_query[i]=temp_query[i]/sum
"""idf"""
idf=[0,0,0,0,0]
count=0
for i in range(0,5):
    count=0
    for j in range(0,5):
        if(temp_documents[j][i]!=0):
            count=count+1
    
    idf[i]=math.log2(5/count)

"""tf*idf"""
for i in range(0,5):
    for j in range(0,5):
        temp_documents[i][j]=(temp_documents[i][j]*idf[j])

for i in range(0,5):
    temp_query[i]=temp_query[i]*idf[i]
rank=[0,0,0,0,0]
"""distance"""
sum2=0
for i in range(0,5):
    sum=0
    sum2=0
    for j in range(0,5):
        sum=sum+temp_documents[i][j]*temp_query[j]
        sum2=sum2+(temp_documents[i][j]-temp_query[j])**2
    sum2=math.sqrt(sum2)
    sum=sum/sum2
    rank[i]=sum
temp_rank=[0,0,0,0,0]
for i in range(0,5):
    temp_rank[i]=rank[i]
list.sort(temp_rank,reverse=True)
print ("Rank of pages according to similarity of query to Documents: ")
for i in range(0,5):
    for j in range(0,5):
        if(temp_rank[i]==rank[j]):
            print('Doc ' + str(j+1))
        