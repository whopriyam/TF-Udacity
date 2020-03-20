def HelloWorld(x,y):
	if (x<10):
	  print ("X was less than 10")
	elif (x<20):
	  print ("X less than 20. but greater than 10")
	else:
	  print ("X greater than 20")

	return x+y

for i in range (8,25,5):
	print("Now running with i:{}".format(i))
	r = HelloWorld(i,i)
	print ("Result from HelloWorld i:{}".format(i,r))