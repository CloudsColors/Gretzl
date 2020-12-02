import os, glob, sys, re, fileinput

'''
Runs the whole script
'''

files = []

def main():
    files = collect_files_from_directory("")
    for f in files:
        open_and_inject_code(f)
    for f in files:
        remove_the_injected_code(f)
    
'''
Collects all the .java files in the path given by the argument pathToDirectory
'''
def collect_files_from_directory(pathToDirectory):
    return glob.glob(r"C:\Users\Andreas\Desktop\Uni\Software evolution project\example_system\**\*.java", recursive=True)
'''

Opens up the file given by the argument filePath, creates a new object of type Logger and puts in a call to this logger in each function.
'''
def open_and_inject_code(filePath):
    # regex for where to inject
    name = ""
    with fileinput.FileInput(filePath, inplace=True) as f:
        for line in f:
            if(re.search(r"((public|private|protected|class)(\s[A-Za-z\s]*)([^}]*)([{]))", line)):
                if("class" in line):
                    regex = r"((public\s|private\s|protected\s|class\s)|(implements\s[ A-Za-z]+|extends\s[ A-Za-z]+)|([{]))"
                    name = re.sub(regex, "", line)
                    line = line + "\tGretzl gretzlLogger = new Gretzl(\""+name.strip("\n")+"\");"
                    print(line, end="\n")
                else:
                    regex = r"((public\s|private\s|protected\s)|(throws\s[A-Za-z]+)|([{]))"
                    name = re.sub(regex, "", line)
                    line = line + "\t\tgretzlLogger.log(\""+name.strip()+"\");"
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
Remove the previously injected code, cleanup!
'''
def remove_the_injected_code(path):
    with fileinput.FileInput(path, inplace=True) as f:
        for line in f:
            if(re.search(r"((Gretzl\sgretzlLogger\s=\snew\sGretzl[(-;]*|gretzlLogger.log[(-;]*))", line)):
                line = ""
            print(line, end="")
    return

if __name__ == "__main__":
    main()