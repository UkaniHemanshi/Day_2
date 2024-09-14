from scipy.integrate import quad


def integrand(x):
    # print(x)
    return x**2

result, error = quad(integrand,0,1)
print(result)