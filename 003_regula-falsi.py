def regula_falsi(f, a, b, tol=1e-5, max_iter=100):
    i = 1
    # Menampilkan header tabel yang tertata rapi
    print(f"{'Iterasi':<8} | {'a':<12} | {'b':<12} | {'c':<12} | {'f(a)':<12} | {'f(b)':<12} | {'f(c)':<12}")
    print("-" * 88)

    while (i <= max_iter):
        fa = f(a)
        fb = f(b)
        # Menghitung titik taksiran c menggunakan interpolasi linear
        c = b - (fb * (b - a)) / (fb - fa)
        fc = f(c)

        # Menampilkan data setiap iterasi sejajar dengan kolom
        print(f"{i:<8} | {a:<12.6f} | {b:<12.6f} | {c:<12.6f} | {fa:<12.6f} | {fb:<12.6f} | {fc:<12.6f}")

        if (abs(fc) < tol):
            return c
        if (fa * fc < 0):
            b = c
        else:
            a = c
        i += 1
    print("-" * 88)
    print("Metode gagal setelah", max_iter, "iterasi")
    return None

# Menggunakan persamaan yang sama
f = lambda x: x**2 - 2
a = 1
b = 2

hasil_rf = regula_falsi(f, a, b)
print("-" * 88)
print("Akar hampiran (Regula Falsi):", hasil_rf)
