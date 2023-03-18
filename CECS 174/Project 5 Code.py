print('Welecome to the Roman Numeral Calculator')

#function for getting roman numeral
def getRomanN():
    #getting input
    user = str(input('Enter a Roman Numeral '))
    roman = user.upper()

    #checking roman numeral with validation function
    while isValidRoman(roman) == False:
        print('\nInvalid Entry')
        user = str(input('Enter a Roman Numeral '))
        roman = user.upper()
        

    return roman


    
#function for validation a roman numeral
def isValidRoman(roman):
    #Make upper case
    for x in roman.upper():
        #Returns false if it is not a valid Roman Numeral
        if (x!= 'I' and x!= 'V' and x!= 'X' and x!= 'L' and x!= 'C'):
            return False
    
    #returns true if input is a valid roman numeral
    return True
    




#Function changing roman input to arabic
def romanToArabic(roman):

    total = 0
    #taking input and correlating roman to arabic values
    for i in (roman):
        if i == 'I':
            total += 1
        elif i == 'V':
            total += 5
        elif i == 'X':
            total += 10
        elif i == 'L':
            total += 50
        elif i == 'C':
            total += 100
    #subtraction rule
    if 'IV' in roman:
        total -= 2
    if 'IX' in roman:
        total -= 2
    if 'IL' in roman:
        total -= 2
    if 'IC' in roman:
        total -= 2
    if 'XL' in roman:
        total -= 20
    if 'XC' in roman:
        total -= 20

    print('Value of', roman, ': ', total)
    return total



    
#Function changing arabic calculations back to roman nunmerals          
def arabicToRoman(arabic):
    total = arabic
    #Creating list to append values to 
    r_numeral = []
    #Getting each digit place in the aravic number
    ones = total % 10
    tens = (total % 100) // 10
    hundreds = total // 100

    #Correlating arabic number to the roman numeral
    if ones:
        
        if ones == 9:
            r_numeral.append('IX')
        elif 5 < ones < 9:
            r_numeral.append('V' + ('I' * (ones % 5)))
        elif ones == 5:
            r_numeral.append('V')
        elif ones == 4:
            r_numeral.append('IV')
        elif ones < 4:
            r_numeral.append('I' * ones)

    #Correlating arabic number to the roman numeral
            
    if tens:
        if tens == 9:
            r_numeral.append('XC')
        elif 5 < tens < 9:
            r_numeral.append('X' * (tens % 5))
        elif tens == 5:
            r_numeral.append('L')
        elif tens == 4:
            r_numeral.append('XL')
        elif tens < 4:
            r_numeral.append('X' * tens)

    #Correlating arabic number to the roman numeral
            
    if hundreds:
        r_numeral.append('C' * hundreds)

    #Reversing the list to show the numeral correctly
    r_numeral.reverse()
    return r_numeral


    

    
#Funciton to add the numbers   
def add(roman1, roman2):
    #converting the inputs given to arabic numbers
    R_to_A = romanToArabic(roman1)
    R_to_A_pt2 = romanToArabic(roman2)
    #adding the numbers
    total_of_both = (R_to_A) + (R_to_A_pt2)
    print()

    #Converting arabic results back to roman numerals
    A_to_R = arabicToRoman(total_of_both)
    
    #printing results
    print(roman1, '+', roman2, '=', ''.join(A_to_R))
    print( R_to_A, '+', R_to_A_pt2, '=',total_of_both)
    print()
    
    return total_of_both
    



#Function to subtract the numbers
def sub(roman1, roman2):
    #converting the inputs given to arabic numbers
    R_to_A = romanToArabic(roman1)
    R_to_A_pt2 = romanToArabic(roman2)
    #subtracting the numbers
    difference_of_both = (R_to_A) - (R_to_A_pt2)
    print()

    #Converting arabic results back to roman numerals
    A_to_R = arabicToRoman(difference_of_both)

    #printing results
    print(roman1, '-', roman2, '=', ''.join(A_to_R))
    print( R_to_A, '-', R_to_A_pt2, '=',difference_of_both)
    print()
    




#Function the multiply the numbers 
def mul(roman1, roman2):
    #converting the inputs given to arabic numbers
    R_to_A = romanToArabic(roman1)
    R_to_A_pt2 = romanToArabic(roman2)
    #multiplying the numbers
    product_of_both = (R_to_A) * (R_to_A_pt2)
    print()

    #Converting arabic results back to roman numerals
    A_to_R = arabicToRoman(product_of_both)

    #printing results
    print(roman1, '*', roman2, '=', ''.join(A_to_R))
    print( R_to_A, '*', R_to_A_pt2, '=',product_of_both)
    print()
    



#function to divide the numbers
def div(roman1, roman2):
    #converting the inputs given to arabic numbers
    R_to_A = romanToArabic(roman1)
    R_to_A_pt2 = romanToArabic(roman2)
    #Dividing the numbers and finding remainder
    quotient_of_both = (R_to_A) // (R_to_A_pt2)
    remainder = (R_to_A) % (R_to_A_pt2)
    print()

    #Converting arabic results back to roman numerals
    A_to_R = arabicToRoman(quotient_of_both)
    A_to_R_pt2 = arabicToRoman(remainder)

    #printing results
    print(roman1, '/', roman2, '=', ''.join(A_to_R), 'remainder', ''.join(A_to_R_pt2))
    print( R_to_A, '/', R_to_A_pt2, '=',quotient_of_both, 'remainder ', remainder)
    print()



#Function to output the menu
def menu():
    
    #repeating untill its a proper input
    factor = False
    while factor == False:
        print('Please select from the following:')
        print()
        print('A- Add two Roman Numerals.')
        print('S- Subtract two Roman Numerals')
        print('M- Multiply two Roman Numerals')
        print('D- Divide two Roman Numerals')
        print('Q- Quit')
        print()
        get_selection = input('Select A, S, M, D or Q only. ')
        #converting to upper case so we dont have to check all cases
        selection = get_selection.upper()
        if selection != 'A' and selection != 'S' and selection != 'M' and selection != 'D' and selection != 'Q':
            print('Invalid entry. Please try again.')
            factor = False

        #returning the menu selction given when it's a correct input   
        else:
            factor = True
            return selection
        
    



#Main function that calls each function based on chosen value
def main(selection):

    #Calls the adding process when 'A' is chosen
    if selection == 'A':
        start = getRomanN()
        start2 = getRomanN()
        add(start,start2)
        
    #Calls the subtracting process when 'S' is chosen   
    if selection == 'S':
        start = getRomanN()
        start2 = getRomanN()
        sub(start,start2)
        
    #Calls the multiplying process when 'M' is chosen
    if selection == 'M':
        start = getRomanN()
        start2 = getRomanN()
        mul(start,start2)

    #Calls the dividing process when 'D' is chosen   
    if selection == 'D':
        start = getRomanN()
        start2 = getRomanN()
        div(start,start2)

    


        
#Loop that runs the program until user chooses 'Q'
test = 0
while test != 'Q':
    test = menu()
    main(test)
   
    
    
#Exits the program only when user chooses 'Q'
if test == 'Q':
    print()
    print('Goodbye')



