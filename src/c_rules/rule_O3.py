# -*- coding: utf-8 -*-

"""
Jane for C Projects
Author: Yohann MARTIN (https://github.com/Astropilot/jane_c)

O3 Rule: No more non-static functions in source files.
"""

from etna_style_utils import *
from srcml import *

class RuleChecker:

    def __init__(self, project):
        self.project = project

    def check_rule(self):
        project = self.project
        print "Checking O3 Rule..."
        print "Rule reminder: No more 5 non-static functions"
        is_rule_ok = True

        source_files = project.get_files_from_project(project.FILE_TYPES["C_SOURCES"])
        for file in source_files:
            mFile = transform_c_to_xml(file)
            tree = strip_ns_prefix(etree.parse(mFile))
            non_static_funcs = tree.xpath("/unit/function[not(specifier) or specifier != 'static']")
            if len(non_static_funcs) > 5:
                is_rule_ok = False
                print "O3 Violation! Concerned file: " + file
        if is_rule_ok:
            print "Good job buddy, no violation!"
