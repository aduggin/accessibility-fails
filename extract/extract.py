import json
from itertools import chain

from bs4 import BeautifulSoup

with open('../index.html') as indexfile:
    html = indexfile.read()
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
    resobj = tests[titlemap[title]][title]['results']
    for toolname in tools:
        resobj[toolname] = (set(result.findChild("td", class_=toolname)['class']) - set(tools)).pop()

with open('tests.json', 'w') as outfile:
    json.dump(tests, outfile, indent=4)
    outfile.close()