import subprocess
import unittest
from cpuperf.cpuinfo import cpuinfo_by_name, get_cpuinfo, build_cpuinfo_table
from tests.helpers import parse_info

sysctl_cmd = ["sysctl", "-n"]

systcl_memory_fields = [
  "hw.memsize",
]

cpuperf_memory_fields = [
  "ram",
]

class CpuInfoTest(unittest.TestCase):
  def setUp(self) -> None:
    # actual memory info from systcl
    result = subprocess.run(sysctl_cmd + systcl_memory_fields, capture_output=True, text=True)
    ameminfo = result.stdout.strip().split("\n") # ameminfo - actual memory info
    self.parsed_meminfo = [parse_info(val) for val in ameminfo]

    cpuinfo = get_cpuinfo()
    self.tmeminfo = cpuinfo_by_name(cpuinfo, cpuperf_memory_fields)

  def test_allmem_fields(self): self.assertListEqual(self.parsed_meminfo, self.tmeminfo)

if __name__ == "__main__":
  unittest.main()