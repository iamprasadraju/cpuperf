#include <stdint.h>
#include <stdio.h>
#include <sys/sysctl.h>

typedef struct {
  char chip_name[32];
  char arch[32]; // architecture
  int ncpu; // number of cores
  int pcores; // number of p cores 
  int lcores; // number of l cores (threads)
  uint64_t ram; // (bytes)
  uint64_t cachelinesize; // (bytes)
  uint64_t p0l1icache; // perfomance level 0; l1 cache for instructions (bytes) 
  uint64_t p0l1dcache; // perfomance level 0; l1 cache for data (bytes)
  uint64_t p0l2cache; // perfomance level 0; l2 cache (bytes)
  uint64_t p1l1icache; // perfomance level 1; l1 cache for instructions (bytes)
  uint64_t p1l1dcache; // perfomance level 1; l1 cache for data (bytes)
  uint64_t p1l2cache; // perfomance level 1; l2 cache (bytes)
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
  if (query_sysctl("hw.physicalcpu", &info->pcores, sizeof(info->pcores)) == -1){
    return -1;
  }
  if (query_sysctl("hw.logicalcpu", &info->lcores, sizeof(info->lcores)) == -1){
    return -1;
  }
  if (query_sysctl("hw.memsize", &info->ram, sizeof(info->ram)) == -1){
    return -1;
  }
  if (query_sysctl("hw.machine", &info->arch, sizeof(info->arch)) == -1){
      return -1;
  }
  if (query_sysctl("hw.cachelinesize", &info->cachelinesize, sizeof(info->cachelinesize)) == -1){
        return -1;
    }
  if (query_sysctl("hw.perflevel0.l1icachesize", &info->p0l1icache, sizeof(info->p0l1icache)) == -1){
        return -1;
    }
  return 0;
}

int main() {
  CpuInfo cpu = {0}; // clean init

  if (get_sysctlbyname(&cpu) == -1)
    return 1;

  printf("Chip: %s\n", cpu.chip_name);
  printf("Architecture: %s\n", cpu.arch);
  printf("Number of Cores: %d\n", cpu.ncpu);
  printf("P Cores: %d\n", cpu.pcores);
  printf("L Cores: %d\n", cpu.lcores);
  printf("RAM: %llu bytes\n", cpu.ram);
  printf("Cache line size: %llu bytes\n", cpu.cachelinesize);
  printf("Perflevel0.L1 i Cache: %llu bytes\n", cpu.p0l1icache);
}
