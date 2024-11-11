# 简介
StatefulSet 是 Kubernetes 中的一种工作负载 API 对象，专为管理有状态应用而设计。与 Deployment 等无状态工作负载不同，StatefulSet 保证 Pod 的稳定网络标识、持久存储和有序部署，适合需要稳定标识和持久存储的应用场景，如数据库、分布式文件系统等。

## 1. StatefulSet 特点
- **稳定的网络标识**: 每个 Pod 都有一个唯一的网络标识，通常是 <StatefulSet-name>-<ordinal> 格式。例如，一个 StatefulSet 名为 mysql，则生成的 Pod 名称可能是 mysql-0、mysql-1 等。

- **稳定且有序的存储**: 每个 Pod 都有一个与之关联的持久存储卷（Persistent Volume），该卷的生命周期与 Pod 绑定，即使 Pod 被删除，数据也不会丢失。

- **有序部署和扩展**: Pod 按顺序创建（从 0 开始），且只有前一个 Pod 运行且准备就绪时，才会创建下一个 Pod。这种有序性对需要先后顺序的应用程序很重要。

- **有序终止**: Pod 按相反的顺序终止（从最大序号开始），这保证了高序号的 Pod 在低序号的 Pod 之前被删除，有助于维护数据一致性和服务稳定性。

## 2. StatefulSet 组成部分
- **apiVersion**: API 版本，通常为 apps/v1。
- **kind**: 对象类型，这里为 StatefulSet。
- **metadata**: 元数据，包括名称、命名空间、标签等。
- **spec**: 主要的配置部分，包括 Pod 模板、服务名称、存储卷配置等。

## 3. StatefulSet 常见用途
- 数据库（如 MySQL、PostgreSQL）
- 分布式缓存（如 Redis、Cassandra）
- 分布式文件系统（如 HDFS）

## 示例：使用 StatefulSet 部署 MySQL
以下是一个使用 StatefulSet 部署 MySQL 数据库的示例，示例包括定义 PersistentVolume、PersistentVolumeClaim、ConfigMap、Service 和 StatefulSet。

[使用 StatefulSet 部署 MySQL](StatefulSet.yaml)

