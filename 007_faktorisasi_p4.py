# 007_faktorisasi_p4
import numpy as np

def faktorisasi_p4(a3, a2, a1, a0, tol=1e-6, max_iter=100):
    """
    Mencari akar persamaan polinomial tingkat 4: x^4 + a3*x^3 + a2*x^2 + a1*x + a0 = 0
    menggunakan metode Faktorisasi P4(x).
    Memecah polinomial menjadi (x - p)(x^3 + qx^2 + rx + s) = 0
    """
    # Tebakan awal untuk p (bisa disesuaikan)
    p = 1.0
    
    print(f"{'Iterasi':<8}{'Nilai p':<15}{'Nilai q':<15}{'Nilai r':<15}{'Nilai s':<15}")
    print("-" * 65)
    
    for i in range(max_iter):
        # Pembagian sintetik / hubungan koefisien
        q = a3 + p
        r = a2 + p * q
        s = a1 + p * r
        
        # Evaluasi sisa / fungsi f(p)
        fp = p * s + a0
        
        # Turunan f'(p) untuk pendekatan Newton-Raphson dalam mencari p
        dfp = s + p * r + p**2 * q + p**3  # atau: 4*p^3 + 3*a3*p^2 + 2*a2*p + a1
        
        if abs(dfp) < 1e-12:
            print("Turunan terlalu kecil (divisi nol).")
            break
            
        # Update nilai p
        p_new = p - fp / dfp
        
        print(f"{i+1:<8}{p_new:<15.6f}{q:<15.6f}{r:<15.6f}{s:<15.6f}")
        
        if abs(p_new - p) < tol:
            p = p_new
            # Hitung q, r, dan s terakhir setelah p konvergen
            q = a3 + p
            r = a2 + p * q
            s = a1 + p * r
            break
            
        p = p_new
    else:
        print("Peringatan: Iterasi maksimum tercapai sebelum konvergen.")

    # Akar pertama (real) dari faktor (x - p) = 0 -> x = p
    akar1 = p
    
    # Akar kedua, ketiga, dan keempat didapat dari rumus ABC pada kubik: x^3 + qx^2 + rx + s = 0
    # Ini adalah contoh sederhana; dalam praktiknya, mungkin perlu metode lebih kompleks seperti Cardano's formula
    diskriminan = q**2 - 4*r
    akar2 = (-q + np.lib.scimath.sqrt(diskriminan)) / 2
    akar3 = (-q - np.lib.scimath.sqrt(diskriminan)) / 2
    
    return akar1, akar2, akar3

# --- CONTOH PENGGUNAAN ---
if __name__ == "__main__":
    # Persamaan: x^4 - 10x^3 + 35x^2 - 50x + 24 = 0  (Akar eksak: 1, 2, 3, 4)
    a3 = -10.0
    a2 = 35.0
    a1 = -50.0
    a0 = 24.0
    
    akar1, akar2, akar3 = faktorisasi_p4(a3, a2, a1, a0)
    print("Akar ditemukan :", akar1, akar2, akar3)