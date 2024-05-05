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

st.title("_SEMI :blue[Seismic Protection Analysis]_:+1:")

#基本訊息
st.header("Basic Information")

#SF of EQ
SF=8
st.write()
st.write(f":red[{SF_t}]",":blue[：Safety Factor of anchor bolt=]",SF)
st.write("")

#SDS, SDsS, Fa
#st.write(SDS_t, str(","), SDsS_t, str(","), Fa_t, str(":"))
st.write(f":red[{SDS_t}]", ":blue[：Spectral response acceleration parameter at short periods.]")
st.write(f":red[{SDsS_t}]", ":blue[：Design horizontal response acceleration coefficients.]")
st.write(f":red[{Fa_t}]", ":blue[：Amplification factor.]")
SDsS, Fa=TW.Area_eng()
SDS=round(SDsS*Fa,2)
st.write(SDsS_t, str("="), SDsS)
st.write(Fa_t, str("="), Fa)
st.write(SDS_t, str("="), SDsS_t, str("*"), Fa_t, str("="), SDS)
st.write("")

#ap
#st.write(ap_t, str("=Component amplification factor:"))
st.write(f":red[{ap_t}]", ":blue[：Component amplification factor:]")
ap_option=st.selectbox("Choose an answer:",
                      ["Generally process equipment. (ap=1.0)",
                       "Flexible equipment (ap=2.5)"]
                      )
if ap_option=="Generally process equipment. (ap=1.0)":
    ap=1.0
else:
    ap=2.5
st.write(ap_t, str("="), ap)
st.write("")

#Ip
st.write(f":red[{Ip_t}]", ":blue[：Component importance factor:]")
Ip_option=st.selectbox("Choose an answer:",
                 ["Life safety related equipment or equipment with toxic or flammable materials. (Ip=1.5)",
                  "Others (Ip=1.0)"]
                 )
if ap_option=="Others (Ip=1.0)":
    Ip=1.0
else:
    Ip=1.5
st.write(Ip_t, str("="), Ip)
st.write("")

#Rpa
#st.write(Rpa_t, str(","), Rp_t, str(":"))
st.write(f":red[{Rpa_t}]", ":blue[：Allowable seismic response reduction factor.]")
st.write(f":red[{Rp_t}]", ":blue[：for general process equipment = 2.5]")
Rp=2.5
Rpa=1+(Rp-1)/1.5
st.write(Rpa_t+str(" = 1+(")+Rp_t+str("-1)/1.5 = "),Rpa)
st.write("")

#hx, hn

#st.write(hn_t, str(","), hx_t, str(":"))
st.write(f":red[{hx_t}]" + ":blue[：Distance between the foundation and the floor.]")
st.write(f":red[{hn_t}]" + ":blue[：Distance between the foundation and the roof.]")
hn=0
hx=0
hn=st.text_input("Input architectural height",0)
hx=st.text_input("Input storey height",0)
hx=float(hx)
hn=float(hn)
#if hn!=0:
    #st.write(hx/hn)
st.write("")

#Screw
st.subheader(":red[Anchor Bolt]")
bolt_t, bolt_s=screw.Screw_eng()
st.write("")

#Table Key Variables
#st.write("Table R4-3 Key Variables")
st.subheader(":red[Device parameters]")
st.write("Input Key Values of ","Wp", ", Z", ", L", ", X", ", N")
Wp_note="The maximum normal operating weight of the equipment."
G_note="The center of gravity of the equipment."
Z_note="The height of the center of gravity."
L_note="The shortest distance from a row of anchor bolts to the horizontal position of G."
X_note="The distance between the two rows of n anchor bolts (= L + L’)."
N_note="The total number of anchor bolts."
n_note="The total number of anchor bolts on one side of the equipment."


r4_3=pd.DataFrame({
                  "Variable":["Wp",   "G",           "Z",    "L",    "X",    "N",    "n"],
                  "Notes"   :[Wp_note, G_note,        Z_note, L_note, X_note, N_note, n_note],
                  "Values"  :["0",    "As indicated", "0",    "0",    "0",    "0",   "0"],
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

st.subheader(":red[Solve]")
Fph_note="The maximum anticipated seismic horizontal force acting on the equipment."
Fpv_note="The vertical seismic force by which the weight is reduced to determine effective weight used for overturning calculations."
WE_note="The effective weight of the equipment accounting for the vertical seismic force (Wp – Fv)."
R_note="The tensile force on an anchor bolt."
r_note="The lateral force on an anchor bolt."

r4_3_2=pd.DataFrame({
                     "Variable":["Fph",   "Fpv",    "WE",    "R",    "r"],
                     "Notes"   :[Fph_note, Fpv_note, WE_note, R_note, r_note],
                     "Values"  :["to be calculated", "to be calculated", 
                                 "to be calculated", "to be calculated",
                                 "to be calculated"],
                     "units"   :["kg",    "kg",     "kg",   "kg",   "kg",]
                     })

st.dataframe(r4_3_2, hide_index=True)

#示意圖
fig=st.file_uploader("Upload Schematic")
if st.button("Apply"):
    fig1=fig
else:
    fig1="fig1.png"
col1, col2, col3 = st.columns(3)
with col1:
    st.image(fig1)
with col2:
    st.image("fig2.png")
with col3:
    st.image("fig3.png")
st.write("")

#計算
if st.button("Calculate", type="primary"):
    #ΣM
    st.write(str("ΣM = ( ") + Fph_t + str(" x Z ) - ( R x X x n ) - ( ") + WE_t + str(" x L ) = 0"))

    try:
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
        R   = round(((Fph*Z)-(WE*L))/(X*n), 3)
        r   = round(Fph/n, 3)
        RSF = round(bolt_t/R, 2)
        rSF = round(bolt_s/r, 2)
        
        st.subheader(":blue[Calculation of Overturning Force]")
        st.write(str("R = [ ( ") + Fph_t + str(" x Z ) - (")+ WE_t + str(" x L ) ] / ( X x n) = "), R, str(" [kg]"))
        if R>=0 and RSF>=SF:
            st.write(str("SF of R = "), RSF)
            st.write("Tensile stress on the anchor bolts")
            st.write(":blue[_Safety factor is adequate._]:ok:")
        elif R>=0 and RSF<=SF:
            st.write(str("SF of R = "), RSF)
            st.write("Tensile stress on the anchor bolts")
            st.write(":red[_Safety factor is inadequate._]:x:")
        elif R<=0:
            st.write(str("SF of R >= "), SF)
            st.write("The screw is not stressed")
        st.write("")
        
        st.subheader(":blue[Calculation of Lateral Force]")
        st.write(str("r = ") + Fph_t + str(" / n = "), r, str(" [kg]"))
        st.write(str("SF of r = "), rSF)
        if rSF>=SF:
            st.write(":blue[_Safety factor is adequate._]:ok:")
        else:
            st.write(":red[_Safety factor is inadequate._]:x:")
    except Exception as e:
        st.write(e)
    st.write("")
    
st.subheader(":black[References]")
st.link_button("[1] Background Statement for SEMI Draft Document 5556B","http://downloads.semi.org/web/wstdsbal.nsf/de4d7939711aeedf8825753e0078317f/ddb843853af6b91788257f9c002f7d25/$FILE/5556B.pdf")
st.link_button("[2] 建築物耐震設計規範及解說部分規定修正規定","https://gazette.nat.gov.tw/EG_FileManager/eguploadpub/eg028109/ch02/type2/gov10/num4/images/Eg01.pdf")
st.write("")
st.write(":orange[SEMI Seismic Protection Analysis PROG_ver.1]")
#"Summary"