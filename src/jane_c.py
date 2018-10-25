#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Jane for C Projects
Author: Yohann MARTIN (https://github.com/Astropilot/jane_c)

Jane is an ETNA standards fault detection program for projects written in C.
This program will check each of the standards defined by ETNA and indicate
the problems found with as much precision as possible.
"""

import os, sys
from os import walk
import imp

from project_utils import Project

######################################################################
#                                                                    #
#                               Rule Loader                          #
#                                                                    #
######################################################################

class RuleLoader:

    def __init__(self, rules_folder, project):
        self.rules_folder = rules_folder
        self.project = project

    def start(self):
        rule_files = []
        for (dirpath, dirnames, filenames) in walk(self.rules_folder):
            rule_files.extend(filenames)
            break
        for rule_file in rule_files:
            self.execute_test(self.rules_folder + "\\" + rule_file)

    def execute_test(self, test_file):
        mod_name,file_ext = os.path.splitext(os.path.split(test_file)[-1])
        if file_ext.lower() == '.py':
            m = imp.load_source(mod_name, test_file)
            RuleChecker = getattr(m, "RuleChecker")
            rule = RuleChecker(self.project)
            rule.check_rule()
            print
            os.remove(test_file + "c")

######################################################################
#                                                                    #
#                               Main program                         #
#                                                                    #
######################################################################

if len(sys.argv) < 2:
    print "Usage: " + sys.argv[0] + " [PROJECT_FOLDER]"
    sys.exit()

projectFolder = sys.argv[1]

if not os.path.isdir(projectFolder):
    print "Folder " + projectFolder + " not exist !"
    sys.exit()

project = Project(projectFolder)
ruleLoader = RuleLoader("c_rules", project)
ruleLoader.start()
project.clean_project()
