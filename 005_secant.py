# metode secant
import numpy as np

def secant(f, x0, x1, tol=1e-6, max_iter=100):
    """
    Parameters:
    f (function): fungsi untuk mencari akar
    x0 (float): tebakan awal
    x1 (float): tebakan kedua
    tol (float): nilai toleransi
    max_iter (int): iterasi max

    Returns:
    float: approksimasi nilai akar
    """
    # cek jika tebakan awal terlalu dekat satu sama lain
    if abs(x0 - x1) < tol:
        print("Tebakan awal terlalu dekat!")
        return None

    for i in range(max_iter):

        # kalkulasi tebakan selanjutnya menggunakan metode secant
        x_new = x1 - f(x1)*(x1 - x0)/(f(x1) - f(x0))
        
        # cek jika tebakan selanjutnya dekat dengan akar
        if abs(f(x_new)) < tol:
            print("-- Akar ditemukan setelah ", i+1, "iterasi! --")
            return x_new

        # update nilai x0 dan x1 untuk iterasi selanjutnya
        x0 = x1
        x1 = x_new
        print("iterasi ke-", i+1, " x = ",x_new)

    print("Max iterasi tercapai!")
    return None

# Contoh
def example_function(x):
    return np.sin(x) - 2*x + 4*np.cos(3*x)

root = secant(example_function, 0, 1)
print("Akar ditemukan :", root)

