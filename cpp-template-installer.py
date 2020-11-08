import sys
from subprocess import call
from shutil import rmtree
from os import remove

def replaceTextInFile(filePath, old, new):
    file = open(filePath, 'r')
    fileData = file.read()
    file.close()

    fileData = fileData.replace(old, new)

    file = open(filePath, 'w')
    file.write(fileData)
    file.close()

if len(sys.argv) != 2:
    print("Please provide the project name as the only argument")
    sys.exit(1)

projectName = sys.argv[1]

print("==> Cloning cpp-template into {0}".format(projectName))
status = call(["git", "clone", "--recursive", "https://github.com/joshpeterson/cpp-template.git", projectName])
if status != 0:
    sys.exit(status)

gitDirectory = "{0}/.git".format(projectName);
print("==> Removing the {0} directory".format(gitDirectory))
rmtree("{0}".format(gitDirectory))

print("==> Changing the project name to {0}".format(projectName))
replaceTextInFile("{0}/CMakeLists.txt".format(projectName), "cpp-template", projectName)
replaceTextInFile("{0}/tools/build-win32-debug.bat".format(projectName), "cpp-template", projectName)
replaceTextInFile("{0}/tools/build-win32-release.bat".format(projectName), "cpp-template", projectName)
replaceTextInFile("{0}/tools/build-win64-debug.bat".format(projectName), "cpp-template", projectName)
replaceTextInFile("{0}/tools/build-win64-release.bat".format(projectName), "cpp-template", projectName)

readmeFile = "{0}/README.md".format(projectName)
print("==> Removing {0}".format(readmeFile))
remove(readmeFile)
