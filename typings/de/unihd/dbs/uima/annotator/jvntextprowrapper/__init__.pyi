
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import jvntextpro.data
import org.apache.uima
import org.apache.uima.analysis_component
import org.apache.uima.cas
import org.apache.uima.jcas
import typing



class JVnTextProWrapper(org.apache.uima.analysis_component.JCasAnnotator_ImplBase):
    PARAM_SENTSEGMODEL_PATH: typing.ClassVar[str] = ...
    PARAM_WORDSEGMODEL_PATH: typing.ClassVar[str] = ...
    PARAM_POSMODEL_PATH: typing.ClassVar[str] = ...
    PARAM_ANNOTATE_TOKENS: typing.ClassVar[str] = ...
    PARAM_ANNOTATE_SENTENCES: typing.ClassVar[str] = ...
    PARAM_ANNOTATE_PARTOFSPEECH: typing.ClassVar[str] = ...
    def __init__(self): ...
    def initialize(self, uimaContext: org.apache.uima.UimaContext) -> None: ...
    def jvnTagging(self, string: str) -> java.util.List[jvntextpro.data.Sentence]: ...
    @typing.overload
    def process(self, jCas: org.apache.uima.jcas.JCas) -> None: ...
    @typing.overload
    def process(self, abstractCas: typing.Union[org.apache.uima.cas.AbstractCas, typing.Callable]) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("de.unihd.dbs.uima.annotator.jvntextprowrapper")``.

    JVnTextProWrapper: typing.Type[JVnTextProWrapper]
