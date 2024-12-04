
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import de.unihd.dbs.uima.annotator
import de.unihd.dbs.uima.consumer
import de.unihd.dbs.uima.reader
import de.unihd.dbs.uima.types
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("de.unihd.dbs.uima")``.

    annotator: de.unihd.dbs.uima.annotator.__module_protocol__
    consumer: de.unihd.dbs.uima.consumer.__module_protocol__
    reader: de.unihd.dbs.uima.reader.__module_protocol__
    types: de.unihd.dbs.uima.types.__module_protocol__
