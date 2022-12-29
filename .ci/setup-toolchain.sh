#!/bin/bash

set -x
set -e

apt-get update
apt-get install -y cifs-utils python3 python3-pip jq

mkdir -p /toolkit
cd /toolkit
git clone --depth 1 --single-branch --branch DSM$DSM_VERSION https://github.com/SynologyOpenSource/pkgscripts-ng

/toolkit/pkgscripts-ng/EnvDeploy -v $DSM_VERSION -p $SPK_PLATFORM
