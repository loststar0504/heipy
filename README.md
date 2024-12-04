# heipy

### requirements

```sh
pip install Jpype1
```

### setup

1. Install HeidelTime Standalone

    ```sh
    ./install_heideltime_standalone
    ```

2. Install python package

    ```sh
    pip install .
    ```

### usage

#### 1. Python package

```python
from heipy.heideltime import ht_process
result = ht_process(some_text)
```

#### 2. CLI Interactive mode

```sh
python heipy/heideltime.py
```

- Example

    ```sh
    ❯ python heipy/heideltime.py
    JAVA_HOME=/home/.sdkman/candidates/java/23.0.1-amzn
    JVM_PATH=/home/.sdkman/candidates/java/23.0.1-amzn/lib/server/libjvm.dylib
    load heideltime...
    interactive heideltime started!!
    > the Costa Rican Civil War lasted from 1948-03-12 to 1948-04-24.
    TEMPONYM: Costa Rican Civil War
    -----Result-----
    <?xml version="1.0"?>
    <!DOCTYPE TimeML SYSTEM "TimeML.dtd">
    <TimeML>
    the <TIMEX3INTERVAL earliestBegin="1948-03-12" latestBegin="1948-03-12" earliestEnd="1948-04-24" latestEnd="1948-04-24"><TIMEX3 tid="t100007" type="TEMPONYM" value="1948-04-24">Costa Rican Civil War</TIMEX3></TIMEX3INTERVAL> lasted from <TIMEX3 tid="t1" type="DATE" value="1948-03-12">1948-03-12</TIMEX3> to <TIMEX3 tid="t2" type="DATE" value="1948-04-24">1948-04-24</TIMEX3>.
    </TimeML>

    > 
    ```