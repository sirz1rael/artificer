import os, sys, subprocess
from termcolor import colored

try:
    project_path = sys.argv[1]
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

mainfile_cpp_text = '#include<iostream>\n\nint main() {\n\tstd::cout << "Hello, world!" << std::endl;\n\treturn 0;\n}'

def gen_main_file(j:str, i:str):

    mainfile = open(src_f[:-1] + "/" + j + "." + i, "w")
    mainfile.write(mainfile_cpp_text)
    mainfile.close()

def cmake():
    mainfile_name = 'main'
    mainfile_ext = 'cpp'

    for i in mkdir:
        os.system("mkdir " + i)

    cmakelists = open(project_path + "/CMakeLists.txt", "w")

    project_name = "project(" + str(input("Name your project: ")) + ")"
    cmake_ver = "cmake_minimum_required(VERSION " + str(cmake_ver_coutput[2])[2:5] + ")"

    cmakelists.write(cmake_ver + "\n")          # cmake_minimum_required()
    cmakelists.write(project_name + "\n")       # project(<name>)

    gen_main_file('main', 'cpp')                # generating mainfile

    cmakelists.write("add_executable(test " + str(src_f.split('/')[1])[:-1] + '/' + mainfile_name + '.' + mainfile_ext + ")") # add_executable()

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
