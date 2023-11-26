from scipy.optimize import fsolve
import numpy as np

# Tənzimləmək istədiyiniz aralığı burada daxil edin
a = 3.0
b = 3.2

#funksiyanı qururuq
def equation(x):
    return np.exp(x) - np.log(x) - 20

# fsolve funksiyası ilə köməkçi funksiyanı həll etmək
result = fsolve(equation, [a, b])

print("Köməkçi funksiyanın kökü:", result)
