# -*- coding: utf-8 -*-

"""
Jane for C Projects
Author: Yohann MARTIN (https://github.com/Astropilot/jane_c)

L4 Rule: Opening curly brackets should be at the end of their line,
         except for functions where they must be placed alone on their line.
         Closing curly brackets should always be alone on their line,
         except in the case of an else statement.
"""

from etna_style_utils import *
from srcml import *

class RuleChecker:

    def __init__(self, project):
        self.project = project

    def check_rule(self):
        project = self.project
        print "Checking L4 Rule..."
        print "Rule reminder: ..."
        is_rule_ok = True

        source_files = project.get_files_from_project(project.FILE_TYPES["C_FILES"])

        re_newline = re.compile(r'\n')
        for file in source_files:
            with open(file, 'U') as content_file:
                content = content_file.readlines()
            content = [x.strip() for x in content]
            mFile = transform_c_to_xml(file)
            root = strip_ns_prefix(etree.parse(mFile))
            all_blocks = root.xpath("//block[starts-with(.,'{')]")
            for block in all_blocks:
                line_block = block.sourceline
                end_line_block = block.sourceline + (len(etree.tostring(block).strip().split('\n')) - 1)
                parent = block.getparent()
                if ((parent.tag == 'function' or parent.tag == 'struct') and line_block == parent.sourceline):
                    is_rule_ok = False
                    print "L4 Violation at line " + str(line_block-1) + ", open curly bracket should NOT be in the same line that the function prototype! File: " + file
                if ((parent.tag != 'function' and parent.tag != 'struct') and line_block != parent.sourceline):
                    is_rule_ok = False
                    print "L4 Violation at line " + str(line_block-1) + ", open curly bracket should be on the previous line! File: " + file
                if (content[end_line_block-2] != "}" and "else" not in content[end_line_block-2]):
                    print "L4 Violation at line " + str(end_line_block-1) + ", closing curly brackets should be alone on their line! File " + file
                    print "/!\ Do not take this violation into account in the case of a structure"

        if is_rule_ok:
            print "Good job buddy, no violation!"
