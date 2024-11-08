# 使用 glances 监控内存、CPU、磁盘、网络等信息
# 访问地址：http://ip:61208 , 见图片glances.jpg
pip install glances fastapi uvicorn jinja2 
nohup glances -w &
cat nohup.out


# 使用 top 命令查看内存、CPU、磁盘、网络等信息
top


# top常用命令解释
# top - 10:52:52 up 1 day,  1:00,  1 user,  load average: 0.00, 0.00, 0.00