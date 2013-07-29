import quasi_interpolator

# Tests the B-spline function using example 10.2.2 page 306
m_max = 3
#m_max = 0
x = 3
t = [0, 1, 2, 4, 5]
for j in range(0, m_max + 1):
  row = []
  for m in range(0, (m_max + 1) - j):
    row.append(quasi_interpolator.b_spline(m, j, x, t))
  print row

