# Perforce P4 Server Package for Synology

Perforce P4 is a full-featured VCS that scales to thousands of users and millions of files, which allows you to maintain software source code, documents, or any type of file.

## Requirements

- DSM >= 7.0
- Synology NAS with a x86_64 processor

## Downloading the package

Download the .spk package corresponding to your NAS in [the Releases page](https://github.com/FrozenStormInteractive/Perforce-Synology/releases).

Packages have names containing the information you need to choose which one to install:
```
HelixCoreServer-<Perforce server version>-<Package version number>-<Processor architecture>-<DSM version>.spk 
```

For example, the package with number 0025 containing P4D 23.1 for Synology NAS with x86_64 processor and DSM 7.1 has the name `HelixCoreServer-23.1-0025-x86_64-7.1.spk`.

## Installing the package

- Go to the DSM Package Center
- At the top left of the Package Center window, next to the search bar, click on the "Manual install" button.
- Select the spk file you have downloaded
- Follow the instruction of the installer
You msut create a perforce server now.

Once installed, you need to create a Perforce server.

## How to create a Perforce server:
1. Sign in to DSM using an account with administrative privileges.
1. Go to **Control Panel** > **Terminal & SNMP** > **Terminal** then enable **SSH service**.
1. (Optional) Go to **Control Panel** > **Shared Folder** and create a shared folder for P4 server repositories.
   This package creates a  shared folder named ***Perforce*** by default
1. On your computer, enter the command below to access Synology NAS via SSH:
   ```
   ssh [Synology NAS admin user name]@[Synology NAS IP address or hostname] -p [The port number of SSH]
   ```
   For example, you can enter:
   ```
   ssh myadminuser@192.168.1.2 -p 22
   ```
1. Enter the command below to change the current directory to the shared folder you created in step 3:
   ```
   cd /[Volume name]/[Shared folder name]/
   ```
   For example, you can enter:
   ```
   cd /volume1/Perforce/
   ```
1. 
   ```
   sudo -u Perforce p4dctl-ng new
   ```

## Upgrading the package

- Download the newest version in [the Releases page](https://github.com/FrozenStormInteractive/Perforce-Synology/releases). 
  
  :warning: You must take a package with a higher perforce server version than your current one, or a higher package number than your current one. The perforce server is not backward-compatible.
- Go to the DSM Package Center
- At the top left of the Package Center window, next to the search bar, click on the "Manual install" button.
- Select the spk file you have downloaded
- Follow the instruction of the installer.
