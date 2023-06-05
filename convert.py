from bs4 import BeautifulSoup
import re


def resolve_html_code(html):
    """
    Resolve Html code
    """    
    return BeautifulSoup(html,features="html.parser").get_text()

def RSTfile(data):
    """
    Format RST file
    """
    pass