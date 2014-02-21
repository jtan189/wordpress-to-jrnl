from lxml import etree
import sys

infile = sys.argv[1]
outfile = sys.argv[2]
f = open(outfile, 'w')

tree = etree.parse(infile)
items = tree.findall('channel/item')

month_dict = {}
month_dict['Jan'] = '01'
month_dict['Feb'] = '02'
month_dict['Mar'] = '03'
month_dict['Apr'] = '04'
month_dict['May'] = '05'
month_dict['Jun'] = '06'
month_dict['Jul'] = '07'
month_dict['Aug'] = '08'
month_dict['Sep'] = '09'
month_dict['Oct'] = '10'
month_dict['Nov'] = '11'
month_dict['Dec'] = '12'

for item in items:

    pub_date = ""
    title = ""
    content = ""

    for element in item.iter():

        text = element.text

        if element.tag == "pubDate":
            pub_date = element.text

            # convert wordpress date format to jrnl date format
            split_date = pub_date.split()
            pub_date = "%s-%s-%s %s" % (month_dict[split_date[2]], split_date[1], split_date[3], split_date[4][:5])

        elif element.tag == "title":
            title = element.text
        elif element.tag == "{http://purl.org/rss/1.0/modules/content/}encoded":
            content = element.text
    
    f.write("%s %s\n%s\n\n" % (pub_date, title, content))

f.close()
