import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter url:  ')
repeat = int(raw_input('Enter repeat : '))
position = int(raw_input ('Enter position : '))

i = 0
for i in range(0,repeat+1): #need range .. range needs to +1 e.g (0,5) means 0 to 4
        html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html,"html.parser")
        tags = soup('a')
        tlist = list()
        nlist = list()
        if i > 5:
            print "Last URL : ", i ,url, "    >  " , names
        else:
            print "Retrieving: ", i ,url
        for tag in tags:
            string = tag.get('href', None)
            names = tag.contents[0]
            tlist.append(string)
            nlist.append(names) #store the contents to list, follow the same logic as url
        url = tlist[position-1] #why - 1? Because the url position start from 0,1,2,3. 3rd position will be a 2
        names = nlist[position - 1]


