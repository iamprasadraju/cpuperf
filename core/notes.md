# Notes

* READ function call address
```bash
nm -gu main.dylib
```

* compile to dylib on mac
```bash
gcc -dynamiclib main.c -o main.dylibb
```

* All hardware descriptions
```bash
sysctl -d hw
```

* All machine-dependent processor descriptions
```bash
sysctl -d machdep
```

## Apple cpu(sysctl) docs
[https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html)

## Apple darwin-xnu
[https://github.com/apple/darwin-xnu/blob/main/bsd/dev/arm/sysctl.c](https://github.com/apple/darwin-xnu/blob/main/bsd/dev/arm/sysctl.c)


# one of the function to get sysinfo(cpu)
```bash
<sys/sysctl.h> -> sysctlbyname()

verbose: sysctlbyname(const char *, void *__sized_by(*oldlenp), size_t *oldlenp,
      |         ^            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  798 |     void *__sized_by(newlen), size_t newlen);
```

## Headers exposed by macos interface:

-  **sys/sysctl.h -->  cpu info**
-  **mach/host_info.h & mach/mach_host.h --> host-level and processor-related information**
-  **IOKit/IOKitLib.h --> user-space i/o Registry (every CPU detail).**
-  **osfmk/arm64/ (Apple silicon) & osfmk/i386/ (Intel)**