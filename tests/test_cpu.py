import subprocess
import unittest
from cpuperf.cpuinfo import get_cpuinfo
from tests.helpers import parse_cpuinfo

cpu_fields = [
  "machdep.cpu.brand_string", 
  "hw.machine", 
  "hw.ncpu", 
  "hw.logicalcpu", 
  "hw.perflevel0.name", 
  "hw.perflevel0.physicalcpu",
  "hw.perflevel1.name",
  "hw.perflevel1.physicalcpu"
]

sysctl_cmd = ["sysctl", "-n"]

test_fields = [
  "chip_name", 
  "arch", 
  "cores", 
  "lcores",
  "perflvl0",
  "perflvl0pcores",
  "perflvl1",
  "perflvl1pcores"
]

class CpuInfoTest(unittest.TestCase):
  def setUp(self) -> None:
    # cpuinfo from cmd using systctl cli (consider as true values)
    result = subprocess.run(sysctl_cmd + cpu_fields, capture_output=True, text=True)
    cpuinfo = result.stdout.strip().split("\n")
    
    self.cleaned_cpuinfo = [parse_cpuinfo(val) for val in cpuinfo]

    # cpuinfo from cpuperf
    cpu = get_cpuinfo()
    self.test_cpuinfo = []
    
    for field in test_fields:
      value = getattr(cpu, field)
      if isinstance(value, bytes):
        value = value.decode()
      self.test_cpuinfo.append(value)
    
  def test_allcpufields(self): self.assertListEqual(self.cleaned_cpuinfo, self.test_cpuinfo)

if __name__ == "__main__":
  unittest.main()

