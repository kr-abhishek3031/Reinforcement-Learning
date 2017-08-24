#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 19:28:38 2017

@author: kumar
"""
import random 
import numpy as np 
import matplotlib.pyplot as plt

def stochastic_dist(no_arms):   
    x= np.array([[]])
    flag =0 
    for i in range(no_arms):    
        if flag==0:
            x = np.random.dirichlet(np.ones(10), size=1) #making dirichlet distribution 
            flag=1
        else:
            
            y =np.random.dirichlet(np.ones(10), size=1).ravel()
            x = np.vstack([x ,y])
    return x

class EpsilonGreedy():
    def __init__(self , epsilon , counts , values ,dist): #dist is distribution of probability distribution for each arm 
        self.epsilon = epsilon 
        self.counts = counts  #vector that counts the number of times an arm is pulled 
        self.values = values #vector for avg value recieved when the arm is pulled.
        self.dist = dist
        self.itr = 0
        self.netreward = [0]
        return
    #initialization
    def initialize(self , no_arms):    
        self.counts = [0 for i in range(no_arms)]
        self.values = [0.0 for i in range(no_arms)]
        self.dist = stochastic_dist(no_arms)
        return 
	#gives the index of the best arm 
    def best_arm(self ,val):
        temp = max(val)
        return val.index(temp)
    
    #selects on the basis of epsilon value whether to explore or exploit
    def select_arm(self):
        test = random.uniform(0.0 , 1.0)
        print ("Random value ->" ,test )
        if test > self.epsilon : 

            return self.best_arm(self.values)
        else:
            return random.randrange(len(self.counts))

    def update(self , chosen_arm ):
        self.counts[chosen_arm]=self.counts[chosen_arm]+1 ;
        self.itr = self.itr +1 
        #generate random  number between 1 to 10
        rd = random.randint(0, 9)
        reward = (rd+1)* (self.dist[chosen_arm][rd]) *10
        n = self.counts[chosen_arm]
        value = self.values[chosen_arm]
        if self.itr==1:
            self.netreward = np.append(self.netreward , reward)
            print ("hello")
        else :
            #print (len(self.netreward))
           # print (self.netreward)
           # print (self.itr)
            t = self.netreward[self.itr-2] + reward
            self.netreward = np.append(self.netreward , t )
            
        new_value = ((n-1)/float(n) * value )+ (1/float(n)) *reward
        self.values[chosen_arm] = new_value
        return  
   
no_of_itr =2000
print ("Enter the epsilon value")
x = float(input())
examp = EpsilonGreedy(x , [] , [] ,[[]])
print ("Enter the number of arms")
y = int(input())
examp.initialize( y)
for i in range(no_of_itr):
	temp1 = examp.select_arm()
	examp.update(temp1)

examp1 = EpsilonGreedy(0.001 ,[],[], [[]])	
examp1.initialize(y)
for i in range(no_of_itr):
	temp1 = examp1.select_arm()
	examp1.update(temp1)
print (examp.counts)
print (examp.values)
print (examp.itr)
print (examp.netreward)
for i in range(no_of_itr+1):
    examp.netreward[i] = examp.netreward[i] / (i+1)
    examp1.netreward[i] = examp1.netreward[i]/(i+1)
plt.plot(list(range(no_of_itr+1)), examp.netreward , list(range(no_of_itr+1)), examp1.netreward , 'k' )
plt.ylabel('average reward')
plt.show()
