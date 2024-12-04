
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import de.unihd.dbs.heideltime.standalone.components.impl
import java.util
import org.apache.uima.jcas
import typing



class JCasFactory:
    def createJCas(self) -> org.apache.uima.jcas.JCas: ...

class ResultFormatter:
    def format(self, jCas: org.apache.uima.jcas.JCas) -> str: ...

class UIMAAnnotator:
    def initialize(self, properties: java.util.Properties) -> None: ...
    def process(self, jCas: org.apache.uima.jcas.JCas) -> None: ...

class PartOfSpeechTagger(UIMAAnnotator):
    TREETAGGER_ANNOTATE_TOKENS: typing.ClassVar[str] = ...
    TREETAGGER_ANNOTATE_SENTENCES: typing.ClassVar[str] = ...
    TREETAGGER_ANNOTATE_POS: typing.ClassVar[str] = ...
    TREETAGGER_IMPROVE_GERMAN_SENTENCES: typing.ClassVar[str] = ...
    TREETAGGER_LANGUAGE: typing.ClassVar[str] = ...
    TREETAGGER_CHINESE_TOKENIZER_PATH: typing.ClassVar[str] = ...
    JVNTEXTPRO_WORD_MODEL_PATH: typing.ClassVar[str] = ...
    JVNTEXTPRO_SENT_MODEL_PATH: typing.ClassVar[str] = ...
    JVNTEXTPRO_POS_MODEL_PATH: typing.ClassVar[str] = ...
    JVNTEXTPRO_ANNOTATE_TOKENS: typing.ClassVar[str] = ...
    JVNTEXTPRO_ANNOTATE_SENTENCES: typing.ClassVar[str] = ...
    JVNTEXTPRO_ANNOTATE_POS: typing.ClassVar[str] = ...
    STANFORDPOSTAGGER_ANNOTATE_TOKENS: typing.ClassVar[str] = ...
    STANFORDPOSTAGGER_ANNOTATE_SENTENCES: typing.ClassVar[str] = ...
    STANFORDPOSTAGGER_ANNOTATE_POS: typing.ClassVar[str] = ...
    STANFORDPOSTAGGER_MODEL_PATH: typing.ClassVar[str] = ...
    STANFORDPOSTAGGER_CONFIG_PATH: typing.ClassVar[str] = ...
    HUNPOS_LANGUAGE: typing.ClassVar[str] = ...
    HUNPOS_MODEL_PATH: typing.ClassVar[str] = ...
    HUNPOS_ANNOTATE_TOKENS: typing.ClassVar[str] = ...
    HUNPOS_ANNOTATE_SENTENCES: typing.ClassVar[str] = ...
    HUNPOS_ANNOTATE_POS: typing.ClassVar[str] = ...
    def reset(self) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("de.unihd.dbs.heideltime.standalone.components")``.

    JCasFactory: typing.Type[JCasFactory]
    PartOfSpeechTagger: typing.Type[PartOfSpeechTagger]
    ResultFormatter: typing.Type[ResultFormatter]
    UIMAAnnotator: typing.Type[UIMAAnnotator]
    impl: de.unihd.dbs.heideltime.standalone.components.impl.__module_protocol__