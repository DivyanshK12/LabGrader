import os

def input_splitter(source_file):
    with open(source_file,"r") as src_file:
        text = src_file.read()
        cases = text.split(";")
        files_created = []
        for i, case in enumerate(cases):
            with open(f"inp_{i}.txt","w") as file:
                file.write(case)
                files_created.append(f"inp_{i}.txt")
        return files_created

def input_cleaner(directory = "."):
    for file in os.listdir(directory):
        if "inp_" in file:
            os.remove(f"{directory}/{file}")

if __name__ == "__main__":
    filename = sys.argv[1]
    cases = input_splitter(filename)