import random
''' Movie Generator '''

movie_genre = input('Enter a movie genre you currently prefer: ')  # Here we make an intput for the user to choose a genre

action =['The Matrix', 'Pirates of the Caribbean', 'The Terminator', 'Mr & Mrs Smith', 'Rush Hour', 'Pearl Harbor']
comedy = ['Johnny English', 'Cheaper by the Dozen', 'The Pink Panther', 'Miss Congeniality', 'Bride Wars', 'Meet the Parents']
drama = ['A Walk to Remember', 'Me Before You', 'Braveheart', 'Karate Kid', 'Dear John', 'Midnight Sun']
fantasy = ['Charlie and the Chocolate Factory', 'Jumanji', 'Edward Scissorhands', 'Maleficent', 'Journey to the Center of the Earth', 'Alice in Wonderland'] 
horror = ['Final Destination', 'The Conjuring', 'Annabelle', 'A Quiet Place', 'Hush', 'Bird Box']
mystery = ['Gone Girl', 'Sherlock Holmes', 'Now You See Me', 'Now You See Me']
romance = ['Twilight', 'The Vow', 'The Proposal', 'Two Weeks Notice', '50 First Dates', 'Everything, Everything']
thriller = ['Speed', 'Non-Stop', 'Greenland', 'Skyscraper', 'San Andreas', 'Tidal Wave'] 
# In the lines above, we create lists that include movies of the same genre

if movie_genre == 'action':  # For example if the user entered 'action', on the next line the programm will print arbitrary movie from the corresponding list
    print(random.choice(action))  # The action is repeated for each genre
elif movie_genre == 'comedy':
    print(random.choice(comedy))
elif movie_genre == 'drama':
    print(random.choice(drama))
elif movie_genre == 'fantasy':
    print(random.choice(fantasy))
elif movie_genre == 'horror':
    print(random.choice(horror))
elif movie_genre == 'mystery':
    print(random.choice(mystery))
elif movie_genre == 'romance':
    print(random.choice(romance))
elif movie_genre == 'thriller':
    print(random.choice(thriller))
else:  # If the user has selected a genre not applied with a list, the program will print 'Error'
    print('Error')