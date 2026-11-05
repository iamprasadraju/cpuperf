
# Define the project name, programming language, and version.
project(
    'cpuperf',
    'c',
    version: '0.1.0',

    # Default compiler and build configuration.
    default_options: [
        'c_std=c11',        # Use the C11 standard.
        'warning_level=3',  # Enable comprehensive compiler warnings.
        'buildtype=release', # Optimize for release builds.
    ],
)

# Build a shared dynamic library.
shared_library(
    'mac_arm',

    # C source files included in the library.
    [
        'core/mac_cpuinfo.c',
        'core/macos/mac_arm64/mac_arm.c',
    ],

    # Directories containing headers included by the source files.
    include_directories: include_directories(
        'core/macos/mac_arm64',
    ),

    # Do not install the library; keep the output in the build directory.
    install: false,
)
