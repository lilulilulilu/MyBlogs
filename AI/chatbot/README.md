# 智能聊天机器人

基于Gradio和LangChain的智能聊天机器人，支持文件上传和知识库检索。

## 功能特性

- 📁 **文件上传**: 支持PDF、TXT、DOCX格式文件上传
- 🧠 **向量存储**: 使用Milvus向量数据库存储文档
- 💬 **智能对话**: 基于Ollama LLM的智能对话
- 🔍 **知识库检索**: 自动从上传的文档中检索相关信息
- 🎨 **现代界面**: 基于Gradio的美观用户界面

## 安装依赖

```bash
pip install -r requirements.txt
```

## 运行应用

### 方法1: 使用启动脚本
```bash
./run_app.sh
```

### 方法2: 直接运行
```bash
cd src
python app.py
```

## 使用说明

1. **上传文件**: 在左侧面板选择并上传PDF、TXT或DOCX文件
2. **开始对话**: 在右侧聊天窗口输入问题
3. **智能回答**: AI会根据上传的文档内容智能回答你的问题

## 技术架构

- **前端**: Gradio
- **LLM**: Ollama (llama3.2:latest)
- **向量数据库**: Milvus
- **文档处理**: LangChain
- **嵌入模型**: Ollama (embeddinggemma:latest)

## 文件结构

```
chatbot/
├── src/
│   ├── app.py          # 主应用文件
│   ├── store.py        # Milvus存储类
│   └── load_data.py    # 文档加载和分割
├── files/              # 上传文件存储目录
├── requirements.txt    # 依赖列表
└── run_app.sh         # 启动脚本
```

## 注意事项

- 确保Ollama服务正在运行
- 首次运行时会创建Milvus数据库文件
- 支持的文件格式: PDF, TXT, DOCX
- 默认端口: 7860