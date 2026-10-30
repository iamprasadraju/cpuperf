#ifndef MAC_H
#define MAC_H

#include <stdint.h>


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

int get_cpuinfo(CpuInfo *info);

#endif
