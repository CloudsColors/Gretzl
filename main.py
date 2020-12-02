import os, glob, sys, re, fileinput

'''
Runs the whole script
'''
def main():
    files = collect_files_from_directory("")
    for f in files:
        open_and_inject_code(f)
    
'''
Collects all the .java files in the path given by the argument pathToDirectory
'''
def collect_files_from_directory(pathToDirectory):
    fileNames = glob.glob(r"C:\Users\Andreas\Desktop\Uni\Software evolution project\example_system\**\*.java", recursive=True)
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