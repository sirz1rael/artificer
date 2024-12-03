import os, sys
from termcolor import colored

try:
    project_path = sys.argv[1]
except:
    print("------------------------------------------------------",
        colored("\nYou need to specify a project folder! Like this: \n", 'light_red', attrs=[]),
        colored("$ python main.py <path/to/project>", 'cyan', attrs=['bold']),
        "\n------------------------------------------------------")

# You can change the names of folders here

lib_f = sys.argv[1] + "/lib "       # Default library folder - /lib
bin_f = sys.argv[1] + "/bin "       # Default binary folder - /bin
inc_f = sys.argv[1] + "/include "   # Default includes folder - /include
src_f = sys.argv[1] + "/src "       # Default sources folder - /src
ast_f = sys.argv[1] + "/assets "    # Default assets folder - /assets

mkdir = {lib_f, bin_f, inc_f, src_f, ast_f}

def cmake():
    print("CMake")

    for i in mkdir:
        os.system("mkdir " + i)

    cmakelists = open(project_path + "CMakeLists.txt", "w")

    cmakelists.close()
    os.system("cd " + project_path + "&& cmake .")

def make():
    print("Make")
    makefile = open("Makefile", 'w')

    makefile.close()

# def ninja():
#     print("ninja")

def main():
    print("WELCOME TO PY GEN C PROJECT SCRIPT!\n")
    first: str = "Choose build system\n(1 - CMake(default), 2 - Make, 3 - Ninja(not working)): "

    try:
        choose: int = int(input(first))
        if choose == 1:
            cmake()
        elif choose == 2:
            make()
        else:
            cmake()
    except:
        cmake()


if __name__ == "__main__":
    main()
