
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import de.unihd.dbs.uima.annotator.heideltime
import de.unihd.dbs.uima.annotator.heideltime.resources
import de.unihd.dbs.uima.types.heideltime
import java.lang
import java.util
import java.util.regex
import org.apache.uima.jcas
import typing



class ContextAnalyzer:
    def __init__(self): ...
    @staticmethod
    def checkInfrontBehind(matchResult: java.util.regex.MatchResult, sentence: de.unihd.dbs.uima.types.heideltime.Sentence) -> bool: ...
    @staticmethod
    def checkTokenBoundaries(matchResult: java.util.regex.MatchResult, sentence: de.unihd.dbs.uima.types.heideltime.Sentence, jCas: org.apache.uima.jcas.JCas) -> bool: ...
    @staticmethod
    def getClosestTense(timex3: de.unihd.dbs.uima.types.heideltime.Timex3, jCas: org.apache.uima.jcas.JCas, language: de.unihd.dbs.uima.annotator.heideltime.resources.Language) -> str: ...
    @staticmethod
    def getLastMentionedX(list: java.util.List[de.unihd.dbs.uima.types.heideltime.Timex3], int: int, string: str, language: de.unihd.dbs.uima.annotator.heideltime.resources.Language) -> str: ...
    @staticmethod
    def getLastTense(timex3: de.unihd.dbs.uima.types.heideltime.Timex3, jCas: org.apache.uima.jcas.JCas, language: de.unihd.dbs.uima.annotator.heideltime.resources.Language) -> str: ...

class DateCalculator:
    def __init__(self): ...
    @staticmethod
    def getLocaleFromString(string: str) -> java.util.Locale: ...
    @staticmethod
    def getWeekOfDate(string: str) -> int: ...
    @staticmethod
    def getWeekdayOfDate(string: str) -> int: ...
    @staticmethod
    def getXNextCentury(string: str, integer: int) -> str: ...
    @staticmethod
    def getXNextDay(string: str, integer: int) -> str: ...
    @staticmethod
    def getXNextDecade(string: str, integer: int) -> str: ...
    @staticmethod
    def getXNextMonth(string: str, integer: int) -> str: ...
    @staticmethod
    def getXNextWeek(string: str, integer: int, language: de.unihd.dbs.uima.annotator.heideltime.resources.Language) -> str: ...
    @staticmethod
    def getXNextYear(string: str, integer: int) -> str: ...

class LocaleException(de.unihd.dbs.uima.annotator.heideltime.HeidelTimeException):
    def __init__(self): ...

class Logger:
    def __init__(self): ...
    @staticmethod
    def getPrintDetails() -> bool: ...
    @typing.overload
    @staticmethod
    def printDetail(class_: typing.Type[typing.Any], string: str) -> None: ...
    @typing.overload
    @staticmethod
    def printDetail(string: str) -> None: ...
    @typing.overload
    @staticmethod
    def printError(class_: typing.Type[typing.Any], string: str) -> None: ...
    @typing.overload
    @staticmethod
    def printError(string: str) -> None: ...
    @staticmethod
    def setPrintDetails(boolean: bool) -> None: ...

class Toolbox:
    def __init__(self): ...
    @staticmethod
    def findMatches(pattern: java.util.regex.Pattern, charSequence: typing.Union[java.lang.CharSequence, str]) -> java.lang.Iterable[java.util.regex.MatchResult]: ...
    @staticmethod
    def sortByValue(hashMap: java.util.HashMap[java.util.regex.Pattern, str]) -> java.util.List[java.util.regex.Pattern]: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("de.unihd.dbs.uima.annotator.heideltime.utilities")``.

    ContextAnalyzer: typing.Type[ContextAnalyzer]
    DateCalculator: typing.Type[DateCalculator]
    LocaleException: typing.Type[LocaleException]
    Logger: typing.Type[Logger]
    Toolbox: typing.Type[Toolbox]
