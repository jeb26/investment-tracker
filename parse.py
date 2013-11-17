import libxml2
import sys
import os
import commands as c
import re
import sys
import MySQLdb as sql

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

def insert_to_db(l,tbl):
    #connect to the local db instance with conn object
    host = 'localhost'
    user = 'test'
    passwd = 'test123'
    db = 'investment_tracker'
    TABLE_NAME = tbl
    SELECT_DB = 'USE investment_tracker;'
    conn = sql.connect(host, user, passwd, db)

    #select db
    conn.query(SELECT_DB)
    
    #inject stock info into db from lst of stock information

    for i in range(1,len(l)):
        symbol = l[i][0]
        name = l[i][1]
        price = l[i][2]
        change = l[i][3]
        percent_change = l[i][4]
        vol = l[i][5]

        #queries
        INSERT = """INSERT INTO `%s` (`Ticker`, `Name`, `Price`, `Change`, `Percent_change`, `Volume`) VALUES ("%s", "%s", "%s", "%s", "%s", "%s");""" % (tbl, symbol, name, price, change, percent_change, vol)      
        #print INSERT
        
        #inject values to db
        conn.query(INSERT)

    #conn.query("""INSERT INTO `stocks` (`Ticker`, `Name`, `Price`, `Change`, `Percent_change`, `Volume`) VALUES ("DAL", "Delta Air Lines Inc", "28.12", "+0.18", "+0.64%", "10,508,616");""")    
    #close the db connection
    conn.commit()
    conn.close()
    

def main():
    html_fn = sys.argv[1]
    fn = html_fn.replace('.html','')
    xhtml_fn = html_to_xhtml(html_fn)

    global dom
    dom = parse(xhtml_fn)

    lst = extract_values(dom)

    insert_to_db(lst,fn)
    
    #cursor = insert_to_db(lst,fn)

##    for i in lst:
##        print "%s" % (i)
    
if __name__=="__main__":
    main()
