import streamlit as st

# 页面配置
st.set_page_config(layout="wide", page_title="胃癌领域大模型")

# 初始化聊天历史
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [{"role": "assistant", "content": "您好！欢迎使用胃癌领域知识问答系统，我是您的助手，请问有什么可以帮助您？"}]

# 页面标题
st.title("胃癌领域大模型平台")

# 两列布局
left_column, right_column = st.columns([1, 2])

# 左侧：数据上传区域
with left_column:
    st.markdown("""
        <div style="background-color: #f9f9f9; padding: 15px; border: 1px solid #ddd; border-radius: 8px;">
            <h3 style="color: #333;">上传数据</h3>
            <p>请上传以下文件进行分析：</p>
    """, unsafe_allow_html=True)

    # 文件上传
    ct_file = st.file_uploader("上传 CT 图像", type=["jpg", "png", "jpeg", "dcm"])
    pathology_file = st.file_uploader("上传病理图像", type=["jpg", "png", "jpeg"])
    case_file = st.file_uploader("上传病例信息", type=["pdf", "txt"])
    
    if st.button("提交分析", key="upload"):
        if ct_file or pathology_file or case_file:
            st.success("数据已提交，正在分析中...")
        else:
            st.warning("请至少上传一项数据后再提交！")
    
    st.markdown("</div>", unsafe_allow_html=True)

# 右侧：聊天窗口区域
with right_column:
    st.markdown("""
        <div style="background-color: #eef6ff; padding: 15px; border: 1px solid #ddd; border-radius: 8px;">
            <h3 style="color: #333;">胃癌知识问答</h3>
    """, unsafe_allow_html=True)

    # 聊天内容显示区域（固定高度，支持滚动）
    chat_container = st.container()
    with chat_container:
        st.markdown("""
            <div style="height: 400px; overflow-y: auto; padding: 10px; border: 1px solid #ddd; border-radius: 8px; background-color: #fff;">
        """, unsafe_allow_html=True)
        
        # 展示聊天记录
        for msg in st.session_state.chat_history:
            if msg["role"] == "user":
                st.markdown(f"""
                    <div style="text-align: right; margin: 5px;">
                        <div style="display: inline-block; background-color: #d1ecf1; padding: 10px; border-radius: 10px; max-width: 70%;">
                            {msg["content"]}
                        </div>
                    </div>
                """, unsafe_allow_html=True)
            elif msg["role"] == "assistant":
                st.markdown(f"""
                    <div style="text-align: left; margin: 5px;">
                        <div style="display: inline-block; background-color: #f8d7da; padding: 10px; border-radius: 10px; max-width: 70%;">
                            {msg["content"]}
                        </div>
                    </div>
                """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

    # 固定在底部的输入框和发送按钮
    with st.container():
        st.markdown("""
            <div style="position: fixed; bottom: 0; left: 0; width: 100%; background-color: #f9f9f9; padding: 10px; border-top: 1px solid #ddd;">
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([4, 1])
        with col1:
            # 设置输入框，确保值与 session_state 同步
            user_input = st.text_input("请输入您的问题：", value="", key="user_input", label_visibility="collapsed")
        with col2:
            if st.button("发送", key="send"):
                if user_input.strip():
                    # 模拟模型响应
                    model_response = f"这是针对“{user_input}”的回答。"
                    # 添加到聊天历史
                    st.session_state.chat_history.append({"role": "user", "content": user_input})
                    st.session_state.chat_history.append({"role": "assistant", "content": model_response})
                    # 清空输入框（通过刷新页面实现）
                    st.session_state.user_input = ""
                else:
                    st.warning("请输入有效的问题！")
        
        st.markdown("</div>", unsafe_allow_html=True)
