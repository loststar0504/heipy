
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import de.unihd.dbs.uima.reader.aceternreader
import de.unihd.dbs.uima.reader.eventi2014reader
import de.unihd.dbs.uima.reader.tempeval2reader
import de.unihd.dbs.uima.reader.tempeval3reader
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("de.unihd.dbs.uima.reader")``.

    aceternreader: de.unihd.dbs.uima.reader.aceternreader.__module_protocol__
    eventi2014reader: de.unihd.dbs.uima.reader.eventi2014reader.__module_protocol__
    tempeval2reader: de.unihd.dbs.uima.reader.tempeval2reader.__module_protocol__
    tempeval3reader: de.unihd.dbs.uima.reader.tempeval3reader.__module_protocol__
