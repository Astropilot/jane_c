# -*- coding: utf-8 -*-

"""
Jane for C Projects
Author: Yohann MARTIN (https://github.com/Astropilot/jane_c)

Very simple wrapper around srcML CLI tool.
"""

import os, sys
from lxml import etree
import subprocess

def transform_c_to_xml(file):
    mFile = file[:-2] + ".xml"
    if not os.path.isfile(mFile):
        os.system("srcml " + file + " -o " + mFile)
    return mFile

def strip_ns_prefix(tree):
    query = "descendant-or-self::*[namespace-uri()!='']"
    for element in tree.xpath(query):
        element.tag = etree.QName(element).localname
    return tree
