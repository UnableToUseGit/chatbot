import streamlit as st

# 页面配置
st.set_page_config(layout="wide", page_title="胃癌领域大模型")

# 初始化聊天历史和用户输入
if "chat_history" not in st.session_state:
    # st.session_state.chat_history = [{"role": "assistant", "content": "您好！欢迎使用胃癌领域知识问答系统，我是您的助手，请问有什么可以帮助您？"},
    #                                  {"role": "user", "content": "什么是胃癌免疫治疗?"},
    #                                 {"role": "assistant", "content": "胃癌免疫治疗是一种利用免疫系统的自然防御机制来治疗胃癌的方法。通过激活或增强患者的免疫系统，免疫治疗能够识别并攻击胃癌细胞。"},
    #                                 {"role": "user", "content": "免疫治疗适合所有胃癌患者吗?"},
    #                                 {"role": "assistant", "content": "免疫治疗并非适合所有胃癌患者。其效果通常与肿瘤的分子特征有关。例如，携带PD-L1高表达或微卫星不稳定（MSI-H）等标志物的胃癌患者可能更易从免疫治疗中受益。此外，免疫治疗往往适用于晚期或转移性胃癌患者，早期胃癌患者通常采用手术治疗为主。"},]

    # st.session_state.chat_history = [{"role": "assistant", "content": "您好！欢迎使用胃癌领域知识问答系统，我是您的助手，请问有什么可以帮助您？"}]
    
    st.session_state.chat_history = [{"role": "assistant", "content": "您好！欢迎使用胃癌领域知识问答系统，我是您的助手，请问有什么可以帮助您？"},
                                     {"role": "assistant", "content": "病人基本情况：病人是一名55岁男性，体重正常，未有明显的基础疾病，过去的病史中没有重大的免疫系统疾病。近期因上腹部不适就诊，胃镜检查发现胃部肿块，经过活检确诊为胃腺癌。CT显示胃肿瘤位于胃体，已经侵犯周围的胃壁，且伴有1个较大的淋巴结转移（大约2cm），另外，肝脏、肺部未见明显转移。肿瘤大小大约为3.5cm×3.0cm。病理报告显示胃癌为胃腺癌，分化较差，肿瘤细胞增生明显。通过免疫组化检查，发现肿瘤细胞PD-L1表达水平为50%（高表达）。微卫星分析结果为MSI-H（微卫星高不稳定），并且肿瘤突变负荷（TMB）为高（大于10个突变/百万碱基）。患者未曾接受过任何抗癌治疗。目前无严重免疫系统缺陷，体力状态良好（ECOG评分0-1）。患者无已知的肝肾功能不良、过敏史或严重副作用史。"},
                                    {"role": "assistant", "content": "免疫治疗适合此患者：基于该患者的PD-L1高表达、MSI-H状态和高TMB，该患者是免疫治疗的潜在适应者。免疫检查点抑制剂（如派姆单抗或纳武单抗）是该患者的推荐治疗方案，可以作为单药治疗或与其他疗法（如化疗）联合使用。疗效预测：由于患者具备多个有利的分子标志物（PD-L1高表达、MSI-H、高TMB），免疫治疗很可能能够延缓疾病进展，提高生存期。但需要定期监测患者的病情和副作用，特别是免疫相关的不良反应（如免疫性肺炎、肝炎等），并根据病情变化调整治疗方案。总的来说，我会推荐这位患者接受免疫治疗，并密切监控疗效和不良反应。"},
                                    


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
