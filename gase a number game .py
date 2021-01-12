import random
randomno=random.randint(1,100)
print ("guess number between 1 to 100  ")

userinput=None 
guess=0
while userinput != randomno :
	userinput=int (input("guess a number : "))
	guess = guess+1
	if randomno==userinput:
		print(" you win !!! ")
	else:
		if userinput > randomno:
			print ("wrong guess , try smaller  number ")
		else :
			print ("wrong guess , try grater number ")
		
	
print (f"\n\tyou guess {randomno} in  {guess} times")

with open("highscore.txt") as f:
	readscore=int( f.read())
	print(f" old record : {readscore}")

if guess < readscore:
	with open ("highscore.txt",'w') as f:
		print("\n\tOld record is breacked !!!\n")
		print ("\n\tyour newrecod is saved in a file ")
		f.write(str(guess))
	



