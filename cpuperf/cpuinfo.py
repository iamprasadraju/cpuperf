import ctypes
import os
from utils.helpers import cfprint, bytes2gb, bytes2kb, bytes2mb

class CpuInfo(ctypes.Structure):
    _fields_ = [
        ("chip_name", ctypes.c_char * 32),
        ("arch", ctypes.c_char * 32),
        ("cores", ctypes.c_int),
        ("pcores", ctypes.c_int),
        ("lcores", ctypes.c_int),
        ("ram", ctypes.c_uint64),
        ("cachelinesize", ctypes.c_uint64),
        ("perflvl0", ctypes.c_char * 32),
        ("perflvl0pcores", ctypes.c_int),
        ("p0l1icache", ctypes.c_uint64),
        ("p0l1dcache", ctypes.c_uint64),
        ("p0l2cache", ctypes.c_uint64),
        ("perflvl1", ctypes.c_char * 32),
        ("perflvl1pcores", ctypes.c_int),
        ("p1l1icache", ctypes.c_uint64),
        ("p1l1dcache", ctypes.c_uint64),
        ("p1l2cache", ctypes.c_uint64),
    ]

def get_cpuinfo(parse: bool = True) -> dict | CpuInfo:
  cpuinfo = CpuInfo()  # Allocate structure; C initializes its contents
  
  # dylib_path = os.path.abspath("/Users/jarvis/repos/cpuperf/core/main.dylib")
  dylib_path = "./core/mach_arm64/mach_arm.dylib"
  if not os.path.exists(dylib_path):
    raise FileNotFoundError(f"Library not found at {dylib_path}")

  lib = ctypes.CDLL(dylib_path)
  lib.get_cpuinfo.argtypes = [ctypes.POINTER(CpuInfo)]
  lib.get_cpuinfo.restype = ctypes.c_int
  status = lib.get_cpuinfo(ctypes.byref(cpuinfo))

  if status != 0:
    raise RuntimeError(f"get_cpuinfo failed with error code {status}")
  if parse:
    return build_cpuinfo_table(cpuinfo)
  else: 
    return cpuinfo

def build_cpuinfo_table(cpuinfo: CpuInfo) -> dict:
  cpu_dict = {}
  for field_name, _ in cpuinfo._fields_:
      val = getattr(cpuinfo, field_name)
      if isinstance(val, bytes):
        val = val.decode('utf-8')
      cpu_dict[field_name] = val
  return cpu_dict

def cpuinfo_by_name(cpuinfo: dict, fields: list | str):
  if isinstance(fields, str):
    # Handle a single field string lookup
    return cpuinfo[fields]
  elif isinstance(fields, list):
    # Handle a list of fields
    return [cpuinfo[field] for field in fields]

def readable_cpuinfo_table(cpu: CpuInfo) -> dict:
  return {
     "Chip": cpu.chip_name.decode(),
     "Architecture": cpu.arch.decode(), # bytestring to str
     "Number of Cores": cpu.cores,
     "Logical Cores (Threads)": cpu.lcores,
     "Physical RAM": cpu.ram,
     "Cache line size": cpu.cachelinesize,
     "Perfomance level 0": cpu.perflvl0.decode(),
     f"{cpu.perflvl0.decode()} Cores": cpu.perflvl0pcores,
     "Perflevel0.L1icache": cpu.p0l1icache,
     "Perflevel0.L1dcache": cpu.p0l1dcache,
     "Perflevel0.L2cache": cpu.p0l2cache,
     "Perfomance level 1": cpu.perflvl1.decode(),
     f"{cpu.perflvl1.decode()} Cores": cpu.perflvl1pcores,
     "Perflevel1.L1icache": cpu.p1l1icache,
     "Perflevel1.L1dcache": cpu.p1l1dcache,
     "Perflevel1.L2cache": cpu.p1l2cache,
  }
  
if __name__ == "__main__":
  cpuinfo = get_cpuinfo(parse=False)
   
  cpuinfo_tabel = readable_cpuinfo_table(cpuinfo)
   
  for attr, value in cpuinfo_tabel.items():
    if (attr == "Physical RAM"):
      value = bytes2gb(value)
    elif ("cache" and "L1" in attr):
      value = bytes2kb(value)
    elif ("L2" in attr):
      value = bytes2mb(value)
    cfprint(attr, value)
