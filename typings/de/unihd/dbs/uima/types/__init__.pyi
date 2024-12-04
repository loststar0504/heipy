
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import de.unihd.dbs.uima.types.heideltime
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("de.unihd.dbs.uima.types")``.

    heideltime: de.unihd.dbs.uima.types.heideltime.__module_protocol__
