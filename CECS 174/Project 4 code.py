#getting input
num = int(input('Please enter an integer (Negative to quit): '))

#while loop to iterate untill negative number is entered
while num >= 0:
    print('for the integer: ', num)
    if num >= 0 and num <=9:
        #For case when number is less than ten
        print('For the integer: ', num)
        print('Additive persistance: 0  Multiplicative persistence: 0')
        print('Additive root: ', num, 'Multiplicative root: ',num)
    
    elif num > 9 and num <= 999:
        #getting individual digits
        ones = num % 10
        tens = (num % 100) // 10
        hundreds = num // 100
        
        #getting additive root
        digit_sum = ones + tens + hundreds
        ones_digit_sum = digit_sum % 10
        tens_digit_sum = (digit_sum % 100) // 10
        additive_root = ones_digit_sum + tens_digit_sum
        
        #getting multiplicative root
        digit_product = ones * tens * hundreds
        ones_digit_product = digit_product % 10
        tens_digit_product = (digit_product % 100)// 10
        multiplicative_root = (tens_digit_product * ones_digit_product) % 10
        

        add_persistence = 1
        multi_persistence = 1
        total = num

        #getting persistences
        while total > 9:
            add_persistence += 1
            total = (num % 10) // 10
            multi_persistence += 1
            

        #printing results   
        print('Additive persistence: ',add_persistence, 'Additive root: ',additive_root )
        print('Multiplicative persistence: ', multi_persistence, 'Multiplicative root: ', multiplicative_root)

    else:
        #calculations for individual digits
        ones = num % 10
        tens = (num % 100) // 10
        hundreds = (num % 1000) // 100
        thousands = (num % 10000) // 1000
        digit_sum = ones + tens + hundreds + thousands

        
        ones_digit_sum = digit_sum % 10
        tens_digit_sum = (digit_sum % 100) // 10

        #getting additive root
        additive_root = ones_digit_sum + tens_digit_sum
        
        #calculations for multiplication
        digit_product = ones * tens * hundreds * thousands
        
        ones_digit_product = digit_product % 10
        tens_digit_product = (digit_product % 100)// 10
        
        #getting multiplicative root
        multiplicative_root = tens_digit_product * ones_digit_product
        

        
        #Gettinbg the persistences
        add_persistence = 1
        multi_persistence = 1
        total = num

        while total > 9:
            add_persistence += 1
            total = (total % 10) // 10
            multi_persistence += 1
            
        #printing results
        print('Additive persistence: ',add_persistence, 'Additive root: ',additive_root )
        print('Multiplicative persistence: ', multi_persistence, 'Multiplicative root: ', multiplicative_root)
            
            
    #continuing the code by asking for another input       
    print()   
    num = int(input('Please enter an integer (Negative to quit): '))


#Exiting code if the user is done
if num < 0:
    print('Thank you for playing with numbers...Goodbye')


