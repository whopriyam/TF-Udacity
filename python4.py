import numpy as np
print ("Showing some basic math on arrays")
b = np.array([0,1,4,3,2])
print ("Max: {}".format(np.max(b)))
print ("Average: {}".format(np.average(b)))
print ("Max Index: {}".format(np.argmax(b)))

print ("Make a 3x3 array with random numbers")
c = np.random.rand(3,3)
print (c)

print ("Shape of b: {}".format(b.shape))
print ("Shape of c: {}".format(c.shape))