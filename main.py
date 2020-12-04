import os, glob, sys, re, fileinput, argparse

'''
Runs the whole script
'''

files = []

def main():
    arguments = process_command_line()   
    if(arguments.dpm == 'mvn'):
        #Do something here 
        mvn = True  
        print(mvn)

    files = collect_files_from_directory(arguments.d)
    for f in files:
        open_and_inject_code(f)
    """ for f in files:
        remove_the_injected_code(f) """

'''
Processes command line arguments
'''
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
    return glob.glob(pathToDirectory +r"/**/*.java", recursive=True)

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
                    line = "import com.CloudsColors.Gretzl.Gretzl; \n\n" + line + "\tGretzl gretzlLogger = new Gretzl(\""+name.strip("\n")+"\");"
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