# Read a list of integers:
# a = [int(s) for s in input().split()]
# Print a value:
# print(a)
data = list( map(int, input().split() ) )
print(max(data),data.index(max(data)))
