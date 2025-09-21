## add sub repo
git submodule add 

git submodule add https://github.com/lilulilulilu/mcp-demo.git


## 克隆仓库并拉取子模块：
使用 --recurse-submodules 参数来确保在克隆主仓库时，也同时克隆所有的子模块：

git clone --recurse-submodules <repository-url>


## 如果仓库已经克隆了，但子模块没有下载：
如果你已经克隆了仓库，但子模块没有下载下来，可以使用以下命令来获取子模块：

git submodule update --init --recursive


## 查看当前子模块状态：
可以通过以下命令查看子模块的当前状态：

git submodule status