import os, sys, subprocess
from termcolor import colored

try:
    project_path = sys.argv[1]
    os.system("mkdir " + str(project_path.split()[0]))
except:
    print("------------------------------------------------------",
        colored("\nYou need to specify a project folder! Like this: \n", 'light_red', attrs=[]),
        colored("$ python main.py <path/to/project>", 'cyan', attrs=['bold']),
        "\n------------------------------------------------------")

try:
    cmake_ver_coutput = subprocess.check_output(['cmake', '--version' ]).split()
except:
    ins_cmake = str(input("ERROR: CMake isn't installed. Press any button to continue."))
    if ins_cmake == "":
        raise SystemExit(1)

# You can change the names of folders here

lib_f = sys.argv[1] + "/lib "       # Default library folder - /lib
bin_f = sys.argv[1] + "/bin "       # Default binary folder - /bin
inc_f = sys.argv[1] + "/include "   # Default includes folder - /include
src_f = sys.argv[1] + "/src "       # Default sources folder - /src
ast_f = sys.argv[1] + "/assets "    # Default assets folder - /assets

mkdir = {lib_f, bin_f, inc_f, src_f, ast_f}

mainfile_cpp_text = '#include <iostream>\n\nint main() {\n\tstd::cout << "Hello, world!" << std::endl;\n\treturn 0;\n}'
mainfile_c_text = '#include "stdio.h"\n\nint main(void) {\n\tprintf("Hello, world!");\n\treturn 0;\n}'
def gen_main_file(j:str, i:str):

    mainfile = open(src_f[:-1] + "/" + j + "." + i, "w")
    if i == 'c':
        mainfile.write(mainfile_c_text)
    elif i == 'cpp':
        mainfile.write(mainfile_cpp_text)
    mainfile.close()

def gen_folders():
    for i in mkdir:
        os.system("mkdir " + i)

def cmake():
    mainfile_name = 'main'
    mainfile_ext = 'cpp'

    gen_folders()

    cmakelists = open(project_path + "/CMakeLists.txt", "w")

    project_name = "project(" + str(input("Name your project: ")) + ")"
    cmake_ver = "cmake_minimum_required(VERSION " + str(cmake_ver_coutput[2])[2:5] + ")"

    cmakelists.write(cmake_ver + "\n")          # cmake_minimum_required()
    cmakelists.write(project_name + "\n")       # project(<name>)

    gen_main_file('main', 'cpp')                # generating mainfile

    cmakelists.write("add_executable(test " + str(src_f.split('/')[1])[:-1] + '/' + mainfile_name + '.' + mainfile_ext + ")") # add_executable()

    cmakelists.close()
    os.system("cd " + project_path + "&& cmake .")
    tst_bld = str(input("\n\nDo you want to do test build(Y/n)? "))
    if tst_bld == 'Y' or tst_bld == 'y':
        os.system("cd " + project_path + " && cmake --build . && ./test")
    else:
        raise SystemExit(0)

cflags = "-c -Wall" # There you can choose cflags for make

def make():
    gen_folders()

    chs = int(input("Choose language(1 - C++, 2 - C): "))

    makefile = open(project_path + "/Makefile", 'w')


    if chs == 1:
        makefile.write("CC=g++\n\n")
        gen_main_file('main', 'cpp')
    elif chs == 2:
        makefile.write("CC=gcc\n\n")
        gen_main_file('main', 'c')

    makefile.write("CFLAGS=" + cflags + "\n\n")

    if chs == 1:
        makefile.write("SRC=" + str(src_f.split('/')[1][:-1]) + "/main.cpp" + "\n")
    elif chs == 2:
        makefile.write("SRC=" + str(src_f.split('/')[1][:-1]) + "/main.c" + "\n")
    makefile.write("LIB=" + lib_f + "\n\n")

    makefile.write("build:\n\t$(CC) $(CFLAGS) $(SRC)\n")
    makefile.write("compile:\n\t$(CC) main.o -o main")

    makefile.close()

    tst_bld = str(input("Do you want to do test build(Y/n)? "))
    if tst_bld == 'Y' or tst_bld == 'y':
        os.system("cd " + project_path + " && (make build && make compile) && ./main")
    else:
        raise SystemExit(0)

def main():
    print("WELCOME TO PY GEN C PROJECT SCRIPT!\n")
    first: str = "Choose build system(1 - CMake(default), 2 - Make): "


    choose: int = int(input(first))
    if choose == 1:
        cmake()
    elif choose == 2:
        make()
    else:
            cmake()


if __name__ == "__main__":
    main()
