for i in range(1,7):
    for j in range(1,7-i):
        if(i==1 or j==1 ):
          print('*',end=' ')
        else:
           print(' ',end=' ') 
    print()    