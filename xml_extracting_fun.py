import urllib
import xml.etree.ElementTree as ET

data = urllib.urlopen('/Users/kayliew/Google Drive/for_fun/country.xml').read()
tree = ET.fromstring(data)
lst = tree.findall('./country') #to get country counts and lists
#print 'Number of counts', len(counts) #test
#print tree.get('name') #test
convert_string__to_list = list()
cnt = 0
for item in lst:
#    print "Hello: ",tree.find('item').text
    if 'a' not in item.get('name').lower():  #cast to case insensitive
        #print "Found :", item.get('name') #test
        #print item.get('name') #test
        convert_string__to_list.append(item.get('name'))
        print cnt, ")", item.get('name')
        cnt = cnt + 1
print "Number of countries without 'a' in the name are ", cnt-1, "out of " , len(lst) , "countries."

'''

0 ) Belgium
1 ) Belize
2 ) Benin
3 ) Burundi
4 ) Chile
5 ) Comoros
6 ) Congo
7 ) Cyprus
8 ) Czech Republic
9 ) Djibouti
10 ) Timor-leste
11 ) Egypt
12 ) Fiji
13 ) Greece
14 ) Hong Kong
15 ) Cote D'ivoire
16 ) Lesotho
17 ) Liechtenstein
18 ) Luxembourg
19 ) Mexico
20 ) Montenegro
21 ) Morocco
22 ) Niger
23 ) Niue
24 ) Peru
25 ) Philippines
26 ) Puerto Rico
27 ) Seychelles
28 ) Sweden
29 ) Togo
30 ) Turkey
31 ) United Kingdom
32 ) Yemen
Number of countries without 'a' in the name are  32 out of  205 countries.

'''
