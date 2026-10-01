# Write a program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# failed. (Something like captcha)

import random

correct_userid = "8189"
correct_pass = "abc@8189"

userid = input('enter correct userid..')
passsword = input('enter correct password..')

if userid == correct_userid and passsword == correct_pass:

    captcha = random.randint(2000 , 9000)
    print('captcha:',captcha)

    user_captcha = int(input('enter captcha..'))
    if captcha == user_captcha:
        print('login successfully..')
    else:
        print('please enter correct captcha..')
else:
    print('invalid userid and password..')


  



    
