# 常见的linux操作系统
1. Ubuntu
2. CentOS
3. Red Hat Enterprise Linux (RHEL)
4. openSUSE
5. Manjaro
6. Linux Mint
7. Elementary OS

# ubuntu文件系统结构
- **/bin**：存放基本的用户命令二进制文件，如 `ls`、`cp` 等。
- **/boot**：存放启动加载器相关的文件，如内核和初始 RAM 磁盘映像。
- **/dev**：存放设备文件，表示系统中的硬件设备。
- **/etc**：存放系统配置文件。
- **/home**：存放用户的主目录，每个用户都有一个子目录。
- **/lib**：存放系统程序使用的共享库文件。
- **/media**：挂载可移动媒体设备（如 CD-ROM、USB 驱动器）的挂载点。
- **/mnt**：临时挂载文件系统的挂载点。
- **/opt**：存放可选的应用程序软件包。
- **/proc**：存放系统进程和内核信息的虚拟文件系统。
- **/root**：超级用户（`root`）的主目录。
- **/run**：存放系统运行时数据。
- **/sbin**：存放系统管理员使用的二进制文件。
- **/srv**：存放系统提供的服务相关的数据。
- **/sys**：存放系统和硬件信息的虚拟文件系统。
- **/tmp**：存放临时文件，系统重启后会清空。
- **/usr**：存放用户级应用程序和文件。
- **/var**：存放经常变化的数据文件，如日志文件、缓存等。


# Ubuntu 系统中一些常见的配置文件及其用途
- **/etc/fstab**：定义文件系统的挂载信息。
- **/etc/hostname**：存放系统的主机名。
- **/etc/hosts**：定义静态的主机名到 IP 地址的映射。
- **/etc/network/interfaces**：配置网络接口。
- **/etc/resolv.conf**：配置 DNS 服务器。
- **/etc/passwd**：存放用户账户信息。
- **/etc/shadow**：存放用户的加密密码信息。
- **/etc/group**：存放用户组信息。
- **/etc/sudoers**：配置 sudo 权限。
- **/etc/apt/sources.list**：定义 APT 包管理器的源列表。
- **/etc/crontab**：配置定时任务。
- **/etc/ssh/sshd_config**：配置 SSH 服务器。
- **/etc/sysctl.conf**：配置内核参数。
- **/etc/environment**：配置全局环境变量。
- **/etc/profile**：配置全局的 shell 环境变量和启动程序。
- **/etc/bash.bashrc**：配置全局的 bash shell 环境。

