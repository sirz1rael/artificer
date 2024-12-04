# Artificer
Python script which can generate blank projects for C and C++ dev.

## Version 0.2
**DISCLAIMER:** This tool is developed firstly for my personal use!
If you want to fix something, then welcome to pull requests.

For now only for linux.
Developed on Arch.
If it doesn't work on your distro, let me know about it and I'll try to fix that.
```
Requirements:
  * Python 3.1x
  * termcolor
  * pyinstaller.
```
Script written in python,
that integrates into system path and helps
you to create blank projects for C and C++ with CMake or Make.

### Installation:
```bash
chmod +x ./install.sh
./install.sh
```
### Usage
```bash
artificer project_name
```

### Basic project structure
```
[project_name]
├── assets
├── bin
├── lib
├── include
├── src
│    └── main.cpp OR main.c
└── CMakeLists.txt OR Makefile
```

### CMakeLists.txt content
```CMake
cmake_minimum_required(3.X)
project(your_project_name)
add_executable(test main.cpp)
```

### Makefile content
```make

CC=gcc or g++

CFLAGS=-c -Wall

SRC=src/main.c or src/main.cpp
LIB=lib

build:
	$(CC) $(CFLAGS) $(SRC)
compile:
	$(CC) main.o -o main
```
