import numpy as np
a=np.array(["Hello","World"])
a=np.append(a,"!")
print ("Current array: {}".format(a))
for i in a:
	print(i)
print("Print each element and their index")
for i,e in enumerate(a):
	print("Index: {}, was: {}".format(i,e))