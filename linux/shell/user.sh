

# 使用su命令切换到root用户，要输入root用户的密码
su - root

# sudo 是一个用户组，系统中属于该组的用户可以执行带有 root 权限的命令，而不需要直接使用 root 账户。

# 使用户具有sudo权限有如下两种方法，一种是将用户加入sudo组，另一种是手动编辑sudoers文件
# 方法一：使用root权限或者使用有sudo权限的账户登录后执行下列命令，将用户加入sudo组:
sudo usermod -aG sudo username
# 或
sudo usermod -aG wheel username # 如果是CentOS，RHEL系统


# 方法二：手动编辑sudoers文件
sudo visudo
# 用户 lilu 可以在所有主机上，以任何用户身份（包括 root），执行任何命令，并且不需要输入密码
lilu ALL=(ALL) NOPASSWD:ALL
# ALL 表示可以在所有主机上执行命令
# (ALL) 表示可以以任何用户身份执行命令
# /etc/sudoers 文件里有如下行，表示 sudo 组中的所有用户都可以在系统上执行任何命令
%sudo   ALL=(ALL:ALL) ALL

