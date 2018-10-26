"""
dexsuite.py

Minimal program to generate 'fancy' HTML report.
v1 here introduces a 'proportion' column for proportion of exons changed. 
"""
import os
import sys

from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader


def main():
    rows = []
    with open(sys.argv[2]) as infile:
        soup = BeautifulSoup(infile)
    on_header = True
    # go through each tr element in the table
    for tr in soup.find("table", {"class": "table-layout:fixed"}).findChildren('tr'):
        if on_header:  # skip header (change to call to 'next'?)
            on_header = False
        else:
            td = tr.findAll('td') # get all td elements in row
            geneids = td[0].find('a').text.split(' ') # first td element is space-separates list of gene id links.
            rows.append([geneids, td[1].text, td[2].text, td[3].text, td[4].text, td[5].text, str(float(td[5].text)/float(td[4].text))])
    j2_env = Environment(loader=FileSystemLoader(sys.argv[1]), trim_blocks=True)
    html_rendered =j2_env.get_template('template.html').render(rows=rows)
    basepath = os.path.dirname(sys.argv[2])
    with open(os.path.join(basepath, sys.argv[3]), 'w') as outfile:
        outfile.write(html_rendered)
    return 0


if __name__ == '__main__':
    main()
