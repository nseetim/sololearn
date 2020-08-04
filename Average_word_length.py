'''
Average Word Length

You are in a college level English class, your professor wants you to write an essay, but you need to find out the average length of all the words you use. It is up to you to figure out how long each word is and to average it out.

Task: 
Takes in a string, figure out the average length of all the words and return a number representing the average length. Remove all punctuation. Round up to the nearest whole number.

Input Format: 
A string containing multiple words.

Output Format: 
A number representing the average length of each word, rounded up to the nearest whole number.

Sample Input: 
this phrase has multiple words

Sample Output: 
6
'''

import re, math
user_input=(input())
#print(user_input)
output=""
for i in user_input:
    regex=re.compile("[^\sa-zA-Z0-9]")
    clean=regex.sub("", i)
    output+=clean
output_list=output.split()
output=output.replace(" ","")
avg_numb_of_words=math.ceil(len(output)/len(output_list))
print(avg_numb_of_words)
#print(output)
#print(output_list)
