#!/bin/bash

source /pkgscripts/include/pkg_util.sh


if [ -z "$SPK_PACKAGE_VERSION" ]; then
    SPK_PACKAGE_VERSION="${P4D_VERSION:-22.2}-${SPK_PACKAGE_BUILD_NUMBER:-0001}"
fi

package="HelixCoreServer"
version="$SPK_PACKAGE_VERSION"
displayname="Perforce Helix Core Server (p4d)"
os_min_ver="7.0-40000"
maintainer="Perforce Software, Inc."
maintainer_url="https://www.perforce.com"
distributor="Frozen Storm Interactive"
distributor_url="https://www.frozenstorminteractive.com"
arch="x86_64 i686"
description="Perforce Helix is a full-featured VCS that scales to thousands of users and millions of files."
dsmuidir="ui"
dsmappname="com.FrozenStormInteractive.HelixCoreServer"
thirdparty="yes"
install_dep_services="syno-share.target"
start_dep_services="network-online.target syno-share.target"
if [ "$SPK_BETA" = true ] ; then
    beta="yes"
fi
[ "$(caller)" != "0 NULL" ] && return 0
pkg_dump_info