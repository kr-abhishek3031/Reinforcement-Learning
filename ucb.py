#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 1:24:38 2017

@author: kumar
"""
import random 
import numpy as np 
import matplotlib.pyplot as plt
import math
def gaussian_dist(no_arms):
    x = np.random.normal(1 ,1 ,no_arms) #calculating the mean value for normal distribution of each arm 
    
    return x 

class Ucb():
    def __init__(self , c , counts , values):
        self.c = c
        self.counts = counts  #vector that counts the number of times an arm is pulled 
        self.values = values #vector for avg value recieved when the arm is pulled.
        self.itr = 1
        self.netreward = [] #this has reward at each iteration
        self.actualmean = []   #mean of each arm around which gaussian distribution is taken 
        self.optarray= []
        self.target_itr = 0
        self.opt_count =0  #counts number of times optimal action is taken 
        return

    #initialization
    def initialize(self , no_arms, mean_of_dist ,itrs):    
        self.counts = [0 for i in range(no_arms)]
        self.values = [0.0 for i in range(no_arms)]
        self.actualmean = mean_of_dist
        self.target_itr = itrs
        return 

    def select_arm(self ,no_arms):
    	explor_para = []
    	for i in range(no_arms):
    		if self.counts[i]==0:
    			parameter = 100000 # large value that can't be attained ,i.e., the actions is maximizing
    		else :
    			parameter = self.values[i] + self.c *(math.sqrt((math.log(self.itr))/self.counts[i] ) )
    		explor_para = explor_para + [parameter]
    	return explor_para.index(max(explor_para))

    def update(self , chosen_arm ):
        self.counts[chosen_arm]=self.counts[chosen_arm]+1 ;
        
        #generate random  number between 1 to 10
        
       # rd = random.randint(0, 9)
        if chosen_arm == np.argmax(self.actualmean):
            self.opt_count = self.opt_count +1
        self.optarray = self.optarray + [self.opt_count]
        reward=np.random.normal(self.actualmean[chosen_arm], 1 ,1)
        
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
        self.itr = self.itr +1 
        return  
    
    def iterations(self , no_arms):
        for i in range(self.target_itr):
            temp = self.select_arm(no_arms)
            self.update(temp)
        return

'''
no_of_itr = 1000
c=2
test = Ucb(c , [],[])
print ("Enter the number of arms")
y = int(input())
mean_dist = gaussian_dist(y)
test.initialize(y , mean_dist ,no_of_itr)
test.iterations(y)
print (test.opt_count)
'''