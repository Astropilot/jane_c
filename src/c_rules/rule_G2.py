# -*- coding: utf-8 -*-

"""
Jane for C Projects
Author: Yohann MARTIN (https://github.com/Astropilot/jane_c)

G2 Rule: Inside a source file, one and only one empty line should
         separate the implementations of functions.
"""

from etna_style_utils import *
from srcml import *

class RuleChecker:

    def __init__(self, project):
        self.project = project

    def check_rule(self):
        project = self.project
        print "Checking G2 Rule..."
        print "Rule reminder: Only one empty line between functions"
        is_rule_ok = True

        source_files = project.get_files_from_project(project.FILE_TYPES["C_FILES"])

        functions_delim_re = re.compile("</function>$(\r*\n*.*)^<function>", re.MULTILINE)
        re_newline = re.compile(r'\n')
        for file in source_files:
            mFile = transform_c_to_xml(file)
            with open(mFile, 'U') as content_file:
                content = content_file.read()
            matches = re.finditer(functions_delim_re, content)
            for match in matches:
                start_line = len(re_newline.findall(content, 0, match.start(1)))+1
                if match.group(1) != "\n\n":
                    is_rule_ok = False
                    print "G2 Violation in " + file + " at line " + str(start_line)
        if is_rule_ok:
            print "Good job buddy, no violation!"
