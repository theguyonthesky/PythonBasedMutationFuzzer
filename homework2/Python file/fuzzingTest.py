import random
import subprocess
import re
import os 
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
count10 = 0
count11 = 0
count12 = 0
count13 = 0

with open('cross.jpg', 'rb') as file:
	array = file.read()
	byte_array = bytearray(array)
#print(byte_array)

# pythonda function yaradarsan, functionun icine arrayivi otur, ve functionun icinde index ve value yarat random, arrayivin random indexindeki valueunu random valueya deyish

# python dictionaryler haqda oyren. mene dictionary yarat icinde 4 string key olsun ve 4 integer value olsun 

# burdan asagi forun icinde yaz. foru 0dan 10000e qeder calishdir

for x in range (0, 100):

	index = random.randrange(len(byte_array))
	#print('index: '+str(index))

	value = bytes([random.randint(0,255)])
	#print('value: ' + str(value))

	byte_array[index] = value[0]

	#print('modified array:')
	#print(byte_array)

	with open('test.jpg', 'wb') as file:
		file.write(byte_array)

	command = "./jpeg2bmp test.jpg test.bmp"

	result = subprocess.run(command, shell=True, capture_output=True, text=True)

	#print(result.stderr)

	if "Triggering Bug" in result.stderr:
		#print("1ci if")
		match = re.search(r"Bug #(\d+)", result.stderr)
		#print('match: '+str(match))
		if match:
			bug_number = match.group(1)
			if str(bug_number) == "1":
				count1 = count1 + 1
			elif str(bug_number) == "2":
				count2 = count2 + 1
			elif str(bug_number) == "3":
				count3 = count3 + 1
			elif str(bug_number) == "4":
				count4 = count4 + 1
			elif str(bug_number) == "5":
				count5 = count5 + 1
			elif str(bug_number) == "6":
				count6 = count6 + 1
			elif str(bug_number) == "7":
				count7 = count7 + 1
			elif str(bug_number) == "8":
				count8 = count8 + 1
			elif str(bug_number) == "9":
				count9 = count9 + 1
			elif str(bug_number) == "10":
				count10 = count10 + 1
			elif str(bug_number) == "11":
				count11 = count11 + 1
			elif str(bug_number) == "12":
				count12 = count12 + 1
			elif str(bug_number) == "13":
				count13 = count13 + 1
			os.rename("test.jpg", "test-"+str(bug_number)+".jpg")
			#print(f"Bug number: {bug_number}")
			
print("Bug 1 is encountered " +str(count1)+ " times")
print("Bug 2 is encountered " +str(count2)+ " times")
print("Bug 3 is encountered " +str(count3)+ " times")
print("Bug 4 is encountered " +str(count4)+ " times")
print("Bug 5 is encountered " +str(count5)+ " times")
print("Bug 6 is encountered " +str(count6)+ " times")
print("Bug 7 is encountered " +str(count7)+ " times")
print("Bug 8 is encountered " +str(count8)+ " times")
print("Bug 9 is encountered " +str(count9)+ " times")
print("Bug 10 is encountered " +str(count10)+ " times")
print("Bug 11 is encountered " +str(count11)+ " times")
print("Bug 12 is encountered " +str(count12)+ " times")
print("Bug 13 is encountered " +str(count13)+ " times")
