import streamlit as st

# 页面布局配置
st.set_page_config(layout="wide", page_title="胃癌领域大模型")

# 页面标题
st.title("胃癌领域大模型平台")

# 分两列布局，左窄右宽
left_column, right_column = st.columns([1, 2])

# 左侧：数据上传区域
with left_column:
    st.markdown("""
        <div style="background-color: #f9f9f9; padding: 15px; border: 1px solid #ddd; border-radius: 8px;">
            <h3 style="color: #333;">上传数据</h3>
            <p>请上传以下文件进行分析：</p>
    """, unsafe_allow_html=True)
    
    # 上传组件
    ct_file = st.file_uploader("上传 CT 图像", type=["jpg", "png", "jpeg", "dcm"])
    pathology_file = st.file_uploader("上传病理图像", type=["jpg", "png", "jpeg"])
    case_file = st.file_uploader("上传病例信息", type=["pdf", "txt"])
    
    if st.button("提交分析", key="upload"):
        if ct_file or pathology_file or case_file:
            st.success("数据已提交，正在分析中...")
            # 在此处调用你的分析模型逻辑
        else:
            st.warning("请至少上传一项数据后再提交！")
    
    st.markdown("</div>", unsafe_allow_html=True)

# 右侧：问答区域
with right_column:
    st.markdown("""
        <div style="background-color: #eef6ff; padding: 15px; border: 1px solid #ddd; border-radius: 8px;">
            <h3 style="color: #333;">胃癌知识问答</h3>
    """, unsafe_allow_html=True)
    
    # 存储历史记录
    chat_history = st.session_state.get("chat_history", [])
    
    # 展示历史对话
    for msg in chat_history:
        if msg.startswith("用户："):
            st.markdown(f"<p style='color: #0056b3;'><b>{msg}</b></p>", unsafe_allow_html=True)
        else:
            st.markdown(f"<p style='color: #333;'>{msg}</p>", unsafe_allow_html=True)
    
    # 输入框与发送按钮
    user_input = st.text_input("请输入您的问题：", key="user_input")
    if st.button("发送", key="send"):
        if user_input.strip():
            # 模拟模型回答逻辑
            model_response = f"这是模型针对问题“{user_input}”的回答。"
            chat_history.append(f"用户：{user_input}")
            chat_history.append(f"模型：{model_response}")
            st.session_state.chat_history = chat_history
        else:
            st.warning("请输入有效的问题后再发送！")
    
    st.markdown("</div>", unsafe_allow_html=True)
