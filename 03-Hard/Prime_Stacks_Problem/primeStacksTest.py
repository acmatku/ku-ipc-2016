

import sys

primesList = [101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997]

def isPrime(a,b,c,primesList):
	num = int(str(a) + str(b) + str(c))
	print "Checking ", num
	if(num in primesList):
		return True
	return False

#nums = sys.argv[1].split(',') + sys.argv[2].split(',')
stack0 = sys.stdin.readline().split(',')
stack1 = sys.stdin.readline().split(',')
stack2 = sys.stdin.readline().split(',')
returnedNums = []

nums.sort()


try:
	#check primes
	for i in range (4):
		a = stack0.pop()
		b = stack1.pop()
		c = stack2.pop()
		if not isPrime(a,b,c, primesList):
			print "Row ", (3-i), " is not a prime number: ", (str(a) + str(b) + str(c))
			sys.exit(-1)
		else:
			print "OK"
		returnedNums.append(a);
		returnedNums.append(b);
		returnedNums.append(c);

	#verify that we gave and got the same list of numbers
	returnedNums.sort()
	print "Input digits: ", nums
	print "Output digits: ", returnedNums
	for i in range (0, len(nums)):
		if nums[i] != returnedNums[i]:
			print "Given digits do not match returned digits!"
			sys.exit(-1)
	print "Correct!"
	sys.exit(0)

except Exception as err:
	print "Exception caught, could not read a number from each stack"
	print err
	sys.exit(-1)
