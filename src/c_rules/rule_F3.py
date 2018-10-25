# -*- coding: utf-8 -*-

"""
Jane for C Projects
Author: Yohann MARTIN (https://github.com/Astropilot/jane_c)

F3 Rule: Inside files, the length of a line should not exceed 80 columns.
"""

from etna_style_utils import *
from srcml import *

class RuleChecker:

    def __init__(self, project):
        self.project = project

    def check_rule(self):
        project = self.project
        print "Checking F3 Rule..."
        print "Rule reminder: No more than 80 columns in files."
        is_rule_ok = True

        source_files = project.get_files_from_project(project.FILE_TYPES["C_FILES"])

        for file in source_files:
            with open(file, 'U') as content_file:
                content = [line.rstrip('\n') for line in content_file]
            count_line = 1
            for line in content:
                line = line.replace('\t', '    ')
                if len(line) > 80:
                    is_rule_ok = False
                    print "F3 Violation! Line " + str(count_line) + " in file " + file
                count_line += 1
        if is_rule_ok:
            print "Good job buddy, no violation!"
