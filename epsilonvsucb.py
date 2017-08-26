#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 19:28:38 2017

@author: kumar
"""
import random 
import numpy as np 
import matplotlib.pyplot as plt
#from scipy.stats import norm
import ucb
def gaussian_dist(no_arms):
    x = np.random.normal(1 ,1 ,no_arms) #calculating the mean value for normal distribution of each arm 
    
    return x 
'''
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
'''
class EpsilonGreedy():
    def __init__(self , epsilon , counts , values ): #dist is distribution of probability distribution for each arm 
        self.epsilon = epsilon 
        self.counts = counts  #vector that counts the number of times an arm is pulled 
        self.values = values #vector for avg value recieved when the arm is pulled.
        self.itr = 1
        self.netreward = []
        self.actualmean = []
        self.optarray= []
        self.target_itr = 0
        self.opt_count =0
        return
    #initialization
    def initialize(self , no_arms, mean_of_dist ,itrs):    
        self.counts = [0 for i in range(no_arms)]
        self.values = [0.0 for i in range(no_arms)]
        self.actualmean = mean_of_dist
        self.target_itr = itrs
        return 
	#gives the index of the best arm     
            
    def best_arm(self ,val):
        temp = max(val)
        return val.index(temp)
    
    #selects on the basis of epsilon value whether to explore or exploit
    def select_arm(self):
        test = random.uniform(0.0 , 1.0)
       # print ("Random value ->" ,test )
        if test > self.epsilon : 

            return self.best_arm(self.values)
        else:
            x =np.random.randint(len(self.counts))
            return x

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
    
    def iterations(self ):
        for i in range(self.target_itr):
            temp = self.select_arm()
            self.update(temp)
        return

print ("Enter the epsilon value")
x = float(input())
print ("Enter the number of arms")
no_arms = int(input())
print ("Enter the value of C(for ucb)")
c= int(input())
print ("Enter the number of iterations")
no_of_itr= int(input())
mean_dist = gaussian_dist(no_arms)
'''
examp1 = EpsilonGreedy(0.01 ,[],[] )	
examp1.initialize(no_arms , mean_dist, no_of_itr)
examp1.iterations()
    
examp2 = EpsilonGreedy(0 ,[],[] )	
examp2.initialize(no_arms , mean_dist, no_of_itr)
examp2.iterations()
'''
c=2
examp = EpsilonGreedy(x , [] , [] )
examp.initialize( no_arms ,mean_dist,no_of_itr)
examp.iterations()
ucb_exam = ucb.Ucb(c, [], [])
ucb_exam.initialize(no_arms, mean_dist, no_of_itr)
ucb_exam.iterations(no_arms)

print (examp.counts)
print (examp.values)
print (ucb_exam.counts)
print (ucb_exam.values)
'''
print(examp1.counts)
print (examp1.values)
print(examp2.counts)
print (examp2.values)
'''
#print (examp.netreward)
for i in range(no_of_itr):
    examp.netreward[i] = examp.netreward[i] / (i+1)
    examp.optarray[i] = (examp.optarray[i] /(i+1))*100
    '''
    examp1.netreward[i] = examp1.netreward[i]/(i+1)
    examp1.optarray[i] = (examp1.optarray[i] /(i+1))*100
    examp2.netreward[i] = examp2.netreward[i]/(i+1)
    examp2.optarray[i] = (examp2.optarray[i] /(i+1))*100
    '''
    ucb_exam.netreward[i] = ucb_exam.netreward[i]/(i+1)
    ucb_exam.optarray[i]= (ucb_exam.optarray[i]/(i+1))*100
plt.figure(1)
plt.subplot(211)
plt.plot(list(range(no_of_itr)), examp.netreward ,'b', list(range(no_of_itr)), ucb_exam.netreward ,'k')
plt.ylabel('average reward')
plt.subplot(212)
plt.plot(list(range(no_of_itr)), examp.optarray ,'b', list(range(no_of_itr)), ucb_exam.optarray ,'k')
plt.ylabel('optimal %')
plt.show()
