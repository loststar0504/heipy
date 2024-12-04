
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import de.unihd.dbs.uima.consumer.aceternwriter
import de.unihd.dbs.uima.consumer.eventi2014writer
import de.unihd.dbs.uima.consumer.tempeval2writer
import de.unihd.dbs.uima.consumer.tempeval3writer
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("de.unihd.dbs.uima.consumer")``.

    aceternwriter: de.unihd.dbs.uima.consumer.aceternwriter.__module_protocol__
    eventi2014writer: de.unihd.dbs.uima.consumer.eventi2014writer.__module_protocol__
    tempeval2writer: de.unihd.dbs.uima.consumer.tempeval2writer.__module_protocol__
    tempeval3writer: de.unihd.dbs.uima.consumer.tempeval3writer.__module_protocol__
