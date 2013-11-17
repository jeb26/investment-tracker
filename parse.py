import libxml2
import sys
import os
import commands as c
import re
import sys
import MySQLdb

from xml.dom.minidom import parse, parseString

# for converting dict to xml 
from cStringIO import StringIO
from xml.parsers import expat

def get_elms_for_atr_val(tag,atr,val):
    lst=[]

    elems = dom.getElementsByTagName(tag)

    for e in elems:
        if e.hasAttribute(atr):
            l = e.childNodes

    for i in l:
        lst.append(i)

    return lst      

# get all text recursively to the bottom
def get_text(e):
    lst=[]

    if e.nodeType in (3,4):
        lst.append(e.data)
    else:
        node = e.childNodes
        for x in node:
            lst = lst + get_text(x)
   
    return lst

# replace whitespace chars
def replace_white_space(str):
    p = re.compile(r'\s+')
    new = p.sub(' ',str)   # a lot of \n\t\t\t\t\t\t
    return new.strip()

# replace but these chars including ':'
def replace_non_alpha_numeric(s):
    p = re.compile(r'[^a-zA-Z0-9:-]+')
    #   p = re.compile(r'\W+') # replace whitespace chars
    new = p.sub(' ',s)
    return new.strip()

# convert to xhtml
# use: java -jar tagsoup-1.2.jar --files html_file
def html_to_xhtml(fn):
    output = c.getoutput('java -jar tagsoup-1.2.1.jar --files %s' % (fn)).split()

    return output[3]

def extract_values(dm):
    lst = []
    l = get_elms_for_atr_val('table','class','most_actives')

    for i in l:
        lst.append(get_text(i))

##    for i in lst:
##        print "%s" % (i)
    return lst

def main():
    html_fn = 'test.html'
    fn = html_fn.replace('.html','')
    xhtml_fn = html_to_xhtml(html_fn)

    global dom
    dom = parse(xhtml_fn)

    lst = extract_values(dom)

    for i in lst:
        print "%s" % (i)
    

main()
