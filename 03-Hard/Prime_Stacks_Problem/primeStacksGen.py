#	Generates two lists of digits assembled from four random 3-digit primes
#	and outputs them to stdout.  Each is output as a csv on its own line,
#	representing the initial state of stack0 and stack1

import random
import math

def shuffle(nums):
	for i in range (len(nums)):
		choice = random.randint(0, len(nums)-1)
		choice2 = random.randint(0, len(nums)-1)
		temp = nums[choice]
		nums[choice] = nums[choice2]
		nums[choice2] = temp
	return

primesList = [101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997]
nums = []

num1 = str(random.choice(primesList))
num2 = str(random.choice(primesList))
num3 = str(random.choice(primesList))
num4 = str(random.choice(primesList))

for i in range(3):
	nums.append(int(num1[i]))
	nums.append(int(num2[i]))
	nums.append(int(num3[i]))
	nums.append(int(num4[i]))

shuffle(nums)

temp = ''
for i in range(6):
	if(i == 5):
		temp += str(nums[i])
	else:
		temp += str(nums[i]) + ", "
print temp
temp = ''
for i in range(6, len(nums)):
	if(i==len(nums)-1):
		temp += str(nums[i])
	else:
		temp += str(nums[i]) + ", "

print temp
