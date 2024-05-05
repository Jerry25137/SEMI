# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 22:44:18 2024

@author: Hsiao
"""
import streamlit as st

KeelungCity={"Zhongzheng Dist.":[0.6, 0.8], "Qi du Dist."     :[0.6, 0.8], "Nuannuan Dist.":[0.6, 0.8],
             "Renai Dist."     :[0.6, 0.8], "Zhongshan Dist.":[0.6, 0.8],  "Anle Dist."    :[0.6, 0.8],
             "Xinyi Dist."     :[0.6, 0.8]}
YilanCounty={"Sanxing Township" :[0.8, 0.9], "Datong Township"   :[0.8, 0.9], "Wujie Township":[0.8, 0.9],
             "Dongshan Township":[0.8, 0.9], "Zhuangwei Township":[0.8, 0.9], "Yilan City"    :[0.8, 0.9],
             "Nanao Township"   :[0.8, 1.0], "Yuanshan Township" :[0.8, 0.9], "Toucheng Town" :[0.8, 0.9],
             "Jiaoxi Township"  :[0.8, 0.9], "Luodong Town"      :[0.8, 0.9], "Suao Town"     :[0.8, 1.0]}
TaoyuanCounty={"Taoyuan City"    :[0.5, 0.8], "Luzhu Township"  :[0.5, 0.7], "Dayuan Township" :[0.5, 0.7],   
               "Guishan Township":[0.5, 0.7], "Guanyin Township":[0.5, 0.7], "Zhongli City"    :[0.6, 0.8],                 
               "Yangmei City"    :[0.6, 0.9], "Bade City"       :[0.6, 0.8], "Pingzhen City"   :[0.6, 0.8],
               "Xinwu Township"  :[0.6, 0.8], "Daxi Town"       :[0.7, 0.9], "Longtan Township":[0.7, 0.9],  
               "Fuxing Township" :[0.7, 0.9]}
HsinchuCounty={"Zhubei City"      :[0.7, 1.0], "Zhudong Town"     :[0.7, 1.0], "Xinpu Town"      :[0.7, 1.0],
               "Guanxi Town"      :[0.7, 1.0], "Hukou Township"   :[0.6, 0.9], "Xinfeng Township":[0.6, 0.9],
               "Xionglin Township":[0.7, 1.0], "Hengshan Township":[0.7, 1.0], "Beipu Township"  :[0.7, 1.0],
               "Baoshan Township" :[0.7, 1.0], "Emei Township"    :[0.8, 1.0], "Jianshi Township":[0.7, 0.9],
               "Wufeng Township"  :[0.7, 0.9]}
HsinchuCity={"Eastern Dist."     :[0.7, 1.0], "North Dist."        :[0.7, 1.0], "Xiangshan Dist."   :[0.7, 1.0]}
MiaoliCounty={"Miaoli City"     :[0.7, 0.9], "Yuanli Town"       :[0.7, 1.0], "Tongxiao Town"    :[0.7, 0.9],
              "Zhunan Town"     :[0.7, 1.0], "Toufen Town"       :[0.7, 1.0], "Houlong Town"     :[0.7, 0.9],
              "Zhuolan Town"    :[0.8, 1.0], "Dahu Township"     :[0.8, 1.0], "Gongguan Township":[0.8, 1.0],
              "Tongluo Township":[0.8, 1.0], "Nanzhuang Township":[0.8, 1.0], "Touwu Township"   :[0.8, 1.0],
              "Sanyi Township"  :[0.8, 1.0], "Xihu Township"     :[0.7, 0.9], "Zaoqiao Township" :[0.8, 1.0], 
              "Sanwan Township" :[0.8, 1.0], "Shitan Township"   :[0.8, 1.0], "Tai'an Township"  :[0.7, 0.9]}
TaichungCity={"Fengyuan Dist." :[0.8, 1.0], "Dongshi Dist.":[0.8, 1.0], "Dajia Dist."  :[0.7, 1.0],
              "Qingshui Dist.":[0.8, 1.0], "Shalu Dist."   :[0.8, 1.0], "Wuqi Dist."   :[0.7, 1.0],
              "Houli Dist."   :[0.8, 1.0], "Kamioka Dist." :[0.8, 1.0], "Tanzi Dist."  :[0.8, 1.0],
              "Daya Dist."    :[0.8, 1.0], "Xinshe Dist."  :[0.8, 1.0], "Shigang Dist.":[0.8, 1.0],
              "Waipu Dist."   :[0.7, 1.0], "Da'an Dist."   :[0.7, 1.0], "Wuri Dist."   :[0.7, 1.0],
              "Dadu Dist."    :[0.7, 1.0], "Longjing Dist.":[0.7, 1.0], "Wufeng Dist." :[0.8, 1.0],
              "Taiping Dist." :[0.8, 1.0], "Dali Dist."    :[0.8, 1.0], "Heping Dist." :[0.7, 1.0],
              "Central Dist." :[0.8, 1.0], "Eastern Dist." :[0.8, 1.0], "South Dist."  :[0.7, 1.0],
              "West Dist."    :[0.8, 1.0], "North Dist."   :[0.8, 1.0], "Xitun Dist."  :[0.7, 1.0],
              "Nantun Dist."  :[0.7, 1.0], "Beitun Dist."  :[0.8, 1.0]}
ChanghuaCounty={"Changhua City"    :[0.7, 0.9], "Lukang Town"      :[0.7, 0.9], "Hemei Town"      :[0.7, 0.9],
                "Xian Xixiang"     :[0.7, 0.9], "Shengang Township":[0.7, 0.9], "Fuxing Township" :[0.7, 0.9],
                "Xiushui Township" :[0.7, 0.9], "Huatan Township"  :[0.7, 0.9], "Fenyuan Township":[0.7, 0.9],
                "Yuanlin Town"     :[0.7, 0.9], "Xihu Town"        :[0.7, 0.9], "Tianzhong Town"  :[0.7, 0.9],
                "Dacun Township"   :[0.7, 0.9], "Puyan Township"   :[0.7, 0.9], "Puxin Township"  :[0.7, 0.9],
                "Yongjing Township":[0.7, 0.9], "Shetou Township"  :[0.7, 0.9], "Ershui Township" :[0.8, 1.0],
                "Beidou Town"      :[0.7, 0.9], "Erlin Town"       :[0.7, 0.9], "Tianwei Township":[0.7, 0.9],
                "Pitou Township"   :[0.7, 0.9], "Fangyuan Township":[0.7, 0.9], "Dacheng Township":[0.7, 0.9],
                "Zhutang Township" :[0.7, 0.9], "Xizhou Township"  :[0.7, 0.9]}
NantouCounty={"Nantou city"     :[0.8, 1.0], "Puli Town"         :[0.7, 0.9], "Caotun Town"      :[0.8, 1.0],
              "Zhushan Town"    :[0.8, 1.0], "Jiji Town"         :[0.8, 1.0], "Mingjian Township":[0.8, 1.0],
              "Lugu Township"   :[0.8, 1.0], "Zhongliao Township":[0.8, 1.0], "Yuchi Township"   :[0.7, 0.9],
              "Guoxing Township":[0.7, 0.9], "Shuili Township"   :[0.7, 0.9], "Xinyi Township"   :[0.7, 0.9],
              "Ren'ai Township" :[0.7, 0.9]}
YunlinCounty={"Douliu City"     :[0.8, 1.0], "Dounan Town"       :[0.7, 0.9], "Huwei Town"       :[0.7, 0.9],
              "Xiluo Town"      :[0.7, 0.9], "tuku Town"         :[0.7, 0.9], "Beigang Town"     :[0.7, 0.9],
              "Gukeng Township" :[0.8, 1.0], "Dapi Township"     :[0.7, 0.9], "Cihtong Township" :[0.7, 0.9],
              "Linnei Township" :[0.8, 1.0], "Erlun Township"    :[0.7, 0.9], "Lunbei Township"  :[0.7, 0.9],
              "Mailiao Township":[0.7, 0.9], "Dongshi Township"  :[0.7, 0.9], "Baozhong Township":[0.7, 0.9],
              "Taixi Township"  :[0.7, 0.9], "Yuanchang Township":[0.7, 0.9], "Sihu Township"    :[0.7, 0.9],
              "Kouhu Township"  :[0.7, 0.9], "Shuilin Township"  :[0.7, 0.9]}
ChiayiCounty={"Taibao City"     :[0.7, 0.9], "Puzi City"        :[0.7, 0.9], "Budai Town"       :[0.7, 0.9],
              "Dalin Town"      :[0.8, 1.0], "Minxiong Township":[0.8, 1.0], "Xikou Township"   :[0.8, 1.0],
              "Xingang Township":[0.7, 0.9], "Liujiao Township" :[0.7, 0.9], "Dongshi Township" :[0.7, 0.9],
              "Yizhu Township"  :[0.7, 0.9], "Lucao Township"   :[0.7, 0.9], "Shuishui Township":[0.7, 0.9],
              "Zhongpu Township":[0.8, 1.0], "Zhuqi Township"   :[0.8, 1.0], "Meishan Township" :[0.8, 1.0],
              "Fanlu Township"  :[0.8, 1.0], "Dabu Township"    :[0.8, 1.0], "Alishan Township" :[0.7, 0.9]}
ChiayiCity={"Eastern Dist.":[0.8, 1.0], "West Dist.":[0.7, 0.9]}
TainanCity={"Xinying Dist."  :[0.7, 0.9], "Yanshuei Dist.":[0.7, 0.9], "Baihe Dist."   :[0.8, 1.0],
            "Liuying Dist."  :[0.7, 0.9], "Houbi Dist."   :[0.7, 0.9], "Dongshan Dist.":[0.7, 0.9],
            "Madou Dist."    :[0.7, 0.9], "Xiaying Dist." :[0.7, 0.9], "Liujia Dist."  :[0.7, 0.9],
            "Guantian Dist." :[0.7, 0.9], "Ouchi Dist."   :[0.7, 0.9], "Jiali Dist."   :[0.7, 0.9],
            "Xuejia Dist."   :[0.7, 0.9], "Xigang Dist."  :[0.7, 0.9], "Qigu Dist."    :[0.7, 0.9],
            "Jiangjun Dist." :[0.7, 0.9], "Beimen Dist."  :[0.7, 0.9], "Xinhua Dist."  :[0.8, 1.0],
            "Shanhua Dist."  :[0.7, 0.9], "Sinshih Dist." :[0.8, 1.0], "Anding Dist."  :[0.7, 0.9],
            "Shanshang Dist.":[0.8, 1.0], "Yujing Dist."  :[0.7, 0.9], "Nanxi Dist."   :[0.7, 0.9],
            "Nanhua Dist."   :[0.7, 0.9], "Zuozhen Dist." :[0.8, 1.0], "Rende Dist."   :[0.7, 0.9],
            "Quy Nhon Dist." :[0.7, 0.9], "Guanmiao Dist.":[0.7, 0.9], "Longqi Dist."  :[0.7, 0.9],
            "Yongkang Dist." :[0.8, 1.0], "Eastern Dist." :[0.7, 0.9], "South Dist."   :[0.7, 0.9],
            "West Dist."     :[0.7, 0.9], "North Dist."   :[0.7, 0.9], "Central Dist." :[0.7, 0.9],
            "Annan Dist."    :[0.7, 0.9], "Anping Dist."  :[0.7, 0.9]}
KaohsiungCity={"Fengshan Dist.":[0.5, 0.7], "Linyuan Dist." :[0.5, 0.7], "Daliao Dist."  :[0.5, 0.7],
               "Dashu Dist."   :[0.6, 0.8], "Dashe Dist."   :[0.6, 0.8], "Renwu Dist."   :[0.6, 0.8],
               "Niaosong Dist.":[0.6, 0.8], "Okayama Dist." :[0.7, 0.9], "Qiaotou Dist." :[0.7, 0.9],
               "Yanchao Dist." :[0.7, 0.9], "Tianliao Dist.":[0.7, 0.9], "Alian Dist."   :[0.7, 0.9],
               "Luzhu Dist."   :[0.7, 0.9], "Hunei Dist."   :[0.7, 0.9], "Qieyu Dist."   :[0.7, 0.9],
               "Yong'an Dist." :[0.7, 0.9], "Amitabha Dist.":[0.7, 0.9], "Ziguan Dist."  :[0.7, 0.9],
               "Qishan Dist."  :[0.7, 0.9], "Meinong Dist." :[0.7, 0.9], "Liugui Dist."  :[0.7, 0.9],
               "Jiaxian Dist." :[0.7, 0.9], "Shanlin Dist." :[0.7, 0.9], "Neimen Dist."  :[0.7, 0.9],
               "Maolin Dist."  :[0.7, 0.9], "Taoyuan Dist." :[0.7, 0.9], "Namasya Dist." :[0.7, 0.9],
               "Yancheng Dist.":[0.6, 0.8], "Gushan Dist."  :[0.6, 0.8], "Zuoying Dist." :[0.6, 0.8],
               "Nanzi Dist."   :[0.6, 0.8], "Sanmin Dist."  :[0.6, 0.8], "Xinxing Dist." :[0.6, 0.8],
               "Qianjin Dist." :[0.6, 0.8], "Lingya Dist."  :[0.5, 0.7], "Qianzhen Dist.":[0.5, 0.7],
               "Cijin Dist."   :[0.5, 0.7], "Xiaogang Dist.":[0.5, 0.7]}
PingtungCounty={"Pingtung City"    :[0.6, 0.8], "Chaozhou Town"    :[0.6, 0.8], "Donggang Town"    :[0.5, 0.7],
                "Hengchun Town"    :[0.5, 0.7], "Wantan Township"  :[0.6, 0.8], "Changzhi Township":[0.7, 0.8],
                "Linluo Township"  :[0.7, 0.9], "Jiuru Township"   :[0.6, 0.8], "Ligang Township"  :[0.7, 0.9],
                "Yanpu Township"   :[0.6, 0.8], "Gaoshu Township"  :[0.7, 0.9], "Wanluan Township" :[0.6, 0.8],
                "Neipu Township"   :[0.6, 0.8], "Zhutian Township" :[0.6, 0.8], "Xinpi Township"   :[0.6, 0.7],
                "Fangliao Township":[0.5, 0.7], "Xinyuan Township" :[0.5, 0.7], "Kanding Township" :[0.5, 0.8],
                "Linbian Township" :[0.5, 0.7], "Nanzhou Township" :[0.5, 0.7], "Jiadong Township" :[0.5, 0.7],
                "Ryukyu Township"  :[0.5, 0.7], "Checheng Township":[0.5, 0.7], "Manzhou Township" :[0.5, 0.7],
                "Fangshan Township":[0.5, 0.7], "Sandimen Township":[0.7, 0.9], "Wutai Township"   :[0.7, 0.9],
                "Majia Township"   :[0.7, 0.9], "Taiwu Township"   :[0.7, 0.9], "Lai Yi Township"  :[0.6, 0.8],
                "Kasuga Township"  :[0.5, 0.7], "Shizi Township"   :[0.5, 0.7], "Mudan Township"   :[0.5, 0.7]}
PenghuCounty={"Magong City"  :[0.5, 0.7], "Huxi Township"   :[0.5, 0.7], "Baisha Township":[0.5, 0.7],
              "Xiyu Township":[0.5, 0.7], "Wang'an Township":[0.5, 0.7]}
TaitungCounty={"Taitung City"    :[0.8, 1.0], "Chenggong Town"       :[0.8, 1.0], "Guanshan Town"    :[0.8, 1.0],
               "Beinan Township" :[0.8, 1.0], "Luye Township"        :[0.8, 1.0], "Chishang Township":[0.8, 1.0],
               "Donghe Township" :[0.8, 1.0], "Changbin Township"    :[0.8, 1.0], "Taimali Township" :[0.7, 0.9],
               "Dawu Township"   :[0.6, 0.8], "Green Island Township":[0.8, 1.0], "Haiduan Township" :[0.8, 1.0],
               "Yanping Township":[0.8, 1.0], "Jinfeng Township"     :[0.7, 0.9], "Daren Township"   :[0.6, 0.8],
               "Lanyu Township"  :[0.8, 0.9]}
HualienCounty={"Hualien City"     :[0.8, 1.0], "Fenglin Town"    :[0.8, 1.0], "Yuli Town"        :[0.8, 1.0],
               "Xincheng Township":[0.8, 1.0], "Ji'an Township"  :[0.8, 1.0], "Shoufeng Township":[0.8, 1.0],
               "Guangfu Township" :[0.8, 1.0], "Fengbin Township":[0.8, 1.0], "Ruisui Township"  :[0.8, 1.0],
               "Fuli Township"    :[0.8, 1.0], "Xiulin Township" :[0.8, 1.0], "Wanrong Township" :[0.8, 1.0],
               "Zhuoxi Township"  :[0.8, 1.0]}
Kinmen_Matsu={"Kinmen & Matsu":[0.5, 0.7]}

dist_eng={"KeelungCity"   :KeelungCity,  "YilanCounty"   :YilanCounty,   "TaoyuanCounty"  :TaoyuanCounty,
          "Hsinchu County":HsinchuCounty,"HsinchuCity"   :HsinchuCity,    "MiaoliCounty"  :MiaoliCounty,
          "TaichungCity"  :TaichungCity, "ChanghuaCounty":ChanghuaCounty, "NantouCounty"  :NantouCounty, 
          "YunlinCounty"  :YunlinCounty, "ChiayiCounty"  :ChiayiCounty,   "ChiayiCity"    :ChiayiCity,
          "TainanCity"    :TainanCity,   "KaohsiungCity" :KaohsiungCity,  "PingtungCounty":PingtungCounty,
          "PenghuCounty"  :PenghuCounty, "TaitungCounty" :TaitungCounty,  "HualienCounty" :HualienCounty,
          "Kinmen_Matsu"  :Kinmen_Matsu}

基隆市={"中正區":[0.6, 0.8], "七堵區":[0.6, 0.8], "暖暖區":[0.6, 0.8],
        "仁愛區":[0.6, 0.8], "中山區":[0.6, 0.8], "安樂區":[0.6, 0.8],
        "信義區":[0.6, 0.8]}
宜蘭縣={"三星鄉":[0.8, 0.9], "大同鄉":[0.8, 0.9], "五結鄉":[0.8, 0.9],
        "冬山鄉":[0.8, 0.9], "壯圍鄉":[0.8, 0.9], "宜蘭市":[0.8, 0.9],
        "南澳鄉":[0.8, 1.0], "員山鄉":[0.8, 0.9], "頭城鎮":[0.8, 0.9],
        "礁溪鄉":[0.8, 0.9], "羅東鎮":[0.8, 0.9], "蘇澳鎮":[0.8, 1.0]}
桃園縣={"桃園市":[0.5, 0.8], "蘆竹鄉":[0.5, 0.7], "大園鄉":[0.5, 0.7],   
        "龜山鄉":[0.5, 0.7], "觀音鄉":[0.5, 0.7], "中壢市":[0.6, 0.8],                 
        "楊梅市":[0.6, 0.9], "八德市":[0.6, 0.8], "平鎮市":[0.6, 0.8],
        "新屋鄉":[0.6, 0.8], "大溪鎮":[0.7, 0.9], "龍潭鄉":[0.7, 0.9],  
        "復興鄉":[0.7, 0.9]}
新竹縣={"竹北市":[0.7, 1.0], "竹東鎮":[0.7, 1.0], "新埔鎮":[0.7, 1.0],
        "關西鎮":[0.7, 1.0], "湖口鄉":[0.6, 0.9], "新豐鄉":[0.6, 0.9],
        "芎林鄉":[0.7, 1.0], "橫山鄉":[0.7, 1.0], "北埔鄉":[0.7, 1.0],
        "寶山鄉":[0.7, 1.0], "峨眉鄉":[0.8, 1.0], "尖石鄉":[0.7, 0.9],
        "五峰鄉":[0.7, 0.9]}
新竹市={"東區":[0.7, 1.0],   "北區":[0.7, 1.0],   "香山區":[0.7, 1.0]}
苗栗縣={"苗栗市":[0.7, 0.9], "苑裡鎮":[0.7, 1.0], "通霄鎮":[0.7, 0.9],
        "竹南鎮":[0.7, 1.0], "頭份鎮":[0.7, 1.0], "後龍鎮":[0.7, 0.9],
        "卓蘭鎮":[0.8, 1.0], "大湖鄉":[0.8, 1.0], "公館鄉":[0.8, 1.0],
        "銅鑼鄉":[0.8, 1.0], "南庄鄉":[0.8, 1.0], "頭屋鄉":[0.8, 1.0],
        "三義鄉":[0.8, 1.0], "西湖鄉":[0.7, 0.9], "造橋鄉":[0.8, 1.0], 
        "三灣鄉":[0.8, 1.0], "獅潭鄉":[0.8, 1.0], "泰安鄉":[0.7, 0.9]}
臺中市={"豐原區":[0.8, 1.0], "東勢區":[0.8, 1.0], "大甲區":[0.7, 1.0],
        "清水區":[0.8, 1.0], "沙鹿區":[0.8, 1.0], "梧棲區":[0.7, 1.0],
        "后里區":[0.8, 1.0], "神岡區":[0.8, 1.0], "潭子區":[0.8, 1.0],
        "大雅區":[0.8, 1.0], "新社區":[0.8, 1.0], "石岡區":[0.8, 1.0],
        "外埔區":[0.7, 1.0], "大安區":[0.7, 1.0], "烏日區":[0.7, 1.0],
        "大肚區":[0.7, 1.0], "龍井區":[0.7, 1.0], "霧峰區":[0.8, 1.0],
        "太平區":[0.8, 1.0], "大里區":[0.8, 1.0], "和平區":[0.7, 1.0],
        "中區"  :[0.8, 1.0], "東區"  :[0.8, 1.0], "南區"  :[0.7, 1.0],
        "西區"  :[0.8, 1.0], "北區"  :[0.8, 1.0], "西屯區":[0.7, 1.0],
        "南屯區":[0.7, 1.0], "北屯區":[0.8, 1.0]}
彰化縣={"彰化市":[0.7, 0.9], "鹿港鎮":[0.7, 0.9], "和美鎮":[0.7, 0.9],
        "線西鄉":[0.7, 0.9], "伸港鄉":[0.7, 0.9], "福興鄉":[0.7, 0.9],
        "秀水鄉":[0.7, 0.9], "花壇鄉":[0.7, 0.9], "芬園鄉":[0.7, 0.9],
        "員林鎮":[0.7, 0.9], "溪湖鎮":[0.7, 0.9], "田中鎮":[0.7, 0.9],
        "大村鄉":[0.7, 0.9], "埔鹽鄉":[0.7, 0.9], "埔心鄉":[0.7, 0.9],
        "永靖鄉":[0.7, 0.9], "社頭鄉":[0.7, 0.9], "二水鄉":[0.8, 1.0],
        "北斗鎮":[0.7, 0.9], "二林鎮":[0.7, 0.9], "田尾鄉":[0.7, 0.9],
        "埤頭鄉":[0.7, 0.9], "芳苑鄉":[0.7, 0.9], "大城鄉":[0.7, 0.9],
        "竹塘鄉":[0.7, 0.9], "溪州鄉":[0.7, 0.9]}
南投縣={"南投市":[0.8, 1.0], "埔里鎮":[0.7, 0.9], "草屯鎮":[0.8, 1.0],
        "竹山鎮":[0.8, 1.0], "集集鎮":[0.8, 1.0], "名間鄉":[0.8, 1.0],
        "鹿谷鄉":[0.8, 1.0], "中寮鄉":[0.8, 1.0], "魚池鄉":[0.7, 0.9],
        "國姓鄉":[0.7, 0.9], "水里鄉":[0.7, 0.9], "信義鄉":[0.7, 0.9],
        "仁愛鄉":[0.7, 0.9]}
雲林縣={"斗六市":[0.8, 1.0], "斗南鎮":[0.7, 0.9], "虎尾鎮":[0.7, 0.9],
        "西螺鎮":[0.7, 0.9], "土庫鎮":[0.7, 0.9], "北港鎮":[0.7, 0.9],
        "古坑鄉":[0.8, 1.0], "大埤鄉":[0.7, 0.9], "莿桐鄉":[0.7, 0.9],
        "林內鄉":[0.8, 1.0], "二崙鄉":[0.7, 0.9], "崙背鄉":[0.7, 0.9],
        "麥寮鄉":[0.7, 0.9], "東勢鄉":[0.7, 0.9], "褒忠鄉":[0.7, 0.9],
        "臺西鄉":[0.7, 0.9], "元長鄉":[0.7, 0.9], "四湖鄉":[0.7, 0.9],
        "口湖鄉":[0.7, 0.9], "水林鄉":[0.7, 0.9]}
嘉義縣={"太保市":[0.7, 0.9], "朴子市":[0.7, 0.9], "布袋鎮":[0.7, 0.9],
        "大林鎮":[0.8, 1.0], "民雄鄉":[0.8, 1.0], "溪口鄉":[0.8, 1.0],
        "新港鄉":[0.7, 0.9], "六腳鄉":[0.7, 0.9], "東石鄉":[0.7, 0.9],
        "義竹鄉":[0.7, 0.9], "鹿草鄉":[0.7, 0.9], "水上鄉":[0.7, 0.9],
        "中埔鄉":[0.8, 1.0], "竹崎鄉":[0.8, 1.0], "梅山鄉":[0.8, 1.0],
        "番路鄉":[0.8, 1.0], "大埔鄉":[0.8, 1.0], "阿里山鄉":[0.7, 0.9]}
嘉義市={"東區":[0.8, 1.0], "西區":[0.7, 0.9]}
臺南市={"新營區":[0.7, 0.9], "鹽水區":[0.7, 0.9], "白河區":[0.8, 1.0],
        "柳營區":[0.7, 0.9], "後壁區":[0.7, 0.9], "東山區":[0.7, 0.9],
        "麻豆區":[0.7, 0.9], "下營區":[0.7, 0.9], "六甲區":[0.7, 0.9],
        "官田區":[0.7, 0.9], "大內區":[0.7, 0.9], "佳里區":[0.7, 0.9],
        "學甲區":[0.7, 0.9], "西港區":[0.7, 0.9], "七股區":[0.7, 0.9],
        "將軍區":[0.7, 0.9], "北門區":[0.7, 0.9], "新化區":[0.8, 1.0],
        "善化區":[0.7, 0.9], "新市區":[0.8, 1.0], "安定區":[0.7, 0.9],
        "山上區":[0.8, 1.0], "玉井區":[0.7, 0.9], "楠西區":[0.7, 0.9],
        "南化區":[0.7, 0.9], "左鎮區":[0.8, 1.0], "仁德區":[0.7, 0.9],
        "歸仁區":[0.7, 0.9], "關廟區":[0.7, 0.9], "龍崎區":[0.7, 0.9],
        "永康區":[0.8, 1.0], "東區"  :[0.7, 0.9], "南區"  :[0.7, 0.9],
        "西區"  :[0.7, 0.9], "北區"  :[0.7, 0.9], "中區"  :[0.7, 0.9],
        "安南區":[0.7, 0.9], "安平區":[0.7, 0.9]}
高雄市={"鳳山區":[0.5, 0.7], "林園區":[0.5, 0.7], "大寮區":[0.5, 0.7],
        "大樹區":[0.6, 0.8], "大社區":[0.6, 0.8], "仁武區":[0.6, 0.8],
        "鳥松區":[0.6, 0.8], "岡山區":[0.7, 0.9], "橋頭區":[0.7, 0.9],
        "燕巢區":[0.7, 0.9], "田寮區":[0.7, 0.9], "阿蓮區":[0.7, 0.9],
        "路竹區":[0.7, 0.9], "湖內區":[0.7, 0.9], "茄萣區":[0.7, 0.9],
        "永安區":[0.7, 0.9], "彌陀區":[0.7, 0.9], "梓官區":[0.7, 0.9],
        "旗山區":[0.7, 0.9], "美濃區":[0.7, 0.9], "六龜區":[0.7, 0.9],
        "甲仙區":[0.7, 0.9], "杉林區":[0.7, 0.9], "內門區":[0.7, 0.9],
        "茂林區":[0.7, 0.9], "桃源區":[0.7, 0.9], "那瑪夏區":[0.7, 0.9],
        "鹽埕區":[0.6, 0.8], "鼓山區":[0.6, 0.8], "左營區":[0.6, 0.8],
        "楠梓區":[0.6, 0.8], "三民區":[0.6, 0.8], "新興區":[0.6, 0.8],
        "前金區":[0.6, 0.8], "苓雅區":[0.5, 0.7], "前鎮區":[0.5, 0.7],
        "旗津區":[0.5, 0.7], "小港區":[0.5, 0.7]}
屏東縣={"屏東市":[0.6, 0.8], "潮州鎮":[0.6, 0.8], "東港鎮":[0.5, 0.7],
        "恆春鎮":[0.5, 0.7], "萬丹鄉":[0.6, 0.8], "長治鄉":[0.7, 0.8],
        "麟洛鄉":[0.7, 0.9], "九如鄉":[0.6, 0.8], "里港鄉":[0.7, 0.9],
        "鹽埔鄉":[0.6, 0.8], "高樹鄉":[0.7, 0.9], "萬巒鄉":[0.6, 0.8],
        "內埔鄉":[0.6, 0.8], "竹田鄉":[0.6, 0.8], "新埤鄉":[0.6, 0.7],
        "枋寮鄉":[0.5, 0.7], "新園鄉":[0.5, 0.7], "崁頂鄉":[0.5, 0.8],
        "林邊鄉":[0.5, 0.7], "南州鄉":[0.5, 0.7], "佳冬鄉":[0.5, 0.7],
        "琉球鄉":[0.5, 0.7], "車城鄉":[0.5, 0.7], "滿州鄉":[0.5, 0.7],
        "枋山鄉":[0.5, 0.7], "三地門鄉":[0.7, 0.9], "霧臺鄉":[0.7, 0.9],
        "瑪家鄉":[0.7, 0.9], "泰武鄉":[0.7, 0.9], "來義鄉":[0.6, 0.8],
        "春日鄉":[0.5, 0.7], "獅子鄉":[0.5, 0.7], "牡丹鄉":[0.5, 0.7]}
澎湖縣={"馬公市":[0.5, 0.7], "湖西鄉":[0.5, 0.7], "白沙鄉":[0.5, 0.7],
        "西嶼鄉":[0.5, 0.7], "望安鄉":[0.5, 0.7]}
臺東縣={"臺東市":[0.8, 1.0], "成功鎮":[0.8, 1.0], "關山鎮":[0.8, 1.0],
        "卑南鄉":[0.8, 1.0], "鹿野鄉":[0.8, 1.0], "池上鄉":[0.8, 1.0],
        "東河鄉":[0.8, 1.0], "長濱鄉":[0.8, 1.0], "太麻里鄉":[0.7, 0.9],
        "大武鄉":[0.6, 0.8], "綠島鄉":[0.8, 1.0], "海端鄉":[0.8, 1.0],
        "延平鄉":[0.8, 1.0], "金峰鄉":[0.7, 0.9], "達仁鄉":[0.6, 0.8],
        "蘭嶼鄉":[0.8, 0.9]}
花蓮縣={"花蓮市":[0.8, 1.0], "鳳林鎮":[0.8, 1.0], "玉里鎮":[0.8, 1.0],
        "新城鄉":[0.8, 1.0], "吉安鄉":[0.8, 1.0], "壽豐鄉":[0.8, 1.0],
        "光復鄉":[0.8, 1.0], "豐濱鄉":[0.8, 1.0], "瑞穗鄉":[0.8, 1.0],
        "富里鄉":[0.8, 1.0], "秀林鄉":[0.8, 1.0], "萬榮鄉":[0.8, 1.0],
        "卓溪鄉":[0.8, 1.0]}
金門與馬祖地區={"金門與馬祖地區":[0.5, 0.7]}

dist_cht={"基隆市":基隆市, "宜蘭縣":宜蘭縣, "桃園縣":桃園縣, "新竹縣":新竹縣,
          "新竹市":新竹市, "苗栗縣":苗栗縣, "臺中市":臺中市, "彰化縣":彰化縣, 
          "南投縣":南投縣, "雲林縣":雲林縣, "嘉義縣":嘉義縣, "嘉義市":嘉義市,
          "臺南市":臺南市, "高雄市":高雄市, "屏東縣":屏東縣, "澎湖縣":澎湖縣,
          "臺東縣":臺東縣, "花蓮縣":花蓮縣, "金門與馬祖地區":金門與馬祖地區}

def Area_eng():
    SDsS=float(0)
    Fa=float(0)
    A=[]
    D=[]
    for i in dist_eng.keys():
        A.append(i)
    area=st.selectbox("Select city:",
                 A,
                 index=None
                 )
    if area!=None:
        for i in dist_eng[area]:
            D.append(i)
        dist=st.selectbox("Select district:",
                     D,
                     index=None
                     )
        if dist!=None:
            SDsS=dist_eng[area][dist][0]
            Fa=dist_eng[area][dist][1]
            #st.write(SDsS,Fa)
    return SDsS, Fa

def Area_cht():
    SDsS=float(0)
    Fa=float(0)
    A=[]
    D=[]
    for i in dist_cht.keys():
        A.append(i)
    area=st.selectbox("Select city:",
                 A,
                 index=None
                 )
    if area!=None:
        for i in dist_cht[area]:
            D.append(i)
        dist=st.selectbox("Select district:",
                     D,
                     index=None
                     )
        if dist!=None:
            SDsS=dist_cht[area][dist][0]
            Fa=dist_cht[area][dist][1]
            #st.write(SDsS,Fa)
    return SDsS, Fa

#Area()
    