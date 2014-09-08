# Copyright (c) Calico Development Team.
# Distributed under the terms of the Modified BSD License.
# http://calicoproject.org/

from jupyter_kernel import Magic, option
import os

class EditMagic(Magic):

    def line_edit(self, filename):
        """%edit FILENAME - load code from filename into next cell for editing"""
        orig_filename = filename
        if filename.startswith("~"):
            filename = os.path.expanduser(filename)
        filename = os.path.abspath(filename)
        text = open(filename).read()
        self.kernel.payload.append({"source": "set_next_input",
                                    "text": "%%file " + orig_filename + "\n" + text})

def register_magics(kernel):
    kernel.register_magics(EditMagic)

