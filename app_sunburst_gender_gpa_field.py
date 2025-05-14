import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Drill-down Sunburst", layout="centered")
st.title("📊 Sunburst: Field → Gender → Job Level (drill-down)")

# Load dữ liệu
df = pd.read_excel("education_career_success.xlsx")

# Nhóm và đếm số sinh viên
grouped = df.groupby(["Field_of_Study", "Gender", "Current_Job_Level"])["Student_ID"].count().reset_index()
grouped.columns = ["Field_of_Study", "Gender", "Current_Job_Level", "Count"]

# Tạo biểu đồ
fig = px.sunburst(
    grouped,
    path=["Field_of_Study", "Gender", "Current_Job_Level"],
    values="Count",
    maxdepth=1,  # 👈 chỉ hiện vòng đầu tiên
    branchvalues="total"
)

fig.update_traces(
    insidetextorientation="radial",
    marker=dict(line=dict(color='white', width=2))
)

st.plotly_chart(fig, use_container_width=True)
