import subprocess
import unittest
from cpuperf.cpuinfo import get_cpuinfo, cpuinfo_by_name
from tests.helpers import parse_info

# true values
systcl_cpu_fields = [
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

# test values
cpuperf_cpu_fields = [
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
    result = subprocess.run(sysctl_cmd + systcl_cpu_fields, capture_output=True, text=True)
    acpuinfo = result.stdout.strip().split("\n") # acpuinfo - actual cpuinfo
    self.parsed_acpuinfo = [parse_info(val) for val in acpuinfo]

    # cpuinfo from cpuperf
    cpuinfo = get_cpuinfo() # tcpuinof - cpuinfo for testing
    self.tcpuinfo = cpuinfo_by_name(cpuinfo, fields=cpuperf_cpu_fields)
    
  def test_allcpu_fields(self): self.assertListEqual(self.parsed_acpuinfo, self.tcpuinfo)

if __name__ == "__main__":
  unittest.main()

