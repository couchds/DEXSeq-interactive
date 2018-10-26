"""
dexsuite.py

Minimal program to generate 'fancy' HTML report.
v1 only makes the 
"""
import os
import sys

from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader



class DEXSReport():
    """ A new, interactive DEXSeq table.
    """
    def __init__(self):
        self.rows = []

    def add_row(self, row):
        self.rows.append(row)
        return 0

    def row_to_HTML(self, row, header=False):
        """ Convert row, a list, to an HTML <tr> element.
        """
        tr = '<tr>'
        dtype = 'th' if header else 'td'
        for d in row:
            tr = '<{}>{}</{}>'.format(dtype, d, dtype)
        return tr + '</tr>\n'


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
            rows.append([td[0].find('a').text, td[1].text, td[2].text, td[3].text, td[4].text, td[5].text])
    j2_env = Environment(loader=FileSystemLoader(sys.argv[1]), trim_blocks=True)
    html_rendered =j2_env.get_template('template.html').render(rows=rows)
    print(html_rendered)
    #with open(sys.argv[1]) as infile:
     #   soup = BeautifulSoup(infile)
    #deu_table = soup.findAll("table", {"class": "table-layout:fixed"})
    #print(deu_table)
    return 0


if __name__ == '__main__':
    main()
