import streamlit as st

# 页面配置
st.set_page_config(layout="wide", page_title="胃癌领域大模型")

# 初始化聊天历史和用户输入
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [{"role": "assistant", "content": "您好！欢迎使用胃癌领域知识问答系统，我是您的助手，请问有什么可以帮助您？"}]
if "user_input" not in st.session_state:
    st.session_state.user_input = ""  # 初始化输入内容

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
        <div style="background-color: #f9f9f9; padding: 15px; border: 1px solid #ddd; border-radius: 8px;">
            <h3 style="color: #333;">聊天窗口</h3>
            <div id="chat-history" style="max-height: 400px; overflow-y: auto; margin-bottom: 50px;">
    """, unsafe_allow_html=True)

    # 显示聊天历史
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    st.markdown("</div>", unsafe_allow_html=True)

    # 用户输入框
    user_input = st.text_input("请输入您的问题：", key="user_input")  # Save input to local variable

    # 按钮提交用户输入
    if st.button("发送"):
        user_message = user_input.strip()  # Use the value stored in local variable
        if user_message:
            # 用户问题加入聊天历史
            st.session_state.chat_history.append({"role": "user", "content": user_message})
            # 模拟助手回答
            assistant_reply = f"您问了：{user_message}。这是模拟回答。"
            st.session_state.chat_history.append({"role": "assistant", "content": assistant_reply})

    # 使用CSS固定输入框位置
    st.markdown("""
        <style>
            /* 固定输入框在页面底部 */
            .stTextInput {
                position: fixed;
                bottom: 0;
                width: 80%;
                margin: 0 10%;
                z-index: 1;
            }
            /* 增加聊天框的滚动 */
            #chat-history {
                overflow-y: scroll;
            }
        </style>
    """, unsafe_allow_html=True)
