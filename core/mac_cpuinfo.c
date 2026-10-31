#include "mach_arm.h"
#include <stdint.h>
#include <stdio.h>

int main() {
  CpuInfo cpu;
  if (get_cpuinfo(&cpu) == 0){
    printf("Chip: %s\n", cpu.chip_name);
    printf("Architecture: %s\n", cpu.arch);
    printf("Number of Cores: %d\n", cpu.cores);
    printf("P Cores: %d\n", cpu.pcores);
    printf("L Cores: %d Threads\n", cpu.lcores);
    printf("RAM: %llu bytes\n", cpu.ram);
    printf("Cache line size: %llu bytes\n", cpu.cachelinesize);

    printf("\nperfomance lvl0: %s \n--------------------------\n", cpu.perflvl0);
    printf("%s Cores: %d\n", cpu.perflvl0, cpu.perflvl0pcores);
    printf("Perflevel0.L1 I cache: %llu bytes\n", cpu.p0l1icache);
    printf("Perflevel0.L1 D cache: %llu bytes\n", cpu.p0l1dcache);
    printf("Perflevel0.L2 cache: %llu bytes\n", cpu.p0l2cache);
    
    printf("\nperfomance lvl1: %s\n--------------------------\n", cpu.perflvl1);
    printf("%s Cores: %d\n", cpu.perflvl1, cpu.perflvl1pcores);
    printf("Perflevel1.L1 I cache: %llu bytes\n", cpu.p1l1icache);
    printf("Perflevel1.L1 D cache: %llu bytes\n", cpu.p1l1dcache);
    printf("Perflevel1.L2 cache: %llu bytes\n\n", cpu.p1l2cache);   
  }
  return 0;
}
