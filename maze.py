""" 
Assignment 8 - problem 1
maze.py
"""

from time import sleep 
from SimpleGraphics import *
setAutoUpdate(False)
resize(600,400)

from random import randint, random


# define the maze
maze = [[4,0,0,0,0,1],
        [1,1,0,0,2,1],
        [0,0,2,1,0,0],        
        [0,1,1,3,0,1],
        [0,1,0,0,1,0],              
        [0,1,1,0,0,5]]

#properties of player
ball_x, ball_y = maze[0][0], maze[0][0]
ball_size = 20             
ball_c = 'blue'          
ball_dx = random()*5-2.5   
ball_dy = random()*5-2.5
score = 0

boxw = getWidth()/6
boxh = getHeight()/6


		  
def draw(maze):
        """ 
        Draws the maze given as input
        The input is a two-dimensional list of integers
        """

        # width and height of the maze
        w = len(maze[0])  # width is number of columns
        h = len(maze)     # height is number of rows

        sizeWidth = getWidth()/w
        sizeHeight = getHeight()/h
                  
        for row in range(h):
                for col in range(w):
                        if maze[row][col] == 1: #empty cell
                                setColor('black')
                        elif maze[row][col] == 2:  #treasure
                                setColor('purple')
                        elif maze[row][col] == 3:  #theft
                                setColor('orange') 
                        elif maze[row][col] == 4:  #start
                                setColor('green')
                        elif maze[row][col] == 5: # exit
                                setColor('red')
                        else:
                                setColor('white')
                                        
                        rect(sizeWidth*col, sizeHeight*row, sizeWidth, sizeHeight)



        
while not closed():
        clear()
        draw(maze)

        setColor('Yellow')
        text(65,10, "Score: " + str(score))

        #drawing player
        setColor(ball_c)
        ellipse(ball_x, ball_y, ball_size, ball_size)

        # move the player
        ballrow = int(((ball_x+ball_dx))/boxw)
        ballcol = int(((ball_y+ball_dy))/boxh)

        keys = getHeldKeys()
        step = 0.20
        if "Up" in keys and "Down" not in keys:
                ball_dy = ball_dy - step
                
        if "Down" in keys and "Up" not in keys:
                ball_dy = ball_dy + step
                
        if "Left" in keys and "Right" not in keys:
                ball_dx = ball_dx - step
                
        if "Right" in keys and "Left" not in keys:
                ball_dx = ball_dx + step

        if maze[ballcol][ballrow]== 0:
                ball_dy = ball_dy
                ball_dx = ball_dx
        if maze[ballcol][ballrow]== 1: #doesn't go through black wall
                ball_dx = 0
                ball_dy = 0
        if maze[ballcol][ballrow] == 2: #treasure
                score +=1
                ball_dy = ball_dy
                maze[ballcol][ballrow] = 0               
        if maze[ballcol][ballrow] == 3: #theft
                score -= 1
                ball_dy = ball_dy
                maze[ballcol][ballrow]= 0
        if maze[ballcol][ballrow] == 4: #start
                ball_dx = ball_dx
                ball_dy = 0
        if maze[ballcol][ballrow] == 5: #end
                setFont("Times", "20", "bold") 
                text(getWidth()/2,getHeight()/2,"Game Over",)
                setFont("Times", "20", "bold") 
                text(getWidth()/2,getHeight()/2 + 25, "Your Score: " + str(score))
                break
        
        ball_x = ball_x + ball_dx
        ball_y = ball_y + ball_dy

        

        if ball_x <= 0 :
                ball_x = 0
        elif ball_x >= getWidth() - ball_size:
                ball_x = getWidth() - ball_size
        if ball_y <= 0:
                ball_y =0
        elif ball_y >= getHeight() - ball_size:
                ball_y = getHeight() - ball_size




                                


                                
                                

        sleep(0.01)
