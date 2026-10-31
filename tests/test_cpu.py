import subprocess
import unittest
from cpuperf.cpuinfo import get_cpuinfo



cpu_fields = ["machdep.cpu.brand_string", "hw.machine", "hw.ncpu"]
sysctl_cmd = ["sysctl", "-n"]

# cpuinfo from cmd using systctl cli (consider as true values)
result = subprocess.run(sysctl_cmd + cpu_fields, capture_output=True, text=True)
cpuinfo = result.stdout.strip().split("\n")

# convert cpuinfo values types to match cpuperf cpuinfo types 
def parse(val):
  val = val.strip()
  return int(val) if val.isdigit() else val

cleaned_cpuinfo = [parse(val) for val in cpuinfo]

# cpuinfo from cpuperf
cpu = get_cpuinfo()
test_fields = ["chip_name", "arch", "ncpu"]
test_cpuinfo = []

for field in test_fields:
  value = getattr(cpu, field)
  if isinstance(value, bytes):
    value = value.decode()
  test_cpuinfo.append(value)

class CpuInfoTest(unittest.TestCase):
  def test_allfields(self):
     self.assertListEqual(cleaned_cpuinfo, test_cpuinfo)

if __name__ == "__main__":
  unittest.main()

