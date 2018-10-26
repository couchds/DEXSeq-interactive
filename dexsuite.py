"""
dexsuite.py

Minimal program to generate 'fancy' HTML report.
v1 only makes the 
"""
import os
import sys

from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader


def main():
    rows = []
    with open(sys.argv[2]) as infile:
        soup = BeautifulSoup(infile)
    i = 0
    for tr in soup.find("table", {"class": "table-layout:fixed"}).findChildren('tr'):
        if i == 0:
            i=1
        else:
            td = tr.findAll('td')
            #print(td[0].find('a').text)
            geneids = td[0].find('a').text.split(' ')
            rows.append([geneids, td[1].text, td[2].text, td[3].text, td[4].text, td[5].text, str(float(td[5].text)/float(td[4].text))])
    j2_env = Environment(loader=FileSystemLoader(sys.argv[1]), trim_blocks=True)
    html_rendered =j2_env.get_template('template.html').render(rows=rows)
    #print(html_rendered)
    basepath = os.path.dirname(sys.argv[2])
    print(basepath)
    with open(os.path.join(basepath, 'transform.html'), 'w') as outfile:
        outfile.write(html_rendered)
    #with open(sys.argv[1]) as infile:
     #   soup = BeautifulSoup(infile)
    #deu_table = soup.findAll("table", {"class": "table-layout:fixed"})
    #print(deu_table)
    return 0


if __name__ == '__main__':
    main()
