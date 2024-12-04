
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import de.unihd.dbs.heideltime
import de.unihd.dbs.uima
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("de.unihd.dbs")``.

    heideltime: de.unihd.dbs.heideltime.__module_protocol__
    uima: de.unihd.dbs.uima.__module_protocol__
