'''
Argentina +10 XP

You are in a hat store in Argentina! The prices are listed in US Dollars and Argentinian Pesos. You have both, but you want to make sure you pay the lower price! Do you pay in Dollars or Pesos? The exchange rate is 2 cents for every Peso.

Task 
Create a program that takes two prices and tells you which one is lower after conversion.

Input Format 
Two integer values, the first one is the price in Pesos and the second one is the price in Dollars.

Output Format 
A string that says which currency you should make the purchase in ('Dollars' or 'Pesos').

Sample Input 
4000
100

Sample Output 
Pesos
'''


pesos_cost=int(input())
dollar_cost=int(input())
convert_to_dollar=pesos_cost*0.02
if convert_to_dollar  < dollar_cost  :
    print("Pesos")
else:
    print("Dollars")
