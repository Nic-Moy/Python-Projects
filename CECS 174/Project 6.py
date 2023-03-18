
###PART A
def is_sorted(array):
    #setting range and acocunting for index starting at 0
    for i in range(len(array) - 1):
        #checks if the value @ the index is greater than the value @ the next index
        if array[i] > array[i+1]:
            return False
    #returns true if assending    
    return True       

#numbers = [6,7,1,2]
#print (is_sorted(numbers))





#PART B
def is_anagram(string1, string2):
    #checks to see if the letters are the same
    if(sorted(string1)== sorted(string2)):
        #returns true if its an anagram
        return True
    #returns false if otherwise
    else:
        return False      
         
 
#string1 ="listen"  
#string2 ="silent"
#print(is_anagram(string1, string2))





#PART C
import random
def has_duplicates(birthday_list):
	#starting index value
  	a=0
  	#this iterates over the randomly generated Bday list
  	for x in range(len(birthday_list)):
		#Checks count with the updated index value
    		if birthday_list.count(birthday_list[a])> 1:
                        #return true if there is an element that appears more than once
     			return True
    		else:
                        #goes to the next index
      			a+=1
#creates a new list of random birthdays
birthday_list=[]
i=0
while i<23:
        #101 = January 1st, 1232 = December 31st cause range is -1
  	birthday_day = random.randint(101, 1232)
  	#Accounts for the months with 30 days
  	if birthday_day//100 == 4 or 6 or 9 or 11:
                #checks the range for the days of the month
    		if birthday_day%100<29:
                        #adds the day to the list
      			birthday_list.append(birthday_day)
      			#moves to next bday
      			i+=1
    		else:
      			i+=0
      	#accounts for months with 31 days
  	elif birthday_day%100<31 and birthday_day%100!=0:
    		birthday_list.append(birthday_day)
    		i+=1
    	#doesn't add number if not in range
  	else:
    		i+=0
#print(birthday_list)
#print(has_duplicates(birthday_list))






#PART D
def remove_duplicates(list):
    #creates new list
    x = []
    #iterates through each element
    for a in list:
        #adds the value to the list if its not already there
        if a not in x:
            x.append(a)
    #returning our value
    return x

#List = [1,2,2,2,2,2,2,5,6,7,8]
#print(remove_duplicates(List))







#PART E    
def filereader():
    #opens the file in our computer
    open_file = open('/Users/Nic/Desktop/words.txt','r')
    f = open_file.readlines()
    
    #time code to check with method is slower
    import time
    t0= time.time()

    #Appending method 
    list1 = []
    for i in f:
        #appends
        list1.append(i.strip())
    print(list1)
    
    t1 = time.time() - t0
    print("Time elapsed: ", t1)
    
    print("append method")
    
def filereader2():
    #opens the file in our computer
    open_file = open('/Users/Nic/Desktop/words.txt','r')
    f = open_file.readlines()
    
    #time code to check with method is slower
    import time
    t2 = time.time()
    
    #idiom method
    list2 = []
    for i in f:
        #concatenates
        list2 += [i]
    print(list2)
    
    t3 = time.time() - t2
    print("Time elapsed: ", (t3))

    print("Idiom method")
    print("the slower method is the idiom method because you have a create a new list each time while appending just adds to the existing list")
    
#filereader()



  




#PART F
##setting list and target values
#my_list = ["hello", "test2", "practice", "test",]
#target = "test"

def bisect(my_list,target):
    #Creating valeus for binary search
    upper_bound = len(my_list) - 1
    lower_bound = 0
    index = (len(my_list) - 1) // 2

    #while loop to produce index value
    while True:
        #returning index if the target index is found
        if my_list[index] == target:
            return index
        #decreases upper bound to get a shorter section for the bisetion search
        elif my_list[upper_bound] > target:
            upper_bound = index - 1
            index = (upper_bound + lower_bound) // 2
        #Return none if the target isnt in the list
        elif upper_bound < lower_bound:
            return None
        #increases lower bound to get a shorter search section for the bisection search
        else:
            lower_bound = index + 1
            index = (upper_bound + lower_bound) // 2

    
#print(bisect(my_list,target))






#PART G
def character_counter():
    #getting user input
    user = str(input("Enter a sentence: "))
    sentence = user
    #creating dictionary
    dictionary = {}
    #going through each letter in the sentence
    for i in user:
        #adding to the count of the letter if the letter is already present
        if i in dictionary:
            dictionary[i] += 1
        #creating a value for the letter if there is not one already
        else:
            dictionary[i] = 1
    print("The count of characters in", sentence, str(dictionary))

#character_counter()









#PART H
#importing all of the modules
    
import string
import matplotlib.pyplot as plt
import numpy as np
def moby():
    #opening the file
    
    open_file = open('/Users/Nic/Desktop/moby.txt','r')
    f = open_file.readlines()

    #create a list and dictionary
    list1 = []
    dictionary = {}
    
    #for every line in file
    for i in f:
        #for every word in each line
        for word in i.split():
            #adding each word to the list
            list1.append(i.split())
    #turns the read lines into a string
    user = str(f)

    #for each word in the string
    for i in user:
        #for each letter in each word
        for letter in i.split():
            #checks if it is an upper/lower case in the ascii alphabet
            if i in list(string.ascii_lowercase) or i in list(string.ascii_uppercase):
                #checks if the letter is already in the dictionary
                if i in dictionary:
                    #+1 to that letter
                    dictionary[i] +=1
                
                else:
                    #creates the spot for the element if it is not already in the dictionary
                    dictionary[i] = 1
                    
    #calculating the total word count
                    
    word_count = len(list1)

    #sorting the dictionary
    
    dictionary_alphabetical = sorted(dictionary.items())

    #print the file contents, word count, and letter frequency
    
    print(list1)
    print("total words", word_count)
    print("Letter frequency: ", dictionary_alphabetical)
    
    
    new_str = ""
    #for each word in the string
    for i in range(len(user)):
        #Converts uppercase to lowercase and adds it to string
        
        if user[i].isupper():
            new_str += user[i].lower()
        #converts lowercase to uppercase and adds it to string
            
        elif user[i].islower():
            new_str+=user[i].upper()
        #Just adds to the string if not a letter
            
        else:
            new_str+=user[i]

    #setting plot X & Y values
            
    keys = list(dictionary.keys())
    values = list(dictionary.values())
    plt.plot(keys,values)
    

    #creating a new txt file
    
    new_file = open('/Users/Nic/Desktop/New file.txt','w')
    #adding the updated string to the new file
    
    new_file.write(new_str)

    #adding results of word count and letter frequency to the new file
    
    result1 = str(word_count)
    new_file = open('/Users/Nic/Desktop/New file.txt','a')
    new_file.write('\n')
    new_file.write('\n')
    new_file.write('\n')
    new_file.write('The word count is: ')
    new_file.write('\n')
    new_file.write(result1)
    new_file.write('\n')
    new_file.write("The frequency of the letters are: ")
    result2 = str(dictionary_alphabetical)
    new_file.write(result2)

    #displays the plot
    plt.show()
    

    



#MAIN
def main():

    #A
    print("Part A")
    numbers = [6,7,1,2]
    print(numbers)
    print (is_sorted(numbers))
    print('\n')
    

    #B
    print("Part B")
    string1 ="listen"  
    string2 ="silent"
    print(string1,"&", string2)
    print(is_anagram(string1, string2))
    print('\n')
    
    
    #C
    print("Part C")
    print(birthday_list)
    print(has_duplicates(birthday_list))
    print('\n')
    

    #D
    print("Part D")
    List = [1,2,2,2,2,2,2,5,6,7,8]
    print(List)
    print(remove_duplicates(List))
    print('\n')
    

    #E
    print("Part E")
    filereader()
    print('\n')
    filereader2()
    print('\n')
    

    #F
    print("Part F")
    my_list = ["hello", "test2", "practice", "test",]
    target = "test"
    print("The list is: ", my_list)
    print("The target is: ", target)
    print(bisect(my_list,target))
    print('\n')
    

    #G
    print("Part G")
    character_counter()
    print('\n')
    

    #H
    print("Part H")
    moby()
    
main()

