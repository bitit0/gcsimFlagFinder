import glob
import os.path
import os
import re

def main():

    found = {}

    charDirectory = "C:\\Users\\natha\\Downloads\\characters\\characters"

    for dirname, dirs, files in os.walk(charDirectory):

        for file in files:
            curr = open(dirname + "\\" + file)

            ln = 0
            for line in curr:
                ln += 1
                first = re.search(r"(p\[\"\w*\"\])", line)      # search for p[""]

                if first:
                    first = first.group()
                    #print(first)
                    second = re.search(r"\w{2,}", first)        # get text inside quotation marks
                    if second:
                        #print(second.group())
                        getFolder = re.search(r"\w*$", dirname).group()
                        fileWithLN = getFolder + "/" + file + ", " + str(ln)
                        found[fileWithLN] = second.group()


    for i in found:
        print(i, ": ", found[i])


if __name__ == "__main__":
    main()