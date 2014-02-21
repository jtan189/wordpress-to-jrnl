from lxml import etree
import sys

infile = sys.argv[1]
outfile = sys.argv[2]
f = open(outfile, 'w')

tree = etree.parse(infile)
items = tree.findall('channel/item')

for item in items:

    pub_date = ""
    title = ""
    content = ""

    for element in item.iter():

        text = element.text

        if element.tag == "pubDate":
            pub_date = element.text
        elif element.tag == "title":
            title = element.text
        elif element.tag == "{http://purl.org/rss/1.0/modules/content/}encoded":
            content = element.text
    
    f.write("%s %s\n%s\n\n" % (pub_date, title, content))

f.close()
