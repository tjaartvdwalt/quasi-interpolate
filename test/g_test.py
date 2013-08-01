import sys
sys.path.append('../src/')
import quasi_interpolator

# Calculate g from equation 10.4.3 on page 322

m = 3
j = 0
t = [-1, 0, 2, 3]

print quasi_interpolator.g(m, j, t)
