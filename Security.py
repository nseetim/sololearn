'''
Security

You are in charge of security at a casino, and there is a thief who is trying to steal the casino's money!  Look over the security diagrams to make sure that you always have a guard between the thief and the money!
There is one money location, one thief, and any number of guards on each floor of the casino.

Task: 
Evaluate a given floor of the casino to determine if there is a guard between the money and the thief, if there is not, you will sound an alarm.

Input Format:
A string of characters that includes $ (money), T (thief), and G (guard), that represents the layout of the casino floor.  
Space on the casino floor that is not occupied by either money, the thief, or a guard is represented by the character x.

Output Format: 
A string that says 'ALARM' if the money is in danger or 'quiet' if the money is safe.

Sample Input: 
xxxxxGxx$xxxT

Sample Output:
 ALARM



'''



import re
user_input=str(input())

#pattern='(\$|T)x*G+x*(T|\$)' # The regex pattern here searches for every occurance of '$' or 'T' followed by zero or more occurance of 'x' then one or more occurance of a G then zero or more occurance of a 'T' or '$'

alarm_pattern='(Tx*[$]x*)|(x*[$]x*Tx*)x*G*' # So for the sake of figuring out the last test case i decided to
# look at the pattern that will set of an alarm then every other pattern will be regarded as quiet, 
# although we should note that this approach isnt safe or secure for real life scenerios

# The same is achieved bellow by spliting the pattern into two but using ome pattern will probably be more efficient and reduce the number of if statements 

#pattern='\$x*Gx*T'
#pattern1='Tx*Gx*\$'
if re.search(alarm_pattern,user_input):
    print("ALARM")
#elif re.search(pattern1,user_input):
#    print("quiet")
else:
    print("quiet")


#Adapted from code by Mansi

user_input=input()
check=0
for index_of_a_particular_letter in range(len(user_input)-1):
    if user_input[index_of_a_particular_letter] =='$'or user_input[index_of_a_particular_letter]=='T':
       for index_of_each_letter in range(index_of_a_particular_letter+1,len(user_input)):
           if user_input[index_of_each_letter]=='G':
              check=1
              break 
           elif user_input[index_of_each_letter]=='T' or user_input[index_of_each_letter]=='$':
                check=2
                break 
        
    if check==1:
       print ("quiet") 
       break 
    elif check==2:
         print("ALARM")
         break

