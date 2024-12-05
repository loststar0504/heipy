#!/usr/bin/env bash

set -o errexit  # abort on nonzero exitstatus
set -o nounset  # abort on unbound variable
set -o pipefail # don't hide errors within pipes

pushd heipy/libs/treetagger
treetagger_path=$(pwd)
bash download.sh
bash install-tagger.sh
popd

original_treetagger_config="SET ME IN CONFIG.PROPS! (e.g., /home/jannik/treetagger)"
sed "s|$original_treetagger_config|$treetagger_path|" heipy/libs/config.props.bak > heipy/libs/config.props

echo "HeidelTime Standalone has been successfully installed."