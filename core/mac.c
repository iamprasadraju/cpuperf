#include "mac.h"

#include <stdint.h>
#include <stdio.h>
#include <sys/sysctl.h>

// macro for sysctlbyname
#define GET_SYSCTL(name, var) do { \
    size_t size = sizeof(var); \
    if (sysctlbyname(name, &(var), &size, NULL, 0) == -1) { \
        perror(name); \
        return -1; \
    } \
} while (0)

int get_cpuinfo(CpuInfo *info) {
  if (info == NULL)
    return -1;
  *info = (CpuInfo) {0}; // clean init (set all fileds to zero)
  GET_SYSCTL("machdep.cpu.brand_string", info->chip_name);
  GET_SYSCTL("hw.ncpu", info->ncpu);
  GET_SYSCTL("hw.physicalcpu", info->pcores);
  GET_SYSCTL("hw.logicalcpu", info->lcores);
  GET_SYSCTL("hw.memsize", info->ram);
  GET_SYSCTL("hw.machine", info->arch);
  GET_SYSCTL("hw.cachelinesize", info->cachelinesize);
  GET_SYSCTL("hw.perflevel0.l1icachesize", info->p0l1icache);
  GET_SYSCTL("hw.perflevel0.l1dcachesize", info->p0l1dcache);
  GET_SYSCTL("hw.perflevel0.l2cachesize", info->p0l2cache);
  GET_SYSCTL("hw.perflevel1.l1icachesize", info->p1l1icache);
  GET_SYSCTL("hw.perflevel1.l1dcachesize", info->p1l1dcache);
  GET_SYSCTL("hw.perflevel1.l2cachesize", info->p1l2cache);
  return 0;
}