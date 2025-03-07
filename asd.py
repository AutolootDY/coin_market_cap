# # import streamlit as st
# # import pandas as pd
# # import plotly.express as px
# # import glob
# # import os

# # # 📂 โฟลเดอร์ที่เก็บไฟล์ CSV
# # data_folder = "top200_by_date"

# # # 🔍 ค้นหาไฟล์ CSV และดึงวันที่ออกมา
# # csv_files = glob.glob(os.path.join(data_folder, "*.csv"))
# # available_dates = sorted([os.path.basename(f).replace("_top200.csv", "") for f in csv_files])

# # # 🎨 ตั้งค่า Streamlit UI
# # st.title("📊 Crypto MarketCap Treemap")
# # st.write("เลือกวันที่เพื่อดู MarketCap ของ 200 เหรียญที่ใหญ่ที่สุด")

# # # 📅 Dropdown ให้ผู้ใช้เลือกวันที่
# # selected_date = st.selectbox("เลือกวันที่", available_dates)

# # # 📖 โหลดข้อมูลของวันที่ที่เลือก
# # if selected_date:
# #     file_path = os.path.join(data_folder, f"{selected_date}_top200.csv")
# #     df = pd.read_csv(file_path)

# #     # 🔢 แปลง market_cap เป็นตัวเลข
# #     df["market_cap"] = pd.to_numeric(df["market_cap"], errors='coerce')

# #     # 🔴 สีขึ้นอยู่กับ % การเปลี่ยนแปลงของราคา (หากมี)
# #     if "price_change_percent" in df.columns:
# #         color_column = "price_change_percent"
# #     else:
# #         color_column = "market_cap"

# #     st.write(df[["coin", "market_cap"]].head())
# #     st.write("🔍 ตรวจสอบข้อมูล market_cap")
# #     st.write(df[["coin", "market_cap"]].describe())  # ดูสถิติ market_cap
# #     st.write(df.head())  # ดูตัวอย่างข้อมูล
# #     # 🎨 สร้าง Treemap
# #     fig = px.treemap(df, 
# #                      path=['coin'],  
# #                      values='market_cap',  
# #                      color=color_column,  
# #                      hover_data=['price', 'total_volume'],
# #                      color_continuous_scale='RdYlGn',
# #                      title=f"🔷 MarketCap Treemap - {selected_date}")

# #     fig.update_traces(textinfo="label+value")  # แสดงชื่อและมูลค่าในกล่อง

# #     # 📌 แสดงผลใน Streamlit
# #     st.plotly_chart(fig, use_container_width=True)



# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import glob
# import os

# # 📂 โฟลเดอร์ที่เก็บไฟล์ CSV
# data_folder = "top200_by_date"

# # 🔍 ค้นหาไฟล์ CSV และดึงวันที่ออกมา
# csv_files = glob.glob(os.path.join(data_folder, "*.csv"))
# available_dates = sorted([os.path.basename(f).replace("_top200.csv", "") for f in csv_files])

# # 🎨 ตั้งค่า Streamlit UI
# st.title("📊 Crypto MarketCap Treemap")
# st.write("เลือกวันที่เพื่อดู MarketCap ของ 200 เหรียญที่ใหญ่ที่สุด")

# # 📅 Dropdown ให้ผู้ใช้เลือกวันที่
# selected_date = st.selectbox("เลือกวันที่", available_dates)

# # 📖 โหลดข้อมูลของวันที่ที่เลือก
# if selected_date:
#     file_path = os.path.join(data_folder, f"{selected_date}_top200.csv")
#     df = pd.read_csv(file_path)

#     # 🔢 แปลง market_cap เป็นตัวเลข
#     df["market_cap"] = pd.to_numeric(df["market_cap"], errors='coerce')

#     # 🧹 ลบค่า NaN และค่า market_cap ที่เป็น 0
#     df = df.dropna(subset=["market_cap"])
#     df = df[df["market_cap"] > 0]

#     # 🔄 รวม market_cap ทั้งหมดของวันนั้น
#     total_market_cap = df["market_cap"].sum()

#     # 🔢 คำนวณสัดส่วนของ market_cap
#     df["market_cap_percentage"] = df["market_cap"] / total_market_cap * 100

#     # 🔴 สีขึ้นอยู่กับ % การเปลี่ยนแปลงของราคา (หากมี)
#     color_column = "price_change_percent" if "price_change_percent" in df.columns else "market_cap"

#     # 🎨 สร้าง Treemap
#     fig = px.treemap(df, 
#                      path=['coin'],  
#                      values='market_cap',  
#                      color=color_column,  
#                      hover_data=['price', 'market_cap_percentage', 'total_volume'],
#                      color_continuous_scale='RdYlGn',
#                      title=f"🔷 MarketCap Treemap - {selected_date}")

#     # ✨ เปิดให้เลื่อนเข้า-ออกด้วย Scroll Mouse
#     fig.update_layout(
#         margin=dict(t=50, l=25, r=25, b=25),  # ปรับระยะขอบ
#         dragmode="zoom",  # เปิดให้ใช้เมาส์ซูมเข้าออก
#     )

#     fig.update_traces(textinfo="label+value+percent entry")  # แสดงชื่อ, market_cap, และ %

#     # 📌 แสดงผลใน Streamlit
#     st.plotly_chart(fig, use_container_width=True)


import streamlit as st
import pandas as pd
import plotly.express as px
import glob
import os

# 📂 โฟลเดอร์ที่เก็บไฟล์ CSV
data_folder = "top200_by_date"

# 🔍 ค้นหาไฟล์ CSV และดึงวันที่ออกมา
csv_files = glob.glob(os.path.join(data_folder, "*.csv"))
available_dates = sorted([os.path.basename(f).replace("_top200.csv", "") for f in csv_files])

# 🎨 ตั้งค่า Streamlit UI
st.title("📊 Crypto MarketCap Treemap")
st.write("เลือกวันที่เพื่อดู MarketCap ของ 200 เหรียญที่ใหญ่ที่สุด")

# 📅 Dropdown ให้ผู้ใช้เลือกวันที่
selected_date = st.selectbox("เลือกวันที่", available_dates)

# 📖 โหลดข้อมูลของวันที่ที่เลือก
if selected_date:
    file_path = os.path.join(data_folder, f"{selected_date}_top200.csv")
    df = pd.read_csv(file_path)

    # 🔢 แปลง market_cap เป็นตัวเลข
    df["market_cap"] = pd.to_numeric(df["market_cap"], errors='coerce')

    # 🧹 ลบค่า NaN และค่า market_cap ที่เป็น 0
    df = df.dropna(subset=["market_cap"])
    df = df[df["market_cap"] > 0]

    # 🔄 รวม market_cap ทั้งหมดของวันนั้น
    total_market_cap = df["market_cap"].sum()

    # 🔢 คำนวณสัดส่วนของ market_cap
    df["market_cap_percentage"] = df["market_cap"] / total_market_cap * 100

    # 🔴 สีขึ้นอยู่กับ % การเปลี่ยนแปลงของราคา (หากมี)
    color_column = "price_change_percent" if "price_change_percent" in df.columns else "market_cap"

    # 🎨 สร้าง Treemap
    fig = px.treemap(df, 
                     path=['coin'],  
                     values='market_cap',  
                     color=color_column,  
                     hover_data=['price', 'market_cap_percentage', 'total_volume'],
                     color_continuous_scale='RdYlGn',
                     title=f"🔷 MarketCap Treemap - {selected_date}")

    # ✨ เปิดให้เลื่อนเข้า-ออกด้วย Scroll Mouse
    fig.update_layout(
        margin=dict(t=50, l=25, r=25, b=25),  # ปรับระยะขอบ
        dragmode="zoom",  # เปิดให้ใช้เมาส์ซูมเข้าออก
    )

    fig.update_traces(textinfo="label+value+percent entry")  # แสดงชื่อ, market_cap, และ %

    # 📌 แสดงผลใน Streamlit (เปิด scrollZoom)
    st.plotly_chart(fig, use_container_width=True, config={"scrollZoom": True})
