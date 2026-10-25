import ctypes
import os


# dylib_path = os.path.abspath("/Users/jarvis/repos/cpuperf/core/main.dylib")
dylib_path = os.path.abspath("../core/main.dylib")

lib = ctypes.CDLL(dylib_path)

lib.add.argtypes = (ctypes.c_size_t, ctypes.c_size_t)
lib.add.restype = ctypes.c_size_t

result = lib.add(3333333333333, 333333333333)
print(result)

# print(load)
