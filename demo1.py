#模块
import math #导入这个模块的所有
print(id(math)) #2078330633488
print(type(math))   #<class 'module'>
print(math) #<module 'math' (built-in)>
print(math.pi)  #3.141592653589793
print('-------------------------')
print(dir(math))
'''['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 
'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1',
'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 
'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan','nextafter', 
'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau',  'trunc', 'ulp']
'''
print(math.pow(2,3),type(math.pow(2,3)))    #2的3次方
'''8.0 <class 'float'>'''
print(math.ceil(9.001)) #10 #最接近的最大整数
print(math.floor(9.99))    #9  #最接近的最小整数
