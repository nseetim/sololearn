'''
Secret Message

You are trying to send a secret message, and you've decided to encode it by replacing every letter in your message with its corresponding letter in a backwards version of the alphabet. 
What do your messages look like?

Task: 
Create a program that replaces each letter in a message with its corresponding letter in a backwards version of the English alphabet.

Input Format: 
A string of your message in its normal form.

Output Format: 
A string of your message once you have encoded it (all lower case).

Sample Input: 
Hello World

Sample Output: 
svool dliow


Explanation: 
If you replace each letter in 'Hello World' with 
the corresponding letter in a backwards version of the alphabet, 
you get 'svool dliow'. 


'''




import string

user_input=str(input()).lower()
lowercase_alphabets=string.ascii_lowercase
lowercase_alphabets=lowercase_alphabets + " "
#print(" " in lowercase_alphabets)
#print(lowercase_alphabets)
secret_message=""
for each_letter in user_input:
    for letter_in_alphabet in lowercase_alphabets:
        position_of_each_letter_in_userinput_in_lowercase_alphabets=lowercase_alphabets.index(each_letter)
        position_of_corresponding_letter_taken_in_reverse_alphabetical_order=25-position_of_each_letter_in_userinput_in_lowercase_alphabets
    secret_message+=lowercase_alphabets[position_of_corresponding_letter_taken_in_reverse_alphabetical_order]
#print(position_of_each_letter_in_userinput_in_lowercase_alphabets)
#print(position_of_corresponding_letter_taken_in_reverse_alphabetical_order)
#print(lowercase_alphabets[position_of_each_letter_in_userinput_in_lowercase_alphabets])
#print(lowercase_alphabets[position_of_corresponding_letter_taken_in_reverse_alphabetical_order])
print(secret_message)
