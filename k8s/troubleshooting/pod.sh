kubectl describe pod gender-detect-54f84dfc57-c5mbz -n cmr
kubectl get events -n cmr --field-selector involvedObject.name=gender-detect-54f84dfc57-c5mbz


kubectl logs gender-detect-54f84dfc57-c5mbz -c gender-detect-container -n cmr --tail=100 -f 
# pod的五种状态
# 1. Pending：Pod 已被 Kubernetes 系统接受，但某些容器尚未创建或启动。可能是因为需要下载镜像或等待调度。
# 2. Running：Pod 已经绑定到一个节点，并且所有容器都已创建。至少有一个容器正在运行，或者正在启动或重启。
# 3. Succeeded：Pod 中的所有容器都已成功终止，并且不会再重启。
# 4. Failed：Pod 中的所有容器都已终止，并且至少有一个容器以非零状态退出。
# 5. Unknown：因为某些原因，无法获取 Pod 的状态，通常是因为与 Pod 所在节点的通信失败。