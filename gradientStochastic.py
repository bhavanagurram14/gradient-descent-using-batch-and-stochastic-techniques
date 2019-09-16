#XOR in Stochastic method
""" XOR Truth Table :
	x0  x1  x2  target
	1   0   0     0
	1   0   1     1
	1   1	0     1
	1   1   1     0"""


#the user enters the value for x1 and x2

print("Enter x1")
x1 = float(input())
print("Enter x2")
x2 = float(input())

#intialize the values of x0,w0,w1,w2

x0 = 1
w0 = 0.2
w1 = 0.2
w2 = 0.2
flag = 0
w00 = 0
w11 = 0
w22 = 0

#the targets are set based on the X-OR truth table

if 0.0<=x1<0.5 and 0.0<=x2<0.5 :	
	target = 0
elif 0.0<=x1<0.5 and 0.5<=x2<1.5 :
	target = 1
elif  0.5<=x1<1.5 and 0.0<=x2<0.5 :
	target = 1
else:
	target = 0 

#this is a recursive function which terminates when the error is less than 0.01

#we have set the learning rate to 0.01, small rates of learning rates are prefered so that the global minimum error point is not lost	

def function ( w0 , w1 , w2 , flag , w00 , w11, w22 ):
	
	flag = flag + 1
	output = w0*x0 + w1*x1 + w2*x2 
	n = 0.01
	error = ( target - output )*( target - output )/2
	if ( error >0.01) :
		w00 = w00 + n*(target-output)*x0
		w11 = w11 + n*(target-output)*x1
		w22 = w22 + n*(target-output)*x2
		w0 = w0 + w00
		w1 = w1 + w11
		w2 = w2 + w22
		function( w0 , w1 , w2 , flag , w00 , w11 , w22 )		
	else:
		print("Target is",target)
		print("Output is ",output)
		print("w0 , w1 , w2 are ",w0,w1,w2)
		print("No of Iterations are",flag)
		return 
function( w0 , w1, w2 , flag , w00 , w11 , w22)	