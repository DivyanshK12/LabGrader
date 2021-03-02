#!/usr/bin/env python3
import sys
import os
import subprocess
from input_generator import input_splitter, input_cleaner

def list_c_files(dirname):
    files =  os.listdir(dirname)
    return [ str(dirname+"/"+file) for file in files if ".c" in file.lower()]

def run_all_files(file_list, inp_file_names, op_name , er_name):
    # Dirty code to start empty in input filename
    f = open(op_name,"w")
    f.close()
    f = open(er_name,"w")
    f.close()

    for file in file_list:
        filename = file[:-2]

        os.system(f"echo '------Errors for {filename} : ------' >> {er_name}")
        with open(er_name, "ab") as f:
            subprocess.run([f"gcc {file} -o {filename}","-lm"], stderr=f, shell=True, timeout=10)

        os.system(f"echo '{filename}\n' >> {op_name} 2>> {er_name}")
        os.system(f"echo '######################################' >> {op_name}")
        # Loop over here for line in input
        for num, inp in enumerate(inp_file_names):
            os.system(f"echo xxxxxxxxx Case {num} xxxxxxxxxx  >> {op_name}")
            run_case(filename, inp, op_name, er_name)
        os.system(f"echo '--------------------------------' >> {op_name}")
        os.system(f"echo '######################################\n' >> {er_name}")
        os.system(f"rm {filename}")


def run_case(filename, inp, oup, err):
    inp_str = open(inp, 'rb')
    out = open(oup, 'ab')
    er = open(err, 'ab')
    subprocess.run([f"./{filename}"], stdin=inp_str, stdout= out, stderr=er, timeout=1,shell=True)
        # subprocess module used to take care of infinite loop cases
    os.system(f"echo '\n######################################\n' >> {oup}")
    inp_str.close()
    out.close()
    er.close()

def do_work(dirname, inp_name, outputfile = "output1.txt", errorfile = "errors.txt"):
    c_files = list_c_files(dirname)
    file_names = input_splitter(inp_name)
    run_all_files(c_files,file_names, outputfile, errorfile)
    input_cleaner(".")
    print("Complete")

def main():
    if len(sys.argv) <3:
        print("Run the program with the following arguements:\n(1)Path of required directory\n(2)Input filename")
        print("Example:\npython3 autograder.py TestFiles input_test_files.txt")
        print("OR\n./run.sh After giving the necessary executable permissions")
    else:
        dirname = sys.argv[1]
        input_name = sys.argv[2]
        do_work(dirname, input_name)

if __name__ == "__main__":
    main()