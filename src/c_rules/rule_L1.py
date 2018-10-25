# -*- coding: utf-8 -*-

"""
Jane for C Projects
Author: Yohann MARTIN (https://github.com/Astropilot/jane_c)

L1 Rule: A line should correspond to only one statement.
"""

from etna_style_utils import *
from srcml import *

class RuleChecker:

    STMT_SAME_LINE = re.compile("^.*((<expr_stmt>.*</expr_stmt>).*){2,}.*$", re.MULTILINE)
    ASSIGN_WITH_COND_OR_WHILE = re.compile(".*((?:<if>|<while>).*<condition>.*<operator>=</operator>.*</condition>)")
    MULTIPLE_ASSIGN = re.compile("^(.*<operator>=</operator>){2,}.*$", re.MULTILINE)
    COMMA_OPERATOR = re.compile("^(.*<operator>,</operator>.*)$", re.MULTILINE)
    ONE_LINE_IF = re.compile("^.*(<if>.*</if>).*$", re.MULTILINE)

    def __init__(self, project):
        self.project = project

    def check_rule(self):
        project = self.project
        print "Checking L1 Rule..."
        print "Rule reminder: Only one statement per line."
        is_rule_ok = True

        source_files = project.get_files_from_project(project.FILE_TYPES["C_SOURCES"])

        re_newline = re.compile(r'\n')
        for file in source_files:
            mFile = transform_c_to_xml(file)
            root = strip_ns_prefix(etree.parse(mFile))
            with open(mFile, 'U') as content_file:
                content = content_file.read()
            matches = re.finditer(self.STMT_SAME_LINE, content)
            for match in matches:
                start_line = len(re_newline.findall(content, 0, match.start(1)))+1
                is_rule_ok = False
                tree = strip_ns_prefix(etree.fromstring(match.group(2)))
                concerned_line = tree.xpath("string(.)")
                print "L1 Violation at line " + str(start_line-1) + ", '" + concerned_line + "' can't be in same line ! File: " + file

            matches = re.finditer(self.ASSIGN_WITH_COND_OR_WHILE, content)
            for match in matches:
                start_line = len(re_newline.findall(content, 0, match.start(1)))+1
                is_rule_ok = False
                print "L1 Violation at line " + str(start_line-1) + ", invalid assignment in if/while! File: " + file

            matches = re.finditer(self.MULTIPLE_ASSIGN, content)
            for match in matches:
                start_line = len(re_newline.findall(content, 0, match.start(1)))+1
                is_rule_ok = False
                print "L1 Violation at line " + str(start_line-1) + ", multiple assignments on same line! File: " + file

            matches = re.finditer(self.COMMA_OPERATOR, content)
            for match in matches:
                start_line = len(re_newline.findall(content, 0, match.start(1)))+1
                is_rule_ok = False
                print "L1 Violation at line " + str(start_line-1) + ", comma operator forbidden! File: " + file

            matches = re.finditer(self.ONE_LINE_IF, content)
            for match in matches:
                start_line = len(re_newline.findall(content, 0, match.start(1)))+1
                is_rule_ok = False
                print "L1 Violation at line " + str(start_line-1) + ", one-line if forbidden! File: " + file

            multiple_decls = root.xpath("/unit//decl_stmt[count(decl) > 1]")
            for multiple_decl in multiple_decls:
                start_line = multiple_decl.sourceline
                is_rule_ok = False
                print "L1 Violation at line " + str(start_line-1) + ", multiple variable declaration on same line! File: " + file

        if is_rule_ok:
            print "Good job buddy, no violation!"
