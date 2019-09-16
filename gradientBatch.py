"""X-OR batch evaluation:
	TRUTH TABLE
  x0   x1   x2   target
  1     0    0    0
  1     0    1    1
  1     1    0    1
  1     1    1    0"""


x0 = 1
weight0 = 0
weight1 = 0
weight2 = 0

"""this is a recursive function which terminates when the error is less than 0.01: here if the error is greater than 0.01 then there is a small change in w0,w1 and w2, thus every 
time this function runs 4 computations(corresponding to each tuple) are done."""


def function ( w01, w02, w03 , w04 , w11, w12 , w13 , w14 , w21 , w22 , w23 , w24 , flag ,weight0,weight1,weight2):
	
	n = 1
	flag = flag + 1
	
	x11 = 0
	x21 = 0
	target1 = 0
	output1 = w01*x0 + w11*x11 + w21*x21
	x12 = 0
	x22 = 1
	target2 = 1
	output2 = w02*x0 + w12*x12 + w22*x22
	x13 = 1
	x23 = 0
	target3 = 1
	output3 = w03*x0 + w13*x13 + w23*x23
	x14 = 1
	x24 = 1
	target4 = 0
	output4 = w04*x0 + w14*x14 + w24*x24
	
	error = ( (target1-output1)*(target1-output1) + (target2-output2)*(target2-output2) + (target3-output3)*(target3-output3) + (target4-output4)*(target4-output4) )/2

	if error > 0.1 :
		weight0 = n*((target1 - output1)*x0 +(target2 - output2)*x0 +(target3 - output3)*x0 +(target4 - output4)*x0) + weight0
		weight1 = n*((target1 - output1)*x11 +(target2 - output2)*x12 +(target3 - output3)*x13 +(target4 - output4)*x14) + weight1
		weight2 = n*((target1 - output1)*x21 +(target2 - output2)*x22 +(target3 - output3)*x23 +(target4 - output4)*x24) + weight2
	
		w01 = w01 + weight0
		w02 = w02 + weight0
		w03 = w03 + weight0
		w04 = w04 + weight0

		w11 = w11 + weight1
		w12 = w12 + weight1
		w13 = w13 + weight1
		w14 = w14 + weight1

	
		w21 = w21 + weight2
		w22 = w22 + weight2
		w23 = w23 + weight2
		w24 = w24 + weight2
		
		function ( w01, w02, w03 , w04 , w11, w12 , w13 , w14 , w21 , w22 , w23 , w24 , flag ,weight0,weight1,weight2)
	else :
		print(output1,output2,output3,output4)
		print(w01, w02, w03 , w04 , w11, w12 , w13 , w14 , w21 , w22 , w23 , w24 )
		print("No of Iterations are")
		print(flag)
		return 
function(0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0,0,0,0)
	