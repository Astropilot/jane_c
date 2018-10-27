# -*- coding: utf-8 -*-

"""
Jane for C Projects
Author: Yohann MARTIN (https://github.com/Astropilot/jane_c)

H3 Rule: Macros should match only one statement.
"""

from etna_style_utils import *
from srcml import *

class RuleChecker:

    def __init__(self, project):
        self.project = project

    def check_rule(self):
        project = self.project
        print "Checking H3 Rule..."
        print "Rule reminder: Macros should match only one statement."
        is_rule_ok = True

        source_files = project.get_files_from_project(project.FILE_TYPES["C_HEADERS"])

        for file in source_files:
            mFile = transform_c_to_xml(file)
            root = strip_ns_prefix(etree.parse(mFile))

            all_macro = root.xpath("/unit//macro")
            for macro in all_macro:
                start_line = macro.sourceline
                macro_name = macro.xpath("name/text()")[0]
                macro_value = macro.xpath("following-sibling::value/text()")
                if len(macro_value) > 0 and ";" in macro_value[0]:
                    is_rule_ok = False
                    print "H3 Violation at line " + str(start_line-1) + ", macro '" + macro_name + "' should match only one statement! File: " + file

        if is_rule_ok:
            print "Good job buddy, no violation!"
