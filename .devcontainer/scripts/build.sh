#!/bin/bash

mkdir -p $TOOLKITPATH/source/HelixCoreServer
cp -r $WORKSPACE_DIRECTORY/. $TOOLKITPATH/source/HelixCoreServer
$PKGSCRIPTSPATH/PkgCreate.py -v $DSMVERSION -p $ARCHITECTURE -c HelixCoreServer
