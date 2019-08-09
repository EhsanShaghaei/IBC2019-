# Read a string:
# s = input()
# Print a value:
# print(s)
# data = list(input().split())
# dictionary={}
# loopTimes = int(data [0])

# data.pop(0);
# c = 0
# for  i in range(0,loopTimes*2,2):
#   dictionary [data [i+1]] = data [i] 
  
#   c = i+2
# if data[c] in dictionary :
#   print(dictionary[data[c]])
dictionary = {}
for i in range(int(input())):
  a,b = input().split()
  dictionary[b] = a
  dictionary[a] = b
d = input()
if d in dictionary:
  print (dictionary[d] )


  
