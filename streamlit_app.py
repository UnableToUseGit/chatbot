import streamlit as st

# 页面配置
st.set_page_config(layout="wide", page_title="胃癌领域大模型")

# 标题
st.title("胃癌领域大模型平台")

# 分两列布局
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
            # 在这里调用模型进行处理
        else:
            st.warning("请至少上传一项数据后再提交！")
    
    st.markdown("</div>", unsafe_allow_html=True)

# 右侧：聊天窗口区域
with right_column:
    st.markdown("""
        <div style="background-color: #eef6ff; padding: 15px; border: 1px solid #ddd; border-radius: 8px;">
            <h3 style="color: #333;">胃癌知识问答</h3>
    """, unsafe_allow_html=True)

    # 聊天记录（存储在 session_state 中）
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # 展示聊天记录
    chat_container = st.container()
    with chat_container:
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

    # 用户输入框和按钮
    user_input = st.text_input("请输入问题：", key="user_input")
    if st.button("发送", key="send"):
        if user_input.strip():
            # 模拟模型响应
            model_response = f"这是关于“{user_input}”的模型回答。"
            # 添加到聊天历史
            st.session_state.chat_history.append({"role": "user", "content": user_input})
            st.session_state.chat_history.append({"role": "assistant", "content": model_response})
        else:
            st.warning("请输入有效的问题！")
    
    st.markdown("</div>", unsafe_allow_html=True)
