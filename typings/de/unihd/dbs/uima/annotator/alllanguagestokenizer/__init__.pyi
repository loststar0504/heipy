
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import de.unihd.dbs.uima.types.heideltime
import java.util
import org.apache.uima.analysis_component
import org.apache.uima.cas
import org.apache.uima.jcas
import typing



class AllLanguagesTokenizer(org.apache.uima.analysis_component.JCasAnnotator_ImplBase):
    def __init__(self): ...
    @typing.overload
    def process(self, jCas: org.apache.uima.jcas.JCas) -> None: ...
    @typing.overload
    def process(self, abstractCas: typing.Union[org.apache.uima.cas.AbstractCas, typing.Callable]) -> None: ...
    def sentenceTokenize(self, jCas: org.apache.uima.jcas.JCas) -> java.util.List[de.unihd.dbs.uima.types.heideltime.Sentence]: ...
    def tokenize(self, jCas: org.apache.uima.jcas.JCas) -> java.util.List[de.unihd.dbs.uima.types.heideltime.Token]: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("de.unihd.dbs.uima.annotator.alllanguagestokenizer")``.

    AllLanguagesTokenizer: typing.Type[AllLanguagesTokenizer]
