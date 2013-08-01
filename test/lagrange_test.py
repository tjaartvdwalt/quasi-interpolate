import sys
sys.path.append('../src/')
import quasi_interpolator

# Calculate the Lagrange Polynomials from
# example 1.2.1 on page 7
# we calculate the case L3,3

t = [-1, 0, 2, 3]
m = 3
k = 3
j = 0

print quasi_interpolator.lagrange(m, j, k, t)
