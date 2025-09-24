import gradio as gr
from typing import List, Tuple
from agent import chat_with_agent

def create_interface():
    """创建Gradio界面"""
    with gr.Blocks(title="智能聊天机器人", theme=gr.themes.Soft()) as demo:
        gr.Markdown("# 🤖 智能聊天机器人")
        gr.Markdown("与AI助手对话，AI可以搜索知识库来回答问题")
        
        # 聊天区域
        chatbot = gr.Chatbot(
            height=600,
            show_label=False,
            container=True,
            bubble_full_width=False
        )
        
        with gr.Row():
            msg_input = gr.Textbox(
                placeholder="输入你的问题...",
                show_label=False,
                scale=4,
                container=False
            )
            send_btn = gr.Button("发送", variant="primary", scale=1)
        
        # 聊天处理
        def handle_chat(message, history):
            return chat_with_agent(message, history)
        
        # 发送消息
        send_btn.click(
            handle_chat,
            inputs=[msg_input, chatbot],
            outputs=[msg_input, chatbot]
        )
        
        # 回车发送
        msg_input.submit(
            handle_chat,
            inputs=[msg_input, chatbot],
            outputs=[msg_input, chatbot]
        )
        
        # 清空聊天记录
        clear_btn = gr.Button("清空对话", variant="secondary")
        clear_btn.click(
            lambda: ([], ""),
            outputs=[chatbot, msg_input]
        )
    
    return demo

if __name__ == "__main__":
    # 创建并启动界面
    demo = create_interface()
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        debug=True
    )
