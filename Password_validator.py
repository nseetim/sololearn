'''
Password Validation

You're interviewing to join a security team. They want to see you build a password evaluator for your technical interview to validate the input.

Task: 
Write a program that takes in a string as input and evaluates it as a valid password. The password is valid if it has at a minimum 2 numbers, 2 of the following special characters ('!', '@', '#', '$', '%', '&', '*'), and a length of at least 7 characters.
If the password passes the check, output 'Strong', else output 'Weak'.

Input Format:
A string representing the password to evaluate.

Output Format:
A string that says 'Strong' if the input meets the requirements, or 'Weak', if not.

Sample Input: 
Hello@$World19

Sample Output: 
Strong
'''


user_password=str(input())
special_characters_tuple=('!', '@', '#', '$', '%', '&', '*')
user_password_list=[]
numeric_count=0
special_character_count=0
[user_password_list.append(each_letter) for each_letter in user_password]
for each_character_of_user_password in user_password_list:
    if each_character_of_user_password in special_characters_tuple:
        special_character_count+=1
    elif user_password_list[user_password_list.index(each_character_of_user_password)].isnumeric():
        numeric_count+=1

if numeric_count > 1 and special_character_count > 1 and len(user_password) >6:
    print('Strong')
else:
    print('Weak')
