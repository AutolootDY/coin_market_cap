
```markdown
# Crypto MarketCap Treemap

## 🎯 วัตถุประสงค์
แอปนี้ถูกพัฒนาเพื่อแสดงข้อมูลของ 200 เหรียญที่ใหญ่ที่สุดในตลาดคริปโตเคอเรนซี โดยใช้ **Plotly Treemap** เพื่อแสดงขนาดของ **MarketCap** ของแต่ละเหรียญในรูปแบบที่เข้าใจง่าย พร้อมทั้งให้ผู้ใช้สามารถเลือกดูข้อมูลของเหรียญในแต่ละวันที่ต้องการ รวมถึงสามารถดาวน์โหลดไฟล์ CSV ของข้อมูลในวันนั้นๆ

## 📊 คุณสมบัติ
- เลือกวันที่เพื่อดูข้อมูล **MarketCap** ของ 200 เหรียญที่ใหญ่ที่สุด
- แสดงข้อมูลในรูปแบบ **Treemap** โดยมีขนาดของแต่ละบล็อกตาม **MarketCap** ของเหรียญ
- แสดงข้อมูลเพิ่มเติม เช่น **ราคา**, **ปริมาณการซื้อขาย**, **สัดส่วน MarketCap**
- สามารถเลือกจำนวนเหรียญที่ต้องการดู (Top 50 หรือ 100)
- ดาวน์โหลดข้อมูลในรูปแบบ **CSV** ของวันนั้นๆ

## 📥 การติดตั้งและใช้งาน
หากคุณต้องการใช้งานแอปนี้ในเครื่องของคุณเอง สามารถทำตามขั้นตอนดังนี้:

### 1. ติดตั้ง Dependencies
```bash
pip install streamlit pandas plotly
```

### 2. รันแอป
ในโฟลเดอร์โปรเจคให้รันคำสั่งนี้:
```bash
streamlit run app.py
```

### 3. โฟลเดอร์ที่เก็บไฟล์ CSV
โปรเจคนี้คาดว่าจะมีไฟล์ **CSV** ที่เก็บข้อมูลตลาดคริปโตในแต่ละวัน โดยไฟล์จะถูกเก็บในโฟลเดอร์ `top200_by_date`. คุณสามารถดาวน์โหลดไฟล์ CSV จากแหล่งข้อมูลต่างๆ หรือใช้ข้อมูลที่ได้จากการรวบรวมข้อมูลของคุณเอง

## 📅 ตัวอย่างการแสดงผล
เมื่อผู้ใช้เลือกวันที่ที่ต้องการดู:
- **Treemap** จะแสดงขนาดของ **MarketCap** ของแต่ละเหรียญในวันนั้นๆ
- ผู้ใช้สามารถเลือกดูข้อมูล **Top 50 หรือ 100 เหรียญ**
- **ปุ่มดาวน์โหลด** ไฟล์ CSV ของวันนั้นๆ จะถูกแสดงเพื่อให้ผู้ใช้สามารถดาวน์โหลดข้อมูลได้

## 🖥 ลิงก์ดูผลงาน
คุณสามารถดูผลงานของแอปที่ถูก Deploy ได้ที่ลิงก์นี้:  
[**Crypto MarketCap Treemap on Streamlit Cloud**](https://coinmarketcap-jq8d5jjfz7gwcffarrwras.streamlit.app](https://coinmarketcap-4femnmqcuz3nje9g3oryb7.streamlit.app/))

## 🎨 ความสามารถเพิ่มเติม
แอปนี้สามารถพัฒนาเพิ่มขึ้นได้ในอนาคต เช่น:
- การแสดงข้อมูลเพิ่มเติมเกี่ยวกับเหรียญแต่ละตัว
- การกรองข้อมูลโดยใช้เกณฑ์อื่นๆ เช่น **ราคา** หรือ **ปริมาณการซื้อขาย**
- การแสดงกราฟอื่นๆ เช่น **กราฟเส้น** หรือ **กราฟแท่ง** เพื่อแสดงข้อมูลย้อนหลังของเหรียญ

## 📑 License
โปรเจคนี้ใช้ **MIT License**.

```

### อธิบาย:
1. **เนื้อหาของ README**:
   - ส่วน **วัตถุประสงค์**: อธิบายจุดประสงค์หลักของแอป
   - ส่วน **คุณสมบัติ**: อธิบายฟีเจอร์หลักที่ผู้ใช้สามารถทำได้
   - ส่วน **การติดตั้งและใช้งาน**: ให้ขั้นตอนการติดตั้งและการรันแอป
   - ส่วน **ตัวอย่างการแสดงผล**: อธิบายเกี่ยวกับสิ่งที่ผู้ใช้จะเห็นเมื่อเลือกวันที่
   - ส่วน **ลิงก์ดูผลงาน**: ให้ลิงก์ที่ผู้ใช้งานสามารถเข้าไปดูแอปที่ deploy บน Streamlit Cloud
   - ส่วน **License**: ข้อมูลเกี่ยวกับการใช้งานซอฟต์แวร์ (ในที่นี้ใช้ MIT License)

คุณสามารถแก้ไขรายละเอียดเพิ่มเติมตามต้องการ เช่น ลิงก์การดูผลงานหรือการปรับแต่งคำอธิบายครับ!
