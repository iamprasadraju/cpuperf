# convert cpuinfo value types to match cpuperf cpuinfo types
def parse_info(val):
  val = val.strip()
  return int(val) if val.isdigit() else val
