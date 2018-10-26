# -*- coding: utf-8 -*-

"""
Jane for C Projects
Author: Yohann MARTIN (https://github.com/Astropilot/jane_c)

V1 Rule: All identifier names should be in English, according to the snake_case convention.
         The type names defined with typedef should end with _t.
         The names of macros and the content of enums should be written in UPPER_CASE.
"""

from etna_style_utils import *
from srcml import *

class RuleChecker:

    def __init__(self, project):
        self.project = project

    def check_rule(self):
        project = self.project
        print "Checking V1 Rule..."
        print "Rule reminder: All identifier names should be in English, according to the snake_case convention."
        print "               The type names defined with typedef should end with _t."
        print "               The names of macros and the content of enums should be written in UPPER_CASE."
        is_rule_ok = True

        source_files = project.get_files_from_project(project.FILE_TYPES["C_FILES"])

        for file in source_files:
            mFile = transform_c_to_xml(file)
            root = ignore_c_comments(strip_ns_prefix(etree.parse(mFile)))

            all_identifiers = root.xpath("/unit//name[not(parent::macro) and not(../../parent::enum) and count(*) = 0]")
            for identifier in all_identifiers:
                start_line = identifier.sourceline
                identifier_str = identifier.xpath("text()")[0]
                if not re.match(SNAKE_CASE_RE, identifier_str):
                    is_rule_ok = False
                    print "V1 Violation at line " + str(start_line-1) + ", identifier '" + identifier_str + "' do not respect snake_case convention! File: " + file

            macro_name_enum_content = root.xpath("/unit//name[parent::macro or ../../parent::enum and count(*) = 0]")
            for identifier in macro_name_enum_content:
                start_line = identifier.sourceline
                identifier_str = identifier.xpath("text()")[0]
                if not re.match(SCREAMING_SNAKE_CASE_RE, identifier_str):
                    is_rule_ok = False
                    print "V1 Violation at line " + str(start_line-1) + ", identifier '" + identifier_str + "' need to be in upper_case! File: " + file

            typedef_names = root.xpath("/unit//typedef/name")
            for typedef_name in typedef_names:
                start_line = typedef_name.sourceline
                name_str = typedef_name.xpath("text()")[0]
                if not name_str.endswith("_t"):
                    is_rule_ok = False
                    print "V1 Violation at line " + str(start_line-1) + ", typedef name '" + name_str + "' should end with '_t'! File: " + file

        if is_rule_ok:
            print "Good job buddy, no violation!"
