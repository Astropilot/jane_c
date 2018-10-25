# -*- coding: utf-8 -*-

"""
Jane for C Projects
Author: Yohann MARTIN (https://github.com/Astropilot/jane_c)

G1 Rule: The source files (.c, .h) should always start
         with the standard header of the school.
"""

from etna_style_utils import *
from srcml import *

class RuleChecker:

    def __init__(self, project):
        self.project = project

    def check_rule(self):
        project = self.project
        print "Checking G1 Rule..."
        print "Rule reminder: Sources files should always start with ETNA Header."
        is_rule_ok = True

        source_files = project.get_files_from_project(project.FILE_TYPES["C_FILES"])

        for file in source_files:
            mFile = transform_c_to_xml(file)
            tree = strip_ns_prefix(etree.parse(mFile))
            first_comment_bloc = tree.xpath("/unit/child::*[1]/text()")[0]
            if not re.match(ETNA_HEADER_RE, first_comment_bloc):
                is_rule_ok = False
                print "G1 Violation! Concerned file: " + file
        if is_rule_ok:
            print "Good job buddy, no violation!"
