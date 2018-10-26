# -*- coding: utf-8 -*-

"""
Jane for C Projects
Author: Yohann MARTIN (https://github.com/Astropilot/jane_c)

L5 Rule: Variables should be declared at the beginning of a scopeself.
         Only one variable should be declared per line.
"""

from etna_style_utils import *
from srcml import *

class RuleChecker:

    def __init__(self, project):
        self.project = project

    def check_rule(self):
        project = self.project
        print "Checking L5 Rule..."
        print "Rule reminder: Variables should be declared at the beginning of a scopeself."
        print "               Only one variable should be declared per line."
        is_rule_ok = True

        source_files = project.get_files_from_project(project.FILE_TYPES["C_FILES"])

        for file in source_files:
            mFile = transform_c_to_xml(file)
            root = strip_ns_prefix(etree.parse(mFile))
            multiple_decls = root.xpath("/unit//decl_stmt[count(decl) > 1]")
            for multiple_decl in multiple_decls:
                start_line = multiple_decl.sourceline
                is_rule_ok = False
                print "L5 Violation at line " + str(start_line-1) + ", multiple variable declaration on same line! File: " + file

            all_decl = root.xpath("/unit//block/decl_stmt")
            for decl in all_decl:
                decl_line = decl.sourceline
                prev_siblings = decl.xpath("preceding-sibling::*")
                is_only_decl_before = True
                for prev_sib in prev_siblings:
                    if (prev_sib.tag != "decl_stmt" and prev_sib.tag != "comment"):
                        is_only_decl_before = False
                        break
                if is_only_decl_before == False:
                    print "L5 Violation at line " + str(decl_line-1) + ", variables need to be declared on the top of the scope! File: " + file

        if is_rule_ok:
            print "Good job buddy, no violation!"
