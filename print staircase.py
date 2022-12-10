arr = [['a', 2, 100],  
       ['b', 1, 19],
       ['c', 2, 27],
       ['d', 1, 25],
       ['e', 3, 15]]
t = 3
checker = True
while checker is True:
  checker = False
  for i in range(1,len(arr)):
    if arr[i-1][2]<arr[i][2]:
        arr[i],arr[i-1] = arr[i-1], arr[i]
        checker = True
job = [1]*t
slot= [False]*t

for i in range(len(arr)):
    for j in range(min(t-1, arr[i][1]-1),-1,-1):
        if slot[j]== False:
            slot[j]= True
            job[j]= arr[i]
            break
            
print(job)
            
        
    

    
    
