# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import TW
import screw

#Tag
Fph_t  = r'''$\textsf{\normalsize F\footnotesize ph}$'''
SDS_t  = r'''$\textsf{\normalsize S\footnotesize DS}$'''
ap_t   = r'''$\textsf{\normalsize a\footnotesize p}$'''
Rpa_t  = r'''$\textsf{\normalsize R\footnotesize pa}$'''
Ip_t   = r'''$\textsf{\normalsize I\footnotesize p}$'''
Wp_t   = r'''$\textsf{\normalsize W\footnotesize p}$'''
WE_t   = r'''$\textsf{\normalsize W\footnotesize E}$'''
hx_t   = r'''$\textsf{\normalsize h\footnotesize x}$'''
hn_t   = r'''$\textsf{\normalsize h\footnotesize n}$'''
SDsS_t = r'''$\textsf{\normalsize S\footnotesize D/S}$''' #S D/S
Fa_t   = r'''$\textsf{\normalsize F\footnotesize a}$'''
Rp_t   = r'''$\textsf{\normalsize R\footnotesize p}$'''
Fpv_t  = r'''$\textsf{\normalsize F\footnotesize pv}$'''
SF_t  = r'''$\textsf{\normalsize S\normalsize F}$'''

st.title("_SEMI :blue[地震力作用於設備分析]_:+1:")

#基本訊息
st.header("基本信息")

#SF of EQ
SF=8
st.write()
st.write(f":red[{SF_t}]",":blue[：地腳螺絲強度目標安全係數 = ]",SF)
st.write("")

#SDS, SDsS, Fa
#st.write(SDS_t, str(","), SDsS_t, str(","), Fa_t, str(":"))
st.write(f":red[{SDS_t}]", ":blue[：設計水平譜加速度(參考地區對照表)。]")
st.write(f":red[{SDsS_t}]", ":blue[：水平譜加速度係數。]")
st.write(f":red[{Fa_t}]", ":blue[：場地響應加速度譜放大係數。]")
SDsS, Fa=TW.Area_cht()
SDS=round(SDsS*Fa,2)
st.write(SDsS_t, str("="), SDsS)
st.write(Fa_t, str("="), Fa)
st.write(SDS_t, str("="), SDsS_t, str("*"), Fa_t, str("="), SDS)

st.write("")

#ap
#st.write(ap_t, str("=Component amplification factor:"))
st.write(f":red[{ap_t}]", ":blue[：設備共振放大係數:]")
ap_option=st.selectbox("請選擇用途：",
                      ["製程設備 (ap=1.0)",
                       "傳輸設備 (ap=2.5)"]
                      )
if ap_option=="製程設備 (ap=1.0)":
    ap=1.0
else:
    ap=2.5
st.write(ap_t, str("="), ap)
st.write("")

#Ip
st.write(f":red[{Ip_t}]", ":blue[：用途係數]")
Ip_option=st.selectbox("請選擇用途：",
                 ["危害用途 (Ip=1.5)",
                  "非危害用途 (Ip=1.0)"]
                 )
if ap_option=="Others (Ip=1.0)":
    Ip=1.0
else:
    Ip=1.5
st.write(Ip_t, str("="), Ip)
st.write("")

#Rpa
#st.write(Rpa_t, str(","), Rp_t, str(":"))
st.write(f":red[{Rpa_t}]", ":blue[：設備容許地震反應折減係數。]")
st.write(f":red[{Rp_t}]", ":blue[：生產設備 ( = 2.5)]")
Rp=2.5
Rpa=1+(Rp-1)/1.5
st.write(Rpa_t+str(" = 1+(")+Rp_t+str("-1)/1.5 = "),Rpa)
st.write("")

#hx, hn

#st.write(hn_t, str(","), hx_t, str(":"))
st.write(f":red[{hn_t}]" + ":blue[：建築物總樓高。]")
st.write(f":red[{hx_t}]" + ":blue[：建築物樓層高。.]")
hn=0
hx=0
hn=st.text_input("請輸入總樓高 [m]：",0)
hx=st.text_input("請輸入樓層高 [m]：",0)
hn=float(hn)
hx=float(hx)

#if hn!=0:
    #st.write(hx/hn)
st.write("")

#Screw
st.subheader(":black[地腳螺絲]")
bolt_t, bolt_s=screw.Screw_cht()
st.write("")

#Table Key Variables
#st.write("Table R4-3 Key Variables")
st.subheader(":black[設備參數]")
st.write("請輸入下列參數的數值：","Wp", ", Z", ", L", ", X", ", N")
Wp_note="設備重量。"
G_note="設備重心。"
Z_note="地板至重心高度。"
L_note="地腳螺絲至重心的最短距離。"
X_note="地腳螺絲之間的距離 (= L + L’)。"
N_note="地腳螺絲的總數。"
n_note="設備單側地腳螺絲的數量"


r4_3=pd.DataFrame({
                  "Variable":["Wp",   "G",           "Z",    "L",    "X",    "N",    "n"],
                  "Notes"   :[Wp_note, G_note,        Z_note, L_note, X_note, N_note, n_note],
                  "Values"  :["0",    "如圖所示", "0",    "0",    "0",    "0",   "0"],
                  "units"   :["kg",   "N/A",          "mm",   "mm",   "mm",   "pcs", "pcs"]
                  })

R4_3=st.data_editor(r4_3, hide_index=True)#,width=2500)

#if st.button("Apply", type="primary"):
Wp= float(R4_3["Values"].values.tolist()[0])
Z = float(R4_3["Values"].values.tolist()[2])
L = float(R4_3["Values"].values.tolist()[3])
X = float(R4_3["Values"].values.tolist()[4])
N = float(R4_3["Values"].values.tolist()[5])
n = float(R4_3["Values"].values.tolist()[6])
st.write("")

st.subheader(":black[求解下列參數]")
Fph_note="水平地震力。"
Fpv_note="垂直地震力。"
WE_note="作用在設備上的有效重量 (Wp – Fv)."
R_note="地腳螺絲的拉伸力。"
r_note="地腳螺栓上的側向力。"

r4_3_2=pd.DataFrame({
                     "Variable":["Fph",   "Fpv",    "WE",    "R",    "r"],
                     "Notes"   :[Fph_note, Fpv_note, WE_note, R_note, r_note],
                     "Values"  :["待計算", "待計算", 
                                 "待計算", "待計算",
                                 "待計算"],
                     "units"   :["kg",    "kg",     "kg",   "kg",   "kg",]
                     })

st.dataframe(r4_3_2, hide_index=True)

#示意圖

fig1="fig1.png" 
on = st.toggle("變更示意圖")
if on:
    fig1=st.file_uploader("上傳示意圖")
    if fig1==None:
        fig1="fig1.png"

col1, col2, col3 = st.columns(3)
with col1:      
    st.image(fig1)
with col2:
    st.image("fig2.png")
with col3:
    st.image("fig3.png")
st.write("")


if st.button("計算結果", type="primary"):
    #ERROR CODE
    if SDS<=0:
        st.write(":red[Error：SDS 必須 > 0。]")
    if hn<=0:
        st.write(":red[Error：hn 總樓高，必須 > 0。]")
    if hx<=0 or hx>hn:
        st.write(":red[Error：hx 樓層高，必須 > 0、hx =< hn。]")
    if Wp<=0:
        st.write(":red[Error：Wp 機台重量，必須 > 0。]")
    if Z<0:
        st.write(":red[Error：Z 地板至重心高度，必須 >= 0。]")
    if L<=0 or L>X:
        st.write(":red[Error：L 距離，必須 >= 0 & 必須 <= X。]")
    if X<=0:
        st.write(":red[Error：X 距離，必須 >= 0。]")
    if N<0 or n<0:
        st.write(":red[Error：N、n 地腳螺絲，必須 >= 0。]")
    
    #計算
    if SDS>0 and hn>0 and hx>0 and hx<=hn and Wp>0 and Z>=0 and L>0 and X>0 and N>=0 and n>=0:
        #ΣM
        st.write(str("ΣM = ( ") + Fph_t + str(" x Z ) - ( R x X x n ) - ( ") + WE_t + str(" x L ) = 0"))
    
        #Fph
        Fph    = round(0.4*SDS*Ip*(ap/Rpa)*(1+2*hx/hn)*Wp, 3)
        Fphmax = round(1.6*SDS*Ip*Wp, 3)
        Fphmin = round(0.3*SDS*Ip*Wp, 3)
    
        if Fph>Fphmax:
            Fph=Fphmax
            st.write(Fph_t+str(" = 1.6 x ")+SDS_t+str(" x ")+Ip_t+str(" x ")+Wp_t+str(" = "), Fph, str(" kg"))           
        elif Fph<Fphmin:
            Fph=Fphmin
            st.write(Fph_t+str(" = 0.3 x ")+SDS_t+str(" x ")+Ip_t+str(" x ")+Wp_t+str(" = "), Fph, str(" kg"))
            
        else:
            st.write(Fph_t + str(" = 0.4 x ") + SDS_t + str(" x ") + Ip_t
                     + str(" x (") + ap_t + str(" / ") + Rpa_t + str(") x (1 + 2 x ")
                     + hx_t + str(" / ") + hn_t + str(") x ") + Wp_t+str(" = "), Fph, str(" [kg]"))
        #Fpv
        Fpv = round(Fph * 2/3, 3)
        st.write(Fpv_t + str(" = ") + Fph_t + str(" x 2 / 3 = "), Fpv, str(" [kg]"))
        
        #WE
        WE = round(Fpv - Wp, 3)
        st.write(WE_t + str(" = ") + Fpv_t + str(" - ")+ Wp_t + str(" = "), WE, str(" [kg]"))
        st.write("")
        
        #R、r
        if n>0:
            R   = round(((Fph*Z)-(WE*L))/(X*n), 3)
            r   = round(Fph/n, 3)
            RSF = round(bolt_t/R, 2)
            rSF = round(bolt_s/r, 2)
            
            st.subheader(":blue[:u6709:地腳螺絲 - 傾倒力計算]")
            st.write(str("R = [ ( ") + Fph_t + str(" x Z ) - (")+ WE_t + str(" x L ) ] / ( X x n) = "), R, str(" [kg]"))
            if R>=0 and RSF>=SF:
                st.write(str("SF of R = "), RSF)
                st.write(":arrow_right: 地腳螺絲承受張力！")
                st.write(":blue[_安全係數：_]:ok:")
            elif R>=0 and RSF<=SF:
                st.write(str("SF of R = "), RSF)
                st.write(":arrow_right: 地腳螺絲承受張力！")
                st.write(":red[_安全係數不足：_]:x:")
            elif R<=0:
                st.write(str("SF of R >= "), SF)
                st.write(":arrow_right: 地腳螺絲不受力！")
            st.write("")
            
            st.subheader(":blue[:u6709:地腳螺絲 - 側向剪力計算]")
            st.write(str("r = ") + Fph_t + str(" / n = "), r, str(" [kg]"))
            st.write(str("SF of r = "), rSF)
            if rSF>=SF:
                st.write(":blue[_安全係數：_]:ok:")
            else:
                st.write(":red[_安全係數不足：_]:x:")
        elif n==0:
            st.subheader(":blue[:u7121:地腳螺絲]")
            st.write("R = 0 & r = 0")
            if Fph*Z >= WE*L:
               st.write(str("( ") + Fph_t + str(" x Z ) >= (")+ WE_t + str(" x L )"))
               st.write("設備:u6709:傾倒風險！ :ng: :x:")
            elif Fph*Z < WE*L:
               st.write(str("( ") + Fph_t + str(" x Z ) =< (")+ WE_t + str(" x L )"))
               st.write("設備:u7121:傾倒風險！ :ok:")
    st.write("")
    
st.subheader(":black[References]")
st.link_button("[1] Background Statement for SEMI Draft Document 5556B","http://downloads.semi.org/web/wstdsbal.nsf/de4d7939711aeedf8825753e0078317f/ddb843853af6b91788257f9c002f7d25/$FILE/5556B.pdf")
st.link_button("[2] 建築物耐震設計規範及解說部分規定修正規定","https://gazette.nat.gov.tw/EG_FileManager/eguploadpub/eg028109/ch02/type2/gov10/num4/images/Eg01.pdf")
st.write("")
st.write(":orange[SEMI Seismic Protection Analysis PROG_ver.1.1]")
st.write(":orange[Design by HSIAO, YC]")
#"Summary"