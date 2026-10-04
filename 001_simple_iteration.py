# 001_simple iteration method

x:float = 0 					# initial search
for iteration in range(1, 101):	# limit iteration to 100 (+1 because it start from 1)
    xnew:float = (2*x**2 + 3)/5 # problem: 2x^2-5x+3=0
    if xnew == x:				# the root has been found (closest value)
        break
    x = xnew
    print(iteration, x)
    
print(f' at the iteration {iteration}, the value is {x}')