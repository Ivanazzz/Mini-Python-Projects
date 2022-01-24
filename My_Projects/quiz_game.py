print()
print('Welcome to my capital city quiz!')
print()

playing = input('Do you want to play? ')

if playing.lower() != 'yes':  # here we convert the user's output all to lower case and if for example it's 'no' the programm will not start
    quit()
print()

print("Great! Let's start! :) ")
print()
score = 0

answer = input("What is the capital city of Germany? ")
if answer.lower() == "berlin":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
print()

answer = input("What is the capital city of Spain? ")
if answer.lower() == "madrid":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
print()

answer = input("What is the capital city of Malta? ")
if answer.lower() == "valletta":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
print()

answer = input("What is the capital city of Bulgaria? ")
if answer.lower() == "sofia":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
print()

answer = input("What is the capital city of Switzerland? ")
if answer.lower() == "bern":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
print()

answer = input("What is the capital city of Slovakia? ")
if answer.lower() == "bratislava":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
print()

answer = input("What is the capital city of Hungary? ")
if answer.lower() == "budapest":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
print()

answer = input("What is the capital city of Denmark? ")
if answer.lower() == "copenhagen":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
print()

answer = input("What is the capital city of Ireland? ")
if answer.lower() == "dublin":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
print()

answer = input("What is the capital city of Finland? ")
if answer.lower() == "helsinki":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
print()

print()
print("You got " + str(score) + " out of 10 questions correct!")
print("Your score is " + str((score)/10 * 100) + "%!")  
# to show the percentage, we divide the user's points by the number of questions and multiply the whole by 100 
