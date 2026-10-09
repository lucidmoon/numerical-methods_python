# Metode Newton Raphson -> Xn+1 = Xn - (f(Xn)/f'(Xn))
def f(x):
  return x**3 - x - 2

def df(x):
  return 3*x**2 - 1

def newton_raphson(x0, tol=1e-5, max_iter=100):
    x = x0

    for i in range(1,max_iter + 1):
      turunan = df(x)
      if turunan == 0:
        print("Error: turunan bernilai 0!")
        return none
      
      xnew = x - f(x)/df(x)
      fxnew = f(xnew)

      print(f'iterasi {i}: x = {xnew:.6f}, f(x) = {fxnew:.6f}')

      if abs(fxnew) < tol:
        return xnew
      x = xnew
    print("Metode tidak konvergen dalam iterasi maksimum")
    return x

akar_newton = newton_raphson(x0=-3)
if akar_newton:
  print(f'akar ditemukan dengan nilai: {akar_newton:.6f}')

akar_newton = newton_raphson(x0=6)
if akar_newton:
  print(f'akar ditemukan dengan nilai: {akar_newton:.6f}')
