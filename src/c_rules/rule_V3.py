# -*- coding: utf-8 -*-

"""
Jane for C Projects
Author: Yohann MARTIN (https://github.com/Astropilot/jane_c)

V3 Rule: The pointer symbol (*) should be attached to the associated variable,
         with no spaces.
"""

from etna_style_utils import *
from srcml import *

class RuleChecker:

    POINTER_OPERATOR_RE = re.compile("<modifier>\*<\/modifier>(?:<\/type>|<\argument>)(.?)<name>([a-z0-9_]*)<\/name>")

    def __init__(self, project):
        self.project = project

    def check_rule(self):
        project = self.project
        print "Checking V3 Rule..."
        print "Rule reminder: The pointer symbol (*) should be attached to the associated variable, with no spaces."
        is_rule_ok = True

        source_files = project.get_files_from_project(project.FILE_TYPES["C_FILES"])

        re_newline = re.compile(r'\n')
        for file in source_files:
            mFile = transform_c_to_xml(file)
            root = strip_ns_prefix(etree.parse(mFile))
            with open(mFile, 'U') as content_file:
                content = content_file.read()
            matches = re.finditer(self.POINTER_OPERATOR_RE, content)
            for match in matches:
                start_line = len(re_newline.findall(content, 0, match.start(1)))+1
                if match.group(1) != '':
                    is_rule_ok = False
                    print "V3 Violation at line " + str(start_line-1) + ", pointer operator '*' need to be followed by '" + match.group(2) + "' identifier! File: " + file

        if is_rule_ok:
            print "Good job buddy, no violation!"
