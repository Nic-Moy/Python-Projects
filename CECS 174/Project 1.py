#getting input times from user
current_time = int(input('Enter the time now (hour): '))
wait_time = int(input('Enter how long till you would like the alarm: '))
combined_time = current_time + wait_time

#testing if it is correct military time
if current_time < 0 or current_time > 24:
    print('That\'s not military time!')

#determining what the time will be using modulus 
if combined_time > 24:
    real_time = combined_time % 24
    if real_time > 11:
        conversion = real_time - 12
        print('The alarm will go off at: ',conversion, 'P.M.')
    elif real_time == 0 or real_time == 24:
        print('The alarm will go off at: 12 A.M.')
    
    else:
        print('The alarm will go off at: ',real_time, 'A.M')
        

#No need for modulus if time is under 24 hours
if combined_time <= 23:
    if combined_time > 11:
        print('The alarm will go off at: ', combined_time - 12, 'P.M')
    else:
        
        print('the alarm will go off at: ',combined_time, 'A.M')
    


