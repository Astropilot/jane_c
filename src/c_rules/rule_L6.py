# -*- coding: utf-8 -*-

"""
Jane for C Projects
Author: Yohann MARTIN (https://github.com/Astropilot/jane_c)

L6 Rule: A line break should separate the variable declarations from
         the remainder of the function.
"""

from etna_style_utils import *
from srcml import *

class RuleChecker:

    def __init__(self, project):
        self.project = project

    def check_rule(self):
        project = self.project
        print "Checking L6 Rule..."
        print "Rule reminder: A line break should separate the variable declarations from"
        print "               the remainder of the function."
        is_rule_ok = True

        source_files = project.get_files_from_project(project.FILE_TYPES["C_FILES"])

        for file in source_files:
            mFile = transform_c_to_xml(file)
            root = ignore_c_comments(strip_ns_prefix(etree.parse(mFile)))
            with open(file, 'U') as content_file:
                content = content_file.readlines()
            content = [x.strip() for x in content]

            last_decl_in_scope = root.xpath("/unit//block/decl_stmt[position() = last() and count(following-sibling::*) > 0]")
            for last_decl in last_decl_in_scope:
                start_line = last_decl.sourceline
                if (content[start_line-1] != '' and (not content[start_line-1].startswith("//") and not content[start_line-1].startswith("/*"))):
                    is_rule_ok = False
                    print "L6 Violation at line " + str(start_line-1) + ", a line break is expected following this instruction! File: " + file

        if is_rule_ok:
            print "Good job buddy, no violation!"
