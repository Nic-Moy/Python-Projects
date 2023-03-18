#constants
convert_gallons = 10
initial_residential = 5
initial_commercial = 1000
initial_industrial = 1000
initial_industrial_2 = 2000
residential_rate = .0005
commercial_rate = .00025
gallon_limit = 4000000
gallon_limit_2 = 10000000
meter_min = 0
meter_max = 999999999

#getting user input
customer_code = input('Enter the customer\'s code: ')
beginning_meter = int(input('Enter the customer\'s beginning meter reading: '))
end_meter = int(input('Enter the customer\'s end meter reading: '))
print('\n')

#calculating when code is r and checking range
if (customer_code == 'r' or customer_code == 'R') and (meter_min <= beginning_meter <= meter_max) and (meter_min <= end_meter <= meter_max):
    if end_meter > beginning_meter:
        #finding how much water is used
        water_used = (end_meter - beginning_meter) / convert_gallons
        #Cost including fee plue rate per gallon
        total_cost = initial_residential + (water_used * residential_rate)
    else:
        #Finding how much water is used while accounting for when the meter resets
        water_used = ((end_meter - beginning_meter) % convert_gallons) / convert_gallons
        #costincluding the fee plus the rate per gallon
        total_cost = initial_residential + (water_used * residential_rate)
        
    #printing results
    print('The customer\'s code: ', customer_code)
    print('The customer\'s beginning meter reading: {:0>9}'.format(beginning_meter))
    print('The customer\'s ending meter reading: {:0>9}'.format(end_meter))
    print('Gallons of water used: ', water_used)
    print('Amount billed: $',format(total_cost,".2f"))

#calculating when code is c and checking range
elif (customer_code == 'c' or customer_code == 'C') and (meter_min <= beginning_meter <= meter_max) and (meter_min <= end_meter <= meter_max):
    if end_meter > beginning_meter:
        #Finding how much water is used
        water_used = (end_meter - beginning_meter)/ convert_gallons
        #finding cost if water used is over the company's limit
        if water_used > gallon_limit:
            total_cost = initial_commercial + ((water_used - gallon_limit) * commercial_rate)
        #finding cost if water is not over the limit
        else:
            total_cost = initial_commercial
            
    else:
        #Finding how much water is used while accounting for when the meter resets
        water_used = ((end_meter - beginning_meter) % convert_gallons) / convert_gallons
        #finding cost if water used is over the company's limit
        if water_used > gallon_limit:
            total_cost = initial_commercial + ((water_used - gallon_limit) * commercial_rate)
        #finding cost if water is not over the limit
        else:
            total_cost = initial_commercial
        
    #printing results
    print('The customer\'s code: ', customer_code)
    print('The customer\'s beginning meter reading: {:0>9}'.format(beginning_meter))
    print('The customer\'s ending meter reading: {:0>9}'.format(end_meter))
    print('Gallons of water used: ', water_used)
    print('Amount billed: $',format(total_cost,".2f"))


#calculating when code is i and checking range
elif (customer_code == 'i' or customer_code == 'I') and (meter_min <= beginning_meter <= meter_max) and (meter_min <= end_meter <= meter_max):
    if end_meter > beginning_meter:
        #finding how much water is used
        water_used = (end_meter - beginning_meter)/ convert_gallons
        #finding cost if water used is less or equal to the company's first limit
        if water_used <= gallon_limit:
            total_cost = initial_industrial

        #finding cost if water used is over the company's first limit and less than the comapny's second limit
        elif water_used > gallon_limit and water_used < gallon_limit_2:
            total_cost = initial_industrial_2

        #finding cost if water used is over the company's second limit
        elif water_used > gallon_limit_2:
            total_cost = initial_industrial_2 + ((water_used - gallon_limit_2) * commercial_rate)
            
            

    else:
        #Finding how much water is used while accounting for when the meter resets
        water_used = ((end_meter - beginning_meter) % convert_gallons) / convert_gallons
        #finding cost if water used is less or equal to the company's first limit
        if water_used <= gallon_limit:
            total_cost = intial_industrial
            
        #finding cost if water used is over the company's first limit and less than the comapny's second limit
        elif water_used > gallon_limit and water_used < gallon_limit_2:
            total_cost = initial_industrial_2

        #finding cost if water used is over the company's second limit
        elif water_used > gallon_limit_2:
            total_cost = initial_industrial_2 + ((water_used - gallon_limit_2) * commercial_rate)

    #printing results
    print('The customer\'s code: ', customer_code)
    print('The customer\'s beginning meter reading: {:0>9}'.format(beginning_meter))
    print('The customer\'s ending meter reading: {:0>9}'.format(end_meter))
    print('Gallons of water used: ', water_used)
    print('Amount billed: $',format(total_cost,".2f"))
            
    
#Checking for incorrect inputs
else:
    if customer_code != ('r', 'R', 'I', 'i', 'c', 'C'):
        print('The customer\'s code: ', customer_code)
        print('The customer\'s beginning meter reading: {:0>9}'.format(beginning_meter))
        print('The customer\'s ending meter reading: {:0>9}'.format(end_meter))
        print('Invalid Entry')
        print('Gallons of water used: 0.0')
        print('Amount billed: $0.00')
        
    
