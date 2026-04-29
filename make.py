import tarfile
import argparse
import requests
import os
from datetime import datetime

# SPK
#conf/
#scripts/
#ui/
#WIZARD_UIFILES/
#INFO
#LICENSE
#PACKAGE_ICON.PNG
#PACKAGE_ICON_256.PNG

# package


_SUPPORTED_ARCHS = ["x86_64"]


def _output_gh_actions_variable(key, val):
    output_path = os.environ.get("GITHUB_OUTPUT")
    if output_path:
        with open(output_path, "a") as f:
            f.write(f"{key}={val}\n")


def make_info(arch: str, version: str, uncompressed_size: int, beta: bool=False):

    print("Generating INFO")

    infos = {
        "package": "HelixCoreServer",
        "version" : version,
        "displayname": "Perforce P4 Server (p4d)",
        "description": "Perforce P4 is a full-featured VCS that scales to thousands of users and millions of files.",

        "arch": arch,

        "os_min_ver": "7.0-40000",
        "maintainer": "Perforce Software, Inc.",
        "maintainer_url": "https://www.perforce.com",
        "distributor": "Frozen Storm Interactive",
        "distributor_url": "https://www.frozenstorminteractive.com",
        "thirdparty": "yes",

        "dsmappname": "com.FrozenStormInteractive.HelixCoreServer",
        "dsmuidir": "ui",

        "install_dep_services": "syno-share.target",
        "start_dep_services": "network-online.target syno-share.target",

        "extractsize": uncompressed_size>>10,
        "create_time": datetime.now().strftime("%Y%m%d-%H:%M:%S"),
    }

    if beta:
        infos["beta"] = "yes"

    with open("out/INFO", "w", encoding="utf-8", newline='\n') as f:
        for key, value in infos.items():
            line = f'{key}="{value}"\n'
            f.write(line)


def make_inner_package(p4d_version: str, arch: str):

    if arch == "x86_64":
        p4_arch = "linux26x86_64"
    else:
        raise Exception(f"Unsupported Perforce arch: {arch}") 

    if not os.path.exists("out/helix-core-server.tgz") or not os.path.isfile("out/helix-core-server.tgz"):
        print("Downloading P4 Server binaries")

        response = requests.get(f"https://www.perforce.com/downloads/perforce/r{p4d_version}/bin.{p4_arch}/helix-core-server.tgz")
        response.raise_for_status()

        with open("out/helix-core-server.tgz", "wb") as f:
            f.write(response.content)

    print("Extracting P4 Server binaries")

    with tarfile.open("out/helix-core-server.tgz", "r:gz") as tar:
        tar.extract("p4", path="out")
        tar.extract("p4broker", path="out")
        tar.extract("p4d", path="out")
        tar.extract("p4p", path="out")

    print("Creating inner package tarball")

    with tarfile.open("out/package.tgz", "w:xz", preset=9) as tar:
        tar.add("ui")
        tar.add("out/p4", arcname="/usr/local/bin/out/p4")
        tar.add("out/p4broker", arcname="/usr/local/bin/p4broker")
        tar.add("out/p4d", arcname="/usr/local/bin/p4d")
        tar.add("out/p4p", arcname="/usr/local/bin/p4p")

        tar.add("out/HelixCoreServerCtl/", arcname="/usr/local/bin/")

    uncompressed_size = 0
    with tarfile.open("out/package.tgz", "r:xz") as tar:
        for member in tar.getmembers():
            uncompressed_size += member.size

    return (uncompressed_size)

def make_spk(dsm_version: str, p4d_version: str, arch: str, build_number: int=None, beta: bool=False, out: str=None):
    os.makedirs("out", exist_ok=True)

    (uncompressed_size) = make_inner_package(p4d_version=p4d_version, arch=arch)

    if build_number is not None:
        version_string = f"{p4d_version}-{build_number:04d}"
    else:
        version_string = p4d_version
    make_info(arch, version_string, uncompressed_size, beta=beta)

    print("Creating SPK tarball")

    if out is None:
        out = f"HelixCoreServer-{version_string}-{arch}-{dsm_version}.spk"
    else:
        os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)

    with tarfile.open(out, "w:") as tar:
        tar.add("conf")
        tar.add("scripts")
        tar.add("ui")
        tar.add("WIZARD_UIFILES")

        tar.add("out/INFO", arcname="INFO")
        tar.add("LICENSE")
        tar.add("PACKAGE_ICON.PNG")
        tar.add("PACKAGE_ICON_256.PNG")
        tar.add("out/package.tgz", arcname="package.tgz")

    _output_gh_actions_variable("package_version", version_string)


parser = argparse.ArgumentParser()

parser.add_argument('--platform-version', type=str, required=True)
parser.add_argument('--arch', choices=_SUPPORTED_ARCHS, type=str, required=True)
parser.add_argument('--p4d-version', type=str, required=True)
parser.add_argument('--build-number', type=int)
parser.add_argument('--beta', action='store_true')
parser.add_argument('--output', type=str)

args = parser.parse_args()

make_spk(dsm_version=args.platform_version, p4d_version=args.p4d_version, arch=args.arch, beta=args.beta, build_number=args.build_number, out=args.output)
