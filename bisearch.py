
mylist = [1,10,8,21,3,4,5,7]

print(mylist)

mylist.sort()

print(mylist)


findVar = 1
x = 0
print (type(x))
x = int(len(mylist)/2)
print(type(x))

while  mylist[x] != findVar and x != 0: 
        print ("loop ", x)
        if mylist[x] < findVar:
                print ("go up")
                x = int((x+len(mylist))/2)
        else:
                print("go down")
                x = int(x/2)
      
      
if mylist[x] == findVar:          
        print (findVar, " found at index ", x)
else:
        print (findVar, " not found")        
                
