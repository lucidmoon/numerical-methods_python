def gauss_jordan(A, b):
  n = len(A)
  # Forward elimination dengan pivot parsial
  for k in range(n-1):
    # Cari pivot terbesar di kolom k
    max_row = max(range(k, n), key=lambda i: abs(A[i][k]))
    if A[max_row][k] == 0:
      raise ValueError("Pivot nol, sistem tidak dapat diselesaikan.")
    # Tukar baris
    if max_row != k:
      A[k], A[max_row] = A[max_row], A[k]
      b[k], b[max_row] = b[max_row], b[k]
    # Eliminasi
    for i in range(k+1, n):
      m = A[i][k] / A[k][k]
      for j in range(k, n):
        A[i][j] -= m * A[k][j]
      b[i] -= m * b[k]
      
  # Back Substitution (sejajar dengan loop 'for k')
  x = [0 for _ in range(n)]
  x[n-1] = b[n-1] / A[n-1][n-1]
  for i in range(n-2, -1, -1):
    sum_ax = sum(A[i][j] * x[j] for j in range(i+1, n))
    x[i] = (b[i] - sum_ax) / A[i][i]
  return x

# Contoh Penggunaan (sejajar di luar fungsi)
A = [
    [2, 3, -1],
    [4, 4, -3],
    [-2, 3, -1]
]
b = [5, 3, 1]
solusi = gauss_jordan(A, b)
print("Solusi sistem persamaan: ", solusi)
