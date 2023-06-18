#!/bin/bash

set -x
set -e

if ! [[ $SPK_PACKAGE_BUILD_NUMBER =~ "^[0-9]+$" ]]; then
   printf -v SPK_PACKAGE_BUILD_NUMBER "%04d" "$SPK_PACKAGE_BUILD_NUMBER"
fi

if [ "$SPK_BETA" = true ] ; then
    SPK_PACKAGE_BUILD_NUMBER+="b"
fi

SOURCE_DIRNAME=helixcoreserverpackage
# move build files into source dir
mkdir -p /toolkit/source
cp -R $GITHUB_WORKSPACE /toolkit/source/$SOURCE_DIRNAME

cd /toolkit/source/$SOURCE_DIRNAME

# build spk
/toolkit/pkgscripts-ng/PkgCreate.py -v $DSM_VERSION -p $SPK_PLATFORM -c $SOURCE_DIRNAME
