# 006_faktorisasi_P3.py
import numpy as np

def faktorisasi_p3(a2, a1, a0, tol=1e-6, max_iter=100):
    """
    Mencari akar persamaan polinomial tingkat 3: x^3 + a2*x^2 + a1*x + a0 = 0
    menggunakan metode Faktorisasi P3(x).
    Memecah polinomial menjadi (x - p)(x^2 + qx + r) = 0
    """
    # Tebakan awal untuk p (bisa disesuaikan)
    p = 1.0 
    
    print(f"{'Iterasi':<8}{'Nilai p':<15}{'Nilai q':<15}{'Nilai r':<15}")
    print("-" * 55)
    
    for i in range(max_iter):
        # Pembagian sintetik / hubungan koefisien
        q = a2 + p
        r = a1 + p * q
        
        # Evaluasi sisa / fungsi f(p)
        fp = p * r + a0
        
        # Turunan f'(p) untuk pendekatan Newton-Raphson dalam mencari p
        dfp = r + p * q + p**2  # atau: 3*p^2 + 2*a2*p + a1
        
        if abs(dfp) < 1e-12:
            print("Turunan terlalu kecil (divisi nol).")
            break
            
        # Update nilai p
        p_new = p - fp / dfp
        
        print(f"{i+1:<8}{p_new:<15.6f}{q:<15.6f}{r:<15.6f}")
        
        if abs(p_new - p) < tol:
            p = p_new
            # Hitung q dan r terakhir setelah p konvergen
            q = a2 + p
            r = a1 + p * q
            break
            
        p = p_new
    else:
        print("Peringatan: Iterasi maksimum tercapai sebelum konvergen.")

    # Akar pertama (real) dari faktor (x - p) = 0 -> x = p
    akar1 = p
    
    # Akar kedua dan ketiga didapat dari rumus ABC pada kuadrat: x^2 + qx + r = 0
    diskriminan = q**2 - 4*r
    akar2 = (-q + np.lib.scimath.sqrt(diskriminan)) / 2
    akar3 = (-q - np.lib.scimath.sqrt(diskriminan)) / 2
    
    return akar1, akar2, akar3

# --- CONTOH PENGGUNAAN ---
if __name__ == "__main__":
    # Persamaan: x^3 - 6x^2 + 11x - 6 = 0  (Akar eksak: 1, 2, 3)
    a2 = -6.0
    a1 = 11.0
    a0 = -6.0
    
    print("Memulai Faktorisasi Polinomial P3...")
    x1, x2, x3 = faktorisasi_p3(a2, a1, a0)
    
    print("-" * 55)
    print("Hasil Akar-Akar Persamaan:")
    print(f"x1 = {x1:.4f}")
    print(f"x2 = {x2}")
    print(f"x3 = {x3}")