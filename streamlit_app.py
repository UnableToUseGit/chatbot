import streamlit as st

# 页面配置
st.set_page_config(layout="wide", page_title="胃癌领域大模型")

# 初始化聊天历史和用户输入
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [{"role": "assistant", "content": "您好！欢迎使用胃癌领域知识问答系统，我是您的助手，请问有什么可以帮助您？"},
                                     {"role": "user", "content": "什么是胃癌免疫治疗?"},
                                    {"role": "assistant", "content": "胃癌免疫治疗是一种利用免疫系统的自然防御机制来治疗胃癌的方法。通过激活或增强患者的免疫系统，免疫治疗能够识别并攻击胃癌细胞。"},
                                    {"role": "user", "content": "免疫治疗适合所有胃癌患者吗?"},
                                    {"role": "assistant", "content": "免疫治疗并非适合所有胃癌患者。其效果通常与肿瘤的分子特征有关。例如，携带PD-L1高表达或微卫星不稳定（MSI-H）等标志物的胃癌患者可能更易从免疫治疗中受益。此外，免疫治疗往往适用于晚期或转移性胃癌患者，早期胃癌患者通常采用手术治疗为主。"},]
if "user_input" not in st.session_state:
    st.session_state.user_input = ""  # 初始化输入内容

# 页面标题
# st.title("胃癌领域大模型平台")
st.markdown("""
    <h1 style="text-align: center; color: #333;">胃癌领域大模型平台</h1>
""", unsafe_allow_html=True)

# 两列布局
left_column, right_column = st.columns([1, 2])

# 左侧：数据上传区域
with left_column:
    st.markdown("""
        <div style="background-color: #f9f9f9; padding: 15px; border: 1px solid #ddd; border-radius: 8px; text-align: center;">
            <h3 style="color: #333;">上传数据</h3>
            <p>请上传以下文件进行分析：</p>
        </div>
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
        <div style="background-color: #f9f9f9; padding: 15px; border: 1px solid #ddd; border-radius: 8px; text-align: center;">
            <h3 style="color: #333;">知识问答</h3>
        </div>
    """, unsafe_allow_html=True)

    # 显示聊天历史
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # 用户输入框
    user_input = st.text_input("请输入您的问题：", key="user_input")  # Save input to local variable

    # 按钮提交用户输入
    if st.button("发送"):
        user_message = user_input.strip()  # Use the value stored in local variable
        if user_message:
            # 用户问题加入聊天历史
            st.session_state.chat_history.append({"role": "user", "content": user_message})
            # 模拟助手回答
             # 对话规则：根据用户输入返回固定回复
            if "什么是胃癌免疫治疗" in user_message:
                assistant_reply = "胃癌免疫治疗是一种利用免疫系统的自然防御机制来治疗胃癌的方法。通过激活或增强患者的免疫系统，免疫治疗能够识别并攻击胃癌细胞。常见的免疫治疗方法包括免疫检查点抑制剂、细胞因子疗法和肿瘤疫苗。"
            elif "免疫治疗适合所有胃癌患者吗？" in user_message:
                assistant_reply = "免疫治疗并非适合所有胃癌患者。其效果通常与肿瘤的分子特征有关。例如，携带PD-L1高表达或微卫星不稳定（MSI-H）等标志物的胃癌患者可能更易从免疫治疗中受益。此外，免疫治疗往往适用于晚期或转移性胃癌患者，早期胃癌患者通常采用手术治疗为主。"
            elif "你好" in user_message or "您好" in user_message:
                assistant_reply = "您好！有什么问题我可以帮助解答吗？"
            else:
                assistant_reply = f"您问了：{user_message}。这是模拟回答。"
                
            st.session_state.chat_history.append({"role": "assistant", "content": assistant_reply})

    st.markdown("</div>", unsafe_allow_html=True)
