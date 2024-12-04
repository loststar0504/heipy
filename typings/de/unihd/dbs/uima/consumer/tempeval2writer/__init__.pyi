
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import jpype
import org.apache.uima.cas
import org.apache.uima.collection
import org.apache.uima.jcas
import org.apache.uima.resource
import typing



class Tempeval2Writer(org.apache.uima.collection.CasConsumer_ImplBase):
    PARAM_OUTPUTDIR: typing.ClassVar[str] = ...
    def __init__(self): ...
    @typing.overload
    def initialize(self, resourceSpecifier: org.apache.uima.resource.ResourceSpecifier, map: typing.Union[java.util.Map[str, typing.Any], typing.Mapping[str, typing.Any]]) -> bool: ...
    @typing.overload
    def initialize(self) -> None: ...
    def printTimexAnnotations(self, jCas: org.apache.uima.jcas.JCas) -> None: ...
    @typing.overload
    def processCas(self, cAS: org.apache.uima.cas.CAS) -> None: ...
    @typing.overload
    def processCas(self, cASArray: typing.Union[typing.List[org.apache.uima.cas.CAS], jpype.JArray]) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("de.unihd.dbs.uima.consumer.tempeval2writer")``.

    Tempeval2Writer: typing.Type[Tempeval2Writer]
