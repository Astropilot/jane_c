# -*- coding: utf-8 -*-

"""
Jane for C Projects
Author: Yohann MARTIN (https://github.com/Astropilot/jane_c)

This file provide a class for extract files from a given project folder
"""

import os, sys
from os import walk
from lxml import etree
import subprocess
import re

class Project:

    FILE_TYPES = {"ALL": [], "C_FILES": [".c", ".h"], "C_SOURCES": [".c"], "C_HEADERS": [".h"]}

    def __init__(self, projectFolder):
        self.projectFolder = projectFolder
        self.load_files()

    def load_files(self):
        self.files = []
        for (dirpath, dirnames, filenames) in walk(self.projectFolder):
            filenames = [dirpath + "\\" + file for file in filenames]
            self.files.extend(filenames)

    def clean_project(self):
        self.load_files()
        files = self.get_files_from_project(self.FILE_TYPES["C_FILES"])
        for file in files:
            file_ext_len = len(os.path.splitext(file)[1])
            file = file[:-file_ext_len]
            os.remove(file + ".xml")

    def get_files_from_project(self, file_type, exclude = False):
        res_files = []
        if (len(file_type) > 0):
            if not exclude:
                res_files = [file for file in self.files if os.path.splitext(file)[1] in file_type]
            else:
                res_files = [file for file in self.files if os.path.splitext(file)[1] not in file_type]
        return res_files
