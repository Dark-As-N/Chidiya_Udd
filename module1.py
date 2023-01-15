
 
import os
filename = "2.png"
tempTuple = os.path.splitext(filename)
# print(tempTuple)
filename = tempTuple[0]
res = [int(i) for i in filename.split() if i.isdigit()]
x=res[0]
print(x)
