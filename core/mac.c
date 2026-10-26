#include <stdio.h>
#include <sys/sysctl.h>

typedef struct {
  char chip_name[32];
  size_t ncpu;
} CpuInfo;

static int query_sysctl(const char *name, void *value, size_t size) {
  if (sysctlbyname(name, value, &size, NULL, 0) == -1) {
    perror(name);
    return -1;
  }
  return 0;
}

int get_sysctlbyname(CpuInfo *info) {
  if (query_sysctl("machdep.cpu.brand_string", info->chip_name, sizeof(info->chip_name)) == -1){
    return -1;
  }
  if (query_sysctl("hw.ncpu", &info->ncpu, sizeof(info->ncpu)) == -1){
    return -1;
  }
  return 0;
}

int main() {
  CpuInfo cpu = {0}; // clean init

  if (get_sysctlbyname(&cpu) == -1)
    return 1;

  printf("Chip: %s\n", cpu.chip_name);
  printf("Number of Cores: %zu\n", cpu.ncpu);
}
