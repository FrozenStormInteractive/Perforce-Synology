#!/bin/bash

set -x
set -e

SOURCE_DIRNAME=helixcoreserverpackage
# move build files into source dir
mkdir -p /toolkit/source
cp -R $GITHUB_WORKSPACE /toolkit/source/$SOURCE_DIRNAME

cd /toolkit/source/$SOURCE_DIRNAME

# build spk
/toolkit/pkgscripts-ng/PkgCreate.py -v $DSM_VERSION -p $SPK_PLATFORM -c $SOURCE_DIRNAME
