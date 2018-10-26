# -*- coding: utf-8 -*-

"""
Jane for C Projects
Author: Yohann MARTIN (https://github.com/Astropilot/jane_c)

C2 Rule: Your code should not contain the goto keyword.
"""

from etna_style_utils import *
from srcml import *

class RuleChecker:

    def __init__(self, project):
        self.project = project

    def check_rule(self):
        project = self.project
        print "Checking C2 Rule..."
        print "Rule reminder: Your code should not contain the goto keyword."
        is_rule_ok = True

        source_files = project.get_files_from_project(project.FILE_TYPES["C_SOURCES"])

        for file in source_files:
            mFile = transform_c_to_xml(file)
            root = ignore_c_comments(strip_ns_prefix(etree.parse(mFile)))

            all_goto = root.xpath("/unit//goto")
            for goto in all_goto:
                start_line = goto.sourceline
                is_rule_ok = False
                print "C2 Violation at line " + str(start_line-1) + ", goto keyword is not recommended! File: " + file

        if is_rule_ok:
            print "Good job buddy, no violation!"
