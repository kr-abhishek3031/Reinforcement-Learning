import random 
class EpsilonGreedy():
	def __init__(self , epsilon , counts , values):
		self.epsilon = epsilon 
		self.counts = counts  #vector that counts the number of times an arm is pulled 
		self.values = values #vector for avg value recieved when the arm is pulled.
		return
	#initialization
	def initialize(self , no_arms):    
		self.counts = [0 for i in range(no_arms)]
		self.values = [0.0 for i in range(no_arms)]
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

	def update(self , chosen_arm , reward ):
		self.counts[chosen_arm]=self.counts[chosen_arm]+1 ;
		n = self.counts[chosen_arm]
		value = self.values[chosen_arm]
		new_value = ((n-1)/float(n) * value )+ (1/float(n)) *reward
		self.values[chosen_arm] = new_value
		return  

print ("Enter the epsilon value")
x = float(input())
examp = EpsilonGreedy(x , [] , [] )
print ("Enter the number of arms")
y = int(input())
examp.initialize( y)
for i in range(1000):
	temp1 = examp.select_arm()
	rew = random.randrange(10)
	examp.update(temp1 , rew)
	print ("Selected arm ->" ,temp1)
	print ("Avg reward ->" , examp.values)


