# Metode Biseksi
# ------------------------------------------
def f(x):
  # f(x) = x^3 - 4x + 1
  return pow(x, 3) - 4 * x + 1

def bisection(a, b, tol):
  if f(a) * f(b) > 0:
    print("Tidak ada akar dalam interval tersebut!")
    return None
  iterasi = 1
  while (b - a) / 2 > tol:
    c = (a + b) / 2
    if f(c) == 0:
      return c
    elif f(a) * f(c) < 0:
      b = c
    else:
      a = c
    print(f"Iterasi {iterasi:2d}: a = {a:<12.6f}, b = {b:<12.6f}, c = {c:<12.6f}, f(c) = {f(c):<12.6f}")
    iterasi += 1
  return (a + b) / 2

# ---- Program Utama ----
a = float(input("Masukkan batas bawah (a): "))
b = float(input("Masukkan batas atas (b): "))
tol = float(input("Masukkan toleransi error: "))
akar = bisection(a, b, tol)
if akar is not None:
  print(f"\nPerkiraan akar: x = {akar:.6f}")
