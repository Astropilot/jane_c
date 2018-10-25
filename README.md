
# Jane for C

Jane is an ETNA standards fault detection program for projects written in C.
It was written in Python 2.7 for Windows and bases its code analysis on the srcml framework.

This program will check each of the standards defined by ETNA and indicate the problems found with as much precision as possible.

Be aware that this program is developed by a student and that the verifications are based on the "C Coding Style" and may differ from the official verification program used by ETNA.

You are invited to participate in the implementation and correction of the verification rules! For that look at the category "Contributing".

## How to use it

### Prerequisites

In order to make Jena work, you will need:
* [Python 2.X](https://www.python.org/downloads/) (X >= 7)
* [lxml library for Python](https://lxml.de/)
* [srcML Framework](https://www.srcml.org/#download)

/!\ Do not forget to add srcML in `PATH` env !

### Installation

Just make a copy of the git repository and go to the `src` folder.

```bash
$> git clone https://github.com/Astropilot/jane_c.git
$> cd src/
```

You can now simply launch the main script with the path to your C project as an argument.

```bash
$> python jane_c.py C:\Projects\ExampleProject
```

## Contributing

Each rule is defined in a separate file, which you can find in the `c_rules` folder.
I invite you to look at the existing rules in order to understand how to use the different tools available.

However, a minimal structure is required for your rule to be functional:

```python
# -*- coding: utf-8 -*-
# These libraries are not required
# but are strongly recommended for code analysis.
from etna_style_utils import *
from srcml import *

class RuleChecker:

    def __init__(self, project):
        self.project = project

    def check_rule(self):
        project = self.project
        # From here, you are free to write your code
```
________

The `project` variable allows you to access the list of files contained in the project given as an argument. You can only request certain files, or exclude some.
```python
files = []
files.extend(project.get_files_from_project(project.FILE_TYPES["ALL"], exclude = False))
```

Here is a list of the already defined types of files you can use:

```python
project.FILE_TYPES["ALL"] = []
project.FILE_TYPES["C_FILES"] = [".c", ".h"]
project.FILE_TYPES["C_SOURCES"] = [".c"]
project.FILE_TYPES["C_HEADERS"] = [".h"]
```

But of course you can customize the desired file types:
```python
files = []
files.extend(project.get_files_from_project([".txt", ".ext"]))
```

________

Thanks to the srcML framework you can obtain the source code of a file in XML format, which allows you to use XPath for example to move around and quickly check the tags.
