#!/usr/bin/env python3
import re
import sys
from input_generator import output_input

def read_in(output_file):
    with open(output_file, "r") as out:
        output = out.read()
    return output

def split_file(output_text):
    output_per_file = output_text.split("--------------------------------")
    output_cases = {}
    for file in output_per_file:
        cases_split = file.split("######################################")
        output_cases[cases_split[0]] = cases_split[1:]
    return output_cases

def find_case(output_list, line, n_lim):
    output_list = map(str, output_list)
    seperators=", ;\n\t"
    pattern = (r"["+seperators+r"]*").join(output_list)
    line = "\n".join(line.strip().split("\n")[-n_lim:])
    result = re.search(pattern, line, re.IGNORECASE)
    return result

def run_all_cases(outputs_list, outputs, m_output, n_lim):
    f = open(m_output, "w")
    for output in outputs:
        f.write(output.strip()+"\n") # Write the name with removing the extra whitespaces
        for required, produced in zip(outputs_list, outputs[output]):
            result = find_case(required, produced, n_lim)
            if result is not None:
                f.write("$$ Result CORRECTLY MATCHED $$\nFILTERED RESULT : ")
                f.write(result.group(0)+"\n")
            else:
                f.write("$$ Result NOT MATCHED $$\nORIGINAL RESULT :\n")
            f.write("\n".join(produced.strip().split("\n")[-n_lim-1:]))
            f.write("\n")
        f.write("\n")
    f.close()

def check():
    print(find_case([5,4,5,4],"Entered : 5;4,5,4 \n"))
    print(find_case(["palindrome"],"The string passed was palindrome \n"))
    print(find_case(["power","NO power","power"],"Power no power power"))

def main():
    inp = len(sys.argv)
    if inp < 5:
        print("Please enter the arguements in the following format : \n(1)expected_output_file \n(2)output_file_from_autograder \n(3)filename_for_modified_output \n(4)number_of_lines_to_scan")
        print("python3 output_filter.py (1) (2) (3) (4)")
        print("OR\n ./modify.sh After giving the necessary executable permissions")
    else :
        out = split_file(read_in(sys.argv[2]))
        run_all_cases(output_input(sys.argv[1]), out, sys.argv[3], int(sys.argv[4]))

if __name__ == "__main__":
    main()