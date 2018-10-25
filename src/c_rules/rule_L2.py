# -*- coding: utf-8 -*-

"""
Jane for C Projects
Author: Yohann MARTIN (https://github.com/Astropilot/jane_c)

L2 Rule: 4 spaces should be used for indentation.
"""

from etna_style_utils import *
from srcml import *

class RuleChecker:

    TAB_IDENT = re.compile("^(\t+)", re.MULTILINE)

    def __init__(self, project):
        self.project = project

    def check_rule(self):
        project = self.project
        print "Checking L2 Rule..."
        print "Rule reminder: 4 spaces should be used for indentation."
        is_rule_ok = True

        source_files = project.get_files_from_project(project.FILE_TYPES["C_FILES"])

        re_newline = re.compile(r'\n')
        for file in source_files:
            with open(file, 'U') as content_file:
                content = content_file.read()
            matches = re.finditer(self.TAB_IDENT, content)
            for match in matches:
                start_line = len(re_newline.findall(content, 0, match.start(1)))+1
                is_rule_ok = False
                print "L2 Violation at line " + str(start_line) + ", tab for identation found! File: " + file

        if is_rule_ok:
            print "Good job buddy, no violation!"
