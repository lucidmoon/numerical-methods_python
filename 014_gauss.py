def gauss(A, b):
  n = len(A)
  # Forward elimination
  for k in range(n-1):
    if A[k][k] == 0:
      raise valueError("Pivot nol, algoritma gagal.")

    for i in range(k+1, n):
      m = A[i][k] / A[k][k]
      for j in range(k, n):
        A[i][j] -= m * A[k][j]
      b[i] -= m * b[k]
      
  # Back subtitution
  x = [0 for _ in range(n)]
  x[n-1] = b[n-1] / A[n-1][n-1]
  for i in range(n-2, -1, -1):
    sum_ax = 0
    for j in range(i+1, n):
      sum_ax += A[i][j] * x[j]
    x[i] = (b[i] - sum_ax) / A[i][i]
  return x

# Contoh Penggunaan
A = [
    [2, 3, -1],
    [4, 4, -3],
    [-2, 3, -1]
]
b = [5, 3, 1]
solusi = gauss(A, b)
print("Solusi sistem persamaan: ", solusi)
