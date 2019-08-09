# Read a list of integers:
# a = [int(s) for s in input().split()]
# Print a value:
# print(a)
data = map(int,input().split())
for x in data :
  if x % 2 == 0 : print(str(x))
