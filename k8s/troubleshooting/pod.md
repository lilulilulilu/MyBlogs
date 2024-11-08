# Kubernetes Pod 状态

Kubernetes 中的 Pod 主要有以下几种状态：

1. **Pending（待定）**  
   Pod 已经被提交到 Kubernetes 系统，但还没有被调度到 Node 上。通常是因为某些资源（如 CPU、内存、存储）不可用，或者正在等待调度。

2. **Running（运行中）**  
   Pod 已被调度到 Node，并且至少有一个容器处于运行状态。如果 Pod 内的所有容器都运行正常，则此状态表明 Pod 正常工作。

3. **Succeeded（成功）**  
   Pod 中的所有容器都已经成功终止，且不会再重新启动（通常是因为容器的退出码为 0）。这种状态适用于一次性任务或者批处理任务。

4. **Failed（失败）**  
   Pod 中的所有容器都已终止，并且至少有一个容器的退出码不是 0。这表明 Pod 执行任务失败。

5. **Unknown（未知）**  
   Kubernetes 无法获取 Pod 的状态信息，可能是由于与 Node 失去连接。

6. **CrashLoopBackOff**  
   虽然不是正式的 Pod 状态，但表示 Pod 中的某个容器不断崩溃并重启。
