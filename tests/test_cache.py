import subprocess
import unittest
from cpuperf.cpuinfo import get_cpuinfo, cpuinfo_by_name
from tests.helpers import parse_info

sysctl_cmd = ["sysctl", "-n"]

sysctl_cache_fields = [
  "hw.perflevel0.l1icachesize",
  "hw.perflevel0.l1dcachesize",
  "hw.perflevel0.l2cachesize",
  
  "hw.perflevel1.l1icachesize",
  "hw.perflevel1.l1dcachesize",
  "hw.perflevel1.l2cachesize",
]

cpuperf_cache_fields = [
  "p0l1icache",
  "p0l1dcache",
  "p0l2cache",
  "p1l1icache",
  "p1l1dcache",
  "p1l2cache",
  
]

class CacheInfoTest(unittest.TestCase):
  def setUp(self) -> None:
    result = subprocess.run(sysctl_cmd + sysctl_cache_fields, capture_output=True, text=True)

    acacheinfo = result.stdout.rstrip("\n").split("\n")
    self.parsed_acacheinfo = [parse_info(val) for val in acacheinfo]

    cpuinfo = get_cpuinfo()
    self.tcpuinfo = cpuinfo_by_name(cpuinfo, fields=cpuperf_cache_fields)

  def test_allcache_fields(self): self.assertListEqual(self.parsed_acacheinfo, self.tcpuinfo)

if __name__ == "__main__":
  unittest.main()
  
