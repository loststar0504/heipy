
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import de.unihd.dbs.uima.annotator.alllanguagestokenizer
import de.unihd.dbs.uima.annotator.heideltime
import de.unihd.dbs.uima.annotator.intervaltagger
import de.unihd.dbs.uima.annotator.jvntextprowrapper
import de.unihd.dbs.uima.annotator.stanfordtagger
import de.unihd.dbs.uima.annotator.treetagger
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("de.unihd.dbs.uima.annotator")``.

    alllanguagestokenizer: de.unihd.dbs.uima.annotator.alllanguagestokenizer.__module_protocol__
    heideltime: de.unihd.dbs.uima.annotator.heideltime.__module_protocol__
    intervaltagger: de.unihd.dbs.uima.annotator.intervaltagger.__module_protocol__
    jvntextprowrapper: de.unihd.dbs.uima.annotator.jvntextprowrapper.__module_protocol__
    stanfordtagger: de.unihd.dbs.uima.annotator.stanfordtagger.__module_protocol__
    treetagger: de.unihd.dbs.uima.annotator.treetagger.__module_protocol__
