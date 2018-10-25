# -*- coding: utf-8 -*-

"""
Jane for C Projects
Author: Yohann MARTIN (https://github.com/Astropilot/jane_c)

F6 Rule: There should be no comment within a function.
"""

from etna_style_utils import *
from srcml import *

class RuleChecker:

    def __init__(self, project):
        self.project = project

    def check_rule(self):
        project = self.project
        print "Checking F6 Rule..."
        print "Rule reminder: No comment should be found in functions"
        is_rule_ok = True

        source_files = project.get_files_from_project(project.FILE_TYPES["C_SOURCES"])

        for file in source_files:
            mFile = transform_c_to_xml(file)
            tree = strip_ns_prefix(etree.parse(mFile))
            functions = tree.xpath("/unit/function")
            for function in functions:
                function_name = function.xpath("name/text()")[0]
                nb_comments = function.xpath("count(block/comment)")
                if nb_comments > 0:
                    is_rule_ok = False
                    print "F6 Violation! Function " + function_name + " should not have comments in file " + file
        if is_rule_ok:
            print "Good job buddy, no violation!"
