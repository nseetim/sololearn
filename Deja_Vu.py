'''
Deja Vu

You aren't paying attention and you accidentally type a bunch of random letters on your keyboard. You want to know if you ever typed the same letter twice, or if they are all unique letters.

Task: 
If you are given a string of random letters, your task is to evaluate whether any letter is repeated in the string or if you only hit unique keys while you typing.

Input Format: 
A string of random letter characters (no numbers or other buttons were pressed).

Output Format: 
A string that says 'Deja Vu' if any letter is repeated in the input string, or a string that says 'Unique' if there are no repeats.

Sample Input: 
aaaaaaaghhhhjkll

Sample Output: 
Deja Vu

'''



from collections import Counter
user_input=str(input())
count = Counter(user_input)
ans=[]
for letter in user_input:
    if count[letter] <= 1:
        ans.append("Unique")
    elif count[letter] > 1:
        ans.append("Deja Vu")
#print(ans)
if "Deja Vu" in ans:
    print("Deja Vu")
elif "Unique" in ans:
    print("Unique")
