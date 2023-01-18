# HelixCoreServerPackage

Perforce Helix is a full-featured VCS that scales to thousands of users and millions of files, which allows you to maintain software source code, documents, or any type of file.

## To create a Git repository:
1. Sign in to DSM using an account with administrative privileges.
1. Go to **Control Panel** > **Terminal & SNMP** > **Terminal** then enable **SSH service**.
1. (Optional) Go to **Control Panel** > **Shared Folder** and create a shared folder for Helix Core server repositories.
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
   cd /volume1/mysharefolder/
   ```
1. 
   ```
   sudo -u Perforce p4dctl-ng new
   ```
