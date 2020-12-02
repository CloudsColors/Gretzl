import os, glob, sys, re, fileinput, argparse

'''
Runs the whole script
'''
def main():
    arguments = process_command_line()   
    if(arguments.dpm == 'mvn'):
        #Do something here 
        mvn = True  
        print(mvn)

    files = collect_files_from_directory(arguments.d)
    for f in files:
        open_and_inject_code(f)


def process_command_line():
    parser = argparse.ArgumentParser(description="Usage:")
    parser.add_argument("-d", type=str, required=True,  help="Add path to dir")
    parser.add_argument("-dpm", choices=["mvn", "gradle"], help="Choose used dependancy manager")
    args = parser.parse_args()
    return args

'''
Collects all the .java files in the path given by the argument pathToDirectory
'''
def collect_files_from_directory(pathToDirectory):
    fileNames = glob.glob(pathToDirectory +"\\**\\*.java", recursive=True)
    return fileNames

'''
Opens up the file given by the argument filePath, creates a new object of type Logger and puts in a call to this logger in each function.
'''
def open_and_inject_code(filePath):
    # regex for where to inject
    with fileinput.FileInput(filePath, inplace=True) as f:
        data = []
        for line in f:
            if(re.search(r"((public|private|protected|class)(\s[A-Za-z\s]*)([^}]*)([{]))", line)):
                if("class" in line):
                    line = line + "\tLogger logger = new Logger();"
                    print(line, end="\n")
                else:
                    line = line + "\t\tlogger.log();"
                    print(line, end="\n")
            else:
                print(line, end="")

'''
Executes the Java system that the tool will explore
'''
def execute_system():
    #execute the java project
    return

'''
Puts the Logger class in the filesystem of the project so that we can call the class.
'''
def put_class_in_system():
    #put the logger class in the system (maybe in its own package or something?)
    return

'''
Remove the previously injected code, cleanup!
'''
def remove_the_injected_code():
    #remove the injected code
    return

if __name__ == "__main__":
    main()