str_var = " hello "
maxcount = len(str_var)
mincount = 0
Up = True
Down = False
count = 0
for i in range(0, 1000):
    if count < maxcount:
        Up = True ; Down =False
        if Up == True:
            count +=1
            print(count,"up")
            print(i,str_var[count-1])
    if count > maxcount:
        Up = False ; Down =True
        if Down == True:
            count -=1
            print(count,"down")
            print(i,str_var[count-1])
        
    
        
        

    
