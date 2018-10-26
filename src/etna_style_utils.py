# -*- coding: utf-8 -*-

"""
Jane for C Projects
Author: Yohann MARTIN (https://github.com/Astropilot/jane_c)

This file provide some usefull variables and method related to ETNA Coding Style
"""

import re

SNAKE_CASE_RE = re.compile("^[a-z0-9_]*$")
SCREAMING_SNAKE_CASE_RE = re.compile("^[A-Z0-9_]*$")

ETNA_HEADER_RE = re.compile("""^/\*
\*\* ETNA PROJECT, [0-9]{2}/[0-9]{2}/[0-9]{4} by [a-z0-9_]*
\*\* .*
\*\* File description:
\*\*      .*
\*/$""")
