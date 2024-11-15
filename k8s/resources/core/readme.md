## pod是什么？
```
pod是k8s中可以创建和管理的最小单元，由一组容器组成。其他资源都是为pod服务的。
Pod 启动过程可以概括为以下步骤：
    提交 Pod 定义：用户提交 Pod 规范。
    API Server 接收请求：将 Pod 定义保存到 etcd。
    调度器选择节点：根据调度策略选择运行 Pod 的节点。
    Kubelet 接收任务：目标节点上的 Kubelet 监视到新的 Pod 分配给自己。
    Kubelet 创建 Pod：检查镜像、创建容器、配置网络、挂载卷。
    启动容器：启动容器中的应用程序。
    运行后处理：监视容器状态并处理重启。
    服务发现和负载均衡：将 Pod 注册到 Service 中。
这个过程确保 Pod 按照定义的规范运行，并在集群中自动处理调度、资源分配和故障恢复。
```
## 