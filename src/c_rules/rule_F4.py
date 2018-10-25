# -*- coding: utf-8 -*-

"""
Jane for C Projects
Author: Yohann MARTIN (https://github.com/Astropilot/jane_c)

F4 Rule: The body of a function should not exceeds 20 lines.
"""

from etna_style_utils import *
from srcml import *

class RuleChecker:

    def __init__(self, project):
        self.project = project

    def check_rule(self):
        project = self.project
        print "Checking F4 Rule..."
        print "Rule reminder: Functions should not exceeds 20 lines."
        is_rule_ok = True

        source_files = project.get_files_from_project(project.FILE_TYPES["C_SOURCES"])

        for file in source_files:
            mFile = transform_c_to_xml(file)
            tree = strip_ns_prefix(etree.parse(mFile))
            functions = tree.xpath("/unit/function")
            for function in functions:
                function_name = function.xpath("name/text()")[0]
                function_content = function.xpath("string(block)")
                function_size = len(function_content.split('\n'))-2
                if function_size > 20:
                    is_rule_ok = False
                    print "F4 Violation! Function " + function_name + " with " + str(function_size) + " lines in file " + file
        if is_rule_ok:
            print "Good job buddy, no violation!"
