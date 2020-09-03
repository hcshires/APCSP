from lxml import html
from lxml import etree
import requests
import numpy
import matplotlib.pyplot as plt

# List of pastor frequency
authors = ["Amanda Neppl", "Andy Hermanson", "Ben Mason", "Chris Kimpston", "Jed Smith", "Jeremy Johnson", "Justin Stoffa", "Josh Linman", "Jon Anenson", "Laura Woods",
           "Luis Arrendondo", "Mark Brandt", "Mike Householder", "Mark Nelson", "Mitch Matthews", "Molly Juntunen", "Molly Weinrich", "Nick Brannen", "Nicole Woodley",
           "Paul Gratton", "Richard Webb", "Scott Rains"]

# Each pastor
amanda = []
andy = []
ben = []
chris = []
jed = []
jeremy = []
justin = []
josh = []
jon = []
laura = []
luis = []
mark = []
markN = []
mike = []
mitch = []
molly = []
mollyW = []
nick = []
nicole = []
paul = []
richard = []
scott = []

# Amount of each pastor
lengths = []


# get web page
page = requests.get('http://sermons.hopedesmoines.org/sermons.xml')

# convert webpage content into html tree
tree = html.fromstring(page.content)

# put the text of all <duration> tags into a list called times
times = tree.xpath("//duration/text()")

# put the text of all <title> tags into a list called titles
titles = tree.xpath("//item/title/text()")

# Pastors from <author> tags
pastors = tree.xpath("//item/author/text()")
pastors.sort()

# Who preaches the most often
'''
for i in range(len(pastors)-1):
if pastors[i] == pastors[i+1]:
nPastor.append(pastors[i])
nPastor.replace("'","")
'''

# Data
print(len(authors)) # 22 Pastors
print(len(pastors)) # Sermons
print(authors) # Each pastor

for i in range(len(pastors)):
    '''
    if pastors[i] != pastors[i-1]:
        print(pastors[i])
    '''
    for author in authors:
        if author in pastors[i]:
            if authors.index(author) == 0:
                amanda.append(author)
            elif authors.index(author) == 1:
                andy.append(author)
            elif authors.index(author) == 2:
                ben.append(author)
            elif authors.index(author) == 3:
                chris.append(author)
            elif authors.index(author) == 4:
                jed.append(author)
            elif authors.index(author) == 5:
                jeremy.append(author)
            elif authors.index(author) == 6:
                justin.append(author)
            elif authors.index(author) == 7:
                josh.append(author)
            elif authors.index(author) == 8:
                jon.append(author)
            elif authors.index(author) == 9:
                laura.append(author)
            elif authors.index(author) == 10:
                luis.append(author)
            elif authors.index(author) == 11:
                mark.append(author)
            elif authors.index(author) == 12:
                mike.append(author)
            elif authors.index(author) == 13:
                markN.append(author)
            elif authors.index(author) == 14:
                mitch.append(author)
            elif authors.index(author) == 15:
                molly.append(author)
            elif authors.index(author) == 16:
                mollyW.append(author)
            elif authors.index(author) == 17:
                nick.append(author)
            elif authors.index(author) == 18:
                nicole.append(author)
            elif authors.index(author) == 19:
                paul.append(author)
            elif authors.index(author) == 20:
                richard.append(author)
            else:
                scott.append(author)

# Send amounts from each list to one list of lengths (MUST be in correct order
lengths.append(len(amanda))
lengths.append(len(andy))
lengths.append(len(ben))
lengths.append(len(chris))
lengths.append(len(jed))
lengths.append(len(jeremy))
lengths.append(len(justin))
lengths.append(len(josh))
lengths.append(len(jon))
lengths.append(len(laura))
lengths.append(len(luis))
lengths.append(len(mark))
lengths.append(len(mike))
lengths.append(len(markN))
lengths.append(len(mitch))
lengths.append(len(molly))
lengths.append(len(mollyW))
lengths.append(len(nick))
lengths.append(len(nicole))
lengths.append(len(paul))
lengths.append(len(richard))
lengths.append(len(scott))

print(lengths)

x = range(len(authors))
x_str = authors
# Create Graph
fig, ax = plt.subplots(1, 1)
a = ax.bar(x, lengths, width=0.8, bottom=None, align='center', color='#4286f4')
ax.set_title('Frequent Pastors at Hope Des Moines')
ax.set_xlabel('Pastor')
ax.set_ylabel('Frequency (# sermons)')

# Adjust Labels
plt.xticks(x, x_str, rotation='vertical')
plt.subplots_adjust(bottom=0.15)

# Show
plt.show()
