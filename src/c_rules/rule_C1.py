# -*- coding: utf-8 -*-

"""
Jane for C Projects
Author: Yohann MARTIN (https://github.com/Astropilot/jane_c)

C1 Rule: Ternaries are allowed as far as they are kept simple and readable,
         and they do not obfuscate code.
         You should never use nested or chained ternaries.
         Ternaries should not be used to control program flow.
"""

from etna_style_utils import *
from srcml import *

class RuleChecker:

    def __init__(self, project):
        self.project = project

    def check_rule(self):
        project = self.project
        print "Checking C1 Rule..."
        print "Rule reminder: Ternaries are allowed as far as they are kept simple and readable,"
        print "               and they do not obfuscate code."
        is_rule_ok = True

        source_files = project.get_files_from_project(project.FILE_TYPES["C_FILES"])

        for file in source_files:
            mFile = transform_c_to_xml(file)
            root = ignore_c_comments(strip_ns_prefix(etree.parse(mFile)))

            all_ternary = root.xpath("/unit//ternary[not(ancestor::ternary)]")
            for ternary in all_ternary:
                start_line = ternary.sourceline

                ternary_nested = ternary.xpath("descendant::ternary")
                if len(ternary_nested) > 0:
                    is_rule_ok = False
                    print "C1 Violation at line " + str(start_line-1) + ", nested ternary is forbidden! File: " + file

                flow_calls = ternary.xpath("descendant::call")
                if len(flow_calls) > 0:
                    is_rule_ok = False
                    print "C1 Violation at line " + str(start_line-1) + ", you can't use ternary for control programme flow! File: " + file

        if is_rule_ok:
            print "Good job buddy, no violation!"
