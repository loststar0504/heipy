import os
import jpype
import jpype.imports
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
HEIDELTIME_JAR_PATH = str(
    PROJECT_ROOT / "libs" / "de.unihd.dbs.heideltime.standalone.jar"
)
CONFIG_PATH = str(PROJECT_ROOT / "libs" / "config.props")


def find_jvm():
    # JAVA_HOME 환경 변수 가져오기
    java_home = os.environ.get("JAVA_HOME")
    if not java_home:
        raise EnvironmentError("JAVA_HOME environment variable is not set.")
    java_home = Path(os.path.realpath(java_home))
    print(f"JAVA_HOME={java_home}")
    for jvmpath in java_home.rglob("libjvm.*"):
        print(f"JVM_PATH={jvmpath}")
        return str(jvmpath)
    raise FileNotFoundError("libjvm not found")


jvmpath = find_jvm()
jpype.startJVM(
    jvmpath,
    classpath=[HEIDELTIME_JAR_PATH],
)

DocumentType = jpype.JClass("de.unihd.dbs.heideltime.standalone.DocumentType")
HeidelTimeStandalone = jpype.JClass(
    "de.unihd.dbs.heideltime.standalone.HeidelTimeStandalone"
)
OutputType = jpype.JClass("de.unihd.dbs.heideltime.standalone.OutputType")
POSTagger = jpype.JClass("de.unihd.dbs.heideltime.standalone.POSTagger")
Language = jpype.JClass("de.unihd.dbs.uima.annotator.heideltime.resources.Language")

outtype = OutputType.TIMEML
postagger = POSTagger.TREETAGGER
conffile = CONFIG_PATH

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
