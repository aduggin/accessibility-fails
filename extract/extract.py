import json
import re
from itertools import chain

from bs4 import BeautifulSoup

with open('../index.html') as indexfile:
    originalhtml = indexfile.read()

    indexfile.seek(0)
    html_lines = indexfile.readlines()
    for idx, line in enumerate(html_lines):
        if "pearls" in line:
            html_lines[idx] = "<!-- %s -->" % line

    html = "".join(html_lines)

    indexfile.close()

soup = BeautifulSoup(html, 'html.parser')

tests = {}

group = ''
testname = ''

for cur in soup.find('h2', id="content").previous_sibling.next_siblings:
    if cur.name == 'h2':
        group = cur.text.strip()
        tests[group] = {}

    if cur.name == 'h3':
        testname = cur.text.strip()
        tests[group][testname] = {
            'example': '',
            'results': {}
        }

    if cur.name == 'div':
        tests[group][testname]['example'] = cur.renderContents()


# Fixing the test we have to comment out
thatTest = tests["HTML"]["Start and close tags don't match"]['example']
tests["HTML"]["Start and close tags don't match"]['example'] = thatTest.replace('<!--', '').replace('-->', '')


with open('../tools.html') as toolfile:
    html = toolfile.read()
    toolfile.close()

soup = BeautifulSoup(html, 'html.parser')
results = soup.find('tbody').findChildren('tr')

tmaps = [zip(ts.keys(), [group]*len(ts.keys())) for group, ts in tests.iteritems()]
titlemap = dict(list(chain.from_iterable(tmaps)))

tools = ["google", "tenon", "wave", "codesniffer", "axe", "tanaguru", "sortsite", "eiii", "achecker", "nu"]

for result in results:
    title = result.findChild('th').text
    if title not in titlemap:
        # If you see these errors, it might be because you have to comment out 
        # the example for the test titled "Start and close tags don't match"
        # the test is testing for broken HTML, it breaks the parser
        print "not in index: %s" % title
    else:
        resobj = tests[titlemap[title]][title]['results']
        for toolname in tools:
            resobj[toolname] = (set(result.findChild("td", class_=toolname)['class']) - set(tools)).pop()

with open('tests.json', 'w') as outfile:
    json.dump(tests, outfile, indent=4)
    outfile.close()