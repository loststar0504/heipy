#!/usr/bin/env bash

detect_os_and_architecture() {
    local os_type="$(uname -s)"
    local architecture="$(uname -m)"
    local result=""

    if [ "$os_type" == "Darwin" ]; then
        if [ "$architecture" == "x86_64" ]; then
            result="mac-intel"
        elif [ "$architecture" == "arm64" ]; then
            result="mac-m1"
        else
            result="macOS-Unknown"
        fi
    elif [ "$os_type" == "Linux" ]; then
        result="linux"
    else
        result="Unknown"
    fi

    echo "$result"
}

get_package_url() {
    local os="$(detect_os_and_architecture)"
    case "$os" in
        mac-m1)
            echo "https://www.cis.uni-muenchen.de/%7Eschmid/tools/TreeTagger/data/tree-tagger-MacOSX-M1-3.2.3.tar.gz"
            ;;
        mac-intel)
            echo "https://www.cis.uni-muenchen.de/%7Eschmid/tools/TreeTagger/data/tree-tagger-MacOSX-Intel-3.2.3.tar.gz"
            ;;
        linux)
            echo "https://www.cis.uni-muenchen.de/%7Eschmid/tools/TreeTagger/data/tree-tagger-linux-3.2.5.tar.gz"
            ;;
    esac
}

echo start
TREE_TAGGER=$(get_package_url)
echo $TREE_TAGGER

curl -OJLs $TREE_TAGGER
curl -OJLs https://www.cis.uni-muenchen.de/%7Eschmid/tools/TreeTagger/data/tagger-scripts.tar.gz
curl -OJLs https://www.cis.uni-muenchen.de/%7Eschmid/tools/TreeTagger/data/install-tagger.sh
curl -OJLs https://www.cis.uni-muenchen.de/%7Eschmid/tools/TreeTagger/data/english.par.gz
echo done