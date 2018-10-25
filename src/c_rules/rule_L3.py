# -*- coding: utf-8 -*-

"""
Jane for C Projects
Author: Yohann MARTIN (https://github.com/Astropilot/jane_c)

L3 Rule: Always place a space after a comma or a keyword.
         No space between name function and opening parenthesis
         or after unary operator.
         All binary and ternary operators should be separated from
         the arguments by a space on both sides.
"""

from etna_style_utils import *
from srcml import *

class RuleChecker:

    C_KEYWORDS = ["auto", "break", "case", "char", "const",
                  "continue", "default", "do", "double", "else",
                  "enum", "extern", "float", "for", "goto", "if",
                  "int", "long", "register", "return", "short", "signed",
                  "sizeof", "static", "struct", "switch", "typedef",
                  "union", "unsigned", "void", "volatile", "while"]

    def __init__(self, project):
        self.project = project

    def check_rule(self):
        pass
        project = self.project
        print "Checking L3 Rule..."
        print "Rule reminder: Always place a space after a comma or a keyword."
        print "               No space between name function and opening parenthesis or after unary operator."
        print "               All binary and ternary operators should be separated from the arguments by a space on both sides."
        is_rule_ok = True

        source_files = project.get_files_from_project(project.FILE_TYPES["C_FILES"])
