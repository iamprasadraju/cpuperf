import ctypes
import os

class CpuInfo(ctypes.Structure):
    _fields_ = [
        ("chip_name", ctypes.c_char * 32),
        ("arch", ctypes.c_char * 32),
        ("ncpu", ctypes.c_int),
        ("pcores", ctypes.c_int),
        ("lcores", ctypes.c_int),
        ("ram", ctypes.c_uint64),
        ("cachelinesize", ctypes.c_uint64),
        ("p0l1icache", ctypes.c_uint64),
        ("p0l1dcache", ctypes.c_uint64),
        ("p0l2cache", ctypes.c_uint64),
        ("p1l1icache", ctypes.c_uint64),
        ("p1l1dcache", ctypes.c_uint64),
        ("p1l2cache", ctypes.c_uint64),
    ]

# dylib_path = os.path.abspath("/Users/jarvis/repos/cpuperf/core/main.dylib")
dylib_path = os.path.abspath("../core/mac.dylib")

lib = ctypes.CDLL(dylib_path)

lib.get_cpuinfo.argtypes = [ctypes.POINTER(CpuInfo)]
lib.get_cpuinfo.restype = ctypes.c_int

cpu = CpuInfo()  # Allocate structure; C initializes its contents

result = lib.get_cpuinfo(ctypes.byref(cpu))

if result == 0:
    print(cpu.chip_name.decode())
    print(cpu.arch.decode())
    print(cpu.ncpu)
    print(cpu.ram)
