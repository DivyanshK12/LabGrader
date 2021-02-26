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

def find_case(output_list, line):
    # result = re.search(r""+text,line)
    output_list = map(str, output_list)
    seperators=", ;\n\t"
    pattern = (r"["+seperators+r"]*").join(output_list)
    result = re.search(pattern, line, re.IGNORECASE)
    return result

def run_all_cases(outputs_list, outputs, m_output):
    f = open(m_output, "w")
    for output in outputs:
        f.write(output.strip()+"\n") # Write the name with removing the extra whitespaces
        for required, produced in zip(outputs_list, outputs[output]):
            result = find_case(required, produced)
            if result is not None:
                f.write("$$ Result CORRECTLY MATCHED $$\nFiltered Result : ")
                f.write(result.group(0)+"\n")
            else:
                f.write("$$ Result NOT MATCHED $$\nOriginal Result : ")
                f.write(produced)
        f.write("\n")
    f.close()

if __name__ == "__main__":
    out = split_file(read_in(sys.argv[2]))
    # print(find_case([5,4,5,4],"Entered : 5;4,5,4 \n"))
    # print(find_case(["palindrome"],"The string passed was palindrome \n"))
    # print(find_case(["power","NO power","power"],"Power no power power"))
    run_all_cases(output_input(sys.argv[1]), out, sys.argv[3])