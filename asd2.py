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

# #     # 🧹 ลบค่า NaN และค่า market_cap ที่เป็น 0
# #     df = df.dropna(subset=["market_cap"])
# #     df = df[df["market_cap"] > 0]

# #     # 🔄 รวม market_cap ทั้งหมดของวันนั้น
# #     total_market_cap = df["market_cap"].sum()

# #     # 🔢 คำนวณสัดส่วนของ market_cap
# #     df["market_cap_percentage"] = df["market_cap"] / total_market_cap * 100

# #     # 🔴 สีขึ้นอยู่กับ % การเปลี่ยนแปลงของราคา (หากมี)
# #     color_column = "price_change_percent" if "price_change_percent" in df.columns else "market_cap"

# #     # 🎨 สร้าง Treemap
# #     fig = px.treemap(df, 
# #                      path=['coin'],  
# #                      values='market_cap',  
# #                      color=color_column,  
# #                      hover_data=['price', 'market_cap_percentage', 'total_volume'],
# #                      color_continuous_scale='RdYlGn',
# #                      title=f"🔷 MarketCap Treemap - {selected_date}")

# #     # ✨ เปิดให้ใช้ Scroll Mouse + ปรับ UI Modebar
# #     fig.update_layout(
# #         margin=dict(t=50, l=25, r=25, b=25),  # ปรับระยะขอบ
# #         dragmode="zoom",  # เปิดให้ใช้เมาส์ซูมเข้าออก
# #     )

# #     fig.update_traces(textinfo="label+value+percent entry")  # แสดงชื่อ, market_cap, และ %

# #     # 📌 แสดงผลใน Streamlit (เปิด scrollZoom และ modebar)
# #     st.plotly_chart(fig, use_container_width=True, config={
# #         "scrollZoom": True,  # เปิดให้ใช้ Scroll Mouse
# #         "displayModeBar": True,  # แสดง ModeBar เพื่อให้มีปุ่มซูม
# #         "modeBarButtonsToAdd": ["zoom", "pan", "resetScale"],  # เพิ่มปุ่มซูม/แพน
# #     })



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

#     # ✨ เปิดให้ใช้ Scroll Mouse + ปรับ UI Modebar
#     fig.update_layout(
#         margin=dict(t=50, l=25, r=25, b=25),
#         dragmode="zoom",
#     )

#     fig.update_traces(textinfo="label+value+percent entry")

#     # 📌 แสดง Treemap ใน Streamlit
#     st.plotly_chart(fig, use_container_width=True, config={
#         "scrollZoom": True,
#         "displayModeBar": True,
#         "modeBarButtonsToAdd": ["zoom", "pan", "resetScale"],
#     })

#     # 🎯 **เพิ่มข้อมูลสรุป**
#     st.subheader(f"📅 รายละเอียดข้อมูลวันที่ {selected_date}")
#     st.write(f"**💰 MarketCap รวม:** ${total_market_cap:,.2f}")

#     # 📊 **แสดงตารางข้อมูล (Top 10)**
#     st.subheader("📋 ข้อมูลเหรียญ (Top 10)")
#     st.dataframe(df[["coin", "market_cap", "price", "price_change_percent", "total_volume"]]
#                  .sort_values(by="market_cap", ascending=False)
#                  .head(10))


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

    # 🔢 แปลง market_cap และ price เป็นตัวเลข
    df["market_cap"] = pd.to_numeric(df["market_cap"], errors='coerce')
    df["price"] = pd.to_numeric(df["price"], errors='coerce')
    df["total_volume"] = pd.to_numeric(df["total_volume"], errors='coerce')

    # 🧹 ลบค่า NaN และ market_cap ที่เป็น 0
    df = df.dropna(subset=["market_cap", "price", "total_volume"])
    df = df[df["market_cap"] > 0]

    # 🔄 รวม market_cap ทั้งหมดของวันนั้น
    total_market_cap = df["market_cap"].sum()

    # 🔢 คำนวณสัดส่วนของ market_cap
    df["market_cap_percentage"] = df["market_cap"] / total_market_cap * 100

    # 🔴 ใช้ market_cap เป็นสีของ Treemap แทน
    color_column = "market_cap"

    # 🎨 สร้าง Treemap
    fig = px.treemap(df, 
                     path=['coin'],  
                     values='market_cap',  
                     color=color_column,  
                     hover_data=['price', 'market_cap_percentage', 'total_volume'],
                     color_continuous_scale='RdYlBu',
                     title=f"🔷 MarketCap Treemap - {selected_date}")

    # ✨ เปิดให้ใช้ Scroll Mouse + ปรับ UI Modebar
    fig.update_layout(
        margin=dict(t=50, l=25, r=25, b=25),
        dragmode="zoom",
    )

    fig.update_traces(textinfo="label+value+percent entry")

    # 📌 แสดง Treemap ใน Streamlit
    st.plotly_chart(fig, use_container_width=True, config={
        "scrollZoom": True,
        "displayModeBar": True,
        "modeBarButtonsToAdd": ["zoom", "pan", "resetScale"],
    })

    # 🎯 **เพิ่มข้อมูลสรุป**
    st.subheader(f"📅 รายละเอียดข้อมูลวันที่ {selected_date}")
    st.write(f"**💰 MarketCap รวม:** ${total_market_cap:,.2f}")

       # 📊 **ให้ผู้ใช้เลือก Top จำนวนที่จะแสดง**
    st.subheader("📋 ข้อมูลเหรียญ (Top)")
    top_options = [50, 100]  # ตัวเลือก 50 หรือ 100
    selected_top = st.selectbox("เลือกจำนวนเหรียญที่แสดง", top_options)

    # 📋 แสดงตารางข้อมูลตามจำนวนที่เลือก
    st.dataframe(df[["coin", "market_cap", "price", "total_volume"]]
                 .sort_values(by="market_cap", ascending=False)
                 .head(selected_top))

    
     # 📥 **เพิ่มปุ่มดาวน์โหลดไฟล์ CSV**
    st.subheader("🔽 ดาวน์โหลดข้อมูล CSV ของวันที่นี้")
    
    # สร้าง CSV ไฟล์ในหน่วยความจำ (ไม่ต้องบันทึกไฟล์บนดิสก์)
    csv = df.to_csv(index=False)
    st.download_button(
        label="ดาวน์โหลดไฟล์ CSV",
        data=csv,
        file_name=f"{selected_date}_top200.csv",
        mime="text/csv"
    )
