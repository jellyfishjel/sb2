
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sunburst mở rẽ nhánh", layout="centered")
st.title("📊 Sunburst Chart: Field → Internship → Projects (phân nhánh rõ)")

# Đọc file Excel
df = pd.read_excel("education_career_success.xlsx")

# Nhóm số lần thực tập
df["Internship_Band"] = pd.cut(
    df["Internships_Completed"],
    bins=[-1, 0, 1, 3, 10],
    labels=["0", "1", "2–3", "4+"]
)

# Nhóm số dự án
df["Project_Band"] = pd.cut(
    df["Projects_Completed"],
    bins=[-1, 0, 2, 5, 20],
    labels=["0", "1–2", "3–5", "6+"]
)

# Nhóm dữ liệu để tính số sinh viên cho từng nhánh
grouped = df.groupby(["Field_of_Study", "Internship_Band", "Project_Band"])["Student_ID"].count().reset_index()
grouped.columns = ["Field_of_Study", "Internship_Band", "Project_Band", "Count"]

# Tạo biểu đồ sunburst
fig = px.sunburst(
    grouped,
    path=["Field_of_Study", "Internship_Band", "Project_Band"],
    values="Count",
    title="Field → Internships → Projects (rẽ nhánh rõ)"
)

fig.update_traces(
    insidetextorientation='radial',
    root_color="white",
    sort=False
)

fig.update_layout(
    margin=dict(t=10, l=10, r=10, b=10),
    sunburstcolorway=["#636EFA", "#EF553B", "#00CC96", "#AB63FA", "#FFA15A"],
    extendsunburstcolors=True
)

st.plotly_chart(fig, use_container_width=True)
