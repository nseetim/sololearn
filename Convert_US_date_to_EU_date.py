'''
Convert US date to EU date

You and your friends are going to Europe! You have made plans to travel around Europe with your friends, but one thing you need to take into account so that everything goes according to play, is that the format of their date is different than from what is used in the United States. Your job is to convert all your dates from MM/DD/YYYY to DD/MM/YYYY.

Task: 
Create a function that takes in a string containing a date that is in US format, and return a string of the same date converted to EU.

Input Format: 
A string that contains a date formatting 11/19/2019 or November 19, 2019.

Output Format: 
A string of the same date but in a different format: 19/11/2019.

Sample Input: 
7/26/2019

Sample Output: 
26/7/2019
'''

import re
import datetime 
entered_date=str(input())
if "/" in entered_date:
    n_entered_date=entered_date.split("/")
    final="{}/{}/{}".format(n_entered_date[1],n_entered_date[0],n_entered_date[2])
    print(final)
else:
    result=re.split('\W+', entered_date)
    long_month_name = result[0]
    datetime_object = datetime.datetime.strptime(long_month_name, "%B")
    month_number = datetime_object.month
    final_date='{}/{}/{}'.format(result[1],month_number,result[2])
    print(final_date)
