
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.apache.uima
import org.apache.uima.analysis_component
import org.apache.uima.cas
import org.apache.uima.jcas
import typing



class IntervalTagger(org.apache.uima.analysis_component.JCasAnnotator_ImplBase):
    PARAM_LANGUAGE: typing.ClassVar[str] = ...
    PARAM_INTERVALS: typing.ClassVar[str] = ...
    PARAM_INTERVAL_CANDIDATES: typing.ClassVar[str] = ...
    def __init__(self): ...
    def initialize(self, uimaContext: org.apache.uima.UimaContext) -> None: ...
    @typing.overload
    def process(self, jCas: org.apache.uima.jcas.JCas) -> None: ...
    @typing.overload
    def process(self, abstractCas: typing.Union[org.apache.uima.cas.AbstractCas, typing.Callable]) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("de.unihd.dbs.uima.annotator.intervaltagger")``.

    IntervalTagger: typing.Type[IntervalTagger]
