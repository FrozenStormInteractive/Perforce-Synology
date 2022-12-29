#!/bin/bash

set -x
set -e

# move build files into source dir
mkdir -p /toolkit/source
cp -R $GITHUB_WORKSPACE /toolkit/source/helixcoreserverpackage

cd /toolkit/source/helixcoreserverpackage

# build spk
/toolkit/pkgscripts-ng/PkgCreate.py -p $SPK_PLATFORM -c helixcoreserverpackage

# copy spk to github workspace
cp /toolkit/build_env/ds.$SPK_PLATFORM-$DSM_VERSION/image/packages/HelixCoreServer-$SPK_PLATFORM-$SPK_PACKAGE_VERSION.spk $GITHUB_WORKSPACE/
