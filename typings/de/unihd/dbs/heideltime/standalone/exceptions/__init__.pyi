
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import typing



class DocumentCreationTimeMissingException(java.lang.Exception):
    def __init__(self): ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("de.unihd.dbs.heideltime.standalone.exceptions")``.

    DocumentCreationTimeMissingException: typing.Type[DocumentCreationTimeMissingException]
