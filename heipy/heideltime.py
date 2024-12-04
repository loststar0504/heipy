import os
import platform
import jpype
import jpype.imports


def check_java_home():
    java_home = os.environ.get("JAVA_HOME")
    if not java_home:
        raise EnvironmentError(
            "JAVA_HOME environment variable is not set. Please set JAVA_HOME to point to the Java installation directory."
        )
    return os.path.realpath(java_home)


def find_jvm():
    system = platform.system()
    if system == "Windows":
        target_ext = ".dll"
    elif system == "Darwin":  # macOS
        target_ext = ".dylib"
    else:  # Linux 및 기타 유닉스 계열
        target_ext = ".so"
    jvm_filename = "libjvm" + target_ext
    java_home = check_java_home()
    return f"{java_home}/jre/lib/server/{jvm_filename}"


jvmpath = find_jvm()
jpype.startJVM(
    jvmpath,
    classpath=[
        "/Users/user/hwisang/workspace/heipy/libs/de.unihd.dbs.heideltime.standalone.jar"
    ],
)

from de.unihd.dbs.heideltime.standalone import (
    DocumentType,
    HeidelTimeStandalone,
    OutputType,
    POSTagger,
)
from de.unihd.dbs.uima.annotator.heideltime.resources import Language

outtype = OutputType.TIMEML
postagger = POSTagger.TREETAGGER
conffile = "libs/config.props"

ht = HeidelTimeStandalone(
    Language.ENGLISH,
    DocumentType.NARRATIVES,
    outtype,
    conffile,
    postagger,
    doIntervalTagging=True,
)
result = ht.process("the Costa Rican Civil War lasted from 1948-03-12 to 1948-04-24.")
print(result)
