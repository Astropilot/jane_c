# -*- coding: utf-8 -*-

"""
Jane for C Projects
Author: Yohann MARTIN (https://github.com/Astropilot/jane_c)

O4 Rule: All identifier names should be in English, according to the
         snake_case convention.
"""

from etna_style_utils import *
from srcml import *

class RuleChecker:

    def __init__(self, project):
        self.project = project

    def check_rule(self):
        project = self.project
        print "Checking O4 Rule..."
        print "Rule reminder: File names need to respect snake_case convention."
        is_rule_ok = True

        source_files = project.get_files_from_project(project.FILE_TYPES["C_FILES"])

        for file in source_files:
            filename = os.path.splitext(os.path.basename(file))[0]
            if not re.match(SNAKE_CASE_RE, filename):
                is_rule_ok = False
                print "O4 Violation! " + file + " is not snake_case!"
        if is_rule_ok:
            print "Good job buddy, no violation!"
