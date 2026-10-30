#include "mac.h"
#include <stdint.h>
#include <stdio.h>

int main() {
  CpuInfo cpu;
  if (get_cpuinfo(&cpu) == 0){
    printf("Chip: %s\n", cpu.chip_name);
    printf("Architecture: %s\n", cpu.arch);
    printf("Number of Cores: %d\n", cpu.ncpu);
    printf("P Cores: %d\n", cpu.pcores);
    printf("L Cores: %d Threads\n", cpu.lcores);
    printf("RAM: %llu bytes\n", cpu.ram);
    printf("Cache line size: %llu bytes\n", cpu.cachelinesize);

    printf("\nperfomance lvl0 cache \n--------------------------\n");
    printf("Perflevel0.L1 I cache: %llu bytes\n", cpu.p0l1icache);
    printf("Perflevel0.L1 D cache: %llu bytes\n", cpu.p0l1dcache);
    printf("Perflevel0.L2 cache: %llu bytes\n", cpu.p0l2cache);
    
    printf("\nperfomance lvl1 cache \n--------------------------\n");
    printf("Perflevel1.L1 I cache: %llu bytes\n", cpu.p1l1icache);
    printf("Perflevel1.L1 D cache: %llu bytes\n", cpu.p1l1dcache);
    printf("Perflevel1.L2 cache: %llu bytes\n\n", cpu.p1l2cache);   
  }
  return 0;
}
