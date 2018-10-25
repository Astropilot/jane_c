# -*- coding: utf-8 -*-

"""
Jane for C Projects
Author: Yohann MARTIN (https://github.com/Astropilot/jane_c)

F2 Rule: All identifier names should be in English, according to the
         snake_case convention.
"""

from etna_style_utils import *
from srcml import *

class RuleChecker:

    def __init__(self, project):
        self.project = project

    def check_rule(self):
        project = self.project
        print "Checking F2 Rule..."
        print "Rule reminder: Function names need to respect snake_case convention."
        is_rule_ok = True

        source_files = project.get_files_from_project(project.FILE_TYPES["C_FILES"])

        for file in source_files:
            mFile = transform_c_to_xml(file)
            tree = strip_ns_prefix(etree.parse(mFile))
            functions_name = tree.xpath("/unit/function/name/text()")
            for function in functions_name:
                if not re.match(SNAKE_CASE_RE, function):
                    is_rule_ok = False
                    print "F2 Violation! Function name " + function + " in " + file + " is not snake_case!"
            functions_name = tree.xpath("/unit/function_decl/name/text()")
            for function in functions_name:
                if not re.match(SNAKE_CASE_RE, function):
                    is_rule_ok = False
                    print "F2 Violation! Function name " + function + " in " + file + " is not snake_case!"
        if is_rule_ok:
            print "Good job buddy, no violation!"
