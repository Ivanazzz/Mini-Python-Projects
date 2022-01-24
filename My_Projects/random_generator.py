import random
'''Random Generator''' # For people whо can't decide ;)
number = int(input('Enter the number of objects between which any will be drawn: '))
random_list = []
objects_count = 0

if number <= 0:   # In this if loop we will show wheter the user entered a number less than or equal to zero
    print('The number you entered cannot be equal to or less than 0!')

elif number > 0:   # In this case, when the number is greater than zero (as it should be), we start a while loop on the next line
    while objects_count < number:   # The While loop works like this: On line 11 checks wheter the objects count (on line 5 it is determined that is equal to zero) is less than the number entered by the user. 
        objects = input('Enter the relevant objects: ')  # As long as the previous statement is true, it will allow the user to enter the corresponding objects, from which the program will choose arbitrarily.
        random_list.append(objects)  # The value entered by the user will then be added to the initially empty list (on line 4 we create an empty list).
        objects_count += 1  # To end the while loop at some point, we increase the value of the objects count by 1 each time, before the loop starts checking again.
    print(random.choice(random_list))  # When the objects count is greater than the number entered by the user, the loop will stop and print the result (in our case, the arbitrary object).