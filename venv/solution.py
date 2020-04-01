import sys
import math


a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

b /= a
c /= a
a /= a

print(f'{int(-b/2 + math.sqrt((b/2)**2-c))}')
print(f'{int(-b/2 - math.sqrt((b/2)**2-c))}')