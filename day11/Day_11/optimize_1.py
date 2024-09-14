from scipy.optimize import minimize

#objective function
def objective_function(x):
    return x**2 + 3*x +2

#perform optimization
result= minimize(objective_function, x0=0)
print(result.x)#optimal value of x