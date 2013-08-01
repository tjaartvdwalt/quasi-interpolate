import sys
sys.path.append('../src/')
import quasi_interpolator

# Calculate alpha
# example (c)  on page 335
# choose r = 0
t = [-3, -2, -1 , 0, 1, 2, 3, 4]
m = 3
j = 0

for k in range(0, 4):
  print quasi_interpolator.alpha(m, j, k, t)
