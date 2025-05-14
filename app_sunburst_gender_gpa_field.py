import plotly.express as px
import pandas as pd

# Đọc dữ liệu
df = pd.read_excel("education_career_success.xlsx")

# Nhóm dữ liệu
grouped = df.groupby(["Field_of_Study", "Gender", "Current_Job_Level"])["Student_ID"].count().reset_index()
grouped.columns = ["Field_of_Study", "Gender", "Current_Job_Level", "Count"]

# Tạo Sunburst chart với drill-down
fig = px.sunburst(
    grouped,
    path=["Field_of_Study", "Gender", "Current_Job_Level"],
    values="Count",
    branchvalues="total",
    maxdepth=1   # 👈 Chỉ hiện vòng đầu tiên (click mới mở rộng)
)

fig.update_traces(
    insidetextorientation='radial',
    sort=False,
    marker=dict(line=dict(color='white', width=2))
)

fig.update_layout(
    margin=dict(t=10, l=10, r=10, b=10),
    uniformtext=dict(minsize=10, mode='hide')
)

fig.show()
