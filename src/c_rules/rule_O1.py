# -*- coding: utf-8 -*-

"""
Jane for C Projects
Author: Yohann MARTIN (https://github.com/Astropilot/jane_c)

O1 Rule: Your delivery folder should contain only files required for
         compilation.
"""

from etna_style_utils import *
from srcml import *

class RuleChecker:

    def __init__(self, project):
        self.project = project

    def check_rule(self):
        project = self.project
        print "Checking O1 Rule..."
        print "Rule reminder: Only files required for compilation"
        is_rule_ok = True

        f = project.get_files_from_project(project.FILE_TYPES["C_FILES"], True)
        if len(f) > 0:
            is_rule_ok = False
            print "O1 Violation ! Concerned files:"
            for file in f:
                print "    - " + file
        if is_rule_ok:
            print "Good job buddy, no violation!"
