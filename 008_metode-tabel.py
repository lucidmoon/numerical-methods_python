# Metode Tabel untuk Mencari Akar Fungsi
def f(x):
  # f(x) = x^2 - 4x + 1
  return pow(x, 2) - 4 * x + 1

# Input Parameter
a = 0
b = 1
n = 10
dx = (b-a)/n #float(input("Masukkan langkah (Δx): "))
x = a
akar_ditemukan = False
a1 = a
b1 = b

print("\nTabel Nilai f(x): ")
print("-------------------------------")
print(" x\t\tf(x)")
print("-------------------------------")
while x <= b:
  fx1 = f(x)
  fx2 = f(x + dx)
  print(f"{x:.4f}\t\t{fx1:.6f}")

  if fx1 * fx2 < 0:
    akar_ditemukan = True
    a1 = x      # batas bawah yang baru
    b1 = x + dx # batas atas yang baru
  x += dx
print("-------------------------------")
if akar_ditemukan:
  print(f"Perubahan tanda terdeteksi antara x = {a1:.4f} dan x = {b1:.4f}")
  print(f"Akar berada di antara interval [{a1:.4f}] dan [{b1:.4f}]")
else:
  print("\nTidak ada akar yang ditemukan pada interval tersebut.")