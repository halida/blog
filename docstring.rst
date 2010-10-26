注意事项
-----------------------

 * 为了统一,docstring的注释用""""""
 * 不要硬性说返回什么,因为无法确定.要表示会返回什么.
 * class的docstring要与上下分离开来,表示单独的一个部分.
 * override重载和extend扩展要注明
 * fill-paragraph断行

实例
-----------------

def kos_root():
    """Return the pathname of the KOS root directory."""
    global _kos_root
    if _kos_root: return _kos_root
    ...

def complex(real=0.0, imag=0.0):
    """Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)

    """
    if imag == 0.0 and real == 0.0: return complex_zero
    ...
