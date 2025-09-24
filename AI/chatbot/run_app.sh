#!/bin/bash

# 激活虚拟环境（如果使用conda）
# conda activate your_env_name

# 安装依赖
pip install -r requirements.txt

# 启动应用
cd src
python app.py
