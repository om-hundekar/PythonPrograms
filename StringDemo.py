s1="Hello World"
#    0 1 2 3 4 5 6 7 8 9 10
#s1= H e l l o   W o r l d
#                      -2-1
print(s1)
print("Length : ",len(s1))
print("Character at 0 index : ",s1[0])
print("Character at 7 index : ",s1[7])

#Slicing
#s1[startingindex:endindex]
print("Slicing from 2 to 8",s1[2:8])
print("Slicing from 1 to 9 with step 2",s1[1:9:2])

#if end index is not given then it will print upto last character
print("Slicing from 2 ",s1[2:])
#if start index is not given then it will print from 0th index 
print("Slicing upto 8 ",s1[:8])


