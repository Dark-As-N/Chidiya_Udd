import numpy as np
from Project2_DAN import *
import time
list1 = [0,0,0]
list1 = motiondetector(list1)
print (list1)
if (NotFly)
	if (list1[0]==1 or list1[1]==1 or list1[2]==1):
		if(list1[0]==1 and list1[1]==1 and list1[2]==1):
			print("Execute all")
		elif(list1[0]==1 and list1[1]==1 and list1[2]==0):
			print("Execute player 1 and 2")
		elif(list1[0]==1 and list1[1]==0 and list1[2]==1):
			print("Execute player 1 and 3")
		elif(list1[0]==0 and list1[1]==1 and list1[2]==1):
			print("Execute player 2 and 3")
		elif(list1[0]==1 and list1[1]==0 and list1[2]==0):
			print("Execute player 1")
		elif(list1[0]==0 and list1[1]==1 and list1[2]==0):
			print("Execute player 2")
		elif(list1[0]==0 and list1[1]==0 and list1[2]==1):
			print("Execute player 3")
	else:
		print("Dont execute")
if (fly):
	if (list1[0]==0 or list1[1]==0 or list1[2]==0):
		if(list1[0]==0 and list1[1]==0 and list1[2]==0):
			print("Execute all")
		elif(list1[0]==0 and list1[1]==0 and list1[2]==1):
			print("Execute player 1 and 2")
		elif(list1[0]==0 and list1[1]==1 and list1[2]==0):
			print("Execute player 1 and 3")
		elif(list1[0]==1 and list1[1]==0 and list1[2]==0):
			print("Execute player 2 and 3")
		elif(list1[0]==0 and list1[1]==1 and list1[2]==1):
			print("Execute player 1")
		elif(list1[0]==1 and list1[1]==0 and list1[2]==1):
			print("Execute player 2")
		elif(list1[0]==1 and list1[1]==1 and list1[2]==0):
			print("Execute player 3")
	else:
		print("Dont execute")
	
