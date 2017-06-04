#Prime Factors in Python

import sys

print("This is the name of the script",sys.argv[0])
print("Numbers of arguments",len(sys.argv))
print("Numbers of arguments",str(sys.argv))

n = int(sys.argv[1])
result = []
for i in xrange(2,n):
    while n % i == 0:
        #print i,"|",n
        n = n/i
        result.append(i)

    if n == 1:
        break

if n > 1:
    result.append(n)
print result
