#5. Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

side_1 = int(input('enter first side of triangle..'))
side_2 = int(input('enter 2nd side of triangle..'))
side_3 = int(input('enter third side of triangle..'))

if(side_1 > 0 and side_2 > 0 and side_3 > 0):
   
   if (side_1 + side_2 > side_3 and side_2 + side_3 > side_1 and side_1 + side_3 > side_1):

       if(side_1 == side_2 == side_3):
           print('triangle is equilateral...')
       elif(side_1 == side_2 or side_2 == side_3 or side_1 == side_3):
           print('triangle is isosceles triangle .')
       else:
           print('triangle is scalene...') 
   else:
       print('invalid triangle....')
else:
    print('triangle side must be positive...')

           
      
    
              

     
               
       
            

       
       
                   