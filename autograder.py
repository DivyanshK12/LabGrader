#!/usr/bin/env python3
import sys
import os
from input_generator import input_splitter, input_cleaner

def list_files(dirname):
    return os.listdir(dirname)

def run_all_files(file_list, inp_file_names, op_name = "output1.txt", er_name="errors.txt"):
    # Dirty code to start empty in input filename
    with open(op_name, "w"):
        pass
    with open(er_name, "w"):
        pass

    for file in file_list:
        filename = file[:-2]
        # Try to break with error like files
        # Currently dont check for errors
        os.system(f"echo '------Errors for {filename} : ------' >> {er_name}")
        os.system(f"gcc {file} -o {filename} -lm 2>> {er_name}") # -lm included for math.h support
        os.system(f"echo '{filename}\n' >> {op_name} 2>> {er_name}")
        # Loop over here for line in input
        for num, inp in enumerate(inp_file_names):
            os.system(f"echo xxxxxxxxx Case {num} xxxxxxxxxx  >> {op_name}")
            run_case(filename, inp, op_name, er_name)
        os.system(f"echo '--------------------------------' >> {op_name}")
        os.system(f"echo '#########################################\n' >> {er_name}")
        os.system(f"rm {filename}")


def run_case(filename, inp, op_name, er_name):
    os.system(f"./{filename} < {inp} >> {op_name} 2>> {er_name}")
    os.system(f"echo '\n######################################\n' >> {op_name}")

def do_work(dirname, inp_name):
    files = list_files(dirname)
    c_files = [ str(dirname+"/"+file) for file in files if ".c" in file.lower()]
    file_names = input_splitter(inp_name)
    run_all_files(c_files,file_names)
    input_cleaner(".")
    print("Complete")

if __name__ == "__main__":
    dirname = sys.argv[1]
    input_name = sys.argv[2]
    do_work(dirname, input_name)