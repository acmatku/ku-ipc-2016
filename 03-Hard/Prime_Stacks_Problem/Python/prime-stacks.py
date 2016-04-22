#Stephen Longofono
#Prime Stacks, Solution
#April 21, 2016

#Expects 5 space-delineated lines of intgers
#first and second line are the original stacks given as input, bottom to top
#third, fourth, and fifth are the solution stacks, bottom to top
#This solves the optimal solution, which should be the first one they could
#arrive at using a breadth first search because science

import sys
import traceback

def deepcopy(src):
	temp = []
	for i in src:
		temp.append(i)
	return temp

def solveIt(stack0, stack1, stack2):
	moves = []
	state = []
	state.append(stack0)
	state.append(stack1)
	state.append(stack2)
	print "Starting states:"
	print stack0, stack1, stack2
	notDone = True
	count = 0;

	#BFS on valid stack moves	print count
	while(notDone):
		#populate new moves from current state
		addMoves(moves, state)

		#update the state to the first move added (make the move)
		state = moves[0]
		moves = moves[1:] #pop the move

		#if we have a solution, we are done, break
		if(checkSolved(state)):
			notDone = False

		count = count + 1

	return state, count

def addMoves(moveStack, state):

	a = state[0]
	b = state[1]
	c = state[2]

	#stack0 to stack1
	if(len(a)>0) and (len(b)<6):
			frame = []
			frame.append(a[:len(a)-1])#add first stack with top removed
			temp = deepcopy(b)
			temp.append(a[-1])
			frame.append(temp)#add removed to second stack
			frame.append(c)#third stack unchanged
			moveStack.append(frame)

	#stack 0 to stack2
	if(len(a)>0) and (len(c)<6):
			frame = []
			frame.append(a[:len(a)-1])#add first stack with top removed
			frame.append(b)#second stack unchanged
			temp = deepcopy(c)
			temp.append(a[-1])
			frame.append(temp)#add removed to third stack
			moveStack.append(frame)

	#stack1 to stack0
	if(len(b)>0) and (len(a)<6):
			frame = []
			temp = deepcopy(a)
			temp.append(b[-1])
			frame.append(temp)#add removed to first stack
			frame.append(b[:len(b)-1])#add second stack with top removed
			frame.append(c)#third stack unchanged
			moveStack.append(frame)

	#stack1 to stack2
	if(len(b)>0) and (len(c)<6):
			frame = []
			frame.append(a)#first stack unchanged
			frame.append(b[:len(b)-1])#add second stack with top removed
			temp = deepcopy(c)
			temp.append(b[-1])
			frame.append(temp)#add removed to third stack
			moveStack.append(frame)

	#stack2 to stack0
	if(len(c)>0) and (len(a)<6):
			frame = []
			temp = deepcopy(a)
			temp.append(c[-1])
			frame.append(temp)#add removed to first stack
			frame.append(b)#second stack unchanged
			frame.append(c[:len(c)-1])#add third stack with top removed
			moveStack.append(frame)

	#stack2 to stack1
	if(len(c)>0) and (len(b)<6):
			frame = []

			frame.append(a)#first stack unchanged
			temp = deepcopy(b)
			temp.append(c[-1])
			frame.append(temp)#add removed to second stack
			frame.append(c[:len(c)-1])#add third stack with top removed
			moveStack.append(frame)


def checkSolved(state):
	a = state[0]
	b = state[1]
	c = state[2]
	if (len(a)<3) or (len(b)<3) or (len(c)<3):
		return False
	for i in range (0,3):
		if not isPrime(a[i], b[i],c[i]):
			return False
	return True

def isPrime(a,b,c):
	primesList = [101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997]
	num = int(str(a) + str(b) + str(c))
	if(num in primesList):
		return True
	return False

nums = sys.stdin.readline().strip('\n').split(' ')
nums2 = sys.stdin.readline().strip('\n').split(' ')
stack0 = sys.stdin.readline().strip('\n').split(' ')
stack1 = sys.stdin.readline().strip('\n').split(' ')
stack2 = sys.stdin.readline().strip('\n').split(' ')


teststack0 = nums
teststack1 = nums2
teststack2 = []

print "Read in input: "
print nums
print nums2

print"Read in solution: "
print stack0
print stack1
print stack2

try:
	for i in range (0,2):
		a = stack0[i]
		b = stack1[i]
		c = stack2[i]
		if not isPrime(a,b,c):
			print "Not a prime number: ", (str(a) + str(b) + str(c))
			sys.exit(-1)

	print "Done"
	#verify that the solution given is the ideal
	#get ideal solution
	ideal, count = solveIt(teststack0, teststack1, teststack2)
	teststack0 = ideal[0]
	teststack1 = ideal[1]
	teststack2 = ideal[2]

	print "Ideal: "
	print teststack0
	print teststack1
	print teststack2

	if (teststack0==stack0) and (teststack1==stack1) and (teststack2==stack2):
		print "Given solution is correct!"
		#if(int(moves) > count):
		#	print "Not an ideal solution, you had more moves than necessary..."
	else:
		print "Given solution is incorrect, you made invalid moves!"
	sys.exit(0)

except Exception as err:
	print "Exception..."
	print err
	traceback.print_exc()
	sys.exit(-1)
