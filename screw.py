# -*- coding: utf-8 -*-
"""
選擇固定螺絲的強度
"""

import streamlit as st
import pandas as pd

#As=area mm^2
dfb=pd.DataFrame({
                  "bolt":["M3",  "M4",  "M5",  "M6",  "M8",  "M10", "M12",
                          "M14", "M16", "M18", "M20", "M22", "M24"],
                  "As"  :[5.03,  8.78,  14.2,  20.1,  36.6,  58,    84.3,
                          115,   157,   192,   245,   303,   353]
                  })

#[tensile strength, shear strength]
df=pd.DataFrame({
                 "12.9":[1220, 517],
                 "10.9":[1040, 428],
                 "8.8": [800, 348],
                 })

bolt=dfb["bolt"].values.tolist()
#print(screw_t)
grade=list(df.columns)
#print(grade)

def Screw_eng():
    Bolt=st.selectbox("Select Screw:", bolt)
    Grade=st.selectbox("Select Screw Grade:", grade)
    
    n=bolt.index(Bolt)  #n為list，尋找資料位置
    yl=round(df[Grade].values.tolist()[0]*dfb["As"].values.tolist()[n]*float(Grade[len(Grade)-1])/10/9.81, 3)
    st.write("Yield load of screw=",yl,str(" [kgf]"))    
    
    sf=round(df[Grade].values.tolist()[1]*dfb["As"].values.tolist()[n]*float(Grade[len(Grade)-1])/10/9.81, 3)
    st.write("Shear Force of screw=",sf,str(" [kgf]"))
    return yl, sf

def Screw_cht():
    Bolt=st.selectbox("請選擇螺絲尺寸：", bolt)
    Grade=st.selectbox("請選擇螺絲等級：", grade)
    
    n=bolt.index(Bolt)  #n為list，尋找資料位置
    yl=round(df[Grade].values.tolist()[0]*dfb["As"].values.tolist()[n]*float(Grade[len(Grade)-1])/10/9.81, 3)
    st.write("螺絲降伏強度 = ",yl,str(" [kgf]"))    
    
    sf=round(df[Grade].values.tolist()[1]*dfb["As"].values.tolist()[n]*float(Grade[len(Grade)-1])/10/9.81, 3)
    st.write("螺絲剪力強度 = ",sf,str(" [kgf]"))
    return yl, sf
#yl, sf = Screw()
    