# -*- coding: utf-8 -*-

"""
Jane for C Projects
Author: Yohann MARTIN (https://github.com/Astropilot/jane_c)

H2 Rule: Headers should be protected from double inclusion.
"""

from etna_style_utils import *
from srcml import *

class RuleChecker:

    def __init__(self, project):
        self.project = project

    def check_rule(self):
        project = self.project
        print "Checking H2 Rule..."
        print "Rule reminder: Headers should be protected from double inclusion."
        is_rule_ok = True

        source_files = project.get_files_from_project(project.FILE_TYPES["C_HEADERS"])

        for file in source_files:
            with open(file, 'U') as content_file:
                content = content_file.read()
            if "#ifndef" not in content and "#pragma once" not in content:
                is_rule_ok = False
                print "H2 possible Violation, is your header protected from double inclusion? File: " + file

        if is_rule_ok:
            print "Good job buddy, no violation!"
