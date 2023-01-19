#WAPP to remove empty list from a list of lists
l=[[1],[1,2],[3,3,4],[],[],[4],[]] 
index=0
while index<len(l):
    if l[index]==[]:
      del l[index]
      index-=1
    index+=1
print("updated list: ",l)
