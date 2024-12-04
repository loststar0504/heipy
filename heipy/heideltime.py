import os
import time
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
if __name__ == "__main__":
    print("load heideltime...")
jpype.startJVM(
    jvmpath,
    classpath=[HEIDELTIME_JAR_PATH],
)


def surpress_java_log():
    # surpress java log
    Logger = jpype.JClass("java.util.logging.Logger")
    Level = jpype.JClass("java.util.logging.Level")
    logger = Logger.getLogger("")
    logger.setLevel(Level.SEVERE)


surpress_java_log()

# load heideltime classes
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


def ht_process(text: str) -> str:
    return ht.process(text)


if __name__ == "__main__":
    import sys

    print("interactive heideltime started!!")
    print(">", end=" ", flush=True)
    for line in sys.stdin:
        result = ht_process(line.strip())
        print("-----Result-----")
        print(result)
        print(">", end=" ", flush=True)
