# 技术栈
1. langchain：ai框架
2. weaviate：充当向量数据库
3. qwen：llm模型

# milvus
| index\_type              | metric\_type     | 精确/近似   | 搜索类型  | 查询时间复杂度                  | 说明                        |
| ------------------------ | ---------------- | ------- | ----- | ------------------------ | ------------------------- |
| **FLAT**                 | L2 / IP / COSINE | 精确      | 最近邻   | O(N·d)                   | 暴力线性扫描，结果 100% 精确，适合小规模数据 |
| **IVF\_FLAT**            | L2 / IP / COSINE | 近似      | 最近邻   | O(log N + (N/nlist)·d)   | 聚类倒排索引 + 桶内扫描，速度快，召回率略低   |
| **IVF\_PQ**              | L2 / IP / COSINE | 近似      | 最近邻   | O(log N + (N/nlist)·d/q) | 倒排 + 乘积量化，内存小，速度快，精度略低    |
| **IVF\_SQ8**             | L2 / IP / COSINE | 近似      | 最近邻   | O(log N + (N/nlist)·d)   | 倒排 + 8bit 量化，适合大规模向量库     |
| **HNSW**                 | L2 / IP / COSINE | 近似      | 最近邻   | O(log N) \~ O(log² N)    | 基于图的 ANN，召回率高，查询快，内存大     |
| **Annoy**                | L2 / IP / COSINE | 近似      | 最近邻   | O(log N)                 | 基于随机投影树，适合静态数据集           |
| **DISKANN**              | L2 / IP / COSINE | 近似      | 最近邻   | O(log N)                 | 磁盘 ANN，超大规模向量库，内存低        |
| **倒排索引 (Elasticsearch)** | -                | 精确 / 近似 | 关键字搜索 | O(log N)                 | 字符串匹配，不是向量检索              |
