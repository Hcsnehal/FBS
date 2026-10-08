def palindrom_num():
  num=int(input('enter a num='))
  rev=0 
  temp=num 

  while(num>0):
    d=num%10
    rev=rev*10+d 
    num=num//10 
  if(temp==rev):
    print('num is palindrom..')
  else:
    print('num is not palindrome..')    
palindrom_num()