# LabGrader :
Automation Scripts to compile and run student submitted code

# System requirements :
* Linux based environment needed. Few bash scripts commands will not work even on powershell. (FUnctionality for windows under work)
* Python 3.7 or above
* GCC-compiler
# Process to use:
* Clone the repository to local environment
* Create an input file with specific syntax described below
* Run the autograder.py script with the first arguement as the directory name and second arguement as the input text file created above
* View outputs in outputs.txt (or any other name you provided) and errors generated in errors.txt (or a name you provided)
* If run using the bash script provided, the output files can be viewed in terminal as well ( Enter 'q' to exit )

# Input file syntax :
* Inputs for each testcase must be space seprated like a normal terminal input
* Testcases need to be semicolon seperated
* Refer the inputfiles included for reference

# Specifics :
* Input files for course included in folder CourseTestCases
* input1.txt has the input format for question 1 of lab exam
* input2.txt has the input format for question 2 of lab exam
* The output for the TestFiles folder with input_test_files has been included in the ReadmeFiles folder

# Demo :
To run the testcases following command is run:
```
python3 autograder.py TestFiles input_test_files.txt
```
- run.sh script has command saved for easy access

To run the testcases output filtering file run :
```
python3 output_filter.py input_test_files.txt output1.txt modified_output.txt 1
```
- modify.sh has this command saved for easy access

* Currently the testcode is an identity map hence same input provided
* Syntax for desired output is same as input files

# Upcoming:
* Powershell/ Command prompt compatibililty (Issue when dealing with windows seprators as they interfere with Python)
* Better documentation coverage