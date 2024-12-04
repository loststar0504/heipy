
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import org.apache.uima.cas
import org.apache.uima.collection
import org.apache.uima.jcas
import org.apache.uima.resource
import org.apache.uima.util
import typing



class Eventi2014Reader(org.apache.uima.collection.CollectionReader_ImplBase):
    def __init__(self): ...
    def addSentenceAnnotation(self, jCas: org.apache.uima.jcas.JCas, int: int, int2: int, string: str) -> None: ...
    def addTokenAnnotation(self, jCas: org.apache.uima.jcas.JCas, int: int, int2: int, int3: int, string: str, int4: int, int5: int) -> None: ...
    def close(self) -> None: ...
    def getNext(self, cAS: org.apache.uima.cas.CAS) -> None: ...
    def getProgress(self) -> typing.MutableSequence[org.apache.uima.util.Progress]: ...
    def hasNext(self) -> bool: ...
    @typing.overload
    def initialize(self, resourceSpecifier: org.apache.uima.resource.ResourceSpecifier, map: typing.Union[java.util.Map[str, typing.Any], typing.Mapping[str, typing.Any]]) -> bool: ...
    @typing.overload
    def initialize(self) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("de.unihd.dbs.uima.reader.eventi2014reader")``.

    Eventi2014Reader: typing.Type[Eventi2014Reader]
