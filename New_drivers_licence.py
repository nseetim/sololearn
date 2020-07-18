'''
New Driver's License

You have to get a new driver's license and you show up at the office at the same time as 4 other people. The office says that they will see everyone in alphabetical order and it takes 20 minutes for them to process each new license. All of the agents are available now, and they can each see one customer at a time. How long will it take for you to walk out of the office with your new license?

Task 
Given everyone's name that showed up at the same time, determine how long it will take to get your new license.

Input Format 
Your input will be a string of your name, then an integer of the number of available agents, and lastly a string of the other four names separated by spaces.

Output Format 
You will output an integer of the number of minutes that it will take to get your license.

Sample Input
'Eric'
2
'Adam Caroline Rebecca Frank'

Sample Output 
40
'''



my_name=str(input())
number_of_attendants=int(input())
names_of_others=str(input()).split() # As the names are entered the are immediately slit using whitespaces and the sokit method returns a list of the names entered
names_of_others.append(my_name) # Use the append method to add my name which i inputed first into the list of the names of others
all_names_sorted=sorted(names_of_others) # Sort all the names alphabetically
#print(all_names_sorted)
time_to_attend_to_one_person=20
my_position_on_the_que=(all_names_sorted.index(my_name))+1 # one is added to the index because of the non-zero indexing style of python
if my_position_on_the_que <= number_of_attendants:
    print(time_to_attend_to_one_person)
elif my_position_on_the_que > number_of_attendants and my_position_on_the_que % number_of_attendants ==0:
	group=my_position_on_the_que//number_of_attendants
	time=group*20
	print(time)
elif my_position_on_the_que > number_of_attendants and my_position_on_the_que % number_of_attendants !=0:
		group=(my_position_on_the_que//number_of_attendants)+1
		time=group*20
		print(time)
