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
    with open(sys.argv[2]) as infile:
        soup = BeautifulSoup(infile)
    for row in soup.find("table", {"class": "table-layout:fixed"}).findChildren('tr'):
        print(row)
    j2_env = Environment(loader=FileSystemLoader(sys.argv[1]), trim_blocks=True)
#    print(j2_env.get_template('template.html').render(
#            rows=[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
#                ))
    #with open(sys.argv[1]) as infile:
     #   soup = BeautifulSoup(infile)
    #deu_table = soup.findAll("table", {"class": "table-layout:fixed"})
    #print(deu_table)
    return 0


if __name__ == '__main__':
    main()
