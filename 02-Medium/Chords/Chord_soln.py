import sys

keys = {}
keys["A"] = ["A", "B", "C", "D", "E"]
keys["B"] = ["B", "Db", "D", "E", "Gb"]
keys["C"] = ["C", "D", "Eb", "F", "G"]
keys["D"] = ["D", "E", "F", "G", "A"]
keys["E"] = ["E", "Gb", "G", "A", "B"]
keys["F"] = ["F", "G", "Ab", "Bb", "C"]
keys["G"] = ["G", "A", "Bb", "C", "D"]

def translateProg(prog):
	result = []
	for i in prog:
		if i=="I":
			result.append(0)
		elif i=="II":
			result.append(1)
		elif i=="III":
			result.append(2)
		elif i=="IV":
			result.append(3)
		else:
			result.append(4)
	return result

def findKey(pattern, progression, firstNoteNum):
	
	for a,b in keys.iteritems():
		print "Key notes: ", b
		#b is the list of notes in this key, check for matches according to chord progression
		if b[progression[0]] == pattern[0] and b[progression[1]] == pattern[1]:
			print "Matched chords ", progression[0]+1,progression[1]+1," to ",pattern[0],pattern[1]
			return a

		if b[progression[1]] == pattern[0] and b[progression[2]] == pattern[1]:
			print "Matched chords ", progression[1]+1,progression[2]+1," to ",pattern[0],pattern[1]
			return a

		if b[progression[2]] == pattern[0] and b[progression[3]] == pattern[1]:
			print "Matched chords ", progression[2]+1,progression[3]+1," to ",pattern[0],pattern[1]
			return a

		if b[progression[3]] == pattern[0] and b[progression[0]] == pattern[1]:
			print "Matched chords ", progression[3]+1,progression[0]+1," to ",pattern[0],pattern[1]
			return a
	return "NULL"

input = open(sys.argv[1], "r")
oldKey = input.readline().strip('\n')
progress = input.readline().strip('\n').split(' ')
notes = input.readline().strip('\n').split(' ')

#Print all keys and notes
for a, b in keys.iteritems():
	print a, b

#Part I - identify progression place
iter = 0
place = 0

for i in keys[oldKey]:
	if notes[0] == i:
		place = iter
	iter = iter +1
prog = translateProg(progress)

print "Started on chord ", (place+1), " in the progression ", progress
	
#Part II - find new key
pattern = [notes[1], notes[2]]
newKey = findKey(pattern, prog, place)
if newKey == "NULL":
	print "No match found"
	sys.exit(1)
result = ""

#Part III - return the progression in the new key
result = result + keys[newKey][prog[0]] + " "
result = result + keys[newKey][prog[1]] + " "
result = result + keys[newKey][prog[2]] + " "
result = result + keys[newKey][prog[3]]

print result
