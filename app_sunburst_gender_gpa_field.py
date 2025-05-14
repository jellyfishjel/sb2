
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sunburst Chart", layout="centered")
st.title("📊 Sunburst Chart: Field → Gender → Job Level")

# Đọc dữ liệu
df = pd.read_excel("education_career_success.xlsx")

# Nhóm dữ liệu và đếm số lượng sinh viên cho từng tổ hợp
grouped = df.groupby(["Field_of_Study", "Gender", "Current_Job_Level"])["Student_ID"].count().reset_index()
grouped.columns = ["Field_of_Study", "Gender", "Current_Job_Level", "Count"]

# Tạo sunburst chart
fig = px.sunburst(
    grouped,
    path=["Field_of_Study", "Gender", "Current_Job_Level"],
    values="Count",
    title="Field of Study → Gender → Current Job Level (Size = Student Count)"
)
fig.update_traces(textinfo="label+percent parent")

st.plotly_chart(fig, use_container_width=True)
