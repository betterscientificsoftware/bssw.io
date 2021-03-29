#!/usr/bin/python
#
# Run as:
#
#   cd bssw.io/
#   ./utils/convert_images_ref_to_rel_path.py <md-file-path>
#
# to replace:
#
#   https://github.com/betterscientificsoftware/images/raw/master/
#
# with the proper local reference to:
#
#   ../../images/
#
# in an input *.md file <md-file-path> where the relative path depends on the
# local directory path of the *.md file.
#

import sys
import os


def getMdFilePathFromCmndLine():
  if len(sys.argv) != 2:
    print("Error, must be passed local path to *.md file!")
    sys.exit(1)
  mdFilePath = sys.argv[1]
  if not os.path.exists(mdFilePath):
    print("Error, input '"+mdFilePath+"' is not a valid file path!")
    sys.exit(1)
  return mdFilePath


g_external_images_repo_str_list = [
  "https://github.com/betterscientificsoftware/images/raw/master/",
  "https://github.com/betterscientificsoftware/images/blob/master/",
  ]

def getRelImagesRefStr(dirDepth):
  relImagesRefStr = "images/"
  for i in range(dirDepth):
    relImagesRefStr = "../" + relImagesRefStr
  return relImagesRefStr

 
def replaceImagesRef(mdFilePath):
  # Find depth in local file path and local images ref
  dirDepth = len(mdFilePath.split("/")) - 1
  localImagesRef = getRelImagesRefStr(dirDepth)
  #print("dirDepth = "+str(dirDepth))
  #print("localImagesRef = "+str(localImagesRef))
  # Get the contents of the file on input
  with open(mdFilePath, 'r') as fileHandle:
    fileContentsInList = fileHandle.read().split("\n")
  # Do replacements for the images ref
  fileContentsOutList = []
  for line in fileContentsInList:
    newLine = line
    for g_external_images_repo_str in g_external_images_repo_str_list:
      newLine = newLine.replace(g_external_images_repo_str, localImagesRef)
    if newLine != line:
      print("Replacing line: "+line)
      print("With line     : "+newLine)
    fileContentsOutList.append(newLine)
  # Write the output file (if it changed)
  if fileContentsOutList != fileContentsInList:
    print("Writing updated output file '"+mdFilePath+"'") 
    with open(mdFilePath, 'w') as fileHandle:
      fileHandle.write("\n".join(fileContentsOutList))


#
# Main
#

if __name__ == '__main__':
  mdFilePath = getMdFilePathFromCmndLine()
  print("Replacing images reference in file '"+mdFilePath+"'")
  replaceImagesRef(mdFilePath)
