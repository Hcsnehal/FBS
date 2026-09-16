# 7. Write a program to check if user has entered correct userid and password.

correct_userid = "1234"
correct_pass = "snehal@123"

user_id = input('enter user id...')
pass_word = input('enter password..')

if(correct_userid == user_id and correct_pass == pass_word):
    print('correct userid and password........')
elif(correct_userid != user_id and correct_pass == pass_word):
    print('userid is incorrect ......')
elif(correct_pass != pass_word and user_id == correct_userid):
    print('incorrect password.....')
else:
    print('both are incorrect plz enter correct userid and password....')        





