# -*- coding: utf-8 -*-

"""
Jane for C Projects
Author: Yohann MARTIN (https://github.com/Astropilot/jane_c)

F5 Rule: The statement of arguments should follow the ISO/ANSI C syntax.
         A function taking no parameters should take void as argument in the
         function declaration.
         A function should not need more than 4 arguments.
"""

from etna_style_utils import *
from srcml import *

class RuleChecker:

    def __init__(self, project):
        self.project = project

    def check_rule(self):
        project = self.project
        print "Checking F5 Rule..."
        print "Rule reminder: A function taking no parameters should take void as argument in the function declaration"
        print "               and no more than 4 arguments."
        is_rule_ok = True

        source_files = project.get_files_from_project(project.FILE_TYPES["C_FILES"])

        for file in source_files:
            mFile = transform_c_to_xml(file)
            tree = strip_ns_prefix(etree.parse(mFile))
            functions = tree.xpath("/unit/function | /unit/function_decl")
            for function in functions:
                function_name = function.xpath("name/text()")[0]
                function_nb_params = function.xpath("count(parameter_list/parameter)")
                if function_nb_params == 0:
                    is_rule_ok = False
                    print "F5 Violation! Function " + function_name + " need to have at least 'void' in file " + file
                elif function_nb_params > 4:
                    is_rule_ok = False
                    print "F5 Violation! Function " + function_name + " can't have more than 4 arguments in file " + file
        if is_rule_ok:
            print "Good job buddy, no violation!"
