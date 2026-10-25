#include <sys/sysctl.h>
#include <stdio.h>



int main(){
  char arch[64];

  size_t size = sizeof(chip);
  
  sysctlbyname("hw.machine", arch, &size);
  printf("%s", chip);
  
}
