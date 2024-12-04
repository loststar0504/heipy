
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import de.unihd.dbs.uima.annotator.heideltime.processors
import de.unihd.dbs.uima.annotator.heideltime.resources
import de.unihd.dbs.uima.annotator.heideltime.utilities
import de.unihd.dbs.uima.types.heideltime
import java.lang
import java.util
import java.util.regex
import org.apache.uima
import org.apache.uima.analysis_component
import org.apache.uima.cas
import org.apache.uima.jcas
import typing



class HeidelTime(org.apache.uima.analysis_component.JCasAnnotator_ImplBase):
    timex_counter: int = ...
    timex_counter_global: int = ...
    flagHistoricDates: bool = ...
    def __init__(self): ...
    def addTimexAnnotation(self, string: str, int: int, int2: int, sentence: de.unihd.dbs.uima.types.heideltime.Sentence, string2: str, string3: str, string4: str, string5: str, string6: str, string7: str, string8: str, jCas: org.apache.uima.jcas.JCas) -> None: ...
    def applyRuleFunctions(self, string: str, matchResult: java.util.regex.MatchResult) -> str: ...
    def checkPosConstraint(self, sentence: de.unihd.dbs.uima.types.heideltime.Sentence, string: str, matchResult: java.util.regex.MatchResult, jCas: org.apache.uima.jcas.JCas) -> bool: ...
    def correctDurationValue(self, string: str) -> str: ...
    def disambiguateHistoricDates(self, jCas: org.apache.uima.jcas.JCas) -> None: ...
    def findTimexes(self, string: str, hashMap: java.util.HashMap[java.util.regex.Pattern, str], hashMap2: java.util.HashMap[str, str], hashMap3: java.util.HashMap[str, str], sentence: de.unihd.dbs.uima.types.heideltime.Sentence, jCas: org.apache.uima.jcas.JCas) -> None: ...
    def getAttributesForTimexFromFile(self, string: str, hashMap: java.util.HashMap[str, str], hashMap2: java.util.HashMap[str, str], hashMap3: java.util.HashMap[str, str], hashMap4: java.util.HashMap[str, str], hashMap5: java.util.HashMap[str, str], matchResult: java.util.regex.MatchResult, jCas: org.apache.uima.jcas.JCas) -> typing.MutableSequence[str]: ...
    def getPosFromMatchResult(self, int: int, int2: int, sentence: de.unihd.dbs.uima.types.heideltime.Sentence, jCas: org.apache.uima.jcas.JCas) -> str: ...
    def initialize(self, uimaContext: org.apache.uima.UimaContext) -> None: ...
    @typing.overload
    def process(self, jCas: org.apache.uima.jcas.JCas) -> None: ...
    @typing.overload
    def process(self, abstractCas: typing.Union[org.apache.uima.cas.AbstractCas, typing.Callable]) -> None: ...
    def removeInvalids(self, jCas: org.apache.uima.jcas.JCas) -> None: ...
    def specifyAmbiguousValues(self, jCas: org.apache.uima.jcas.JCas) -> None: ...
    def specifyAmbiguousValuesString(self, string: str, timex3: de.unihd.dbs.uima.types.heideltime.Timex3, integer: int, list: java.util.List[de.unihd.dbs.uima.types.heideltime.Timex3], jCas: org.apache.uima.jcas.JCas) -> str: ...

class HeidelTimeException(java.lang.Exception):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    def getMessage(self) -> str: ...

class ProcessorManager:
    def __init__(self): ...
    def executeProcessors(self, jCas: org.apache.uima.jcas.JCas, priority: 'ProcessorManager.Priority') -> None: ...
    def initializeAllProcessors(self, uimaContext: org.apache.uima.UimaContext) -> None: ...
    @typing.overload
    def registerProcessor(self, string: str) -> None: ...
    @typing.overload
    def registerProcessor(self, string: str, priority: 'ProcessorManager.Priority') -> None: ...
    class Priority(java.lang.Enum['ProcessorManager.Priority']):
        PREPROCESSING: typing.ClassVar['ProcessorManager.Priority'] = ...
        POSTPROCESSING: typing.ClassVar['ProcessorManager.Priority'] = ...
        ARBITRARY: typing.ClassVar['ProcessorManager.Priority'] = ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'ProcessorManager.Priority': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.MutableSequence['ProcessorManager.Priority']: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("de.unihd.dbs.uima.annotator.heideltime")``.

    HeidelTime: typing.Type[HeidelTime]
    HeidelTimeException: typing.Type[HeidelTimeException]
    ProcessorManager: typing.Type[ProcessorManager]
    processors: de.unihd.dbs.uima.annotator.heideltime.processors.__module_protocol__
    resources: de.unihd.dbs.uima.annotator.heideltime.resources.__module_protocol__
    utilities: de.unihd.dbs.uima.annotator.heideltime.utilities.__module_protocol__
