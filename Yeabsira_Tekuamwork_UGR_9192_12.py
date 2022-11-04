'''
This is a simple program to check the validity of html tags in an html file.
The program checks if an opening tag is not closed or a closing tag hasn't been opened.
 
It first ask the user to choose a file,
it validate the selected html
and it prints the problems found.
'''
from tkinter import *
from tkinter import filedialog
 
checkable_tags = ["<html>", "</html>", "<head>", "</head>", "<title>", "</title>", "<Body>",
                  "</body>", "<div>", "</div>", "<span>", "</span>", "<a>", "</a>", "<table>",
                  "</table>", "<thead>", "</thead>", "<tbody>", "</tbody>", "<tr>", "</tr>",
                  "<td>", "</td>", "<script>", "</script>", "<ul>", "</ul>", "<li>", "<li>",
                  "<strong>", "</strong>", "<h1>", "</h>", "<h2>", "</h2>", "<h3>", "</h3>",
                  "<h4>", "</h4>", "<h5>", "</h5>"]
 
# The following lines will ask the user to choose a file
input("Press 'Enter' and choose your html file, the result from the html checker will be printed here.")
file_selector = Tk()
file_selector.attributes('-topmost', True)
path = filedialog.askopenfilename()
html = open(path, "r").read()
 
# The following lines check the validity of the file
unclosed_tags = {}
problems = []
index = 1
tags = html.split(">")
for tag in tags:
    orignal_string = tag
    if "<" in tag:
        tag = tag[tag.index("<"):]
        if " " in tag:
            tag = tag[:tag.index(" ")]
        tag += ">"
        if not tag in checkable_tags:
            continue
        if tag[1] == "/":
            opening_tag = "<"+tag[2:]
            if opening_tag in unclosed_tags:
                unclosed_tags[opening_tag] -= 1
                if unclosed_tags[opening_tag] == 0:
                    unclosed_tags.pop(opening_tag)
            else:
                problems.append("The closing tag '"+tag+"' (starting at " +
                                str(index)+") comes with no opening tag!")
        else:
            if tag in unclosed_tags:
                unclosed_tags[tag] += 1
            else:
                unclosed_tags[tag] = 1
    index += len(orignal_string)
if unclosed_tags:
    for key in unclosed_tags:
        problems.append("The opening tag '"+key+"' is not closed (at " +
                        str(unclosed_tags[key])+" place"+("s" if unclosed_tags[key] > 1 else "")+")!")
if problems:
    print("\nThe following problems are found:")
    for problem in problems:
        print("    ", problem)
else:
    print("No problems found.")
 

