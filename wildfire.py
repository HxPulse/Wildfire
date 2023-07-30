#%%
from tkinter import *
from random import randint

def wildfire(h, l, p):
    # Simulate a wildfire in a grid of height h length l and with a propagation probability p
    # To properly use the display, close the window for each fire spreading iteration
    forest = [([0 for i in range(l)]) for j in range(h)]
    #show(forest)
    
    forest = random_fire(forest, p)
    #forest = initial_fire(forest)
    #show(forest)
    
    while still_in_fire(forest):
        forest = fire_spreading(forest, p)
        #show(forest)
        display_forest(forest)
    return('Fire extinguished')

def show(forest):
    # Displays the forest through the command terminal
    print('==================')
    for i in forest:
        print(i)
    print('===================')

def still_in_fire(forest):
    # Checks if the wildfire is still spreading
    # 0 = no fire
    # 1 = in fire
    # 2 = ashes
    
    for line in forest:
        for tile in line:
            
            if tile == 1:
                return True
    return False

def random_fire(forest, p):
    # Starts a random wildfire in a given forest and with a given probability p
    
    for i in range(len(forest)):
        for j in range(len(forest[i])):
            
            proba = randint(0, 100)
            if proba <= p * 10:
                forest[i][j] = 1
        
    return forest
    
def display_forest(forest):
    # Displays the forest in a TKinter window
    colors = ['green', 'orange', 'black']
    window = Tk()
    canva = Canvas(window, bg = 'white', height = 5*len(forest), width = 5*len(forest[0]))      
    canva.pack()
    for i in range(len(forest)):
        for j in range(len(forest[i])):
            canva.create_rectangle(5*i, 5*j, 5*i+5, 5*j+5, fill=colors[forest[i][j]])

    window.mainloop()

def fire_spreading(forest, p):
    # Spreads a wildfire in a given forest and with a propagation probability p
    tiles_to_spread = []
    for i in range(len(forest)):
        for j in range(len(forest[i])):
            
            if forest[i][j] == 1:
                neighbors = can_spread(forest, i, j)
                tiles_to_spread.append(neighbors)
                forest[i][j] = 2
                
                
    for tiles in tiles_to_spread:
        for tile in tiles:
            if randint(0, 100) <= p * 100:
                forest[tile[0]][tile[1]] = 1
    
    return forest
        
def can_spread(forest, i, j):
    neighbors = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for dx, dy in directions:
        x, y = i + dx, j + dy
        if 0 <= x < len(forest) and 0 <= y < len(forest[i]) and forest[x][y] == 0:
            neighbors.append([x, y])

    return neighbors
          
def initial_fire(forest):
    tiles = []
    n = int(input('How many tiles do you want to put fire up ?'))
    for i in range(n):
        coord1 = int(input('Fire spot ' + str(i) + ' x coord '))
        coord2 = int(input('Fire spot ' + str(i) + ' y coord '))
        tiles.append([coord1, coord2])
    for tile in tiles:
        forest[tile[0]][tile[1]] = 1
        
    return forest
    

wildfire(100, 100, 0.6)
        
                
                 
#%%
