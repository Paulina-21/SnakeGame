
import numpy as np
from random import randint 
from typing import List
from models.snake import Snake
from models.directions import Directions
class PlayGround:
    """
    PlayGround Class
    for future improvements (ex. obstacles)
    """
    def __init__(self,n):
        self.n=n      

class View:
    """
    View Class

    Attributes
    ----------
        matrix: list[list[int,int]]
    
    Methods
    -------
        draw(snake: Snake)
        
    """
    matrix:list[list[int,int]]=[]
    def __init__(self,play_ground:PlayGround):
        self.play_ground=play_ground
    
    def draw(self,new_snake:Snake):
        if (new_snake.coordinates[0][0]<0 or 
            new_snake.coordinates[0][1]<0 or 
            new_snake.coordinates[0][0]>=self.play_ground.n or
            new_snake.coordinates[0][1]>=self.play_ground.n):
                raise Exception("You hit the wall")
        self.matrix=[]

        food_coord=get_food_coordinates(new_snake,self.play_ground.n)
        print(food_coord)
        for y_coord in range (self.play_ground.n):
            self.matrix.append([])
            for x_coord in range(self.play_ground.n):
                #add 1 if coordinates of snake
                if [y_coord,x_coord] in new_snake.coordinates:
                    self.matrix[y_coord].append(1)
                elif[y_coord,x_coord]== food_coord:
                    self.matrix[y_coord].append(3)
                else: self.matrix[y_coord].append(0)
            print(self.matrix[y_coord])

def get_food_coordinates(snake:Snake,n:int)->List[int]:
    coord=[randint(0,n),randint(0,n)]
    while coord in snake.coordinates:
        coord=[randint(0,n),randint(0,n)]
    return coord

def start():
    while True:
        n=input("Dimmensions for playground")
        
        try:
    
            s1=Snake([[2,2],[2,3]]) 
            #print(get_food_coordinates(s1,10))
            p1=PlayGround(10)
            print(p1)
            v1=View(p1)
            v1.draw(s1)
            s1.move(Directions.Up)
            print()
            print()
            v1.draw(s1)
            s1.move(Directions.Up)
            print()
            print()
            v1.draw(s1)
            s1.move(Directions.Up)
            print()
            print()
            v1.draw(s1)
    
        except Exception as ex:
            print(ex)

start()
