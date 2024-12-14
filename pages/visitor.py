import streamlit as st
import pandas as pd
import openpyxl as xl
import plotly.express as px
import matplotlib.pyplot as plt
from math import log, floor
from streamlit_option_menu import option_menu
import plotly.graph_objects as go
# import streamlit_vertical_slider as svs
import streamlit_toggle as sts
from  streamlit_vertical_slider import vertical_slider
import datetime
from datetime import timedelta
# from dateutil.relativedelta import relativedelta
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time
import os
import altair as alt





# https://stackoverflow.com/questions/73027461/oserror-errno-28-inotify-watch-limit-reached

# import ipywidgets as widgets
# from ipywidgets import interact
# from IPython.display import display
# alt.themes.enable('opaque')


# import streamlit.components.v1 as components
# import bar_chart_race as bcr
# import plotly.figure_factory as ff

# https://plotly.streamlit.app/Bar_Charts
# import dateutil.parser
# import math
# from streamlit_vertical_slider import vertical_slider
# from streamlit_vertical_slider import vertical_slider

# conda update -c conda-forge streamlit -y

st.set_page_config(
page_title = "LOMA Visitor Dashboard",
page_icon = "Active",        
layout="wide"
)

st.sidebar.success('Select a page above')

# <META http-equiv="imagetoolbar" content="no">
# st.header("test")
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
# Your Streamlit app code here

# Inject custom CSS
st.markdown("""
<style>
.streamlit-expanderHeader {
    background-color: #0f62fe; /* Change to your desired color */
    color: white;
}
</style>
""", unsafe_allow_html=True)

# st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

# streamlit_style = """
# <style>
#     @import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic&display=swap');
  
#     html, body, [class*="css"] {
#         .nanum-gothic-regular {
#         font-family: "Nanum Gothic", sans-serif;
#         font-weight: 400;
#         font-style: normal;
#         }
#         }
#     </style>
#   """
# st.markdown(streamlit_style, unsafe_allow_html=True)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic&display=swap');
body {
    font-family: 'Nanum Gothic', sans-serif;
}
</style>
""", unsafe_allow_html=True)


st.html(
"""
    <style>
    .clickable {
        color: rgb(46, 154, 255);
        text-decoration: underline;
    }
    
    div[data-testid="stChatMessageContent"] {
        background-color: white;
        color: black; # Expander content color
    } 
    
    div[data-testid="stChatMessage"] {
        background-color: white;
        color: black; # Adjust this for expander header color
    }
    </style>
""")

# @st.cache_data
# def fontRegistered():
#     font_dirs = [os.getcwd() + '/customFonts']
#     font_files = fm.findSystemFonts(fontpaths=font_dirs)

#     fm._load_fontmanager(try_read_cache=False)

# st.markdown("폰트테스트")


# @import url("https://fonts.googleapis.com/css2?family=Nanum+Gothic&display=swap");

# streamlit_style = """
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic&display=swap');
# </style>
#     .nanum-gothic-regular {
#     font-family: "Nanum Gothic", sans-serif;
#     font-weight: 400;
#     font-style: normal;
#     }
# </style>
# """
# st.markdown(streamlit_style, unsafe_allow_html=True)


# try:
#     with open( "style.css" ) as css:
#         st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
# except:
#     with open( "pages/style.css" ) as css:
#         st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

#markdown style

st.markdown("""
<style>

	.stTabs [data-baseweb="tab-list"] {
		gap: 2px;
    }

	.stTabs [data-baseweb="tab"] {
		height: 50px;
        white-space: pre-wrap;
		background-color: #364159;
		border-radius: 4px 4px 0px 0px;
		gap: 1px;
		padding-top: 10px;
		padding-bottom: 10px;
    }

	.stTabs [aria-selected="true"] {
  		background-color: #91645d;
	}

</style>""", unsafe_allow_html=True)

st.markdown("""
                <style>
                .ctn {color: #c2c2bc;border-style: hidden;}
                </style>
                """, unsafe_allow_html=True)

st.markdown("""
                <style>
                .ctn2 {color: #f5d47f;}
                </style>
                """, unsafe_allow_html=True)



st.markdown("""
                <style>
                .big-font2 {font-size:30px;letter-spacing: -2px;line-height : 2.5; word-spacing : .5rem;}
                </style>
                """, unsafe_allow_html=True)



st.markdown("""
                <style>
                .big-font {font-size:17px;letter-spacing: -2px;line-height : 2.5; word-spacing : .5rem;}
                </style>
                """, unsafe_allow_html=True)

    # write(f'<p class ="big-font"> Today 

# st.write("폰트 테스트")

# st.write(f'<p class = "big-font"> 폰트 테스트 </p>', unsafe_allow_html=True )

background_col = """

<style> .bg-red { background-color: #FF0000; } </style>

"""

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://cdn.pixabay.com/photo/2015/09/09/18/01/black-932213_1280.jpg");
background-size: cover;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
</style>
"""
# https://pixabay.com/photos/black-fabric-material-932213/
# https://discuss.streamlit.io/t/how-to-change-the-background-color-of-my-streamlit-app/47173/3
st.markdown(page_bg_img, unsafe_allow_html=True)


# class Main():
#     def __init__(self):
#         self.is_first =True
#     def method01 == True:
#         if self.is_first ==True:


# st.title("LOMA Visitor DashBoard")
st.markdown("<h1 style='text-align: center; color: white;'>LOMA Visitors DashBoard</h1>", unsafe_allow_html=True)


# st.sidebar.markdown('![Visitor count](https://shields-io-visitor-counter.herokuapp.com/badge?page=https://share.streamlit.io/https://visitor3/&label=VisitorsCount&labelColor=000000&logo=GitHub&logoColor=FFFFFF&color=1D70B8&style=for-the-badge)')
# title_alignment=
# """
# <style>
# #the-title {
# text-align: center
# }
# </style>
# """
# st.markdown(title_alignment, unsafe_allow_html=True)


# 스트림릿 케쉬 지정
@st.cache_data
# 엑셀 파일 읽어오기 함수
def get_data_from_excel():
    try:
        df_all = pd.read_excel(
                    io = 'pages/visitor.xlsx',
                    engine = 'openpyxl',
                    sheet_name ='daily',
                    skiprows = 1,
                    usecols='a:n',
                    nrows = 1500,
        )
    except:
        df_all = pd.read_excel(
                    io = 'visitor.xlsx',
                    engine = 'openpyxl',
                    sheet_name ='daily',
                    skiprows = 1,
                    usecols='a:n',
                    nrows = 1500,   
        
        )
    return df_all

get_data_from_excel()
df_all = get_data_from_excel()
pd.options.mode.chained_assignment = None
# 데이터 프레임 정리함수 _ 전시명이 없는 행 제거 후 데이터 프레임 타입 지정

# 기준주차계산################################################
# st.dataframe(df_all)

# MAX_Day = df_all.loc[(df_all['전시명'] == '아샴')] 
# st.dataframe(MAX_Day)
# df = df_all.dropna(subset=['전시명'], how='any', axis=0)
# # MAX_Day = MAX_Day['관람객'] != 0
# st.dataframe(MAX_Day)
# MAX_Day = MAX_Day.max(MAX_Day['일차'])
# st.text(f"최대일차 : {MAX_Day}")

# 경과주차 = MAX_Day//7+1
# 진행주차 = MAX_Day%7




# 전시시작, 전시종료
####################################################




####################################################



# 컬럼명[전시명] 중 내용이 없는 행 제거
df = df_all.dropna(subset=['전시명'], how='any', axis=0)
df = df[df['전시명'] != 0]
# print(df)

# 1차 데이터 추출
S_df1 = df.astype({'년':'str','월':'str', '관람객':'int', '일차':'int', '일자':'str','무료':'str', '유료':'str', '전시명':'str'})
S_df =S_df1
# get_df1()
# S_df['일자'] = pd.to_datetime(S_df['일자'], format='%Y-%m-%d') # 안됨
# S_df['일자']= S_df['일자'].astype('str')
S_df['일자'].apply(lambda x : datetime.datetime.strptime(x,'%Y-%m-%d'))
# st.dataframe(S_df['일자'])
# S_df['일자'] = pd.to_datetime(S_df['일자']) # 안됨
# st.dataframe(S_df['일자'])
# get_df1()
# S_df = pd.DataFrame(S_df)
# st.text(df.dtypes)
# st.text(S_df.dtypes)
#####################################


S_df_아샴 = df.astype({'년':'str','월':'str', '관람객':'int', '일차':'int', '무료':'str', '유료':'str', '전시명':'str'})
# get_df1()
# S_df['일자'] = pd.to_datetime(S_df['일자'], format='%Y-%m-%d') # 안됨
# S_df['일자']= S_df['일자'].astype('str')
S_df_아샴['요일']=S_df_아샴['일자'].dt.day_name()
df_아샴2 = S_df_아샴[S_df_아샴["전시명"] == "아샴"]
df_아샴3 = S_df_아샴
df_아샴2 = df_아샴2[df_아샴2['관람객'] != 0]

df_아샴2= df_아샴2.astype({'일자':'str'})
df_아샴2['일자'].apply(lambda x : datetime.datetime.strptime(x,'%Y-%m-%d'))
df_아샴2 = df_아샴2.set_index(['년','월'])
# st.dataframe(df_아샴2)


전시명4 = df_아샴2["요일"].unique()



#####################################3


# 전시선택 멀티 셀렉트
df_all_국내 = S_df[((S_df["전시명"] == "드리머") | (S_df["전시명"] == "김정기"))] # 기존

df_all_국내_전체 = df_all_국내.groupby(by=["전시명"]).sum()[["관람객"]]


# 최근 전시일 확인
df_MAX_D = S_df.loc[(S_df['전시명'] == '아샴') & (S_df['관람객'] > 0)]


# st.dataframe(df_MAX_D)
df_MAX_D = df_MAX_D.set_index("전시명")
# st.dataframe(df_MAX_D)
# st.dataframe(df_MAX_D)
# df_MAX_D = pd.to_datetime(df_MAX_D['일자'])
# df_MAX_D = df_MAX_D['일차'])
# global MAX_Day, MAX_Date
MAX_Day = df_MAX_D['일차'].max(axis=0)
MAX_Date = df_MAX_D['일자'].max(axis=0) 
MAX_Date = datetime.datetime.strptime(MAX_Date, "%Y-%m-%d").date()


# 시종일자 수정
시작일자 = datetime.date(2024,7,12)
종료일자 = datetime.date(2024,10,13)
# 시작일자 = datetime.strptime("2024-02-23",'%Y-%m-%d') #https://blog.naver.com/wideeyed/221603462366 
# st.text(f"시작일자 : {시작일자}")
# st.text(f"MAX_Date: {MAX_Date}")

# st.text(type(시작일자))
# st.text(type(MAX_Date))

# 전체기간 = MAX_Date - 시작일자 + relativedelta(days= 1)


###★ 재점검 필요 : 일자 형식이 이상함...

# 진행기간 = (MAX_Date - 시작일자 + timedelta(days= 1).strftime("%Y-%m-%d"))
# 전체기간 = 종료일자 - 시작일자 + timedelta(days= 1)
# 진행기간 = (MAX_Date - 시작일자 + timedelta(days=1)).strftime('%Y-%m-%d')
진행기간 = MAX_Date - 시작일자 
진행기간 = 진행기간.days + 1

전체기간 = 종료일자 - 시작일자
전체기간 = 전체기간.days + 1
잔여기간 = 전체기간 - 진행기간

# st.text(전체기간)
# st.text(진행기간)
진행율 = round(진행기간/전체기간*100,1)
당일누적관람객_df = df_MAX_D.loc[df_MAX_D['일차']<= MAX_Day, '관람객']
당일누적관람객_df = 당일누적관람객_df.to_frame()

# Comparison of previous day

당일누적관람객_df = 당일누적관람객_df.groupby(by=["전시명"]).sum()[["관람객"]]
당일누적관람객 = 당일누적관람객_df.iloc[0].loc["관람객"] # 작동
당일누적관람객 = round(당일누적관람객,1)

일평균관람객 = int(round(당일누적관람객/진행기간,0))
관람객추정 = round(일평균관람객*전체기간/10000,1)
관람객추정 = str(관람객추정)
# st.text(f"진도율 : {int(진행기간)}/{int(전체기간)}")
# st.text(f"진행율: {진행율}%")






#################################################



df = df_all.dropna(subset=['전시명'], how='any', axis=0)
df = df[df['전시명'] != 0]

# 1차 데이터 추출
S_df = df.astype({'년':'str','월':'str', '관람객':'int', '일자':'str','일차':'int', '무료':'str', '유료':'str', '전시명':'str'})


# 최근 전시일 확인
df_MAX_D = S_df.loc[(S_df['전시명'] == '아샴') & (S_df['관람객'] > 0)]
df_MAX_D=df_MAX_D.set_index("전시명")
df_MAX_D_line=S_df.set_index("전시명")
MAX_Day = df_MAX_D['일차'].max(axis=0)

당일관람객_df = df_MAX_D.loc[df_MAX_D['일차']== MAX_Day, '관람객']
당일관람객_df =당일관람객_df.to_frame()
당일관람객 = 당일관람객_df.iloc[0].loc["관람객"] # 작동

당일누적관람객_df = df_MAX_D.loc[df_MAX_D['일차']<= MAX_Day, '관람객']
당일누적관람객_df = 당일누적관람객_df.to_frame()

# Comparison of previous day

당일누적관람객_df = 당일누적관람객_df.groupby(by=["전시명"]).sum()[["관람객"]]
당일누적관람객 = 당일누적관람객_df.iloc[0].loc["관람객"] # 작동
당일누적관람객 = round(당일누적관람객/10000,1)
try:
    lsatweek관람객_df = df_MAX_D.loc[df_MAX_D['일차']== MAX_Day-7, '관람객']
    lsatweek관람객_df =lsatweek관람객_df.to_frame()
    # st.dataframe(당일관람객_df)
    # st.text(당일관람객_df.info)
    lsatweek관람객 = lsatweek관람객_df.iloc[0].loc["관람객"] # 작동
    lsatweek누적관람객_df = df_MAX_D.loc[df_MAX_D['일차']<= MAX_Day-7, '관람객']
    # st.dataframe(당일누적관람객_df)
    lsatweek누적관람객_df = lsatweek누적관람객_df.to_frame()

    lsatweek누적관람객_df = lsatweek누적관람객_df.groupby(by=["전시명"]).sum()[["관람객"]]
    # 당일누적관람객_df = 당일누적관람객_df.to_frame()
    # 당일누적관람객_df =당일누적관람객_df.style.format(thousands=',')
    lsatweek누적관람객 = lsatweek누적관람객_df.iloc[0].loc["관람객"] # 작동
    lsatweek누적관람객 = round(lsatweek누적관람객/10000,1)

    전일관람객_df = df_MAX_D.loc[df_MAX_D['일차']== MAX_Day-1, '관람객']
    전일관람객_df =전일관람객_df.to_frame()
# st.dataframe(당일관람객_df)
# st.text(당일관람객_df.info)
    전일관람객 = 전일관람객_df.iloc[0].loc["관람객"] # 작동
    전일대비 = 당일관람객-전일관람객
except:
    pass







class Main():
    def __init__(self):
        self.is_first = True

    def method01(self):

        if self.is_first == True:
            
            self.is_first = False

            if 전일대비 < 0 :
                st.balloons()
            
            else:
                st.snow()
            self.is_first == False
        else:
            pass
        
# m = Main()
# m.method01()


# flag = False
# if flag:
#     flag = True
#     평가()
# else:
#     flag = False
#     pass

    # st.text(start)
    # start = start + 1
    # st.text(start)




# global xx
# xx = True
# def 평가():
#     if xx == True:
#         if 전일대비 < 0 :
#             st.balloons()   
#             xx = False
#         else:
#             st.balloons()
#             xx = False
#     else :
#         pass
# 평가()


################################################3


now =  datetime.datetime.today()
now = now.strftime("%Y-%m-%d")
# now = now[-2:]

df_all = get_data_from_excel()
# 데이터 프레임 정리함수 _ 전시명이 없는 행 제거 후 데이터 프레임 타입 지정

# 컬럼명[전시명] 중 내용이 없는 행 제거
df = df_all.dropna(subset=['전시명'], how='any', axis=0)
df = df[df['전시명'] != 0]

# 1차 데이터 추출
S_df = df.astype({'년':'str','월':'str', '관람객':'int', '일자':'str','일차':'int', '무료':'str', '유료':'str', '전시명':'str'})


# 최근 전시일 확인
df_MAX_D = S_df.loc[(S_df['전시명'] == '아샴') & (S_df['관람객'] > 0)]
df_MAX_D=df_MAX_D.set_index("전시명")
df_MAX_D_line=S_df.set_index("전시명")
MAX_Day = df_MAX_D['일차'].max(axis=0)

당일관람객_df = df_MAX_D.loc[df_MAX_D['일차']== MAX_Day, '관람객']
당일관람객_df =당일관람객_df.to_frame()
당일관람객_f = format(당일관람객_df.iloc[0].loc["관람객"],",") # 작동
당일관람객 = 당일관람객_df.iloc[0].loc["관람객"] # 작동

전일관람객_df = df_MAX_D.loc[df_MAX_D['일차']== MAX_Day-1, '관람객']
전일관람객_df =전일관람객_df.to_frame()

try:
    전일관람객_f = format(전일관람객_df.iloc[0].loc["관람객"],",") # 작동
    전일관람객 = 전일관람객_df.iloc[0].loc["관람객"] # 작동
except:
    전일관람객_f = 0
    전일관람객 = 0

전일대비 = 당일관람객 - 전일관람객

당일누적관람객_df = df_MAX_D.loc[df_MAX_D['일차']<= MAX_Day, '관람객']
당일누적관람객_df = 당일누적관람객_df.to_frame()



# 해당일자 관람객으로 수정 필요


# Comparison of previous day

당일누적관람객_df = 당일누적관람객_df.groupby(by=["전시명"]).sum()[["관람객"]]
당일누적관람객 = 당일누적관람객_df.iloc[0].loc["관람객"] # 작동
당일누적관람객_명 = 당일누적관람객 
당일누적관람객_명 = format(당일누적관람객_명,",")
당일누적관람객 = round(당일누적관람객/10000,2)

# st.markdown('''
# <style>
# /*center metric label*/
# [data-testid="stMetricLabel"] > div:nth-child(1) {
#     justify-content: center;
# }

# /*center metric value*/
# [data-testid="stMetricValue"] > div:nth-child(1) {
#     justify-content: center;
# }
# </style>
# ''', unsafe_allow_html=True)

css = """
<style>
div[data-testid="stMetric"] {
    min-height: 100px;
}
</style>
"""
st.markdown(css, unsafe_allow_html=True)
# c5 = st.container(border=False)
    # c5.write(f"<h5 style='text-align: center; color: white;'>   Update : {MAX_Date}    </h5> ", unsafe_allow_html=True)
    # c5.write(f"<h5 style='text-align: center; color: white;'>   {MAX_Day}th day , {round(진행기간//7)+1}weeks   </h5> ", unsafe_allow_html=True)
# c5.write(f"<h5 style='text-align: right; color: white;'>   Update : {MAX_Date}    </h5> ", unsafe_allow_html=True)
# c5.write(f"<h5 style='text-align: right; color: white;'>   {MAX_Day}th day , {round(진행기간//7)+1}weeks   </h5> ", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col2:
    st.subheader(f"")
    # st.markdown(f"<h5 style='text-align: center; color: white;'> - Today : {now} - </h5> ", unsafe_allow_html=True)
    # st.markdown(f"<h5 style='text-align: center; color: white;'> -   - </h5> ", unsafe_allow_html=True)
    c6 = st.container(border=True)
    c6.write(f"<h1 style='text-align: center; color: white; padding:0px;'>{당일관람객_f}<small>명</small> </h1>", unsafe_allow_html=True)
    if 전일대비 >= 0 :
        c6.caption(f'<div style="text-align: center"> 전일대비: +{전일대비}</div>', unsafe_allow_html=True)
        # &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbs;
        # c6.caption('<div style="text-align: center"> ------------------------------------&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </div>', unsafe_allow_html=True)
        # c6.write(":heavy_minus_sign:" * 34)
        # c6.write(f"<h6 style='text-align: center; color: white;'>   전일대비 : + {전일대비}명 </h6> ", unsafe_allow_html=True)
        # c6.write(f"<h6 style='text-align: center; color: white;'>   누적 : {당일누적관람객_명}명 </h6> ", unsafe_allow_html=True)
    else :
        c6.caption(f'<div style="text-align: center"> 전일대비: {전일대비}</div>', unsafe_allow_html=True)
        # &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        # c6.caption('<div style="text-align: center"> ------------------------------------&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </div>', unsafe_allow_html=True)
        # c6.write(":heavy_minus_sign:" * 34)
        # c6.write(f"<h6 style='text-align: center; color: white;'>   전일대비 : - {전일대비}명 </h6> ", unsafe_allow_html=True)
        # c6.write(f"<h6 style='text-align: center; color: white;'>   누적 : {당일누적관람객_명}명 </h6> ", unsafe_allow_html=True)
        # c6.markdown("---")

    c7 = st.container(border=True)
    # c8 = st.container(border=True)
    c6.write(f"<h3 style='text-align: center; color: white; padding:20px;'>Total : {당일누적관람객_명}<small>명</small> </h3> ", unsafe_allow_html=True)
    # c6.write(f"<h3 style='text-align: center; color: white; padding:20px;'>Total </h3> ", unsafe_allow_html=True)
#작동#################################################################################
    # st.markdown("""
    # <style>
    # .stTextArea [data-baseweb=base-input] {
    #     background-image: linear-gradient(140deg, rgb(54, 36, 31) 0%, rgb(121, 56, 100) 50%, rgb(106, 117, 25) 75%);
    #     -webkit-text-fill-color: black;
    # }

    # .stTextArea [data-baseweb=base-input] [disabled=""]{
    #     background-image: linear-gradient(45deg, red, purple, red);
    #     -webkit-text-fill-color: gray;
    # }
    # </style>
    # """,unsafe_allow_html=True)


    # st.text_area("ttt",f"{당일누적관람객_명}")

    ##################################################################################
    st.markdown("""
    <style>

    .stTextArea [data-baseweb=base-input] {
        background: transparent;;color:transparent;
        -webkit-text-fill-color: transparent;
    
    }

    .stTextArea [data-baseweb=base-input] [disabled=""]{
            -webkit-text-fill-color: transparent;
    }

    input[class]{
font-weight: bold;
font-size:120%;
color: transparent;
}
    
   textarea {
     background: transparent;
    color: transparent;
  resize: none;
  border: 0 none;
  width: 100%;
  font-size: 5em;
  outline: none;
  height: 100%;
  position: absolute;
}
    </style>
    """,unsafe_allow_html=True)

    # c6.markdown("00")
    # c6.markdown('<span style="font-size:1px:"> CK </span>', unsafe_allow_html=True)
    c6.text_area('', f"{당일누적관람객_명}")

    
    
    
    
    
    
    
    
    
    
    
    
    # c6.text_area(f"<h3 style='text-align: center; color: white;; padding:20px;'>Total : {당일누적관람객_명}<small>명</small> </h3> ")
    # st.text_area(f"<style = 'text-align: center;'>Total</style>", unsafe_allow_html=True)
                #  f"<h3 style='text-align: center;{당일누적관람객_명}<small>명</small> </h3>")
    # st.button("total")
    # st.text_area("Total",f"{당일누적관람객_명}<small>명</small>", unsafe_allow_html=True)
    # st.write(f"{당일누적관람객_명}")



# with col2:
    
    c5 = st.container(border=False)
    c5.write(f"<h6 style='text-align: center; color: white;'>   Update : {MAX_Date}    </h6> ", unsafe_allow_html=True)
    c5.write(f"<h6 style='text-align: center; color: white;'>   {MAX_Day}th day , {round(진행기간//7)+1}weeks   </h6> ", unsafe_allow_html=True)
    

    # https://discuss.streamlit.io/t/personnal-css-for-only-one-container/34646/2
    # col1, col2 = st.columns(2)
    # with col1:
    #     col1.metric(label="Update day", value=f"{당일관람객_f} 명", delta=f"전일대비{전일대비}명")
    # with col2:
    #     col2.metric(label="Totlal", value=f"{당일누적관람객_명} 명")
    # c5.write(f"<h6 style='text-align: center; color: #f5d47f;'> [ &nbsp; Update day {당일관람객_f}명&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;누적 {당일누적관람객_명}명 &nbsp; ]</h5> ", unsafe_allow_html=True)
    
    # st.markdown(f"<h5 style='t주중대비 주말 평균관람객 비교ext-align: center; color: white;'> -  Last : {MAX_Date} | {MAX_Day}day , {round(진행기간//7+1)}weeks  - </h5> ", unsafe_allow_html=True)
    
# 진행기간
# st.divider()
now1 = datetime.datetime.now().strftime('%Y-%m-%d')
# now1 = datetime.date.today()
# st.caption(f'<div style="text-align: right">Totay : {now1}</div>', unsafe_allow_html=True)
st.caption('<div style="text-align: right">interpark t-admin | 당일실적 19시 기준</div>', unsafe_allow_html=True)
st.markdown("---")

# if "reset" not in st.session_state:
#     st.session_state.reset = False

# with st.container():
#     default_values = {"inp1": 0.5, "inp2": 10.28, "inp3": 0.5, "inp4": 1.0}

#     inp1 = default_values["inp1"] if st.session_state.reset else st.session_state.get("inp1", default_values["inp1"])
#     inp2 = default_values["inp2"] if st.session_state.reset else st.session_state.get("inp2", default_values["inp2"])
#     inp3 = default_values["inp3"] if st.session_state.reset else st.session_state.get("inp3", default_values["inp3"])
#     inp4 = default_values["inp4"] if st.session_state.reset else st.session_state.get("inp4", default_values["inp4"])

#     st.session_state.inp1 = st.number_input("Min Vug Area", value=inp1)
#     st.session_state.inp2 = st.number_input("Max Vug Area", value=inp2)
#     st.session_state.inp3 = st.number_input("Min Circ Ratio", value=inp3)
#     st.session_state.inp4 = st.number_input("Max Circ Ratio", value=inp4)

#     # Reset button
#     if st.button("Reset values"):
#         st.session_state.reset = True  # Mark reset as True if button is pressed
#         st.experimental_rerun()  # Rerun the script
#     else:
#         st.session_state.reset = False  


# st.markdown("---")


# df_all = get_data_from_excel()
# # 데이터 프레임 정리함수 _ 전시명이 없는 행 제거 후 데이터 프레임 타입 지정

# # 컬럼명[전시명] 중 내용이 없는 행 제거
# df = df_all.dropna(subset=['전시명'], how='any', axis=0)
# df = df[df['전시명'] != 0]

# # 1차 데이터 추출
# S_df = df.astype({'년':'str','월':'str', '관람객':'int', '일자':'str','일차':'int', '무료':'str', '유료':'str', '전시명':'str'})


# # 최근 전시일 확인
# df_MAX_D = S_df.loc[(S_df['전시명'] == '아샴') & (S_df['관람객'] > 0)]
# df_MAX_D=df_MAX_D.set_index("전시명")
# df_MAX_D_line=S_df.set_index("전시명")
# MAX_Day = df_MAX_D['일차'].max(axis=0)

# 당일관람객_df = df_MAX_D.loc[df_MAX_D['일차']== MAX_Day, '관람객']
# 당일관람객_df =당일관람객_df.to_frame()
# 당일관람객 = 당일관람객_df.iloc[0].loc["관람객"] # 작동

# 당일누적관람객_df = df_MAX_D.loc[df_MAX_D['일차']<= MAX_Day, '관람객']
# 당일누적관람객_df = 당일누적관람객_df.to_frame()

# # 해당일자 관람객으로 수정 필요


# # Comparison of previous day

# 당일누적관람객_df = 당일누적관람객_df.groupby(by=["전시명"]).sum()[["관람객"]]
# 당일누적관람객 = 당일누적관람객_df.iloc[0].loc["관람객"] # 작동
# 당일누적관람객_명 = 당일누적관람객 
# 당일누적관람객 = round(당일누적관람객/10000,2)
try:
    lsatweek관람객_df = df_MAX_D.loc[df_MAX_D['일차']== MAX_Day-7, '관람객']
    lsatweek관람객_df =lsatweek관람객_df.to_frame()
    # st.dataframe(당일관람객_df)
    # st.text(당일관람객_df.info)
    lsatweek관람객 = lsatweek관람객_df.iloc[0].loc["관람객"] # 작동

    lsatweek누적관람객_df = df_MAX_D.loc[df_MAX_D['일차']<= MAX_Day-7, '관람객']
    # st.dataframe(당일누적관람객_df)
    lsatweek누적관람객_df = lsatweek누적관람객_df.to_frame()

    lsatweek누적관람객_df = lsatweek누적관람객_df.groupby(by=["전시명"]).sum()[["관람객"]]
    # 당일누적관람객_df = 당일누적관람객_df.to_frame()
    # 당일누적관람객_df =당일누적관람객_df.style.format(thousands=',')
    lsatweek누적관람객 = lsatweek누적관람객_df.iloc[0].loc["관람객"] # 작동
    lsatweek누적관람객 = round(lsatweek누적관람객/10000,1)
except:
    pass
전일관람객_df = df_MAX_D.loc[df_MAX_D['일차']== MAX_Day-1, '관람객']
전일관람객_df =전일관람객_df.to_frame()
# st.dataframe(전일관람객_df)
try:
    전일관람객_f = format(전일관람객_df.iloc[0].loc["관람객"],",") # 작동
    전일관람객 = 전일관람객_df.iloc[0].loc["관람객"] # 작동
except:
    전일관람객_f = 0
    전일관람객 = 0

# 전일관람객 = 전일관람객_df.iloc[0].loc["관람객"] # 작동
# st.text(전일관람객)
# st.dataframe(당일관람객_df)
# st.text(당일관람객_df.info)
# 전일관람객 = 전일관람객_df.iloc[0].loc["관람객"] # 작동
# 전일대비 = 당일관람객 - 전일관람객
# st.text(전일대비)
try:
    전일관람객 = 전일관람객_df.iloc[0].loc["관람객"] # 작동
    전일대비 = 당일관람객 - 전일관람객
    # st.text(전일대비)
except:
    전일대비 = 0
    # st.text(전일대비)
global first

# def 평가():
#     if 전일대비 < 0 :
#         st.balloons()   
#     else:
#         st.balloons()
# 평가()

# run_once =0
# while 1:
    # if run_once ==0:
    #     평가()
    #     run_once =1

# def only_once(): 
#     first = True 
#     # def ret_fun(*args, **kwargs): 
#     def 평가(): 
    
#         nonlocal first 
#         if first: 
#             first = False 
#             # return 평가(*args, **kwargs)
#             return 평가()
             
#     # return 평가

# # @only_once
# only_once

try:
    전주전일_df = df_MAX_D.loc[df_MAX_D['일차']== MAX_Day-8, '관람객']
    전주전일_df =전주전일_df.to_frame()
    # st.dataframe(당일관람객_df)
    # st.text(당일관람객_df.info)
    전주전일관람객 = 전주전일_df.iloc[0].loc["관람객"] # 작동

    전주전일대비 =lsatweek관람객-전주전일관람객
except:
    pass
# st.markdown("""
markdown_style = """
        <style>
        .big-font {font-size:20px;letter-spacing: -0.5px; line-height : 2.5; word-spacing : .7rem;}
        </style>
        """
# 
# write(f'<p class ="big-font"> TodS_dfay 
# 평가()
col1, col2 = st.columns(2)

# st.text("test")     
    
with col1:
    st.markdown(
    """
    <style>
        .stProgress > div > div > div > div {
            background-color: #91645d;
        }
    </style>""",
    unsafe_allow_html=True,
    )

    진행율 = int(round(진행율,0))

    # st.error(f"<p>일자진행율 : {진행율}%")
    # st_tt = st.container
    st.error(f"일자진행율 : {진행율}%")


    # with st.chat_message(name='A'):
    #     st.write(f'일차진행율: {진행율}%')
    # https://discuss.streamlit.io/t/changing-the-background-color-of-the-expander-element-and-chat-message/61038/6
   



    # st.markdown(f" ttt : white-background[Balloons or Snow]")
    latest_iteration = st.empty()
    my_bar = st.progress(0)
    for percent_comlete in range(진행율):
        # latest_iteration.text(f'일차진행율 : {진행율}')
        my_bar.progress(percent_comlete)
        time.sleep(0.01)
    
    # st.subheader(f"Today : {당일관람객}명   | Compa,rison of previous day ( {전일대비}명 )"),
    # st.subheader(f"Accumulate : {당일누적관람객}명")
    # c1 = container
    # st.markdown('<p class ="ctn">c1</p>',unsafe_allow_html=True)
    with st.expander("전시개요"):
        c1 = st.container(border=True)    
        목표일평균관람객 = round(40000/94,1)
        
        c1.write(f'<p class ="ctn"> 전시일수 : {진행기간}일           |        전체일수 : {전체기간}일</p>', unsafe_allow_html=True)
        #전시기간수정
        c1.write(f'<p class ="ctn"> 전시시작일 : 2024-07-12 </p>', unsafe_allow_html=True)
        c1.write(f'<p class ="ctn"> 전시종료일 : 2024-10-13 </p>', unsafe_allow_html=True)
        c1.write(f'<p class ="ctn"> 관람객목표 : 4만명,  <목표일평균 : {목표일평균관람객}명>  </p>', unsafe_allow_html=True)
    # c1.write(f'<p class ="ctn"> 목표일평균관람객 : {목표일평균관람객}명 </p>', unsafe_allow_html=True)

    # st.warning(f"일자진행율 : {진행율}%")
    # my_bar = st.progress(0)
    # for percent_comlete in range(진행율):
    #     time.sleep(0.01)
    #     my_bar.progress(percent_comlete + 10)

#####################################3
    # st.text(당일누적관람객)

with col2:    
    st.markdown(
    """
    <style>
        .stProgress > div > div > div > div {
            background-color: #91645d;
        }
    </style>""",
    unsafe_allow_html=True,
    )

    # 관람객달성 = int(round((당일누적관람객/4)*100,1))
    관람객달성 = int(round((당일누적관람객/4)*100,1))

    # st.error(f"<p>일자진행율 : {진행율}%")
    # st_tt = st.container

    st.error(f"관람객달성율 : {관람객달성}%")
    latest_iteration = st.empty()
    my_bar = st.progress(0)
    for percent_comlete in range(관람객달성):
        # latest_iteration.text(f'일차진행율 : {진행율}')
        my_bar.progress(percent_comlete)
        time.sleep(0.01)
    with st.expander("실적요약"):
        c2 = st.container(border=True)
        # c2.write(f"{lsatweek관람객}")
        # c2.write("test")    
        # c2.write("test2")
        # c2.write(f'<p class ="ctn"> 전시일수 : {진행기간}일           |        전체일수 : {전체기간}일  ({진행율}%) </p>', unsafe_allow_html=True)
        if 전일대비 == 0:
            c2.write(f'<p class ="ctn2"> Update day      :      {당일관람객}명             |    전일동일 </p>', unsafe_allow_html=True) 
        elif 전일대비 >= 0 :
            c2.write(f'<p class ="ctn2"> Update day      :      {당일관람객}명             |    전일대비 ( {전일대비}명 증가 )</p>', unsafe_allow_html=True)
        else:
            c2.write(f'<p class ="ctn2"> Update day      :      {당일관람객}명             |    전일대비 ( {전일대비*-1}명 감소 )</p>', unsafe_allow_html=True) 
        
        목표일평균대비 = 일평균관람객 - 목표일평균관람객
        일평균달성율 = round((일평균관람객/목표일평균관람객)*100,1)
        # 당일누적관람객_명 = format(당일누적관람객_명,",")
        c2.write(f'<p class ="ctn"> 누적       :{당일누적관람객_명}명      (※ 인터파크 관람객기준)</p>', unsafe_allow_html=True)
        if 목표일평균대비 >= 0:
            c2.write(f'<p class ="ctn2"> 목표 일평균관람객 대비 : +{목표일평균대비}명, ({일평균달성율}%)  </p>', unsafe_allow_html=True)
        else:
            c2.write(f'<p class ="ctn2"> 목표 일평균관람객 대비 : {목표일평균대비}명, ({일평균달성율}%)  </p>', unsafe_allow_html=True)
        c2.write(f'<p class ="ctn"> 평균 : {일평균관람객}명    추세지속시 : {관람객추정}만명(보수추정) </p>', unsafe_allow_html=True)
        
    진행율 = int(round(진행율,0))
    
    # 스타일 테스트
# st.markdown(markdown_style, unsafe_allow_html=True)

######################################################
    # 관람객달성 = int(round(당일누적관람객/40,0))

    # # st.error(f"<p>일자진행율 : {진행율}%")
    # # st_tt = st.container
    # st.error(f"관람객달성율 : {관람객달성}%")

    # latest_iteration = st.empty()
    # my_bar = st.progress(0)
    # for percent_comlete in range(관람객달성):
    #     # latest_iteration.text(f'일차진행율 : {진행율}')
    #     my_bar.progress(percent_comlete + 10)
    #     time.sleep(0.01)





####################################################
    









#############################################






# st.markdown('--------------')

# 일단 멀티셀렉트 제거
# st.write('<p class ="big-font"> 🔍 필요시 전시를 선택해주세요.</p>', unsafe_allow_html=True)

# 전시 = st.multiselect(
# "Select the 전시:",
# options=S_df["전시명"].unique(),
# default=S_df["전시명"].unique()
# )


# 조건에 맞는 행 서식 변경
def color_vowel(value):
    return f"background-color: gray; font color: black"

# st.dataframe(S_df)

S_df_기존 = S_df
# st.dataframe(S_df_기존)
S_df_기존 =S_df_기존.dropna(subset=['전시명'], how='any', axis=0)
S_df_기존 = S_df_기존[S_df_기존['전시명'] != 0]
# st.dataframe(S_df_기존)

# 해당일차 관람객으로 테이블 전체 수정하여 진행 필요





# 이후 살림?##############

# 진행일 평균







#해당일자 기준 group by 테이블 생성후 평균관람객 산출 필요 - 아샴포함 일평균 관람객 표현

# mask = (S_df_기존.전시명 !="아샴")
# S_df_기존 = S_df_기존.loc[mask, :]

S_df_기존 = S_df_기존[S_df_기존['전시명'] != 0]
S_df_기존_아샴 = S_df.dropna(subset=['전시명'], how='any', axis=0)

mask = (S_df.dropna(subset=['전시명'], how='any', axis=0).전시명 =="아샴")
S_df_기존_아샴 = S_df_기존_아샴.loc[mask, :]
S_df_기존_아샴 = S_df_기존_아샴[S_df_기존_아샴['관람객'] != 0]

## 수정필요요용
S_df_기존_진행일차 = S_df_기존[S_df_기존['일차'] <= 진행기간]
# st.dataframe(S_df_기존_진행일차)
S_df_기존_진행일차 = S_df_기존_진행일차.groupby(by=S_df_기존_진행일차["전시명"]).agg({"관람객":'sum'}).reset_index()
S_df_기존_진행일차["일평균"] = round(S_df_기존_진행일차["관람객"]/진행기간,0)
# st.dataframe(S_df_기존_진행일차)
아샴일평균 = int(S_df_기존_진행일차.at[0,"일평균"])
아샴관람객 = int(S_df_기존_진행일차.at[0,"관람객"])





S_df_기존_아샴 = S_df_기존_아샴.groupby(by=S_df_기존_아샴["전시명"]).agg({"관람객":'sum','일차':'max'}).reset_index()
S_df_기존_아샴["일평균"] = round(S_df_기존_아샴["관람객"]/S_df_기존_아샴["일차"],0)

아샴일평균 = int(S_df_기존_아샴.at[0,"일평균"])
아샴관람객 = int(S_df_기존_아샴.at[0,"관람객"])
# st.text(아샴일평균)
######################3


# S_df_기존["일평균"] = (S_df_기존["관람객"]/S_df_기존["관람객"].value_counts())
# S_df_기존["일차"]=S_df_기존["일차"].agg(**{'관람객':lambda x : x.max()}).reset_index()
# S_df_기존 = S_df_기존.groupby(by=S_df_기존["전시명"]).agg({"관람객":'sum','일차':'max'}).reset_index().rename(columns={"관람객2":"일차2"})
S_df_기존 = S_df_기존.groupby(by=S_df_기존["전시명"]).agg({"관람객":'sum','일차':'max'}).reset_index()

# S_df_기존 = S_df_기존.reset_index()

# go.Scatter(name="주평균", x=S_df_selection2['주차'], y=S_df_selection2['주평균관람객'],mode="lines+markers+text",text=S_df_selection2['주평균관람객'],textposition = "top center", textfont_size=15, line_color='#75451b', line_width=3), secondary_y=True)

S_df_기존["일평균"] = round(S_df_기존["관람객"]/S_df_기존["일차"],0)
S_df_기존_2 = S_df_기존.sort_values("일평균",ascending=False)

# st.dataframe(S_df_기존_2)

# S_df_기존_2 = S_df_기존_2.style.format(
#         {
#             "관람객": lambda x : '{:,.0f}'.format(x),
#             "일차": lambda x : '{:,.0f}'.format(x),
#             "일평균": lambda x : '{:,.0f}'.format(x)
#         },
#     decimal=','
#     )

# st.dataframe(S_df_기존_2)

# S_df_기존_2 = S_df_기존_2.set_index("전시명")
# S_df_기존_2 = S_df_기존_2.reset_index()
# st.markdown("※ 인터파크 관람객기준")
# st.dataframe(S_df_기존_2)

# S_df_기존_2 = S_df_기존_2.set_index("전시명")
# st.dataframe(S_df_기존_2["전시명"])
# st.text(S_df_기존_2.index)

################################################3
# fig_t1 = px.bar(x=S_df_기존["전시명"],y=S_df_기존['관람객'],text=S_df_기존['관람객'])
# fig_t2 = px.scatter(x=S_df_기존["전시명"],y=S_df_기존['일평균'], size=S_df_기존['일평균'], text=S_df_기존['일평균'])

# st.plotly_chart(fig_t1, use_container_width=True)
# st.plotly_chart(fig_t2, use_container_width=True)
################################################3

# chart_data= ({
#     "전시명": S_df_기존_2["전시명"],
#     "관람객": S_df_기존_2['관람객'],
#     "일평균": S_df_기존_2['일평균'],
# }
# )

# bar_text = alt.Chart(S_df_기존_2).mark_text(align='center',baseline='line-top',color='white').encode(
#     x=alt.X('전시명'),
#     y=alt.Y('관람객', stack='zero'),
#     detail='일평균',
#     text=alt.Text('관람객')   
#     )

# # text=alt.Text('관람객', format='d')
# # chart_data.update_traces(textangle=0)
# text=alt.Chart(bar_text).mark_text(dx=0,dy=0).encode(y="관람객",text=alt.Text('관람객'))
# # st.bar_chart(chart_data+text, x="전시명", y="관람객", color="일평균" ,use_container_width=True)
# # st.altair_chart(chart_data+text, x="전시명", y="관람객", color="일평균" ,use_container_width=True)
# st.altair_chart(bar_text+text, use_container_width=True)
# st.dataframe(S_df_기존_아샴)
# st.warning(f"아샴일평균관람객 : {아샴일평균}")
# st.success(f"아샴일평균관람객 : {아샴일평균}")
# st.text(f"test{아샴관람객}")
with st.expander("🔍기존전시 비교"):    
    # st.error("최근전시 실적")
    # if 전일대비 >= 0:
    #     st.balloons()
    #     st.popover(f'전일대비 {전일대비}명 증가', help=None, disabled=False, use_container_width=False)
    # else :
    #     st.snow()
    #     st.popover(f'전일대비 {전일대비*-1}명 감소', help=None, disabled=False, use_container_width=False)


    choice = st.radio(
            f"Total Visitor or {진행기간}th day Visitor Choice",
            ["Total Visitor", f"{진행기간}th day &nbsp;Aver"],
            key="Total Visitor",
            # label_visibility=st.session_state.visibility,
            # disabled=st.session_state.disabled,
            # horizontal=st.session_state.horizontal,
        )
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        # st.write("You selected:", choice)

    if choice == 'Total Visitor':
        c1 = st.container(border=True)    
        c1.write(f'전시별 누적관람객 - 아샴(진행중) : {당일누적관람객}만명  \n(일평균 : {아샴일평균}명)</p>', unsafe_allow_html=True)
        # st.info(f"전시별 누적관람객 - 아샴(진행중) : {당일누적관람객}만명  \n(일평균 : {아샴일평균}명)")

        ######################기존작동##################################################
        # chart = alt.Chart(S_df_기존_2, title='전시별관람객').mark_bar().encode(
        # 	x=alt.X('전시명', sort=None), y='관람객', color='일평균')

        # text = alt.Chart(S_df_기존_2).mark_text(dx=0, dy=0, align='center',baseline='bottom',color='white', size=15).encode(
        # 	x=alt.X('전시명', sort=None), y='관람객', detail='일평균', text=alt.Text('일평균:Q'))
        # st.altair_chart(chart+text, use_container_width=True)

        ##변경테스트######################################################################
        # st.text(threshold)
        # threshold = 아샴일평균
        S_df_기존_2["관람객k"] = round(S_df_기존_2["관람객"]/1000,1)
        # st.dataframe(S_df_기존_2)
        threshold = 아샴관람객/1000
        # st.text(아샴관람객)
        # bars = alt.Chart(S_df_기존_2).mark_bar(color="steelblue").encode(
        # st.dataframe(S_df_기존_2)
        bars = alt.Chart(S_df_기존_2).mark_bar(color="steelblue", cornerRadiusTopLeft=15,
            cornerRadiusTopRight=15).encode(

            x="전시명",
            # y=alt.Y("관람객:Q",axis=alt.Axis(labels=False)),
            y=alt.Y("관람객k:Q"),
        
            # text= alt.Y("관람객:Q", format=',.0f'),
            # color='일평균',
            color=alt.Color('관람객k', legend=alt.Legend(
            orient='top',
            legendX=130, legendY=-40,
            direction='horizontal',
            titleAnchor='middle',
            title = '누적관람객(단위:k명)'))

            # text="관람객",
        )
        # .configure(background='#FFFFFF')
        # 유무료 관련 사항 추가 확인

        # st.dataframe(S_df_기존_2)


        # chart.transform_regression('x', 'y').mark_line()
        #★https://github.com/vega/altair/issues/921
        # ★★★ https://altair-viz.github.io/user_guide/customization.html
        #★★★ https://altair-viz.github.io/user_guide/compound_charts.html
        #★https://github.com/vega/altair/issues/1899
        highlight = bars.mark_bar(color="#f5f5eb").encode(
            y2=alt.Y2(datum=threshold),
        ).transform_filter(
            alt.datum.Value > threshold
        )

        #이후 일평균으로 다시 수정 필요

        text = alt.Chart(S_df_기존_2).mark_text(dx=0, dy=0, align='center',baseline='line-bottom',color='white', size=15).encode(
            # x=alt.X('전시명', sort=None), y='관람객', detail='일평균', text=alt.Text('일평균:Q'))
            x=alt.X('전시명', sort=None), y='관람객k', detail='일평균', text=alt.Text('관람객k:Q', format=',.1f'))

        # center
        rule = alt.Chart().mark_rule(color="#f5f5eb").encode(
            y=alt.Y(datum=threshold)
        )

        label = rule.mark_text(
            x="width",
            dx=-2,
            align="left",
            baseline="bottom",
            text="아샴",
            size=15,
            color='white'
        )

        # (bars + highlight + rule + label)
        st.altair_chart(bars + text + highlight + rule + label, use_container_width=True)
    else:
        # 초기 그래프 - 임시생성
        # st.info(f"{진행기간}일차 전시별 일평균 관람객")
        c1 = st.container(border=True)    
        c1.write(f"{진행기간}일차 전시별 일평균 관람객</p>", unsafe_allow_html=True)


        threshold = 아샴관람객
        # st.text(아샴관람객)
        # bars = alt.Chart(S_df_기존_2).mark_bar(color="steelblue").encode(
        # st.dataframe(S_df_기존_2)
        bars = alt.Chart(S_df_기존_진행일차).mark_bar(color="steelblue",cornerRadiusTopLeft=15,
            cornerRadiusTopRight=15).encode(

            x="전시명",
            # y=alt.Y("관람객:Q",axis=alt.Axis(labels=False)),
            y=alt.Y("관람객:Q"),

            # color='일평균',
            color=alt.Color('일평균', legend=alt.Legend(
            orient='top',
            legendX=130, legendY=-40,
            direction='horizontal',
            titleAnchor='middle'))

            # text="관람객",
        )




        # chart.transform_regression('x', 'y').mark_line()
        #★https://github.com/vega/altair/issues/921
        # ★★★ https://altair-viz.github.io/user_guide/customization.html
        #★★★ https://altair-viz.github.io/user_guide/compound_charts.html
        #★https://github.com/vega/altair/issues/1899
        highlight = bars.mark_bar(color="#f5f5eb").encode(
            y2=alt.Y2(datum=threshold),
        ).transform_filter(
            alt.datum.Value > threshold
        )

        text = alt.Chart(S_df_기존_진행일차).mark_text(dx=0, dy=0, align='center',baseline='line-bottom',color='white', size=15).encode(
            x=alt.X('전시명', sort=None), y='관람객', detail='일평균', text=alt.Text('일평균:Q', format=',.0f'))

        # center
        rule = alt.Chart().mark_rule(color="#f5f5eb").encode(
            y=alt.Y(datum=threshold)
        )

        label = rule.mark_text(
            x="width",
            dx=-2,
            align="left",
            baseline="bottom",
            text="아샴",
            size=15,
            color='white'
        )

        # (bars + highlight + rule + label)
        st.altair_chart(bars + text + highlight + rule + label, use_container_width=True)

















# st.info("History-Bar_Race_Chart")
# S_df22=S_df
# S_df22["주차"] = S_df22['일차'].apply(lambda x: (x//7)+1)
# # S_df22 = S_df22[S_df22['관람객'] != 0]

# # st.dataframe(S_df22)

# # S_df22 = S_df22.groupby(['전시명'])['관람객'].cumsum() #0이 아닌 값중 최소값
# # S_df22 = S_df22[S_df22['관람객'] != 0]
# S_df22['누적관람객'] = S_df22.groupby(['전시명'])['관람객'].cumsum()

# date_t = {'일차': range(1,max(S_df['일차'])+1)}
# date_t = pd.DataFrame(date_t)
# # date_t = date_t.set_index(['일차'])
# # st.dataframe(date_t)

# ########################################################
# S_df22_아샴 = S_df22[S_df22["전시명"]=="아샴"]
# S_df22_아샴 = pd.merge(date_t, S_df22_아샴, on=['일차'], how= 'left')
# S_df22_아샴 = S_df22_아샴.fillna(method='ffill')
# # st.dataframe(S_df22_아샴)

# S_df22_마르지엘라 = S_df22[S_df22["전시명"]=="마르지엘라"]
# S_df22_마르지엘라 = pd.merge(date_t, S_df22_마르지엘라, on=['일차'], how= 'left')
# S_df22_마르지엘라 = S_df22_마르지엘라.fillna(method='ffill')
# # st.dataframe(S_df22_마르지엘라)

# S_df22_바스키아 = S_df22[S_df22["전시명"]=="바스키아"]
# S_df22_바스키아 = pd.merge(date_t, S_df22_바스키아, on=['일차'], how= 'left')
# S_df22_바스키아 = S_df22_바스키아.fillna(method='ffill')
# # st.dataframe(S_df22_바스키아)

# S_df22_페어리 = S_df22[S_df22["전시명"]=="페어리"]
# S_df22_페어리 = pd.merge(date_t, S_df22_페어리, on=['일차'], how= 'left')
# S_df22_페어리 = S_df22_페어리.fillna(method='ffill')

# S_df22_알렉스 = S_df22[S_df22["전시명"]=="알렉스"]
# S_df22_알렉스 = pd.merge(date_t, S_df22_알렉스, on=['일차'], how= 'left')
# S_df22_알렉스 = S_df22_알렉스.fillna(method='ffill')

# S_df22_오스틴리 = S_df22[S_df22["전시명"]=="오스틴 리"]
# S_df22_오스틴리 = pd.merge(date_t, S_df22_오스틴리, on=['일차'], how= 'left')
# S_df22_오스틴리 = S_df22_오스틴리.fillna(method='ffill')

# S_df22_김정기 = S_df22[S_df22["전시명"]=="김정기"]
# S_df22_김정기 = pd.merge(date_t, S_df22_김정기, on=['일차'], how= 'left')
# S_df22_김정기 = S_df22_김정기.fillna(method='ffill')

# S_df22_드리머 = S_df22[S_df22["전시명"]=="드리머"]
# S_df22_드리머 = pd.merge(date_t, S_df22_드리머, on=['일차'], how= 'left')
# S_df22_드리머 = S_df22_드리머.fillna(method='ffill')
# # st.dataframe(S_df22_김정기)

# # S_df22_제이알 = S_df22[S_df22["전시명"]=="제이알"]
# # S_df22_제이알 = pd.merge(date_t, S_df22_제이알, on=['일차'], how= 'left')
# # S_df22_제이알 = S_df22_제이알.fillna(method='ffill')

# s_df22_m = pd.concat([S_df22_드리머,S_df22_김정기,S_df22_마르지엘라,S_df22_아샴,S_df22_오스틴리,S_df22_알렉스, S_df22_페어리, S_df22_바스키아])



# # #############################################
# bar = px.bar(s_df22_m, x='누적관람객', y="전시명",color='전시명',text='누적관람객', animation_frame='일차')
# # bar = px.bar(S_df22, x='누적관람객', y="전시명",color='전시명',text='누적관람객', animation_frame='일차',width=370)
# # bar = px.bar(S_df22, x='누적관람객', y="전시명",color='전시명',text='누적관람객', animation_frame='일차',width=370)

# bar.update_layout(xaxis_rangeslider_visible=False)

# # bar.update_yaxes(showticklabels=False)
# #차트 내림차순 재정렬
# bar.update_yaxes(type='category', categoryorder='max ascending')

# bar.update_layout(showlegend=False)
# bar.update_layout(transition = {'duration': 1500})
# # bar.layout.xaxis.rangeslider.visible = False
# # bar.show(config={ 'modeBarButtonsToRemove': ['zoom', 'pan'] })
# # bar.xaxis.fixedrange = True
# bar.layout.xaxis.fixedrange = True
# bar.layout.yaxis.fixedrange = True
# # bar.update_layout(use_container_width=True)
# # st.write(bar, use_container_width=True)
# my_config ={"scrollWhellZoom" : False, "displayModeBar":False, "Pan" : False,"scrollZoom" : False, "MiddleClickDragZoom" : False, "dragmode" : False}
# st.plotly_chart(bar, use_container_width=True,congig=my_config)
# st.plotly_chart(bar, use_container_width=True)
# st.write(bar)
# # st.altair_chart(bar)
# st.markdown(bar)
#############################################
# bar = alt.Chart(S_df22, x='누적관람객', y="전시명",color='전시명',text='누적관람객', animation_frame='일차',width=370)
# st.write(bar)

########################################

# bars = alt.Chart(S_df22).mark_bar(color="steelblue").encode(
# x="전시명",
# y=alt.Y("누적관람객:Q"))
# st.altair_chart(bars, use_container_width=True)

# def demo(i):
#     # return alt.Chart(S_df22).mark_bar().encode(x='일차',y='누적관람객')
#     # return alt.Chart(S_df22).mark_bar().encode(x='일차',y='누적관람객')
#     bars = alt.Chart(S_df22).mark_bar(color="steelblue").encode(
#     x="전시명",
#     y=alt.Y("누적관람객:Q"))
#     st.altair_chart(bars, use_container_width=True)
#     # st.altair_chart(bars + text + highlight + rule + label, use_container_width=True)
#     # return alt.Chart(S_df22).mark_bar().encode(x='일차',y='누적관람객')
    
#     # st.altair_chart(bars + text + highlight + rule + label, use_container_width=True)

# interact(demo, i = widgets.Play(
#     value=0,
#     min=1,
#     max=140,
#     step=1,
#     description="press play",
#     disabled=False
# ))

#######################################################

# for i in range(140):
#     time.sleep(.1)
#     display(alt.Chart(S_df22).mark_bar().encode(
#         x='전시명',
#         y='누적관람객'
#     ))



# components.html(
#     bcr.bar_chart_race(
#       df=S_df22, title="trace visiotor", n_bars=4  
#     ).data
# )

# html_str = bcr.bar_chart_race(df=S_df22,title="trace", n_bars=4)
# components.html(html_str.data)
# date_t = {'일차': range(1,max(S_df22['일차']))}
# date_t = pd.DataFrame(date_t)
# date_t = date_t.set_index(['일차'])
# st.dataframe(date_t)




################################################################################

# fig_t1 = make_subplots(specs=[[{"secondary_y":True}]])
# # fig_t1 = px.bar(x=S_df_기존.index,y=S_df_기존['관람객'])

# fig_t1.add_trace(
#     go.Bar(name="일평균관람객",x=S_df_기존["전시명"],y=S_df_기존['일평균'],text=S_df_기존['일평균'], textposition = "inside", textfont_size=13),
#     secondary_y=True
# )
# fig_t1.add_trace(
#     go.Bar(name="관람객",x=S_df_기존["전시명"],y=S_df_기존['관람객'],text=S_df_기존['관람객'], textposition = "inside", textfont_size=13),
#     secondary_y=False)

    # go.area(name="일평균관람객",x=S_df_기존["전시명"],y=S_df_기존['일평균']),
    
# fig_t1.update_layout(yaxis_range=[0,10000])
# fig_t1.update_yaxes(S_df_기존['일평균']+S_df_기존['관람객'])
# fig_t2.add_trace(
#     go.Scatter(x=df_MAX_D_line_RANGE['주차'],y=df_MAX_D_line_RANGE['일평균관람객'],mode="lines+markers+text",text=df_MAX_D_line_RANGE['일평균관람객'], textposition = "top center", textfont_size=13),
#     secondary_y=True,
# )

# st.plotly_chart(fig_t1, use_container_width=True)



st.markdown("-----")
st.write('<p> 🔍 Select Menu </p>', unsafe_allow_html=True)

# tab1, tab2, tab3 = st.tabs(['테이블', '아샴일평균', '주차별그래프'])
# listtabs = ["A tab","🦈","More tabs","A long loooooong tab","🎨","x²"]
# tabs = st.tabs(listtabs)
# tabs = st.tabs([s.center(9,"\u2001") for s in tabs])

# st.dataframe(S_df)

# chart = alt.Chart(S_df).mark_circle().encode(
#     x='일차',
#     y='관람객',
#     color='전시명',
# ).interactive()
# st.altair_chart(chart, theme="streamlit", use_container_width=True)


# chart_data = pd.DataFrame(S_df, columns=S_df["전시명"].unique())
# S_df_test = S_df.reset_index()
# # S_df_test =S_df.set_index("전시명")
# 전시명 = S_df_test["전시명"].unique()
# # st.dataframe(S_df_test)
# # chart_data = pd.DataFrame(S_df_test, columns=S_df_test.index)

# # st.area_chart(chart_data)
# 전시명_test = S_df_test["전시명"]
# 관람객 = S_df_test["관람객"]
# 일차_test = S_df_test["일차"]



#  df = pd.DataFrame(MonitorWatchDog())
# columns = 전시명
# df.columns = columns
# chart = st.area_chart(S_df_test) # initialize chart


# hist_data = [관람객,일차_test]

# group_labels = 전시명

# # Create distplot with custom bin_size
# fig = ff.create_distplot(
#         hist_data, group_labels, bin_size=[.1, .25, .5])
#         # hist_data, group_labels)

# st.plotly_chart(fig, use_container_width=True)


# tab1, tab2, tab3, tab4, tab5 = st.tabs(['🏳 Trend', '🏳 Weekly', '🏳 Average', '🏳 Forcasting', '🏳 History'])

tab1, tab2, tab3, tab4, tab5 = st.tabs(['🏳 Trend', '🏳 Weekly', '🏳 Average', '🏳 Forcasting', '🏳 History'])


with tab1:
 
    전시명 = S_df["전시명"].unique()
    

    # option = st.selectbox(
    # 'Select Exhibition',
    # (전시명), index=8,
    # )

    # css = '''
    # <style>
    #     .stSelectbox div[data-baseweb="select"] > div:first-child {
    #         background-color: #FFFFFF;
    #         border-color: #2d408d;
    #         color:#051345;
    #         border-radius:2%;
    #         border-style: solid;
    #         border-color: red;
    #         font-weight : 900;
    #     }
    # </style>
    # '''
    # st.markdown(css, unsafe_allow_html=True)

    # st.markdown(f'Selection : {option}')
 
    ## 국가 목록 가져오기
    
    ## 선택 상자 생성
    # selected_country = st.selectbox('국가 선택:', option)
    
    ## 데이터 필터링

    option = '아샴'
    filtered_data = S_df[S_df["전시명"] == option]
    # if option == '아샴':
    #     filtered_data = S_df[S_df["전시명"] == option]
    #     # filtered_data = filtered_data.reindex()
    #     filtered_data["주차"] = filtered_data['일차'].apply(lambda x: (x//7)+1)
    #     filtered_data =filtered_data[filtered_data['주차'] <= (MAX_Day//7)]
    #     # st.dataframe(filtered_data)    
    # else:
    #     filtered_data = S_df[S_df["전시명"] == option]
    #     filtered_data["주차"] = filtered_data['일차'].apply(lambda x: (x//7)+1)
    #     # filtered_data = S_df[S_df["전시명"] == option]
    

    
    
    ## 필터링된 데이터 표시
    # st.write(filtered_data)




# ##############################################
#     dtest_tt = filtered_data["일차"].copy()
#     df_test_tt = dtest_tt.map(lambda x: (x//7)+1)
#     filtered_data["주차"] = df_test_tt
##############################################

    filtered_data["주차"] = filtered_data["일차"].map(lambda x: (x//7)+1)
    # st.write(filtered_data)

    S_df_t = filtered_data
    # S_df_t = S_df_t.set_index(['전시명'])
    # # S_df_t = S_df_t.reset_index()
    # # S_df_t = S_df_t.loc[S_df_t['전시명']== option]

    # # st.dataframe(S_df_t)
    S_df_selection_t = S_df_t
    # st.dataframe(S_df_selection_t)
 
    df_MAX_D_line_MAX = S_df_selection_t.groupby(['전시명','주차'])['관람객'].agg(**{'최대값':lambda x : x.max()}).reset_index()
    df_MAX_D_line_MIN = S_df_selection_t.groupby(['전시명','주차'])['관람객'].agg(**{'최소값':lambda x : x.min()}).reset_index() #0이 아닌 값중 최소값
    df_MAX_D_line_주차별관람객 = S_df_selection_t.groupby(['전시명','주차'])['관람객'].agg(**{'주차별관람객':lambda x : x.sum()}).reset_index() #0이 아닌 값중 최소값
    df_MAX_D_line_fir = S_df_selection_t.groupby(['전시명','주차'])['관람객'].apply(lambda x: x.value_counts().index[0]).reset_index(name="fir")
    df_MAX_D_line_lst = S_df_selection_t.groupby(['전시명','주차'])['관람객'].apply(lambda x: x.value_counts().index[-1]).reset_index(name="lst")
    
    
    

    df_MAX_D_line_MAX = df_MAX_D_line_MAX.set_index(['전시명','주차'])
    df_MAX_D_line_MIN = df_MAX_D_line_MIN.set_index(['전시명','주차'])
    df_MAX_D_line_주차별관람객 = df_MAX_D_line_주차별관람객.set_index(['전시명','주차'])
    df_MAX_D_line_fir = df_MAX_D_line_fir.set_index(['전시명','주차'])
    df_MAX_D_line_lst = df_MAX_D_line_lst.set_index(['전시명','주차'])
    
    df_MAX_D_line_RANGE = pd.merge(df_MAX_D_line_MAX,df_MAX_D_line_MIN, on=['전시명','주차'])
    df_MAX_D_line_RANGE = pd.merge(df_MAX_D_line_RANGE,df_MAX_D_line_fir, on=['전시명','주차'])
    df_MAX_D_line_RANGE = pd.merge(df_MAX_D_line_RANGE,df_MAX_D_line_lst, on=['전시명','주차'])
    df_MAX_D_line_RANGE = pd.merge(df_MAX_D_line_RANGE,df_MAX_D_line_주차별관람객, on=['전시명','주차'])

    df_MAX_D_line_RANGE = df_MAX_D_line_RANGE.reset_index()
    df_MAX_D_line_주차별관람객 = df_MAX_D_line_주차별관람객.reset_index()
    df_MAX_D_line_RANGE['누적관람객'] = df_MAX_D_line_주차별관람객['주차별관람객'].cumsum()
    df_MAX_D_line_RANGE['일평균관람객'] = round(df_MAX_D_line_RANGE['누적관람객']/(df_MAX_D_line_RANGE['주차']*7),0)
    df_MAX_D_line_RANGE['주평균관람객'] = round(df_MAX_D_line_RANGE['주차별관람객']/7,0)
    df_MAX_D_line_RANGE['관람객k'] = round(df_MAX_D_line_RANGE['주차별관람객']/1000,1)

    # # st.dataframe(df_MAX_D_line_RANGE)
    # st.markdown("General Trend")
    # my_config ={"scrollZoom" : False, "displayModeBar":False}
    
    # fig_t2 = make_subplots(specs=[[{"secondary_y":True}]])

    # fig_t2.add_trace(
    #     go.Bar(name="누적관람객",x=df_MAX_D_line_RANGE['주차'],y=df_MAX_D_line_RANGE['누적관람객'],text=df_MAX_D_line_RANGE['누적관람객'], textposition = "inside", textfont_size=15),      
    #      secondary_y=False,
    # )
    # fig_t2.add_trace(
    #      go.Scatter(name="일평균",x=df_MAX_D_line_RANGE['주차'],y=df_MAX_D_line_RANGE['일평균관람객'],mode="lines+markers+text",text=df_MAX_D_line_RANGE['일평균관람객'], textposition = "top center", textfont_size=17, line_color='#75451b', line_width=3),
    #      secondary_y=True,
    # )

    # fig_t2.update_traces(marker_color='rgb(54, 65, 89)', marker_line_color='rgb(54, 65, 89)',
    #                   marker_line_width=1.5, opacity=0.6)
    

    # fig_t2.update_layout(xaxis=dict(showgrid=False),
    #           yaxis=dict(showgrid=False)
    # )
    # fig_t2.update_yaxes(showticklabels=False)
    # fig_t2.update_layout(xaxis_rangeslider_visible=False)
    # fig_t2.update_layout(yaxis=dict(title=None,showgrid=False,showline=False))
    # fig_t2.update_layout(legend=dict(
    # orientation="h",
    # yanchor="bottom",
    # y=1.02,
    # xanchor="right",
    # # bgcolor="nation",
    # x=1,
    # # color='lifeExp'
    # ))

    # st.plotly_chart(fig_t2, use_container_width=True, congig=my_config)

# ######################test#############################
#     # base = alt.Chart(df_MAX_D_line_RANGE).encode(x=alt.X('주차',axis=alt.Axis(labelAngle=325)))
#     base = alt.Chart(df_MAX_D_line_RANGE).encode(x=alt.X('주차'))    #,axis=alt.Axis(labels=False)
#     line = base.mark_line(color='#75451b').encode(y=alt.Y('일평균관람객:Q', axis=alt.Axis(labels=False))) #axis=alt.Axis(grid=False)
#     # bar = base.mark_bar().encode(y='누적관람객:Q')
#     bar = base.mark_area(color='rgb(54, 65, 89)').encode(y=alt.Y('주차별관람객:Q', axis=alt.Axis(labels=False), title="주차별관람객(단위:k명)")).properties(height=600)

    
#     text1 = alt.Chart(df_MAX_D_line_RANGE).mark_text(dx=0, dy=0, align='center',baseline='bottom',color='white', size=15).encode(
#         # x=alt.X('주차', sort=None), y='일평균관람객', detail='일평균관람객', text=alt.Text('일평균관람객:Q'))
#         # check
#         x=alt.X('주차', sort=None),y=alt.Y('일평균관람객:Q', axis=alt.Axis(labels=False),title=""), text=alt.Text('일평균관람객:Q', format=',.0f'))
#         # x=alt.X('주차', sort=None),y=alt.Y('일평균관람객:Q', axis=alt.Axis(labels=False),title=""), text=alt.Text('일평균관람객:Q' +'k'))
 
#     text2 = alt.Chart(df_MAX_D_line_RANGE).mark_text(dx=0, dy=0, align='center',baseline='line-top',color='white', size=16).encode(
#         # x=alt.X('주차', sort=None), y='일평균관람객', detail='일평균관람객', text=alt.Text('일평균관람객:Q'))
#         # x=alt.X('주차', sort=None),y=alt.Y('주차별관람객:Q', axis=alt.Axis(labels=False)), text=alt.Text('관람객k:Q', format=',1f')).transform_calculate(label=f'format(".1f") + "k"')
#         x=alt.X('주차', sort=None),y=alt.Y('주차별관람객:Q', axis=alt.Axis(labels=False),title=""), text=alt.Text('관람객k:Q', format='.1f'))
#         # x=alt.X('주차', sort=None),y=alt.Y('주차별관람객:Q', axis=alt.Axis(labels=False)), text=alt.Text('관람객k:Q', format=''))
#     # .transform_calculate(label=f'format(datum.{'관람객k:Q'},".1f") + " inches"')
#     #format=',.0f', ',.1f'

#     # st.altair_chart((line+bar+text).resolve_scale(y='independent',), use_container_width=True)
#     st.altair_chart((line+bar+text1+text2).resolve_scale(y='independent'), use_container_width=True)

    


    # 얼리버드 추가 계산

    # if st.checkbox('Early Bird Visitor Check'):
    # st.error("ⅰ. Early Bird Visitor")
    # st.dataframe(df_all)
    # df_all_얼리2 = df_all['얼리버드계'].dropna()
    df_all_얼리2 = df_all.loc[(df_all['전시명'] == '아샴') & (df_all['일차'] <= MAX_Day) & (df_all['관람객'] > 0) ]
    # df_all_얼리 = df_all.dropna(subset=['얼리버드계'], how='any', axis=0)
    df_all_얼리2 = df_all_얼리2.rename(columns={'얼리버드비율':'얼리버드비율(%)'})
    df_all_얼리 = df_all_얼리2[df_all_얼리2['관람객'] != 0]
    # st.text(MAX_Day)
    # st.dataframe(df_all_얼리)
    df_all_얼리 = df_all_얼리.astype({'년':'str','월':'str', '관람객':'int', '일차':'int', '일자':'str','무료':'int', '유료':'int', '전시명':'str','얼리버드':'int','슈퍼얼리버드':'int','얼리버드계':'int','얼리버드비율(%)':'int'})
    # st.dataframe(df_all_얼리)
    df_all_얼리["얼리버드외 유료"] = df_all_얼리["유료"] - df_all_얼리["얼리버드계"]
    df_all_얼리 = df_all_얼리[['일자','일차' ,'관람객','유료','무료','얼리버드계','얼리버드비율(%)','슈퍼얼리버드','얼리버드','얼리버드외 유료' ]]
    # df_all_얼리['얼리버드비율'].map('{:.1%}'.format)
    # df_all_얼리.style.format({'얼리버드비율':'{:.2%}'.format})
    # df_all_얼리.loc[:,"얼리버드비율"] = df_all_얼리["얼리버드비율"].map('{:.1%}'.format)
    # df_all_얼리.loc['합계', : ] = df_all_얼리.loc['2024-07-12':'2024-07-13',:].sum(axis=0)
    # df_all_얼리 = df_all_얼리.shift(1)

    df_all_얼리 = df_all_얼리.transpose()

    # 합계 == "합      계"
    
    header = df_all_얼리.iloc[0]
    df_all_얼리 = df_all_얼리[1:]
    df_all_얼리.rename(columns=header, inplace=True)
    df_all_얼리['합계'] = df_all_얼리.sum(axis=1)
    columns = list(df_all_얼리.columns)
    columns_reverse = sorted(columns, reverse=True)
    df_all_얼리 = df_all_얼리[columns_reverse]

    # df_all_얼리.iloc[4] = ((df_all_얼리.iloc[3]*100//df_all_얼리.iloc[1])).astype('str')+"%"
    df_all_얼리.iloc[0,0] = df_all_얼리.iloc[0,1]
    # st.dataframe(df_all_얼리)
    df_all_얼리.style.format(thousands=',')
    
    df_all_얼리.style.format(formatter={'합계':'{:,}'.format})
    # st.dataframe(df_all_얼리)
    df_all_얼리.at['얼리버드비율(%)','합계'] = ((df_all_얼리.at['얼리버드계','합계']*100//df_all_얼리.at['관람객','합계']))
    
    
    # df_all_얼리.iloc[1].style.format(formatter={'합계':'{:,}'.format})
    # df_all_얼리["합계"].
    # df_all_얼리["합계"] = df_all_얼리["합계"].apply('{:,}'.format)
    # df_all_얼리.assign(합계=df_all_얼리['합계'].apply('{:,}'.format))
    # st.dataframe(df_all_얼리)
    
    # df_all_얼리.iloc[4] = ((df_all_얼리.iloc[3]*100//df_all_얼리.iloc[1])).astype('str')+"%"
    # df_all_얼리.iloc[0,0] =""


    #★★★인덱스 추가방법, 인덱스 추가 및 서식 변경, 값 추출 방법 또는 열 복사 및 값추출 후 해당열 숨기기 방법
    

                    # 누적얼리버드 = df_all_얼리.at[3,'합   계']
                    # 얼리버드비율 = df_all_얼리.at[4,'합   계']
                    # 누적슈퍼얼리버드 = df_all_얼리.at[5,'합   계']
              
##########################
    누적얼리버드_n = df_all_얼리.iloc[3].loc['합계']
    누적슈퍼얼리버드_n = df_all_얼리.iloc[5].loc['합계']
    일반얼리버드  = 누적얼리버드_n  - 누적슈퍼얼리버드_n
    누적얼리버드 = format(df_all_얼리.iloc[3].loc['합계'],',')
    얼리버드비율 = df_all_얼리.iloc[4].loc['합계']
    누적슈퍼얼리버드 = format(df_all_얼리.iloc[5].loc['합계'],',')



    # df_all_얼리= df_all_얼리.style.format(thousands=',')
    




    
    # df_all_얼리 = df_all_얼리.drop('합계', axis=1)   
##########################
    # df_all_얼리.set_index(keys=['합   계'])
    
    # 누적얼리버드 = format((df_all_얼리.iloc[3].loc['합   계']),",")
    # 얼리버드비율 = format((df_all_얼리.iloc[4].loc['합   계']),",")
    # 누적슈퍼얼리버드 = format((df_all_얼리.iloc[5].loc['합   계']),",")
    
    # col1, col2, col3 = st.columns(3)
    # df_all_얼리.data = df_all_얼리.data.drop('합      계', axis=1)  
    # df_all_얼리.set_index('합      계', inplace=True)
    # c6 = st.container(border=True)
    # c5.write(f'<p class ="ctn">{MAX_Day}일차 누적 얼리버드입장 : {누적얼리버드}명</p>', unsafe_allow_html=True)
    # c5.write(f'<p class ="ctn">수퍼얼리버드 : {누적슈퍼얼리버드}명</p>', unsafe_allow_html=True)
    # c5.write(f'<p class ="ctn">관람객 중 얼러버드비율 : {얼리버드비율}</p>', unsafe_allow_html=True)
    # col1.metric(label=f"{MAX_Day}일차 누적 얼리버드입장",value=f"{누적얼리버드}명")
    # col2.metric(label=f"수퍼얼리버드",value=f"{누적슈퍼얼리버드}명")
    # col3.metric(label=f"얼리버드비율",value=f"{얼리버드비율}")

    일반얼리버드  = 누적얼리버드_n  - 누적슈퍼얼리버드_n
    ######################################
    st.error("ⅰ. Early Bird Visitor")
    c5 = st.container(border=True)
    c5.write(f'<p class ="ctn2">{MAX_Day}일차 누적 얼리버드입장 : {누적얼리버드}명</p>', unsafe_allow_html=True)
    c5.write(f'<p class ="ctn">&nbsp;&nbsp;&nbsp;수퍼얼리버드 : {누적슈퍼얼리버드}명, 일반얼리버드 : {일반얼리버드}명 </p>', unsafe_allow_html=True)
    c5.write(f'<p class ="ctn">&nbsp;&nbsp;&nbsp;수퍼얼리버드 종료 : 2024-08-11</p>', unsafe_allow_html=True)
    c5.write(f'<p class ="ctn">&nbsp;&nbsp;&nbsp;관람객 중 얼리버드비율 : {얼리버드비율}</p>', unsafe_allow_html=True)
        
 ######################################   

    with st.expander("🔍세부내역"):
        # df_all_얼리 = df_all_얼리['합계'].style.hide()      
        # df_all_얼리.set_index(["합계"],inplace=True)
        # df_all_얼리.style.set_sticky(axis=1)
        # df_all_얼리 = df_all_얼리.set_index(keys=['합계'],append=True)
        # st.dataframe(df_all_얼리, use_container_width=True)
    
    
    # df_all_얼리 = df_all_얼리.style.clear()
        # df_all_얼리 = df_all_얼리.reset_index()

        # st.dataframe(df_all_얼리, use_container_width=True)
        # df_all_얼리.style.format({'합계': "{:,.0f}"})
        # df_all_얼리['합계'] = pd.Series(["{:,.0f}명".format(val) for val in df_all_얼리['합계']], index = df_all_얼리.index)
        # df_all_얼리['합계'] = df_all_얼리['합계'].astype(str)

        # df_all_얼리['합계'] = df_all_얼리['합계'].round(2)
        # df_all_얼리['합계'] = df_all_얼리['합계'].apply(lambda x : '{0:,}'.format(x))
# https://stackoverflow.com/questions/71419733/valueerror-cannot-specify-with-s-when-adding-comma-and-set-to-two-decima
        # df_all_얼리.iloc[4].astype('str') + '%'




        # df_all_얼리['합계'] = df_all_얼리['합계']
        # df_all_얼리['합계'] = df_all_얼리['합계'].apply('{:,.0f}').format.astype(str)
        # df_all_얼리['합계'] = df_all_얼리['합계'].astype(str).str.format("{:,.0f}명")
        
        # def draw_color_cell(x,color):
        #     color = f'background-color:{color}'
        #     color = f'color:{color}'
        #     return color
        
        # df_all_얼리["구분"] = df_all_얼리[['index','합계']].agg(': '.join, axis=1)
        # df_all_얼리 = df_all_얼리.drop('index',axis=1)       
        # df_all_얼리 = df_all_얼리.drop('합계',axis=1).set_index("구분")       
        # df_all_얼리 = df_all_얼리.style.format(thousands=',')

        # df_all_얼리.style.map(draw_color_cell,color='#ff9090',subset=pd.IndexSlice[1:2,f'{MAX_Day}'])
        # df_all_얼리.style.map(draw_color_cell,color='#ff9090',subset=pd.IndexSlice[1:2,'2024-07-24'])
        
        # df_all_얼리.style.apply()

        
        st.dataframe(df_all_얼리, use_container_width=True)
        st.caption('<div style="text-align: left">※ 무료 : 만4세 미만, 초대권, EVENT </div>', unsafe_allow_html=True)


    # st.error("유무료 관람객") 


    # def draw_color_cell(x,color):
    #     color = f'background-color:{color}'
    #     return color
 
    # df_all_얼리.style.map(draw_color_cell,color='#ff9090',subset=pd.IndexSlice[0:7,'계'])
    # df_all_얼리.iloc[4] = round((int(df_all_얼리.iloc[3])/int(df_all_얼리.iloc[1]))*100)
    # df_all_얼리= df_all_얼리.iloc[4].astype('str') + '%'
    # df_all_얼리.iloc[4] = df_all_얼리.iloc[4].astype('str') + '%'
    
    # df_all_얼리.iloc[4] = ((df_all_얼리.iloc[3]/df_all_얼리.iloc[1])*100).astype('int').astype('str') + '%'
    # df_all_얼리['계'] = df_all_얼리['계'].apply(lambda int_num : '{:,}'.format(int_num)) 
    # st.dataframe(df_all_얼리)
    # df_all_얼리.iloc["얼리버드비율"].astype('str') + '%'


    
    # df_all_얼리.iloc[4].map('{:.1%}'.format)
    # .astype('str') + '%'
    # df_all_얼리.iloc[4].style.format('{:.2%}'.format)
    

    # def format_row_wise(styler, formatter):
    #     for row, row_formatter in formatter.items():
    #         row_num = styler.index.get_loc(row)

    #     for col_num in range(len(styler.columns)):
    #         styler._display_funcs[(row_num, col_num)] = row_formatter
    #     return styler
    
    
    # formatters = {"얼리버드비율":lambda x: f"{x:.1%}"}
    # styler = format_row_wise(df_all_얼리.style, formatters)
    # # styler.render()



    # st.dataframe(df_all_얼리)

    # # df_all_얼리.loc['합계', '관람객': ] = df_all_얼리.sum(axis=0)
    # df_all_얼리.loc[:,"얼리버드비율"] = df_all_얼리["얼리버드비율"].map('{:.1%}'.format)
    # df_all_얼리 = df_all_얼리.set_index('일자')
    # # df_all_얼리 = df_all_얼리.set_index('일자')
    

    # df_all_얼리 = df_all_얼리.reset_index()
    # df_all_얼리_임시합계 = df_all_얼리[df_all_얼리['일자'].isnull()]
    # df_all_얼리 = df_all_얼리.transpose()
    # df_all_얼리_임시합계 = df_all_얼리_임시합계.transpose()

    # st.dataframe(df_all_얼리)
    
    # st.dataframe(df_all_얼리_임시합계)
    # df_all_얼리_임시합계외 = df_all_얼리[df_all_얼리['일자'].notnull()] 
    
    # df_all_얼리 = pd.concat([df_all_얼리_임시합계,df_all_얼리_임시합계외])
    # df_all_얼리.fillna("",inplace=True)
    # df_all_얼리 = df_all_얼리.set_index('일자')
    # df_all_얼리.iloc[0,0] = "합계"

    # df_all_얼리 = df_all_얼리.transpose()


    
    
    # df_all_얼리 = df_all_얼리.astype({'일차':'int'})
    # df_all_얼리['일차'] = df_all_얼리['일차'].astype(int)
    # df_all_얼리.iloc[-1]= df_all_얼리.iloc[0]
    # df_all_얼리.set_option('display.colheader_justify', 'center')
    # df_all_얼리 = df_all_얼리.style.set_properties(**{'text-align': 'center'})
    # df_all_얼리.set_table_styles([dict(selector='th', props=[('text-align', 'right')])])
    # df_all_얼리 = df_all_얼리.style.set_properties(**{
    # "background-color": "white", 
    # "color": "black", 
    # "border-color": "black", 
    # 'text-align': 'center'
    # })
    # st.dataframe(df_all_얼리.style.highlight_max(axis=0))
    # st.dataframe(df_all_얼리.style.highlight_max(axis=0))
    # st.table(df_all_얼리)



    


# else :
    pass    
    # st.dataframe(df_all_얼리, use_container_width=True)
    # S_df.map(color_vowel, subset=pd.IndexSlice['아샴','순위':'현상']), use_container_width=True)


    # if st.checkbox(f'{진행기간}th visitor'):
        # st.error("Early Bird Visitor")

##########################################################
    # st.write("<h6 style='text-align: left; color: white;'> Choice period :</h6>", unsafe_allow_html=True)
    st.markdown('--------------')
    st.error("ⅱ. 전시별 일자별 관람객") 
    
    
    
    global 일차
    일차  = MAX_Day
    # 일차 = st.slider("Choice period : ", 1, 136, value = MAX_Day) # 슬라이더 수직필요해서 일단 중지
    global 순위
    
    def perday(일차) :
        df_MAX_D = S_df.loc[(S_df['전시명'] == '아샴') & (S_df['관람객'] > 0) & (S_df['일차'] == MAX_Day)]

        S_df_selection = S_df.query(
            "일차 == @일차")
        S_df_selection = S_df_selection.groupby(by=["전시명"]).sum()[["관람객"]].sort_values(by="관람객", ascending=False)

        S_df_selection_d = S_df.query(
            "일차 == @일차")
        S_df_selection_d = S_df_selection_d.groupby(by=["전시명"]).sum()[["관람객"]].sort_values(by="관람객", ascending=False)

        # st.markdown(f"<h6 style='text-align: left; color: white;'></h6>", unsafe_allow_html=True)
        S_df_d = S_df_selection.reset_index(level='전시명') # ★ groupby후 groupby기준을 컬럼으로 활용하기 위해 기존인덱스를 살리고 새롭게 인덱스 할때
        mask = (S_df_d.전시명 =="아샴")
        S_df_temp = S_df_d.loc[mask, :]
        아샴실적 = S_df_temp.iloc[0].loc["관람객"] # 작동
        S_df_d["아샴관람객"] = 아샴실적
        S_df_d["해당전시대비"] =  S_df_d["아샴관람객"] - S_df_d["관람객"] 
        S_df_d["현상"] = S_df_d["해당전시대비"].apply(lambda x : '초과' if x>0 else '-' if x==0 else '부족') #★
        S_df_d = S_df_d.drop(labels='아샴관람객', axis=1)


        S_df_d = S_df_d.set_index("전시명")

        # 조건에 맞는 행 서식 변경
        def color_vowel(value):
                return f"background-color: gray; font color: black"

        S_df_d['순위'] = S_df_d['관람객'].rank(ascending=False)
        S_df_d['순위']=round(S_df_d['순위'],0)
        S_df_d = S_df_d[['순위','관람객','해당전시대비','현상']]

        S_df_temp = S_df_d
        #★style 후 조건부 서식 가능
        S_df_1 = S_df_d.style.format(
            {
                "관람객": lambda x : '{:,.0f}'.format(x),
                "해당전시대비": lambda x : '{:,.0f}'.format(x),
                "순위": lambda x : '{:,.0f}위'.format(x)
            },
        decimal=','
        )


        
        
        S_df_temp =  S_df_temp.reset_index()
        # st.dataframe(S_df_temp)

        S_df_temp2 = S_df_temp[S_df_temp["전시명"] =="아샴"]
        
        
        # st.dataframe(S_df_temp2)
        누적관람객 = format(S_df_temp2.iloc[0].loc['관람객'],',')
        순위 = format(S_df_temp2.iloc[0].loc['순위'],'.0f')
        # 누적관람객 = format(S_df_temp2.iloc[0].iloc['관람객'],',')
        c5 = st.container(border=False)
        df_MAX_D = S_df.loc[(S_df['전시명'] == '아샴') & (S_df['관람객'] > 0) & (S_df['일차'] == 일차)] 
        # st.dataframe(S_df_1) 
        st.dataframe(S_df_1.map(color_vowel, subset=pd.IndexSlice['아샴','순위':'현상']), use_container_width=True) #★ 향후 전시명이 아샴일 경우로 조건문 조절 필요
        # st.dataframe(S_df_selection)
        return

    # 얼리버드비율 = df_all_얼리.iloc[4].loc['합   계']
    # 누적슈퍼얼리버드 = format(df_all_얼리.iloc[5].loc['합   계'],',')


    # col1, col2 = st.columns(2)

    # c6 = st.container(border=True)
    # c5.write(f'<p class ="ctn">{MAX_Day}일차 누적 얼리버드입장 : {누적얼리버드}명</p>', unsafe_allow_html=True)
    # c5.write(f'<p class ="ctn">수퍼얼리버드 : {누적슈퍼얼리버드}명</p>', unsafe_allow_html=True)
    # c5.write(f'<p class ="ctn">관람객 중 얼러버드비율 : {얼리버드비율}</p>', unsafe_allow_html=True)
    # col1.metric(label=f"{일차}일차 누적 얼리버드입장",value=f"{누적관람객}명")
    # col2.metric(label=f"바스키아 이후(20년 10월~) 전시대비 순취",value=f"{순위}명")
    # col3.metric(label=f"얼리버드비율",value=f"{얼리버드비율}")

    
    # c5 = st.container(border=False)
    # df_MAX_D = S_df.loc[(S_df['전시명'] == '아샴') & (S_df['관람객'] > 0) & (S_df['일차'] == MAX_Day)]  
    # st.dataframe(df_MAX_D.map(color_vowel, subset=pd.IndexSlice['아샴','순위':'현상']), use_container_width=True) #★ 향후 전시명이 아샴일 경우로 조건문 조절 필요
    
    # c5.write(f'<p class ="ctn">바스키아 이후(20년 10월~) 전시대비 : {순위}위</p>', unsafe_allow_html=True)
    
    
    

    with st.expander(f"🔍세부내역 - Daily Visitors"):    
        일차 = st.number_input("일차선택 :", min_value=1, max_value=136, step=1, format="%i", value = MAX_Day)
        perday(일차)
        
        # st.dataframe(df_MAX_D.map(color_vowel, subset=pd.IndexSlice['아샴','순위':'현상']), use_container_width=True) #★ 향후 전시명이 아샴일 경우로 조건문 조절 필요

        # df_MAX_D = S_df.loc[(S_df['전시명'] == '아샴') & (S_df['관람객'] > 0) & (S_df['일차'] == MAX_Day)]
        # st.dataframe(S_df_1.map(color_vowel, subset=pd.IndexSlice['아샴','순위':'현상']), use_container_width=True) #★ 향후 전시명이 아샴일 경우로 조건문 조절 필요
        # st.dataframe(df_MAX_D.map(color_vowel, subset=pd.IndexSlice['아샴','순위':'현상']), use_container_width=True) #★ 향후 전시명이 아샴일 경우로 조건문 조절 필요

    # else:
    #     pass
    st.markdown('--------------')
    st.error("ⅲ. 전시별 일자별 누적관람객") 
    # st.dataframe(S_df)
    
    global 일차22
    일차22  = MAX_Day
    def totalperday(일차22) :
        # st.dataframe(df_아샴3)
        # st.dataframe(S_df)
        # S_df = S_df.reset_index()   
        # global 일차
        # 일차  = MAX_Day
        # 일차 = st.slider("Choice period : ", 1, 136, value = MAX_Day) # 슬라이더 수직필요해서 일단 중지
        # st.dataframe(S_df)
        df_MAX_D = df_아샴3.loc[(df_아샴3['관람객'] > 0) & (df_아샴3['일차'] <= 일차22)]
        # st.dataframe(df_MAX_D)
        S_df_selection = df_MAX_D.query(
            "일차 <= @일차22")
        # st.dataframe(df_MAX_D)
        
        S_df_selection = df_MAX_D.groupby(by=["전시명"]).sum(numeric_only=True)[["관람객"]].sort_values(by="관람객", ascending=False)

        S_df_selection_d = df_MAX_D.query(
            "일차 == @일차22")
        # S_df_selection_d['일자'].apply(lambda x : datetime.datetime.strptime(x,'%Y-%m-%d'))
        # st.dataframe(S_df_selection_d)
        S_df_selection_d = S_df_selection_d.groupby(by=["전시명"]).sum(numeric_only=True)[["관람객"]].sort_values(by="관람객", ascending=False)
        # st.markdown(f"<h6 style='text-align: left; color: white;'>{일차}th Day Visitors _ Table</h6>", unsafe_allow_html=True)
        S_df = S_df_selection.reset_index(level='전시명') # ★ groupby후 groupby기준을 컬럼으로 활용하기 위해 기존인덱스를 살리고 새롭게 인덱스 할때
        mask = (S_df.전시명 =="아샴")
        S_df_temp = S_df.loc[mask, :]
        아샴실적 = S_df_temp.iloc[0].loc["관람객"] # 작동
        S_df["아샴관람객"] = 아샴실적
        S_df["해당전시대비"] =  S_df["아샴관람객"] - S_df["관람객"] 
        S_df["현상"] = S_df["해당전시대비"].apply(lambda x : '초과' if x>0 else '-' if x==0 else '부족') #★
        S_df = S_df.drop(labels='아샴관람객', axis=1)


        S_df = S_df.set_index("전시명")

        # 조건에 맞는 행 서식 변경
        def color_vowel(value):
                return f"background-color: gray; font color: black"

        S_df['순위'] = S_df['관람객'].rank(ascending=False)
        S_df['순위']=round(S_df['순위'],0)
        S_df = S_df[['순위','관람객','해당전시대비','현상']]

        S_df_temp = S_df
        #★style 후 조건부 서식 가능
        S_df = S_df.style.format(
            {
                "관람객": lambda x : '{:,.0f}'.format(x),
                "해당전시대비": lambda x : '{:,.0f}'.format(x),
                "순위": lambda x : '{:,.0f}위'.format(x)
            },
        decimal=','
        )

        
        S_df_temp =  S_df_temp.reset_index()
        # st.dataframe(S_df_temp)

        S_df_temp2 = S_df_temp[S_df_temp["전시명"] =="아샴"]
        
        
        # st.dataframe(S_df_temp2)
        누적관람객 = format(S_df_temp2.iloc[0].loc['관람객'],',')
        순위 = format(S_df_temp2.iloc[0].loc['순위'],'.0f')
        # 누적관람객 = format(S_df_temp2.iloc[0].iloc['관람객'],',')

        # 얼리버드비율 = df_all_얼리.iloc[4].loc['합   계']
        # 누적슈퍼얼리버드 = format(df_all_얼리.iloc[5].loc['합   계'],',')


        # col1, col2 = st.columns(2)

        # c6 = st.container(border=True)
        # c5.write(f'<p class ="ctn">{MAX_Day}일차 누적 얼리버드입장 : {누적얼리버드}명</p>', unsafe_allow_html=True)
        # c5.write(f'<p class ="ctn">수퍼얼리버드 : {누적슈퍼얼리버드}명</p>', unsafe_allow_html=True)
        # c5.write(f'<p class ="ctn">관람객 중 얼러버드비율 : {얼리버드비율}</p>', unsafe_allow_html=True)
        # col1.metric(label=f"{일차}일차 누적 얼리버드입장",value=f"{누적관람객}명")
        # col2.metric(label=f"바스키아 이후(20년 10월~) 전시대비 순취",value=f"{순위}명")
        # col3.metric(label=f"얼리버드비율",value=f"{얼리버드비율}")

        
        c5 = st.container(border=False)
        # c5.write(f'<p class ="ctn">{일차}일차 누적 관람객 : {누적관람객}명</p>', unsafe_allow_html=True)
        c5.write(f'<p class ="ctn">바스키아 이후(20년 10월~) 전시대비 : {순위}위</p>', unsafe_allow_html=True)
        # c5.write(f'<p class ="ctn">관람객 중 얼러버드비율 : {얼리버드비율}</p>', unsafe_allow_html=True)
        st.dataframe(S_df.map(color_vowel, subset=pd.IndexSlice['아샴','순위':'현상']), use_container_width=True)
        
        return


    with st.expander(f"🔍세부내역 - Daily Total Visitors"):    
        일차22 = st.number_input("일차선택:", min_value=1, max_value=136, step=1, format="%i", value = MAX_Day)
        totalperday(일차22)
        # st.dataframe(S_df.map(color_vowel, subset=pd.IndexSlice['아샴','순위':'현상']), use_container_width=True)
        #★ 향후 전시명이 아샴일 경우로 조건문 조절 필요
    # else:
    #     pass







    # 유무료 확인 후 반영예정
    st.markdown('--------------')
    st.error(f"ⅳ. {MAX_Day}일차누계 무료관람객") 

        # st.write("You selected:", choice)

    # st.dataframe(df_all)


    S_df_tt = df_all.dropna(subset=['전시명'], how='any', axis=0)
    S_df_tt = S_df_tt[S_df_tt['전시명'] != 0]
    S_df_tt = S_df_tt.loc[S_df_tt['일차'] <= MAX_Day]
    

    # S_df1_유무료 = S_df_tt.groupby(by=['전시명','일차']).sum()[['관람객','유료','무료']]
    
    S_df1_유무료 = S_df_tt.groupby(by=['전시명']).agg({"관람객":'sum','유료':'sum','무료':'sum'}).reset_index()
    S_df1_유무료['무료비율'] = round((S_df1_유무료['무료']/S_df1_유무료['관람객'])*100,1)
    아샴무료_t = S_df1_유무료[S_df1_유무료['전시명'] == "아샴"]
    # st.dataframe(아샴무료_t)
    # 천단위 컴마 표시
    아샴무료 = format(아샴무료_t.iloc[0,3],',')
    
    # 아샴무료 = 아샴무료.style.format(thousands=',')
    무료비율 = format(아샴무료_t.iloc[0,4],',')
    # st.text(아샴무료)

    c6 = st.container(border=False)
    c6.write(f'<p class ="ctn2">아샴무료관람객 : {아샴무료}명   -   무료비율 {무료비율}%</p>', unsafe_allow_html=True)
    # st.info(f'아샴무료관람객 : {아샴무료}명   -   무료비율 {무료비율}%')
    # st.dataframe(S_df1_유무료)
    


    # bars = alt.Chart(S_df1_유무료).mark_bar(color="steelblue",cornerRadiusTopLeft=15,
    # cornerRadiusTopRight=15).encode(

    # x="전시명",
    # # y=alt.Y("관람객:Q",axis=alt.Axis(labels=False)),
    # y=alt.Y("무료비율"),
    # )

    # text = alt.Chart(S_df1_유무료).mark_text(dx=0, dy=0, align='center',baseline='line-bottom',color='white', size=15).encode(
    # x=alt.X('전시명', sort=None), y='무료비율', detail='무료비율', text=alt.Text('무료비율', format=',.1f'))

    # # st.altair_chart(bars + text, use_container_width=True)

    # #ver 2

    # ver 3
    S_df1_유무료 = S_df1_유무료.sort_values("무료",ascending=False)
    S_df1_pay = S_df1_유무료.reset_index(drop=True)
        # st.dataframe(S_df1_pay)
    
    with st.expander("🔍타전시 비교"):    

        choice = st.radio(
                f"{진행기간}th day Graph or {진행기간}th day Table",
                [f"{진행기간}th day Graph", f"{진행기간}th day Table"],
                key="{진행기간}th day Graph",
                # label_visibility=st.session_state.visibility,
                # disabled=st.session_state.disabled,
                # horizontal=st.session_state.horizontal,
            )
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        
    
        if choice == f"{진행기간}th day Graph":  
    
            t = alt.Chart(S_df1_pay).mark_bar(tooltip=True).encode(
                x = alt.X('무료:Q'),
                y = alt.Y('전시명:N',sort=alt.EncodingSortField(field="무료", order='ascending')),
                # color='무료비율',
                color=alt.Color('무료비율', legend=alt.Legend(
                orient='top',
                legendX=130, legendY=-40,
                direction='horizontal',
                titleAnchor='middle',
                title = '무료비율')),

                # y = alt.Y('전시명:N',sort=alt.EncodingSortField(field="무료", order='ascending')),
                tooltip=['전시명','관람객','무료','무료비율'],
                
                # alt.X('무료:Q', sort=alt.EncodingSortField(field="무료", order='ascending')),
                # alt.Y('전시명:N'),
                # tooltip=['전시명','관람객','무료','무료비율'],

                # alt.X('무료:Q', sort=alt.EncodingSortField(field="무료", op="count", order='ascending')),
                # https://stackoverflow.com/questions/52877697/order-bar-chart-in-altair

            # text = alt.Chart(S_df1_유무료).mark_text(dx=0, dy=0, align='center',baseline='line-bottom',color='white', size=15).encode(
            # x=alt.X('전시명', sort=None), y='무료비율', detail='무료비율', text=alt.Text('무료비율', format=',.1f'))
            # text = t.mark_text(dy=-5).encode(
            #     x='전시명:N',
            #     y='무료비율:Q',
            #     text='무료비율:N'
            ).properties(height=500)

            text = t.mark_text(dx= 3, align='left', size=15, color='white').encode(text='무료')
    
            st.altair_chart(t + text, use_container_width=True)
            # st.altair_chart(t + bars + text).properties(height=900).facet(column='FieldName:N')
        else:
            S_df1_pay = S_df1_pay.set_index('전시명')
            S_df1_pay = S_df1_pay.style.format(
                {
                    "관람객": lambda x : '{:,.0f}'.format(x),
                    "유료": lambda x : '{:,.0f}'.format(x),
                    "무료": lambda x : '{:,.0f}'.format(x),
                    "무료비율": lambda x : '{:,.1f}%'.format(x)
                },
            decimal=','
            )
            st.caption('<div style="text-align: right"><단위:명, %></div>', unsafe_allow_html=True)
            st.dataframe(S_df1_pay.map(color_vowel, subset=pd.IndexSlice['아샴','관람객':'무료비율']), use_container_width=True)

            # st.dataframe(S_df1_pay, hide_index=True  ,use_container_width=True)
    # with st.expander("유무료비교 상세"):    
        # if st.button('유무료비교 상세') :
        #     t = alt.Chart(S_df1_유무료).mark_bar().encode(
        #     x = '인원:Q',
        #     y = '유무료:N',
        #     color = 'type:N',
        #     row = alt.Row('전시명'),
        #     # text = '무료비율',
        #     ).transform_fold(
        #         as_ = ['유무료','인원'],
        #         fold=['유료','무료']
        #     )
        #     # bars = t.mark_bar().encode(
        #     #     x='전시명:N',
        #     #     y='무료비율:Q',
        #     #     # color='var:N'
        #     # )
        #     # text = alt.Chart(S_df1_유무료).mark_text(dx=0, dy=0, align='center',baseline='line-bottom',color='white', size=15).encode(
        #     # x=alt.X('전시명', sort=None), y='무료비율', detail='무료비율', text=alt.Text('무료비율', format=',.1f'))
        #     text = t.mark_text(dy=-5, align='left', size=15, color='white').encode(
        #         text='무료비율:N'
        #     )
        #     st.altair_chart(t, use_container_width=True)


# https://stackoverflow.com/questions/72181211/grouped-bar-charts-in-altair-using-two-different-columns






    # st.bar_chart(S_df1_유무료, x="전시명", y=['무료','유료'], color="관람객", horizontal=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #########################################
    # S_df1_유무료 =S_df1_유무료.reset_index()
    
    # st.dataframe(S_df1_유무료)

    # bars1 = alt.Chart(S_df1_유무료).mark_bar(color="steelblue").encode(

    #     x="전시명",
    #     # y=alt.Y("관람객:Q",axis=alt.Axis(labels=False)),
    #     y=alt.Y("관람객:Q"),
    #     # text= alt.Y("관람객:Q", format=',.0f'),
    #     # color='일평균',
    #     color=alt.Color('관람객', legend=alt.Legend(
    #     orient='top',
    #     legendX=130, legendY=-40,
    #     direction='horizontal',
    #     titleAnchor='middle',
    #     title = '누적관람객(단위:k명)'))

    #     # text="관람객",
    # )

    # bars2 = alt.Chart(S_df1_유무료).mark_bar(color="steelblue").encode(

    #     x="전시명",
    #     # y=alt.Y("관람객:Q",axis=alt.Axis(labels=False)),
    #     y=alt.Y("유료:Q"),
    #     # text= alt.Y("관람객:Q", format=',.0f'),
    #     # color='일평균',
    #     color=alt.Color('유료', legend=alt.Legend(
    #     orient='top',
    #     legendX=130, legendY=-40,
    #     direction='horizontal',
    #     titleAnchor='middle',
    #     title = '유료(단위:k명)'))

    #     # text="관람객",
    # )

    # # 유무료 관련 사항 추가 확인

    # # st.dataframe(S_df_기존_2)


    # # chart.transform_regression('x', 'y').mark_line()
    # #★https://github.com/vega/altair/issues/921
    # # ★★★ https://altair-viz.github.io/user_guide/customization.html
    # #★★★ https://altair-viz.github.io/user_guide/compound_charts.html
    # #★https://github.com/vega/altair/issues/1899
    # highlight = bars.mark_bar(color="#f5f5eb").encode(
    #     y2=alt.Y2(datum=threshold),
    # ).transform_filter(
    #     alt.datum.Value > threshold
    # )

    # #이후 일평균으로 다시 수정 필요

    # text = alt.Chart(S_df1_유무료).mark_text(dx=0, dy=0, align='center',baseline='line-bottom',color='white', size=15).encode(
    #     # x=alt.X('전시명', sort=None), y='관람객', detail='일평균', text=alt.Text('일평균:Q'))
    #     x=alt.X('전시명', sort=None), y='관람객', detail='유료', text=alt.Text('유료:Q', format=',.1f'))

    # # center
    # rule = alt.Chart().mark_rule(color="#f5f5eb").encode(
    #     y=alt.Y(datum=threshold)
    # )

    # label = rule.mark_text(
    #     x="width",
    #     dx=-2,
    #     align="left",
    #     baseline="bottom",
    #     text="아샴",
    #     size=15,
    #     color='white'
    # )

    # # (bars + highlight + rule + label)
    # st.altair_chart(bars1 + bars2 + text + highlight + rule + label, use_container_width=True)


























    # st.text(전시명4)

    # 요일별은 나중에 다시살림
    # 전시명4[0],전시명4[1],전시명4[2],전시명4[3],전시명4[4],전시명4[5],전시명4[6],전시명4[7] =전시명4[2],전시명4[3],전시명4[4],전시명4[5],전시명4[6],전시명4[0],전시명4[1],전시명4[7]
    # try:
    #     전시명4[0],전시명4[1],전시명4[2],전시명4[3],전시명4[4],전시명4[5],전시명4[6] =전시명4[2],전시명4[3],전시명4[4],전시명4[5],전시명4[6],전시명4[0],전시명4[1]
    # except:
    #     pass

    # # st.text(전시명4)
    # # st.dataframe(df_아샴2)
    # # st.text(MAX_Date.weekday())
    # st.text(MAX_Date.isoweekday())
    # st.markdown(f'[참조] 아샴 요일별 실적 비교')
    # option40 = st.selectbox(
    # 'Select Day of the week',
    # (전시명4),
    # index=MAX_Date.weekday(),
    # # index=전시명4.index(MAX_Date.day_name()),
    # )

    # # , index= 전시명4.index(MAX_Day.day_name()
    # # st.text(MAX_Date.weekday())
    # # index_t= 전시명4.index(MAX_Day.day_name())
    # # st.text(index_t)
    # df_아샴2_요일별 = df_아샴2[df_아샴2['요일'] ==option40]
    # df_아샴2_요일별 = df_아샴2_요일별.reset_index()
    # del df_아샴2_요일별['요일']
    # del df_아샴2_요일별['전시명']
    # del df_아샴2_요일별['년']
    # del df_아샴2_요일별['월']
    # df_아샴2_요일별[["관람객","무료","유료"]] = df_아샴2_요일별[["관람객","무료","유료"]].apply(pd.to_numeric) 
    # # df_아샴2_요일별.index = df_아샴2_요일별.index+1
    # # df_아샴2_요일별.index.name = '주차'
    # # df_아샴2_요일별 = df_아샴2_요일별.dorp(['전시명'], axis=1)
    # df_아샴2_요일별 = df_아샴2_요일별.sort_values('관람객', ascending=False)
    # df_아샴2_요일별 = df_아샴2_요일별[['관람객','일자','일차','유료','무료']]
    # df_아샴2_요일별 = df_아샴2_요일별.set_index('관람객')
    # st.dataframe(df_아샴2_요일별, use_container_width=True)


with tab3:
    st.expander("🔍세부내역 - 최근실적", expanded=False)
    st.markdown("Crurrent Exhibition Average Visitors")

    

    # if 전일대비 >= 0:
    #     st.balloons()
    #     st.popover(f'전일대비 관람객 {전일대비}명 증가', help=None, disabled=False, use_container_width=False)
    # else :
    #     st.snow()
    #     st.popover(f'전일대비 관람객 {전일대비*-1}명 감소', help=None, disabled=False, use_container_width=False)


    global 일차3
    # 일차3 = st.slider("Select Working days : ", 1, MAX_Day, value=MAX_Day) # 슬라이더 수직필요해서 일단 중지
    일차3 = 진행기간
    S_df2 = df_MAX_D_line[df_MAX_D_line["일차"] <= 일차3]
    S_df2 = S_df2.reset_index()
    S_df2 = S_df2.loc[S_df2['전시명']=='아샴']
    # st.dataframe(S_df2)

    S_df_selection = S_df2.query(
    "일차 <=@일차3")
    S_df_selection["누적관람객"] = S_df_selection["관람객"].cumsum()

    S_df_selection["일평균"] = round(S_df_selection["누적관람객"]/S_df_selection["일차"],0)
    # st.dataframe(S_df_selection)
    
    # st.scatter_chart(S_df_selection, x='일차', y='일평균', size='관람객', color='#9CB7E2', mode="lines+markers+text", text='일평균',width=0, height=700, use_container_width=True)
    # st.scatter_chart(S_df_selection, x='일차', y='일평균', size='관람객', color='#9CB7E2',width=0, height=700, use_container_width=True)
    # st.bar_chart(S_df_selection, x='일차', y='일평균', color='#9CB7E2',use_container_width=True)
    
 #########################################################3  
  
    # st.dataframe(S_df_selection)   
    my_config ={"scrollZoom" : False, "displayModeBar":False}
    fig_일자별 = make_subplots(specs=[[{"secondary_y":True}]])
    fig_일자별.add_trace(
        go.Bar(name ="누적", x=S_df_selection['일차'], y=S_df_selection['누적관람객']),secondary_y=False) #text=S_df_selection['누적관람객'],textposition = "inside", textfont_size=2
    fig_일자별.add_trace(
        go.Scatter(name ="일평균", x=S_df_selection['일차'], y=S_df_selection['일평균'], line_color='#f2f7f5', line_width=1),secondary_y=True) #mode="lines+markers+text",text=S_df_selection['일평균'],textposition = "top center", textfont_size=10
    
    fig_일자별.add_trace(
        go.Scatter(name ="일별관람객", x=S_df_selection['일차'], y=S_df_selection['관람객'], line_width=1, line_color='#f00732'), secondary_y=True) #,mode="lines+markers+text",text=S_df_selection['일평균'],textposition = "top center", textfont_size=10, line_color='#75451b', 
    fig_일자별.update_traces(marker_color='rgb(54, 65, 89)', marker_line_color='rgb(54, 65, 89)',
    # fig_t2.update_traces(marker_color = '#91645d;', marker_line_color='rgb(8,48,107)',
                      marker_line_width=1.5, opacity=0.6)
    

    fig_일자별.update_layout(xaxis=dict(showgrid=False),
              yaxis=dict(showgrid=False)
    )
    fig_일자별.update_yaxes(showticklabels=False)
    fig_일자별.update_layout(xaxis_rangeslider_visible=False)
    # fig_일주.update_layout(xaxis_rangeslider_visible=True)
    # fig_일주.update_layout(yaxis=dict(title=None,showgrid=False,showline=False))
    fig_일자별.update_layout(yaxis=dict(title=None,showgrid=False,showline=False))
    

    fig_일자별.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    # bgcolor="nation",
    x=1,
    
    # color='lifeExp'
    ))
    
    # st.dataframe(S_df_selection)
    누적_t = round(S_df_selection.iloc[-1].loc["누적관람객"]/1000,1)
    일별_t = S_df_selection.iloc[-1].loc["관람객"]
    일평균_t = int(S_df_selection.iloc[-1].loc["일평균"])
    일평균_t_전일 = int(S_df_selection.iloc[-2].loc["일평균"])
    # )
    c5 = st.container(border=True)
    c5.write(f'<p class ="ctn"> {진행기간}일차 누적관람객 : {누적_t}만명</p>', unsafe_allow_html=True)
    c5.write(f'<p class ="ctn">일평균관람객 : {일평균_t}명 (전일 : {일평균_t_전일}명)</p>', unsafe_allow_html=True)

    

    # st.markdown(f" {진행기간}일차 누적관람객 : {누적_t}만명") 
    # st.markdown(f"        일평균관람객 : {일평균_t}명 ") 
    

    ## 일단숨김
    # st.plotly_chart(fig_일자별, use_container_width=True, congig=my_config)
    ## 일단숨김

#########################################################3
    # fig_t = go.Figure()
    # fig_t = fig_t.add_trace(st.Scatter_chart(x=S_df_selection['일차'], y=S_df_selection['일평균'], size=S_df_selection['관람객']), color='#9CB7E2', width=0, height=0)
    # fig_t.update_layout(legend=dict(
    #     orientation="h",
    #     yanchor="bottom",
    #     y=1.02,
    #     xanchor="right",
    #     x=1
    #     ))
    # fig_t.update_yaxes(showticklabels=False)
    # st.plotly_chart(fig_t, use_container_width=True)
        # 컬러참조 : https://docs.streamlit.io/develop/api-reference/widgets/st.color_picker


# c5 = st.container(border=True)
#         c5.write(f'<p class ="ctn2">{option4} 트랜드 반영 시 아샴예상관람객 : {경과감안관람객추정}만명</p>', unsafe_allow_html=True)
    st.markdown('--------------')    
        

    font_css ='''
            <style>
                .streamlit-expanderHeader.st-ae.st-dj.st-ag.st-ah.st-ai.st-aj.st-bv.st-dk.st-bw.st-dl.st-dm.st-dn.st-do.st-ar.st-as.st-dp.st-dq.st-b3.st-cj.st-c5.st-dr.st-b4.st-ds.st-c3.st-c4.st-c2.st-c1{
                    font-size:30px;
                    text-align:center;     
                    color:blue;
                    background-color :red;
            }
            </style>
            
        '''
    st.write(font_css,unsafe_allow_html = True)

        
    with st.expander(f"☑️ 아샴 최근10일 평균관람객 :red-background[Balloons or Snow]"):
        # https://background-colors.streamlit.app/
    
    # # st.button(f"☑️ 아샴 최근10일 평균관람객 :gray-background[Balloons or Snow]")
    # if st.button(f"☑️ 아샴 최근10일 평균관람객 :gray-background[Balloons or Snow]") is True:
        # st.markdown("Weekly Average")
        경과주차 = MAX_Day//7+1
        진행주차 = MAX_Day%7

        # 주차9 = st.slider("Select Working Weeks : ", 1, 경과주차-1, value=경과주차-1) # 슬라이더 수직필요해서 일단 중지

        # try:


            # st.dataframe(df_MAX_D_line)

        # ################
        # try:
        #     # global 주차9
        #     주차9 = st.slider("Select Working Weeks : ", 1, 경과주차-1, value=경과주차-1) # 슬라이더 수직필요해서 일단 중지
        # except:
        #     pass
        # 
        주차9 = 경과주차    
        # df_MAX_D = S_df.loc[(S_df['전시명'] == '아샴') & (S_df['관람객'] > 0) & (S_df['주차'] <= MAX_Day)]
        # S_df = S_df.reset_index()
        
        # st.dataframe(df_MAX_D_line)

        # S_df2 = df_MAX_D_line_주차별관람객[df_MAX_D_line_주차별관람객["주차"] <= 경과주차]
        # S_df_selection2 = S_df2.groupby(by=["전시명","주차"]).sum()[["관람객"]].sort_values(by=["전시명","주차","관람객"], ascending=False)
        # df_MAX_D_line["주차"] = df_MAX_D_line['일차'].apply(lambda x: (x//7)+1)
    #     # S_df_t = df_MAX_D_line[df_MAX_D_line["주차"] <= 주차9]
        S_df_t = df_MAX_D_line

        # S_df_t = S_df_t.reset_index()
        # st.dataframe(S_df_selection_t)
        S_df_t = S_df_selection_t.loc[S_df_selection_t['전시명']=='아샴']
        S_df_selection_t = S_df_t.query(
            "주차 <= @주차9")

        df_MAX_D_line_MAX = S_df_selection_t.groupby(['전시명','주차'])['관람객'].agg(**{'최대값':lambda x : x.max()}).reset_index()
        df_MAX_D_line_MIN = S_df_selection_t.groupby(['전시명','주차'])['관람객'].agg(**{'최소값':lambda x : x.min()}).reset_index() #0이 아닌 값중 최소값
        df_MAX_D_line_주차별관람객 = S_df_selection_t.groupby(['전시명','주차'])['관람객'].agg(**{'주차별관람객':lambda x : x.sum()}).reset_index() #0이 아닌 값중 최소값
        df_MAX_D_line_fir = S_df_selection_t.groupby(['전시명','주차'])['관람객'].apply(lambda x: x.value_counts().index[0]).reset_index(name="fir")
        df_MAX_D_line_lst = S_df_selection_t.groupby(['전시명','주차'])['관람객'].apply(lambda x: x.value_counts().index[-1]).reset_index(name="lst")
        
        
        

        df_MAX_D_line_MAX = df_MAX_D_line_MAX.set_index(['전시명','주차'])
        df_MAX_D_line_MIN = df_MAX_D_line_MIN.set_index(['전시명','주차'])
        df_MAX_D_line_주차별관람객 = df_MAX_D_line_주차별관람객.set_index(['전시명','주차'])
        df_MAX_D_line_fir = df_MAX_D_line_fir.set_index(['전시명','주차'])
        df_MAX_D_line_lst = df_MAX_D_line_lst.set_index(['전시명','주차'])
        
        df_MAX_D_line_RANGE = pd.merge(df_MAX_D_line_MAX,df_MAX_D_line_MIN, on=['전시명','주차'])
        df_MAX_D_line_RANGE = pd.merge(df_MAX_D_line_RANGE,df_MAX_D_line_fir, on=['전시명','주차'])
        df_MAX_D_line_RANGE = pd.merge(df_MAX_D_line_RANGE,df_MAX_D_line_lst, on=['전시명','주차'])
        df_MAX_D_line_RANGE = pd.merge(df_MAX_D_line_RANGE,df_MAX_D_line_주차별관람객, on=['전시명','주차'])

        df_MAX_D_line_RANGE = df_MAX_D_line_RANGE.reset_index()
        df_MAX_D_line_주차별관람객 = df_MAX_D_line_주차별관람객.reset_index()
        df_MAX_D_line_RANGE['누적관람객'] = df_MAX_D_line_주차별관람객['주차별관람객'].cumsum()
        df_MAX_D_line_RANGE['일평균관람객'] = round(df_MAX_D_line_RANGE['누적관람객']/(df_MAX_D_line_RANGE['주차']*7),0)
        df_MAX_D_line_RANGE['주평균관람객'] = round(df_MAX_D_line_RANGE['주차별관람객']/7,0)
        # st.dataframe(df_MAX_D_line_RANGE)
        
        ## 주말 최소, 최대 그래프 확인 필요
        
        # except:
        #     pass    

        
        # st.text("이중축그래프 테스트")
        # fig_t1 = px.bar(x=df_MAX_D_line_RANGE['주차'],y=df_MAX_D_line_RANGE['누적관람객'])
        # # st.plotly_chart(fig_t1, use_container_width=True)
        
        # fig_t2 = make_subplots(specs=[[{"secondary_y":True}]])

        # fig_t2.add_trace(
        #      go.Bar(x=df_MAX_D_line_RANGE['주차'],y=df_MAX_D_line_RANGE['누적관람객'],text=df_MAX_D_line_RANGE['누적관람객'], textposition = "inside", textfont_size=13),
        #      secondary_y=False,
        # )
        # fig_t2.add_trace(
        #      go.Scatter(x=df_MAX_D_line_RANGE['주차'],y=df_MAX_D_line_RANGE['일평균관람객'],mode="lines+markers+text",text=df_MAX_D_line_RANGE['일평균관람객'], textposition = "top center", textfont_size=13),
        #      secondary_y=True,
        # )
        # st.plotly_chart(fig_t2, use_container_width=True)

    ################# 다시확인필요
        # try:
        st.markdown(f"Full weeks: {경과주차-1}th weeks")

        df_MAX_D_line["주차"] = df_MAX_D_line['일차'].apply(lambda x: (x//7)+1)
        # df_MAX_D_line["주평균"] = df_MAX_D_line['관람객'].apply(lambda x: (x//7)+1)
        df_MAX_D_line["주평균"] = round(df_MAX_D_line_RANGE['주차별관람객']/7,0)
        # st.dataframe(df_MAX_D_line_RANGE)
        # # st.dataframe(df_MAX_D_line)
        # try:
        #     global 주차
        #     주차3 = st.slider("주차선택 : ", 1, 경과주차-1) # 슬라이더 수직필요해서 일단 중지
        # except:
        #         pass
                

        S_df2 = df_MAX_D_line[df_MAX_D_line["주차"] <= 주차9]
        # st.dataframe(S_df2)
        S_df2 = S_df2.reset_index()
        S_df2 = S_df2.loc[S_df2['전시명']=='아샴']
        S_df_selection = df_MAX_D_line_RANGE.query(
        "주차 <=@주차9")
        # df_MAX_D_line_RANGE= df_MAX_D_line_RANGE
        # S_df_selection2 = df_MAX_D_line_RANGE.groupby(by=["주차"]).sum()[["관람객", "주평균"]]
        S_df_selection2 = df_MAX_D_line_RANGE.reset_index()
        # st.dataframe(S_df_selection2)
        # S_df_selection2 = S_df_selection2
        # st.dataframe(S_df_selection2)
        # visitor2 = S_df_selection2.reset_index() # 변경
        # df_line = visitor2[visitor2["주차"] <= 주차3] # 기존
        # fig_t = go.Figure()
        # fig_t.add_traces(go.scatter(S_df_selection2, x='주차', y='주평균관람객', size='주평균관람객', color='#9CB7E2', width=0, height=0))
        # fig_t.add_trace(go.Scatter(mode="markers+text", text='주평균관람객'))
        


        # st.scatter_chart(S_df_selection2, x='주차', y='주평균관람객', size='주평균관람객',color='#9CB7E2', width=0, height=700, use_container_width=True)
        # try:
        my_config ={"scrollZoom" : False, "displayModeBar":False}
        fig_일주 = make_subplots(specs=[[{"secondary_y":True}]])
        fig_일주.add_trace(
            go.Bar(name="일평균",x=S_df_selection2['주차'], y=S_df_selection2['일평균관람객'],text=S_df_selection2['일평균관람객'],textposition = "inside", textfont_size=15), secondary_y=False)
        fig_일주.add_trace(    
            # go.Scatter(name="주평균",x = S_df_selection2['주차'], y=S_df_selection2['주평균관람객'], size=S_df_selection2['주평균관람객']), secondary_y=True)
            go.Scatter(name="주평균", x=S_df_selection2['주차'], y=S_df_selection2['주평균관람객'],mode="lines+markers+text",text=S_df_selection2['주평균관람객'],textposition = "top center", textfont_size=15, line_color='#75451b', line_width=3), secondary_y=True)
        # https://wikidocs.net/187241

        fig_일주.update_traces(marker_color='rgb(54, 65, 89)', marker_line_color='rgb(54, 65, 89)',
        # fig_t2.update_traces(marker_color = '#91645d;', marker_line_color='rgb(8,48,107)',
                        marker_line_width=1.5, opacity=0.6)
        

        fig_일주.update_layout(xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=False)
        )
        fig_일주.update_yaxes(showticklabels=False)
        fig_일주.update_layout(xaxis_rangeslider_visible=False)
        # fig_일주.update_layout(xaxis_rangeslider_visible=True)
        # fig_일주.update_layout(yaxis=dict(title=None,showgrid=False,showline=False))
        fig_일주.update_layout(yaxis=dict(title=None,showgrid=False,showline=False))
        

        fig_일주.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
        ))

        S_df_아샴최근일주일 = df.dropna(subset=['전시명'], how='any', axis=0)

        S_df_아샴최근일주일 = S_df_아샴최근일주일[S_df_아샴최근일주일['전시명'] != 0]
        mask = (S_df_아샴최근일주일.dropna(subset=['전시명'], how='any', axis=0).전시명 =="아샴")
        
        S_df_아샴최근일주일 = S_df_아샴최근일주일.loc[mask, :]
        S_df_아샴최근일주일['누적관람객'] = S_df_아샴최근일주일['관람객'].cumsum()
        S_df_아샴최근일주일 = S_df_아샴최근일주일[S_df_아샴최근일주일["일차"]>=MAX_Day-9]
        S_df_아샴최근일주일 = S_df_아샴최근일주일[S_df_아샴최근일주일['관람객'] != 0]
        S_df_아샴최근일주일["일평균관람객"] = round(S_df_아샴최근일주일['누적관람객']/S_df_아샴최근일주일['일차'],0)
        
        아샴목표일평균 = int(40000/94)
        threshold2 = 아샴목표일평균
        threshold3 = int(45000/94)
        threshold4 = int(50000/94)

        res1 = S_df_아샴최근일주일.loc[S_df_아샴최근일주일['일차'] == MAX_Day, '일평균관람객'].iloc[0]
        res2 = S_df_아샴최근일주일.loc[S_df_아샴최근일주일['일차'] == MAX_Day-1, '일평균관람객'].iloc[0]
        
        # st.dataframe(res1)
        res = res1 - res2

        bars = alt.Chart(S_df_아샴최근일주일).mark_bar(color="steelblue").encode(
            x="일차",
            # y="일평균관람객:Q",
            y=alt.Y("일평균관람객:Q",axis=alt.Axis(labels=False)),

            # color='일평균관람객'
            # text="관람객",
            color=alt.Color('일평균관람객', legend=alt.Legend(
            orient='top',
            legendX=130, legendY=-40,
            direction='horizontal',
            titleAnchor='middle'))
        ).properties(height=500)
        

        line = alt.Chart(S_df_아샴최근일주일).mark_line(interpolate="monotone").encode(

            x="일차:Q",
            # y="일평균관람객:Q",
            # y=alt.Y("일평균관람객:Q",axis=alt.Axis(labels=False)),
            y="일평균관람객:Q",
            # mode="lines", line_color='white', line_width=13
            # mode="lines", line_color='#f5f5eb', line_width=3
        
        )
        highlight = bars.mark_bar(color="#f5f5eb").encode(
            y2=alt.Y2(datum=threshold2)
        ).transform_filter(
            alt.datum.Value > threshold2
        )

        text = alt.Chart(S_df_아샴최근일주일).mark_text(dx=0, dy=0, align='center',baseline='bottom',color='white', size=15).encode(
            x=alt.X('일차', sort=None), y='일평균관람객', detail='일평균관람객', text=alt.Text('일평균관람객:Q'))


        rule = alt.Chart().mark_rule(color="#f5f5eb").encode(
            y=alt.Y(datum=threshold2)
        )

        label = rule.mark_text(
            x="width",
            dx=-2,
            align="left",
            baseline="bottom",
            text="4.0만",
            size=15,
            color='white'
        )


        rule2 = alt.Chart().mark_rule(color="#f5f5eb").encode(
            y=alt.Y(datum=threshold3)
        )

        label2 = rule2.mark_text(
            x="width",
            dx=-2,
            align="left",
            baseline="bottom",
            text="4.5만",
            size=15,
            color='white'
        )

        rule3 = alt.Chart().mark_rule(color="#f5f5eb").encode(
            y=alt.Y(datum=threshold4)
        )

        label3 = rule3.mark_text(
            x="width",
            dx=-2,
            align="left",
            baseline="bottom",
            text="5.0만",
            size=15,
            color='white'
        )



        if res >= 0:
            st.balloons()
            c5 = st.container(border=True)
            c5.write(f'<p class ="ctn2"> 😁전일대비 일평균관람객 {res}명 증가</p>', unsafe_allow_html=True)
            
        else :
            st.snow()
            c5 = st.container(border=True)
            c5.write(f'<p class ="ctn2"> 🤔전일대비 일평균관람객 {res*-1}명 감소</p>', unsafe_allow_html=True)


    # (bars + highlight + rule + label)
        st.altair_chart(bars + line + text + highlight + rule + label + rule2 + label2 + rule3 + label3, use_container_width=True)

   
    st.markdown('--------------')
    with st.expander("Average Visitor"): 
    # st.markdown("Average Visitor")
        choice = st.radio(
            f"Total Aver or {진행기간}th day Aver Choice",
            ["Total Aver", f"{진행기간}th day &nbsp;Aver"],
            key="Total Sum",
            # label_visibility=st.session_state.visibility,
            # disabled=st.session_state.disabled,
            # horizontal=st.session_state.horizontal,
        )
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        # st.write("You selected:", choice)

        if choice == 'Total Aver':
        # st.write('You like coding.')


        # st.write("You do not like coding.")

            S_df_기존_아샴제외 = S_df_기존[S_df_기존['전시명'] != "아샴"]
            S_df_기존_아샴제외 = S_df_기존_아샴제외.sort_values(by=['일평균'], axis=0, ascending=False)
            
            st.dataframe(S_df_기존_아샴제외, hide_index=True , use_container_width=True)
        else:
            S_df_기존_아샴포함 = S_df_기존_진행일차
            S_df_기존_아샴포함 = S_df_기존_아샴포함.sort_values(by=['일평균'], axis=0, ascending=False)
            # S_df_기존_아샴포함 = S_df_기존_아샴포함.reset_index()
            S_df_기존_아샴포함 = S_df_기존_아샴포함.set_index('전시명')   
            S_df_기존_아샴포함 = S_df_기존_아샴포함.style.format(
                {
                    "관람객": lambda x : '{:,.0f}'.format(x),
                    "일평균": lambda x : '{:,.0f}'.format(x),
                },
            decimal=','
            )


            def color_vowel(value):
                return f"background-color: gray; font color: black"
            # 스타일 이후 가능
            
            # # https://zephyrus1111.tistory.com/62
            
            # S_df_기존_아샴포함 = S_df_기존_아샴포함[S_df_기존_아샴포함["전시명"] =="아샴"]

            
            # st.dataframe(S_df_기존_아샴포함)
            # st.dataframe(S_df_기존_아샴포함.map(color_vowel, subset=pd.IndexSlice['아샴','관람객':'일평균']), hide_index=True , use_container_width=True)
            # st.dataframe(S_df_1)
            # st.dataframe(S_df_기존_아샴포함, use_container_width=True)
            st.dataframe(S_df_기존_아샴포함.map(color_vowel, subset=pd.IndexSlice['아샴','관람객':'일평균']), use_container_width=True)
            
            
            
            # st.dataframe(S_df_기존_아샴포함, hide_index=True , use_container_width=True)
            # st.dataframe(S_df.map(color_vowel, subset=pd.IndexSlice['아샴','순위':'현상']), use_container_width=True) #★ 향후 전시명이 아샴일 경우로 조건문 조절 필요
###############################################################
# bars = alt.Chart(source).mark_bar(color="steelblue").encode(
#     x="Day:O",
#     y="Value:Q",
# )

# highlight = bars.mark_bar(color="#e45755").encode(
#     y2=alt.Y2(datum=threshold)
# ).transform_filter(
#     alt.datum.Value > threshold
# )

# rule = alt.Chart().mark_rule().encode(
#     y=alt.Y(datum=threshold)
# )

# label = rule.mark_text(
#     x="width",
#     dx=-2,
#     align="right",
#     baseline="bottom",
#     text="hazardous"
# )

# (bars + highlight + rule + label)





#####################################################33
#★★★ https://altair-viz.github.io/gallery/bar_chart_with_single_threshold.html


#     chart = alt.Chart(S_df_아샴최근일주일, title='최근일주일관람객').mark_bar().encode(
# 	    x=alt.X('일차', sort=None), y=alt.Y('일평균관람객'),  color='일평균관람객')
#     # ,trendline="ols"
#     text = alt.Chart(S_df_아샴최근일주일).mark_text(dx=0, dy=0, align='center',baseline='bottom',color='white', size=13).encode(
# 	    # x=alt.X('일차', sort=None), y='일평균관람객',  detail='일평균관람객', text=alt.Text('일평균관람객:Q'))
# 	    x=alt.X('일차', sort=None),  y=alt.Y('일평균관람객'),  detail='일평균관람객', text=alt.Text('일평균관람객:Q'))

# # chart.update_layout(font=dict(size=14))
    
#     st.altair_chart(chart+text, use_container_width=True)
#     # st.altair_chart(chart, use_container_width=True)


# https://discuss.streamlit.io/t/turn-vertical-bar-chart-to-horizontal/20107/4





















with tab2:
# st.dataframe(df_MAX_D_line)

    # 경과주차 = MAX_Day//7+1
    # 진행주차 = MAX_Day%7
    # st.dataframe(경과주차)

    st.error("ⅰ. 야샴 요일별 평균관람객")
    # st.info(f"전시별 누적관람객 - 아샴(진행중) : {당일누적관람객}만명  \n(일평균 : {아샴일평균}명)")
    # st.dataframe(df_아샴2)
    df_아샴2_요일평균 = df_아샴2.groupby(['요일'])['관람객'].agg(**{'평균':lambda x : x.mean()}).reset_index()
    df_아샴2_요일평균 = df_아샴2_요일평균.sort_values(by=['평균'], axis=0, ascending=False)
    df_아샴2_요일평균['평균'] = round(df_아샴2_요일평균['평균'],1)
    st.dataframe(df_아샴2_요일평균,hide_index=True, use_container_width=True)

    전시명4 = 전시명4.tolist()
    with st.expander("🔍세부내역"):
        option40 = st.selectbox(
        'Select Day of the week',
        (전시명4),
        # 형식을 요일으로 변경
        index = 전시명4.index(MAX_Date.strftime('%A')),
        )
        df_아샴2_요일별 = df_아샴2[df_아샴2['요일'] ==option40]
        df_아샴2_요일별 = df_아샴2_요일별.reset_index()
        del df_아샴2_요일별['요일']
        del df_아샴2_요일별['전시명']
        del df_아샴2_요일별['년']
        del df_아샴2_요일별['월']
        df_아샴2_요일별[["관람객","무료","유료"]] = df_아샴2_요일별[["관람객","무료","유료"]].apply(pd.to_numeric) 
        df_아샴2_요일별 = df_아샴2_요일별.sort_values('관람객', ascending=False)
        df_아샴2_요일별 = df_아샴2_요일별[['관람객','일자','일차','유료','무료']]
        st.dataframe(df_아샴2_요일별, hide_index=True, use_container_width=True)
    st.markdown('--------------')
    
    st.error("ⅱ. 주중대비 주말 평균관람객 비교")
    with st.expander("🔍세부내역"):



        # st.dataframe(df_MAX_D_line_RANGE,hide_index=True, use_container_width=True)
        
        # df_all = df_all[df_all['전시명'] != 0]
        # df_all = df_all[df_all['전시명'] != 'nan']
        전시명3 = df_all["전시명"].dropna().unique()
        df_all = df_all[df_all['전시명'] != 0]
        df_all = df_all[df_all['전시명'] != 'nan']

        전시명44 = df_all["전시명"].dropna().unique()
        option44 = st.selectbox(
        'Reference Exhibition',
        (전시명44),
        index=len(전시명44)-1,
        )



        주차80 = st.number_input("주차선택  :", min_value=1, max_value=20, step=1, format="%i", value = 경과주차-1)
        # 주차80 = st.slider("Select Working Weeks  : ", 1, 20, value=경과주차-1) # 슬라이더 수직필요해서 일단 중지

        S_df_tt["주차"] = S_df_tt['일차'].apply(lambda x: (x//7)+1)
        # st.dataframe(S_df_tt)

        
        


        S_df_t = S_df_tt[S_df_tt["주차"] <= 주차80]
        S_df_t = S_df_t.reset_index()
        S_df_t = S_df_t.loc[S_df_t['전시명'] == option44]
        S_df_selection_t = S_df_t.query(
            "주차 <= @주차80")
        S_df_selection_t["누적관람객2"] = S_df_selection_t['관람객'].cumsum()
        S_df_selection_t["일평관람객2"] = round(S_df_selection_t['누적관람객2']/S_df_selection_t['일차'])

        df_MAX_D_line_MAX = S_df_selection_t.groupby(['전시명','주차'])['관람객'].agg(**{'최대값':lambda x : x.max()}).reset_index()
        df_MAX_D_line_MIN = S_df_selection_t.groupby(['전시명','주차'])['관람객'].agg(**{'최소값':lambda x : x.min()}).reset_index() #0이 아닌 값중 최소값
        df_MAX_D_line_주차별관람객 = S_df_selection_t.groupby(['전시명','주차'])['관람객'].agg(**{'주차별관람객':lambda x : x.sum()}).reset_index() #0이 아닌 값중 최소값
        
        df_MAX_D_line_fir = S_df_selection_t.groupby(['전시명','주차'])['관람객'].apply(lambda x: x.value_counts().index[0]).reset_index(name="fir")
        df_MAX_D_line_lst = S_df_selection_t.groupby(['전시명','주차'])['관람객'].apply(lambda x: x.value_counts().index[-1]).reset_index(name="lst")
        
        
        

        df_MAX_D_line_MAX = df_MAX_D_line_MAX.set_index(['전시명','주차'])
        df_MAX_D_line_MIN = df_MAX_D_line_MIN.set_index(['전시명','주차'])
        df_MAX_D_line_주차별관람객 = df_MAX_D_line_주차별관람객.set_index(['전시명','주차'])
        df_MAX_D_line_fir = df_MAX_D_line_fir.set_index(['전시명','주차'])
        df_MAX_D_line_lst = df_MAX_D_line_lst.set_index(['전시명','주차'])
        
        df_MAX_D_line_RANGE = pd.merge(df_MAX_D_line_MAX,df_MAX_D_line_MIN, on=['전시명','주차'])
        df_MAX_D_line_RANGE = pd.merge(df_MAX_D_line_RANGE,df_MAX_D_line_fir, on=['전시명','주차'])
        df_MAX_D_line_RANGE = pd.merge(df_MAX_D_line_RANGE,df_MAX_D_line_lst, on=['전시명','주차'])
        df_MAX_D_line_RANGE = pd.merge(df_MAX_D_line_RANGE,df_MAX_D_line_주차별관람객, on=['전시명','주차'])


        df_MAX_D_line_RANGE = df_MAX_D_line_RANGE.reset_index()
        df_MAX_D_line_주차별관람객 = df_MAX_D_line_주차별관람객.reset_index()
        df_MAX_D_line_RANGE['누적관람객'] = df_MAX_D_line_주차별관람객['주차별관람객'].cumsum()
        df_MAX_D_line_RANGE['일평균관람객'] = round(df_MAX_D_line_RANGE['누적관람객']/(df_MAX_D_line_RANGE['주차']*7),0)
        df_MAX_D_line_RANGE['주평균관람객'] = round(df_MAX_D_line_RANGE['주차별관람객']/7,0)


        # st.dataframe(S_df_selection_t)
        # df_아샴2_평일 = df_MAX_D_line_RANGE[df_MAX_D_line_RANGE['평일휴일']=='평일'].mean(skipna=True)
        # df_아샴2_주말 = df_MAX_D_line_RANGE[df_MAX_D_line_RANGE['평일휴일']=='주말'].mean(skipna=True)

        df_아샴2_주말평일 = S_df_selection_t.groupby(['평일휴일'])['관람객'].agg(**{'평균':lambda x : x.mean()}).reset_index()
        # df_아샴2_wnakf = df_MAX_D_line_RANGE.groupby(['평일휴일'])['관람객'].agg(**{'평균':lambda x : x.mean()}).reset_index()
        
        # st.dataframe(df_아샴2_주말평일)

        평일 = df_아샴2_주말평일[df_아샴2_주말평일['평일휴일'] =='평일']
        주말 = df_아샴2_주말평일[df_아샴2_주말평일['평일휴일'] =='주말']

        # st.dataframe(평일)
        # st.dataframe(주말)


        평일v = 평일.iloc[0].loc["평균"]
        주말v = 주말.iloc[0].loc["평균"]
        # st.text(평일v)
        # st.text(주말v)

        # 평일 = df_아샴2_주말평일[df_아샴2_주말평일['평일휴일'] =='평일'].loc['평균']
        # 주말 = df_아샴2_주말평일[df_아샴2_주말평일['평일휴일'] =='주말'].loc['평균']
        주말지수 = 1 + round((주말v/평일v)*100,1)

        # st.text(주말지수)

        
    
        
        c5 = st.container(border=True)
        # c5.write(f'<p class ="ctn">{일차}일차 누적 관람객 : {누적관람객}명</p>', unsafe_allow_html=True)
        c5.write(f'<p class ="ctn">{option44}-{주차80}주차 주말/평일 평균관람객% : {주말지수}%</p>', unsafe_allow_html=True)
        c5.write(f'<p class ="ctn"><평일평균:{round(평일v,1)}명, 주말평균:{round(주말v,1)}명></p>', unsafe_allow_html=True)
    
    # c5 = st.container(border=True)     
    # c5.write(f'<p class ="ctn">주별 관람객 분포 -  {option44}  <  {주차80}주차  ></p>', unsafe_allow_html=True)
    #     # st.error(f'주별 관람객 분포 -  {option44}  <  {주차80}주차  >')



    # with st.expander("세부내역보기"):
        c5 = st.container(border=True)     
        c5.write(f'<p class ="ctn">주별 관람객 분포 -  {option44}  <  {주차80}주차  ></p>', unsafe_allow_html=True)
    
        bar = alt.Chart(S_df_selection_t).mark_bar(cornerRadius=10, height=20).encode(
            x=alt.X('min(관람객):Q').scale(domain=[0, S_df_selection_t['관람객'].max()]).title('관람객'),
            x2='max(관람객):Q',
            y=alt.Y('주차:O').title("주차"),
            color=alt.value("#116EA1"),
            
        )
        # .configure_
        
    # bar.configure_title(fontSize=14).configure(background='#D9E9F0')
        text_min = alt.Chart(S_df_selection_t).mark_text(align='right', dx=-5,color='white', size=13).encode(
            x='min(관람객):Q',
            y=alt.Y('주차:O'),
            text='min(관람객):Q',
            # color= "white"
        ).properties(height=500)

        text_max = alt.Chart(S_df_selection_t).mark_text(align='left', dx=5,color='white',size=13).encode(
            x='max(관람객):Q',
            y=alt.Y('주차:O'),
            text='max(관람객):Q',
            # color="white"
        )
        # .properties(colors='white')

        # (bar + text_min + text_max).properties(
        #     title=alt.Title(text='Temperature variation by month', subtitle='Seatle weather, 2012-2015'))
        # .configure(background='#DDEEFF')
        # .configure(background='#DDEEFF')
        # st.altair_chart(bar + text_min + text_max, use_container_width=True).configure(background='#D9E9F0')
        st.altair_chart(bar + text_min + text_max, use_container_width=True)

















        # df_all = df_all[df_all['전시명'] != 0]
        # # df_all = df_all[df_all['전시명'] != 'nan']
        # 전시명3 = df_all["전시명"].dropna().unique()
        # option3 = st.selectbox(
        # 'Select Exhibition ',
        # (전시명3), index=8,
        # )

        # st.dataframe(S_df_tt)
        # S_df_t = S_df_t.loc[S_df_t['전시명'] == option3]
        # S_df_selection_t = S_df_t.query(
        #     "주차 <= @주차8")







    # 요일별은 나중에 다시살림
    # 전시명4[0],전시명4[1],전시명4[2],전시명4[3],전시명4[4],전시명4[5],전시명4[6],전시명4[7] =전시명4[2],전시명4[3],전시명4[4],전시명4[5],전시명4[6],전시명4[0],전시명4[1],전시명4[7]
    # try:
    #     전시명4[0],전시명4[1],전시명4[2],전시명4[3],전시명4[4],전시명4[5],전시명4[6] =전시명4[2],전시명4[3],전시명4[4],전시명4[5],전시명4[6],전시명4[0],전시명4[1]
    # except:
    #     pass

    # # st.text(전시명4)
    # # st.dataframe(df_아샴2)
    # # st.text(MAX_Date.weekday())
    # st.text(MAX_Date.isoweekday())
    # st.markdown(f'[참조] 아샴 요일별 실적 비교')
    # option40 = st.selectbox(
    # 'Select Day of the week',
    # (전시명4),
    # index=MAX_Date.weekday(),
    # # index=전시명4.index(MAX_Date.day_name()),
    # )

    # # , index= 전시명4.index(MAX_Day.day_name()
    # # st.text(MAX_Date.weekday())
    # # index_t= 전시명4.index(MAX_Day.day_name())
    # # st.text(index_t)
    # df_아샴2_요일별 = df_아샴2[df_아샴2['요일'] ==option40]
    # df_아샴2_요일별 = df_아샴2_요일별.reset_index()
    # del df_아샴2_요일별['요일']
    # del df_아샴2_요일별['전시명']
    # del df_아샴2_요일별['년']
    # del df_아샴2_요일별['월']
    # df_아샴2_요일별[["관람객","무료","유료"]] = df_아샴2_요일별[["관람객","무료","유료"]].apply(pd.to_numeric) 
    # # df_아샴2_요일별.index = df_아샴2_요일별.index+1
    # # df_아샴2_요일별.index.name = '주차'
    # # df_아샴2_요일별 = df_아샴2_요일별.dorp(['전시명'], axis=1)
    # df_아샴2_요일별 = df_아샴2_요일별.sort_values('관람객', ascending=False)
    # df_아샴2_요일별 = df_아샴2_요일별[['관람객','일자','일차','유료','무료']]
    # df_아샴2_요일별 = df_아샴2_요일별.set_index('관람객')
    # st.dataframe(df_아샴2_요일별, use_container_width=True)
    
            

    global 주차c
    st.markdown('--------------')
    st.error("ⅲ. Weekly Line Graph")
    with st.expander("📊 그래프"):    
        st.markdown(f"Full weeks: {경과주차-1}th")
        

        try:
            # global 주차c
            주차c = st.number_input("주차선택. :", min_value=1, max_value=20, step=1, format="%i", value = 경과주차-1)
            # 주차c = st.slider("Select Working Weeks : ", 1, 20, value= 경과주차-1) # 슬라이더 수직필요해서 일단 중지
        except:
            pass

        

        # st.dataframe(df_MAX_D_line)
        df_MAX_D_line["주차"] = df_MAX_D_line['일차'].apply(lambda x: (x//7)+1)
    
        # st.dataframe(df_MAX_D_line)
        S_df2 = df_MAX_D_line[df_MAX_D_line["주차"] <= 주차c]
        S_df_selection = S_df2.query(
        "주차 <=@주차c")
        S_df_selection2 = S_df2.groupby(by=["전시명","주차"]).sum()[["관람객"]].sort_values(by=["전시명","주차","관람객"], ascending=False)

        visitor2 = S_df_selection2.reset_index() # 변경
        df_line = visitor2[visitor2["주차"] <= 주차c] # 기존

        전시들 = {전시: df_line[df_line["전시명"] == 전시] for 전시 in 전시명}

        S_df_selection2 = S_df_selection2.groupby(by=["전시명","주차"]).sum()[["관람객"]]

        df_line = df_line[df_line['관람객'] != 0]
        # st.dataframe(df_line)
        df_line = df_line.style.format(
            {
                "관람객": lambda x : '{:,.0f}'.format(x),
            },
        decimal=','
        )
        #check
        
        
        st.write("Recently Exhibition")

    #######################ver2#######################

        S_df_selection2 = S_df_selection2[S_df_selection2['관람객'] != 0]
        S_df_selection2_ttt = S_df_selection2.reset_index()
        # st.dataframe(S_df_selection2_ttt)
        # c = alt.Chart(S_df_selection2).transform_filter(alt.datum.symbol != "아샴").mark_area().encode(
        c = alt.Chart(S_df_selection2_ttt).mark_line(interpolate="monotone", tooltip=True).encode(
        #  axis=alt.Axis(labels=False)
            x=alt.X("주차:Q",title=""),
            # y="관람객:Q",
            y=alt.Y("관람객:Q", type="quantitative", aggregate="mean", title=""),
            # color="전시명:N",
            color= alt.Color("전시명").legend(None),
            # color=alt.Color('전시명', legend=alt.Legend(orient='bottom',direction='vertical')),
            # color=alt.Color('전시명', legend=alt.Legend(orient='top',direction='horizontal')),
            
            tooltip=['전시명','주차','관람객'],
            strokeWidth=alt.condition(
                "datum.전시명 == '아샴'",
                alt.value(4),
                alt.value(1)),
            # row="전시명:N",
            # row=alt.Row("전시명:N").sort(["바스키아", "김정기", "드리머", "알렉스","페어리","마르지엘라","제이알","오스틴 리","아샴"]),
        ).properties(height=500)

        표식 = c.mark_circle(size=60).encode(alt.X('주차:Q'), alt.Y('관람객:Q'))

        #참고 스터디 사이트 https://altair-viz.github.io/altair-viz-v4/gallery/one_dot_per_zipcode.html#gallery-one-dot-per-zipcode
        # lst주차 = c.mark_circle().encode(x=alt.datum(경과주차-1)).transform_aggregate('관람객')
        # lst주차 = c.mark_circle().encode(x=alt.datum(경과주차-1)).transform_aggregate(groupby='전시명')
        lst주차 = c.mark_circle().encode(x=alt.X("fr['주차']:Q"), y=alt.Y("fr['관람객']:Q")).transform_aggregate(fr ='argmin(주차)',groupby=['전시명'])
        # 전시이름 = c.mark_text(align="left",dx=3).encode(x=alt.datum(경과주차-1), text="전시명").transform_aggregate(주차='argmin(주차)')
        전시이름 = lst주차.mark_text(align="left",dx=5, dy=-5,size=15).encode(text="전시명")

        # legend = c.mark_square(size=150).encode(y=alt.Y('전시명',axis=alt.Axis(domain=False, ticks=False)))
        # st.markdown(c.mark_square(size=150).encode(y=alt.Y('전시명',axis=alt.Axis(domain=False, ticks=False))))
        # ).properties(height=500).interactive()
        # nearest = alt.selection(type='single', nearest=True, on='mouseover',
        #                     fields=['관람객'])
        
        # text = line.mark_text(align='left', dx=3, dy=-3).encode(
        #     text=alt.condition('전시명:N', alt.value(' ')))

        ###############################################################

        # points = c.transform_filter(c).mark_circle(size=65)

        # tooltips = (
        # alt.Chart(S_df_selection2_ttt)
        # .mark_rule()
        # .encode(
        #     x="주차:Q",
        #     y=alt.Y("관람객:Q", type="quantitative", aggregate="mean"),
        #     opacity=alt.condition(c, alt.value(0.3), alt.value(0)),
        #     tooltip=[
        #         alt.Tooltip("전시명", title="전시명"),
        #         alt.Tooltip("주차", title="주차"),
        #         alt.Tooltip("관람객", title="관람객"),
        #     ],
        # )
        # .add_selection(c)
        # )

        ################################################################


        xrule = (
        alt.Chart(S_df_selection2_ttt)
        .mark_rule(color="cyan", strokeWidth=3)
        .encode(x=alt.datum(경과주차-1))
    )
        # st.markdown(c.color)
    # https://stackoverflow.com/questions/69436980/change-thickness-of-one-line-on-altair-chart
        
    # .configure_axis(grid=False)
        # #.properties(height=50, width=400)
        # st.altair_chart(c+xrule+tooltips+points, use_container_width=True)
        # st.altair_chart(c+xrule+lst주차+전시이름, use_container_width=True)

        test = alt.layer(c+xrule+전시이름+표식).configure_view(stroke=None).configure_axis(grid=False)

        st.altair_chart(test, use_container_width=True)

        # st.altair_chart(c+xrule+전시이름+표식, use_container_width=True)

        
#################################################


        # fig = go.Figure()
        # for 전시, df_line in 전시들.items():
        #     fig = fig.add_trace(go.Scatter(x=df_line["주차"], y=df_line["관람객"], name=전시, mode="lines+markers+text", text=df_line["관람객"], textposition = "top center"),
        #     # fig = fig.add_trace(go.Scatter(x=df_line["일차"], y=df_line["관람객"], name=전시, mode="lines"),
        #     )
        # fig = fig.update_layout(yaxis=dict(title=None,showgrid=False,showline=False))
    
        # fig.update_layout(legend=dict(
        # orientation="h",
        # yanchor="bottom",
        # y=1.02,
        # xanchor="right",
        # x=1,
        # ))
        # fig.update_yaxes(showticklabels=False)

    # grid 없에기 테스트 필요
    # fig.update_layout(grid=False)
    # https://plotly.com/python/legend/#legend-position
    # 일단기존 숨김
    # st.plotly_chart(fig, use_container_width=True)





    # 경과주차2 = (MAX_Day//7) +1
    # try:
    #     global 주차2
    #     주차2 = st.slider("Select Working Weeks ; ", 1, 30, value=경과주차-1) # 슬라이더 수직필요해서 일단 중지 경과주차2
        
    # except:
    #         pass
    # S_df2 = df_MAX_D_line[df_MAX_D_line["주차"] <= 주차2]
    # S_df_selection = S_df2.query(
    # "주차 <=@주차2")
    # S_df_selection2 = S_df2.groupby(by=["전시명","주차"]).sum()[["관람객"]].sort_values(by=["전시명","주차","관람객"], ascending=False)

    # visitor3 = S_df_selection2.reset_index() # 변경
    # # df_line3 = visitor3[(visitor3["주차"] <= 주차2) & ((visitor3["전시명"] == "드리머") | (visitor3["전시명"] == "아샴") | (visitor3["전시명"] == "김정기"))] # 기존
    # df_line3 = visitor3[(visitor3["주차"] <= 주차2) & ((visitor3["전시명"] != "드리머") | (visitor3["전시명"] != "윤협") | (visitor3["전시명"] != "김정기"))] # 해외전시만
    # st.dataframe(df_line3)
    # # 국내전시들 = df_line3["전시명"].unique()

    # # 국내전시들 = {국내전시: df_line3[df_line3["전시명"] == 국내전시] for 국내전시 in 국내전시들}

    # 해외전시들 = df_line3["전시명"].unique()

    # 해외전시들 = {해외전시: df_line3[df_line3["전시명"] == 해외전시] for 해외전시 in 해외전시들}

    
    # # check
    # 일차 = st.slider("Select Working days ; ", 1, 150, value=진행기간-1) # 슬라이더 수직필요해서 일단 중지 경과주차2

    # df_line3 = df_line3.groupby(by=["전시명","주차"]).sum()[["관람객"]]
    # df_line3= df_line3.reset_index()
    # # st.write("<h7 style='text-align: left; color: white;'> Compare Domestic Exhibition :</h7>", unsafe_allow_html=True)
    # st.write("<h7 style='text-align: left; color: white;'> Compare Foreign Exhibition :</h7>", unsafe_allow_html=True)
    # # st.text("국내전 비교")
    # # st.write("<h8 style='text-align: left; color: white;'> 국내전 전체관람인원 :</h8>", unsafe_allow_html=True)
    # st.markdown(f"(아샴 full week {경과주차-1}th)")
    # fig2 = go.Figure()
    # # for 국내전시, df_line3 in 국내전시들.items():
    # for 해외전시, df_line3 in 해외전시들.items():
    
    #     # st.text(국내전시)
    # # for 국내전시, df_line3 in 국내전시들:
    #     # fig.add_trace(go.Scatter(x=df_line["주차"], y=df_line["관람객"], name=전시, mode="lines+markers+text", text=df_line["관람객"], textposition = "top center"),
    #     # fig.add_trace(go.Scatter(x=df_line["주차"], y=df_line["관람객"], name=전시, mode="lines+markers+text", text=df_line["관람객"], textposition = "top center"),
    #     fig2 = fig2.add_trace(go.Scatter(x=df_line3["주차"], y= [float("NaN") if x == 0 else  x  for x in df_line3["관람객"]], name=해외전시, mode="lines+markers+text",text=df_line3["관람객"], textposition = "top center", textfont_size=14),
    #     )
    #     fig2 = fig2.update_layout(yaxis=dict(title=None,showgrid=False,showline=False))
    # # st.dataframe(df_line3)
        
    #     # fig2 = fig2.add_trace(go.Scatter(textfont_size=[25 if  국내전시 == '아샴' else 13 for 국내전시, df_line3 in 국내전시들.items()]))
    #     # fig2 = fig2.add_trace(go.Scatter(textfont_size=[25 if  n == '아샴' else 13  for n in fig2.__annotations__])) 에러
    #     # fig2 = fig2.add_trace(go.Scatter(textfont_size=[25 if  n == '아샴' else 13  for n in go.Line.__annotations__])) 반응없음
    #     # fig2 = fig2.add_trace(go.Scatter(textfont_size=[25 if  n == '아샴' else 13  for n in go.])) 반응없음
        
    # # fig2.update_traces(
    # #     marker_color=['red' if y == highlighted_bar else 'grey' for y in df_line3["전시명"]],  # Blue for 'Clothing', grey for others
    # #     textfont_size=[25 if  y == highlighted_bar else 13 for y in df_line3["전시명"]],
    # #     # textposition='outside',  # Position the text inside the bars
    # #     # fig2 = fig2.add_trace(go.Scatter(x=df_line3["주차"], y=df_line3["관람객"], name=국내전시, mode="lines+markers+text",text=df_line3["관람객"], textposition = "top center"),
    # #     )
    #     fig2.update_layout(legend=dict(
    #     orientation="h",
    #     yanchor="bottom",
    #     y=25.02,
    #     xanchor="right",
    #     x=1
    #     ))
    #     fig2.update_yaxes(showticklabels=False)
    # # 일단기존 숨김##########
    # # st.plotly_chart(fig2, use_container_width=True)
    # # 일단기존 숨김##########

    # st.markdown("Compare Domestic Exhibition Visitors")
    st.markdown('--------------')
    st.error("ⅳ. Daily Line Graph")
    with st.expander("📊 그래프"):    
        st.markdown("Compare Foreign Exhibition Visitors")

        # 일단기존 숨김##########

        # st.dataframe(df_all_국내_전체.T, use_container_width=True)
        # 일단기존 숨김##########

        ##NEW############################################################
        # st.dataframe(df_MAX_D_line)
        # 일차 = st.slider("Select Working days ; ", 1, 150, value=진행기간) # 슬라이더 수직필요해서 일단 중지 경과주차2
        일차 = st.number_input("일차선택 : ", min_value=1, max_value=150, step=1, format="%i", value = MAX_Day)
        S_df_selection2 = df_MAX_D_line.reset_index()
        # S_df_selection2 = S_df_selection2[S_df_selection2['관람객'] != 0]
        # st.dataframe(S_df_selection2)
        # S_df_selection2_ttt_국내 = S_df_selection2[(S_df_selection2["주차"] <= 주차2) & ((S_df_selection2["전시명"] == "드리머") | (S_df_selection2["전시명"] == "아샴") | (visitor3["전시명"] == "김정기"))] # 기존
        S_df_selection2_ttt_해외 = S_df_selection2[(S_df_selection2["일차"] <= 일차) & (S_df_selection2['관람객'] != 0) & ((S_df_selection2["전시명"] != "드리머") & (S_df_selection2["전시명"] != "윤협") & (S_df_selection2["전시명"] != "김정기"))] # 기존
        # check
        # st.dataframe(S_df_selection2)
        # S_df_selection2_ttt_해외 = S_df_selection2[(S_df_selection2["일차"] <= 일차)] # 기존
        # S_df_selection2_ttt_해외 = S_df_selection2_ttt_해외[S_df_selection2_ttt_해외['전시명'] != "드리머"]
        # S_df_selection2_ttt_해외 = S_df_selection2_ttt_해외[S_df_selection2_ttt_해외['전시명'] != "윤협"]
        # S_df_selection2_ttt_해외 = S_df_selection2_ttt_해외[S_df_selection2_ttt_해외['전시명'] != "김정기"]

        S_df_selection2_ttt_해외 = S_df_selection2_ttt_해외.reset_index()
        # st.dataframe(S_df_selection2_ttt_해외)
        
        
        # S_df_selection2_ttt_국내 = S_df_selection2_ttt_국내.reset_index()
        
        # st.dataframe(S_df_selection2_ttt)
        # c = alt.Chart(S_df_selection2).transform_filter(alt.datum.symbol != "아샴").mark_area().encode(
        # c2 = alt.Chart(S_df_selection2_ttt_국내).mark_line(interpolate="monotone").encode(
        c2 = alt.Chart(S_df_selection2_ttt_해외).mark_line(interpolate="monotone").encode(
        

            x = alt.X("일차:Q",title=""),
            y = alt.Y("관람객:Q",title=""),
            # color="전시명:N",
            # color=alt.Color('전시명', legend=alt.Legend(orient='top',direction='horizontal')),
            color= alt.Color("전시명").legend(None),
            strokeWidth=alt.condition(
                "datum.전시명 == '아샴'",
                alt.value(4),
                alt.value(1)),
            
            
            # .configure_axis(grid=False).configure_view(strokeWidth=0)
            #차트 조건부 서식 참조
            # https://github.com/vega/altair/issues/1590

            # row="전시명:N",
            # row=alt.Row("전시명:N").sort(["바스키아", "김정기", "드리머", "알렉스","페어리","마르지엘라","제이알","오스틴 리","아샴"]),
        ).properties(height=500)
        # .configure_axis(grid=False).configure_view(stroke=None)
        표식 = c2.mark_circle(size=60).encode(alt.X('일차:Q'), alt.Y('관람객:Q'))
        lst일차 = c2.mark_circle().encode(x=alt.X("fr['일차']:Q"), y=alt.Y("fr['관람객']:Q")).transform_aggregate(fr ='argmin(일차)',groupby=['전시명'])
        # 전시이름 = c.mark_text(align="left",dx=3).encode(x=alt.datum(경과주차-1), text="전시명").transform_aggregate(주차='argmin(주차)')
        전시이름2 = lst일차.mark_text(align="left",dx=5, dy=-5,size=15).encode(text="전시명")


        xrule = (alt.Chart(S_df_selection2_ttt_해외)
        .mark_rule(color="cyan", strokeWidth=3)
        .encode(x=alt.datum(진행기간))
        )
        # #.properties(height=50, width=400)

        test2 = alt.layer(c2+xrule+전시이름2+표식).configure_view(stroke=None).configure_axis(grid=False)

        st.altair_chart(test2, use_container_width=True)
        # st.altair_chart(c2+xrule+전시이름2+표식, use_container_width=True)
        # st.altair_chart(c2)

######################################################
# df_line3 = visitor3[(visitor3["주차"] <= 주차2) & ((visitor3["전시명"] == "드리머") | (visitor3["전시명"] == "아샴") | (visitor3["전시명"] == "김정기"))] # 기존
    try:
        # df_all = df_all[df_all['전시명'] != 0]
        # # df_all = df_all[df_all['전시명'] != 'nan']
        # 전시명3 = df_all["전시명"].dropna().unique()
        # option3 = st.selectbox(
        # 'Select Exhibition ',
        # (전시명3), index=8,
        # )
        # st.write('Selection :', option3)

        # st.error("Trends Weekly")

        # global 주차8
        # 주차8 = st.slider("Select Working Weeks  : ", 1, 20, value=경과주차-1) # 슬라이더 수직필요해서 일단 중지
        
        # 주차8 = st.slider("Select Working Weeks  : ", 1, 20, value=주차8) # 슬라이더 수직필요해서 일단 중지
        
        df_all =df_all.dropna(subset=['전시명'], how='any', axis=0)
        df_all = df_all[df_all['전시명'] != 0]


        S_df_t = df_MAX_D_line[df_MAX_D_line["주차"] <= 주차8]
        # st.dataframe(S_df2)
        S_df_t = S_df_t.reset_index()
        S_df_t = S_df_t.loc[S_df_t['전시명'] == option3]
        S_df_selection_t = S_df_t.query(
            "주차 <= @주차8")
        S_df_selection_t["누적관람객2"] = S_df_selection_t['관람객'].cumsum()
        S_df_selection_t["일평관람객2"] = round(S_df_selection_t['누적관람객2']/S_df_selection_t['일차'])
        df_MAX_D_line_MAX = S_df_selection_t.groupby(['전시명','주차'])['관람객'].agg(**{'최대값':lambda x : x.max()}).reset_index()
        df_MAX_D_line_MIN = S_df_selection_t.groupby(['전시명','주차'])['관람객'].agg(**{'최소값':lambda x : x.min()}).reset_index() #0이 아닌 값중 최소값
        df_MAX_D_line_주차별관람객 = S_df_selection_t.groupby(['전시명','주차'])['관람객'].agg(**{'주차별관람객':lambda x : x.sum()}).reset_index() #0이 아닌 값중 최소값
        df_MAX_D_line_fir = S_df_selection_t.groupby(['전시명','주차'])['관람객'].apply(lambda x: x.value_counts().index[0]).reset_index(name="fir")
        df_MAX_D_line_lst = S_df_selection_t.groupby(['전시명','주차'])['관람객'].apply(lambda x: x.value_counts().index[-1]).reset_index(name="lst")
        
        

        df_MAX_D_line_MAX = df_MAX_D_line_MAX.set_index(['전시명','주차'])
        df_MAX_D_line_MIN = df_MAX_D_line_MIN.set_index(['전시명','주차'])
        df_MAX_D_line_주차별관람객 = df_MAX_D_line_주차별관람객.set_index(['전시명','주차'])
        df_MAX_D_line_fir = df_MAX_D_line_fir.set_index(['전시명','주차'])
        df_MAX_D_line_lst = df_MAX_D_line_lst.set_index(['전시명','주차'])

        
        df_MAX_D_line_RANGE = pd.merge(df_MAX_D_line_MAX,df_MAX_D_line_MIN, on=['전시명','주차'])
        df_MAX_D_line_RANGE = pd.merge(df_MAX_D_line_RANGE,df_MAX_D_line_fir, on=['전시명','주차'])
        df_MAX_D_line_RANGE = pd.merge(df_MAX_D_line_RANGE,df_MAX_D_line_lst, on=['전시명','주차'])
        df_MAX_D_line_RANGE = pd.merge(df_MAX_D_line_RANGE,df_MAX_D_line_주차별관람객, on=['전시명','주차'])

        df_MAX_D_line_RANGE = df_MAX_D_line_RANGE.reset_index()
        df_MAX_D_line_주차별관람객 = df_MAX_D_line_주차별관람객.reset_index()
        df_MAX_D_line_RANGE['누적관람객'] = df_MAX_D_line_주차별관람객['주차별관람객'].cumsum()
        df_MAX_D_line_RANGE['일평균관람객'] = round(df_MAX_D_line_RANGE['누적관람객']/(df_MAX_D_line_RANGE['주차']*7),0)
        df_MAX_D_line_RANGE['주평균관람객'] = round(df_MAX_D_line_RANGE['주차별관람객']/7,0)


        # st.dataframe(S_df_selection_t)

        

        bar = alt.Chart(S_df_selection_t).mark_bar(cornerRadius=10, height=20).encode(
            x=alt.X('min(관람객):Q').scale(domain=[0, S_df_selection_t['관람객'].max()]).title('관람객'),
            x2='max(관람객):Q',
            y=alt.Y('주차:O').title("주차"),
            color=alt.value("#116EA1"),
        )

    # bar.configure_title(fontSize=14).configure(background='#D9E9F0')
        text_min = alt.Chart(S_df_selection_t).mark_text(align='right', dx=-5,color='white', size=13).encode(
            x='min(관람객):Q',
            y=alt.Y('주차:O'),
            text='min(관람객):Q',
            # color= "white"
        ).properties(height=700)

        text_max = alt.Chart(S_df_selection_t).mark_text(align='left', dx=5,color='white',size=13).encode(
            x='max(관람객):Q',
            y=alt.Y('주차:O'),
            text='max(관람객):Q',
            # color="white"
        )
        # .properties(colors='white')

        (bar + text_min + text_max).properties(
            title=alt.Title(text='Temperature variation by month', subtitle='Seatle weather, 2012-2015'))
        # .configure(background='#DDEEFF')
        # .configure(background='#DDEEFF')
        # st.altair_chart(bar + text_min + text_max, use_container_width=True).configure(background='#D9E9F0')
        st.altair_chart(bar + text_min + text_max, use_container_width=True)
    except:
        pass


    
with tab4:
   
    try:
        # 내용확인 필요 - 수치 검증
        # 디자인 변경 - 이상치로 그래프 가시성이 떨어짐...




        전체주차실적 = df_MAX_D_line.groupby(['전시명','주차'])['관람객'].agg(**{'주차별관람객':lambda x : x.sum()}).reset_index() #0이 아닌 값중 최소값
        전체주차실적 = 전체주차실적.groupby(['전시명'])['주차별관람객'].sum()
        전체주차실적 = 전체주차실적.reset_index()
        전체주차실적 = 전체주차실적.loc[전체주차실적['전시명'] != "아샴"]
        전체주차실적 = 전체주차실적.set_index(["전시명"])
        # st.dataframe(전체주차실적)

        잔여주차실적 = df_MAX_D_line.groupby(['전시명','주차'])['관람객'].agg(**{'주차별관람객':lambda x : x.sum()}).reset_index().rename(columns={"주차별관람객": "잔여주차관람객"}) #0이 아닌 값중 최소값
        잔여주차실적 = 잔여주차실적[잔여주차실적["주차"] > 경과주차-1]
        잔여주차실적 = 잔여주차실적.groupby(['전시명'])['잔여주차관람객'].sum()
        # 잔여주차실적 = 잔여주차실적.rename(columns={'주차별관람객': '잔여주차관람객'})
        # 잔여주차실적 = 잔여주차실적.set_index(["전시명"])
        # st.dataframe(잔여주차실적)

        잔여추정 = pd.merge(전체주차실적,잔여주차실적, on=['전시명'])


        df_MAX_D_line= df_MAX_D_line.reset_index()
        # st.dataframe(df_MAX_D_line)
        
        아샴경과주차관람객 = df_MAX_D_line.loc[df_MAX_D_line['전시명'] == "아샴"]
        # st.dataframe(아샴경과주차관람객)

        아샴경과주차관람객 = 아샴경과주차관람객[아샴경과주차관람객['주차']<= 경과주차-1]
        아샴경과주차관람객 = 아샴경과주차관람객.groupby(['전시명'])['관람객'].sum()
        아샴경과주차관람객 = 아샴경과주차관람객.reset_index()
        아샴경과주차관람객 = 아샴경과주차관람객.iloc[0].loc["관람객"]
        # st.text(f"{경과주차-1}기준 아샴경과주차 관람객 : {round(아샴경과주차관람객/10000,1)}만명")
        # st.dataframe(아샴경과주차관람객)

        잔여추정['잔여비율(%)'] = round((잔여추정['잔여주차관람객'] / 잔여추정['주차별관람객'])*100,1)
        잔여추정['아샴경과주관람객'] = 아샴경과주차관람객
        잔여추정['아샴관람객예상'] = round(아샴경과주차관람객 / (1-잔여추정['잔여비율(%)']/100),-1)
        잔여추정.loc["평균"] = round(잔여추정.mean(axis='rows'),0)

        # 잔여추정_T = 잔여추정.T
        # 잔여추정_T["평균"] = round(잔여추정_T.mean(axis='columns'),0)
        # st.dataframe(잔여추정)

        # st.text("기존전시 누적관람객, 경과주차 관람객 진도율")
        # st.dataframe(잔여추정_T)
        # st.dataframe(전체주차실적)
        # st.dataframe(잔여주차실적)
        
        #[인덱스로] df.set_index(df['key'], inplace=True)
        st.error("아샴 관람객 예측")

        # 진도율_df_T = 진도율_df.T
        # st.dataframe(진도율_df)
        # # st.write('선택한 전시:', option4)
        # 잔여추정_반영.loc[option4] = 잔여추정_반영.at[0,'잔여주차관람객']
        # 잔여추정_반영.loc['경과주차누적'] =잔여추정_반영.iloc[0]-잔여추정_반영.iloc[1]
        
        # st.dataframe(잔여추정)
        # st.text(len(잔여추정.index))


        # 잔여추정_반영_T = 잔여추정_반영.T

        # st.dataframe(잔여추정_반영_T)
        전시명4 = 잔여추정.index
        option4 = st.selectbox(
        'Reference Exhibition',
        (전시명4),
        index=len(잔여추정.index)-1,
        )



        잔여추정_반영 = 잔여추정.reset_index()
        잔여추정_반영 = 잔여추정_반영.set_index('전시명')
        # st.dataframe(잔여추정_반영)
        잔여추정_반영.insert(2,'누적관람객',잔여추정_반영['주차별관람객'] - 잔여추정_반영['잔여주차관람객'])
        # st.dataframe(잔여추정_반영)
        
        # 잔여추정_반영.insert(4,'누적관람객',['주차별관람객'] - 잔여추정_반영['잔여주차관람객'])
        # st.dataframe(잔여추정_반영)
        # 잔여추정_반영 = 잔여추정_반영.set_index('전시명')
        잔여추정_반영 = 잔여추정_반영.reset_index()
        잔여추정_반영 = 잔여추정_반영[잔여추정_반영['전시명'] == option4]
        잔여추정_반영 = 잔여추정_반영.set_index('전시명')
        # df쪼개서 가져오기 (파이차트 범위)
        진도율_df = 잔여추정_반영[['잔여주차관람객', '누적관람객']]
        # st.dataframe(진도율_df)
        진도율_df_c = 진도율_df.iloc[0].copy()
        진도율_df.loc[1] = 진도율_df_c.loc['누적관람객']
        # 진도율_df.loc[1] = 진도율_df_c.iloc[0].loc['누적관람객']
    

        경과감안관람객추정 =  round(아샴경과주차관람객/(100-잔여추정_반영.iloc[0].loc['잔여비율(%)'])/100,1)
        경과감안관람객추정 = round(경과감안관람객추정,1)
        아샴경과주차관람객_만 = round(아샴경과주차관람객/10000,1)
        
        c5 = st.container(border=True)
        c5.write(f'<p class ="ctn2">{option4} 트랜드 반영 시 아샴예상관람객 : {경과감안관람객추정}만명</p>', unsafe_allow_html=True)
        
        
        # st.info(f'{option4} 트랜드 반영 시 아샴예상관람객 : {경과감안관람객추정}만명')


        st.write('※타전시 잔여주차 비율 낙관추정')
        st.write(f'<p class ="cnt">{경과주차-1}th weeks 아샴관람객 : {아샴경과주차관람객_만}만명 </p>', unsafe_allow_html=True)
    except:
        pass

    # st.dataframe(진도율_df)
    
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        try:
            pie_chart = px.pie(진도율_df,
                        title=f"Full weeks{경과주차-1}th Visitors",
                        values = 진도율_df['잔여주차관람객'],
                        names = ("잔여", "경과"),
                        # color_discrete_sequence=px.colors.sequential.RdBu,
                        # color_discrete_sequence=px.colors.sequential.amp_r,
                        color_discrete_sequence=px.colors.sequential.Brwnyl,
                        hole = .5)
            # https://wikidocs.net/186283
            pie_chart.update_yaxes(showticklabels=False)
            pie_chart.update_layout(xaxis_rangeslider_visible=False)
            pie_chart.update_layout(yaxis=dict(title=None,showgrid=False,showline=False))
            pie_chart.update_traces(hoverinfo='label+percent', textinfo='value+percent', textfont_size=17)
            # pie_chart.add_trace(textfont_size=13)
            pie_chart.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            # labelfont_size= 24,
            # textprops={'fontsize': 14},
            font_size = 12,
            xanchor="right",
            x=1
            ))
            st.plotly_chart(pie_chart,use_container_width=True)
        except:
            pass
        
        # st.text()
    q1 = st.container(border=True)
    # st.text(round(아샴경과주차관람객,1))
    # 아샴경과주차관람객_만 = round(아샴경과주차관람객/10000,1)
    # st.error(f'{option4} 트랜드 반영 시 아샴예상관람객 : {경과감안관람객추정}만명')
    # q1.write(f'<p class ="cnt">{경과주차-1}주차 기준 아샴누계관람객 : {아샴경과주차관람객_만}만명 </p>', unsafe_allow_html=True)
    # q1.write(f'<p class ="big-font"> 관람객진도율 : 잔여추정_반영.iloc[0].loc['잔여비율(%)'] </p>', unsafe_allow_html=True)                    

    # st.error("Trends Weekly")

    # global 주차8
    # 주차8 = st.slider("Select Working Weeks  : ", 1, 20, value=경과주차2-1) # 슬라이더 수직필요해서 일단 중지
    
    # df_all =df_all.dropna(subset=['전시명'], how='any', axis=0)
    # df_all = df_all[df_all['전시명'] != 0]

    
    # 전시명3 = df_all["전시명"].unique()
    # option3 = st.selectbox(
    # 'Select Exhibition ',
    # (전시명3), index=8,
    # )
    # # st.write('Selection :', option3)
 
    # df_MAX_D = S_df.loc[(S_df['전시명'] == '아샴') & (S_df['관람객'] > 0) & (S_df['주차'] <= MAX_Day)]
    # S_df = S_df.reset_index()
    try:
        S_df_t = df_MAX_D_line[df_MAX_D_line["주차"] <= 주차8]
        # st.dataframe(S_df2)
        S_df_t = S_df_t.reset_index()
        S_df_t = S_df_t.loc[S_df_t['전시명'] == option3]
        S_df_selection_t = S_df_t.query(
            "주차 <= @주차8")
        S_df_selection_t["누적관람객2"] = S_df_selection_t['관람객'].cumsum()
        S_df_selection_t["일평관람객2"] = round(S_df_selection_t['누적관람객2']/S_df_selection_t['일차'])
        # st.dataframe(df_MAX_D_line)
        # st.dataframe(df_MAX_D_line)
        # df_MAX_D_line = df_all.dropna(subset=['관람객'], how='any', axis=0)
        # df_MAX_D_line_MM = S_df_selection_t[S_df_selection_t['관람객'] != 0]
        df_MAX_D_line_MAX = S_df_selection_t.groupby(['전시명','주차'])['관람객'].agg(**{'최대값':lambda x : x.max()}).reset_index()
        df_MAX_D_line_MIN = S_df_selection_t.groupby(['전시명','주차'])['관람객'].agg(**{'최소값':lambda x : x.min()}).reset_index() #0이 아닌 값중 최소값
        # df_MAX_D_line_관람객 = S_df_selection_t.groupby(['전시명','주차'])['관람객'].cumsum()
        # df_MAX_D_line_주차별관람객 = S_df_selection_t.groupby(['전시명','주차'])['관람객'].sum()
        df_MAX_D_line_주차별관람객 = S_df_selection_t.groupby(['전시명','주차'])['관람객'].agg(**{'주차별관람객':lambda x : x.sum()}).reset_index() #0이 아닌 값중 최소값
        
        # st.dataframe(df_MAX_D_line_주차별관람객)
        # df_MAX_D_line_일차 = S_df_selection_t.groupby(['전시명','주차'])['관람객'].count()

        
        # df_MAX_D_line_aver = S_df_selection_t.groupby(['전시명','주차'])['관람객'].agg(**{'평균':lambda x : x.mean()}).reset_index() #0이 아닌 값중 최소값
        
        
        # S_df_selection_t = S_df_selection_t.reset_index()
        # df_MAX_D_line_주차별관람객 = S_df_selection_t.groupby(['전시명','주차'])['관람객'].apply(lambda x: x.sum()).reset_index(name="주차별관람객").sort_values(by='관람객',ascending=True)
        # df_MAX_D_line_누적관람객 = [S_df_selection_t['관람객'].cumsum()].sort_values(by=['관람객'], axis=0,)
        # df_MAX_D_line_누적관람객 = S_df_selection_t['관람객'].cumsum()
        # st.dataframe(df_MAX_D_line_누적관람객)
        # df_MAX_D_line_누적관람객 = df_MAX_D_line_누적관람객.sort_values(by=['관람객'], axis=0)

        # df_MAX_D_line_일차 = S_df_selection_t.groupby(['전시명','주차'])['일차'].apply(lambda x: x.cumsum()).reset_index(name="일차")
        df_MAX_D_line_fir = S_df_selection_t.groupby(['전시명','주차'])['관람객'].apply(lambda x: x.value_counts().index[0]).reset_index(name="fir")
        df_MAX_D_line_lst = S_df_selection_t.groupby(['전시명','주차'])['관람객'].apply(lambda x: x.value_counts().index[-1]).reset_index(name="lst")
        
        
        

        # .groupby('States')['Counts'].apply(lambda x: x.value_counts().index[0]).reset_index(name='val')
        df_MAX_D_line_MAX = df_MAX_D_line_MAX.set_index(['전시명','주차'])
        df_MAX_D_line_MIN = df_MAX_D_line_MIN.set_index(['전시명','주차'])
        df_MAX_D_line_주차별관람객 = df_MAX_D_line_주차별관람객.set_index(['전시명','주차'])
        # df_MAX_D_line_aver = df_MAX_D_line_aver.set_index(['전시명','주차'])
        df_MAX_D_line_fir = df_MAX_D_line_fir.set_index(['전시명','주차'])
        df_MAX_D_line_lst = df_MAX_D_line_lst.set_index(['전시명','주차'])
        # df_MAX_D_line_누적관람객 = df_MAX_D_line_누적관람객.set_index(['전시명'])

        # df_MAX_D_line_일차 = df_MAX_D_line_일차.set_index(['전시명','주차'])
        
        
        # st.dataframe(df_MAX_D_line_MAX)
        # st.dataframe(df_MAX_D_line_MIN)
        # st.dataframe(df_MAX_D_line_cumsum)

        # df_MAX_D_line_RANGE = pd.concat([df_MAX_D_line_MAX,df_MAX_D_line_MIN], axis=0)
        
        df_MAX_D_line_RANGE = pd.merge(df_MAX_D_line_MAX,df_MAX_D_line_MIN, on=['전시명','주차'])
        # df_MAX_D_line_RANGE = pd.merge(df_MAX_D_line_RANGE,df_MAX_D_line_aver, on=['전시명','주차'])
        df_MAX_D_line_RANGE = pd.merge(df_MAX_D_line_RANGE,df_MAX_D_line_fir, on=['전시명','주차'])
        df_MAX_D_line_RANGE = pd.merge(df_MAX_D_line_RANGE,df_MAX_D_line_lst, on=['전시명','주차'])
        # df_MAX_D_line_RANGE = pd.merge(df_MAX_D_line_RANGE,df_MAX_D_line_관람객, on=['전시명'])
        df_MAX_D_line_RANGE = pd.merge(df_MAX_D_line_RANGE,df_MAX_D_line_주차별관람객, on=['전시명','주차'])

        # st.dataframe(df_MAX_D_line_RANGE)
        # df_MAX_D_line_RANGE['누계관람'] = df_MAX_D_line_RANGE['관람객'].cumsum() #0이 아닌 값중 최소값
        # df_MAX_D_line_RANGE['누적일차'] = df_MAX_D_line_RANGE['일차'].cumsum() #0이 아닌 값중 최소값
        df_MAX_D_line_RANGE = df_MAX_D_line_RANGE.reset_index()
        df_MAX_D_line_주차별관람객 = df_MAX_D_line_주차별관람객.reset_index()
        # st.dataframe(df_MAX_D_line_RANGE)
        df_MAX_D_line_RANGE['누적관람객'] = df_MAX_D_line_주차별관람객['주차별관람객'].cumsum()
        df_MAX_D_line_RANGE['일평균관람객'] = round(df_MAX_D_line_RANGE['누적관람객']/(df_MAX_D_line_RANGE['주차']*7),0)
        df_MAX_D_line_RANGE['주평균관람객'] = round(df_MAX_D_line_RANGE['주차별관람객']/7,0)
        # st.dataframe(df_MAX_D_line_RANGE)

        # df_MAX_D_line_RANGE = df_MAX_D_line_RANGE.loc[(df_MAX_D_line_RANGE['전시명']=='아샴')]
        
        # df_MAX_D_line_RANGE["누적관람객"] = df_MAX_D_line_RANGE.cumsum(df_MAX_D_line_RANGE["관람객"])
        # df_MAX_D_line_RANGE["누적평균"] = df_MAX_D_line_RANGE["누계관람"]/df_MAX_D_line_RANGE["주차"],
        
        # st.dataframe(df_MAX_D_line_RANGE)

        fig_c = go.Figure()
        # fig_c.add_trace(go.Candlestick(x=df_MAX_D_line_RANGE['주차'],open=df_MAX_D_line_RANGE['평균'],high=df_MAX_D_line_RANGE['최대값'],low=df_MAX_D_line_RANGE['최소값'],close=df_MAX_D_line_RANGE['최소값']))
        # fig_c.add_trace(go.Candlestick(x=df_MAX_D_line_RANGE['주차'],open=df_MAX_D_line_RANGE['평균'],high=df_MAX_D_line_RANGE['최대값'],low=df_MAX_D_line_RANGE['평균'],close=df_MAX_D_line_RANGE['최소값']))
        fig_c.add_trace(go.Candlestick(name="일평균관람객증감",x=df_MAX_D_line_RANGE['주차'],open=df_MAX_D_line_RANGE['일평균관람객'],high=df_MAX_D_line_RANGE['최대값'],low=df_MAX_D_line_RANGE['최소값'],close=df_MAX_D_line_RANGE['주평균관람객']))

    ############새작업################
        # st.dataframe(S_df_selection_t)
        # st.dataframe(df_MAX_D_line_RANGE)
        # st.dataframe(S_df_selection_t)
        # c = alt.Chart(S_df_selection_t).mark_boxplot(extent='min-max').encode(
        #     x='주차:Q',
        #     y='관람객:Q').properties(height=500).configure(background="#878686")
        #.mark_text("관람객")
        # ,color=alt.value('#32a852')
        # st.altair_chart(c, use_container_width=True)
    ############################
    ##########새작업2#################
    # .replace(0,float(“NaN”))

        # S_df_selection_t = S_df_selection_t.replace(0,value="NaN")
        # st.dataframe(S_df_selection_t)
        line = c = alt.Chart(S_df_selection_t).mark_line().encode(
            x='주차',
            y="mean(관람객)")
        # configure_line(color="red")
        text = alt.Chart(S_df_selection_t).mark_text(dx=0, dy=0, align='center',baseline='bottom',color='white', size=15).encode(
            # x=alt.X('주차', sort=None),y=alt.Y('일평균관람객:Q', axis=alt.Axis(labels=False)), text=alt.Text('일평균관람객:Q'))
            x=alt.X('주차', sort=None),y=alt.Y('mean(관람객)', axis=alt.Axis(labels=False,grid=False)), text=alt.Text('median(관람객)'))
        
        # c = alt.Chart(S_df_selection_t).mark_errorband(extent='ci', borders=True).encode(
        c = alt.Chart(S_df_selection_t).mark_errorband(extent='ci', borders=True).encode(

            x='주차',
            y=alt.Y('관람객:Q',scale=alt.Scale(zero=False))).properties(height=500)
        
        # st.altair_chart(c+line+text, use_container_width=True)

        # st.dataframe(S_df_selection_t)
    #################################################
    #     open_close_color = alt.condition(
    #         "datum.open <= datum.close",
    #         alt.value("#06982d"),
    #         alt.value("#ae1325")
    #     )


    #     base = alt.Chart(S_df_selection_t).encode(
    #         alt.X('주차:T')
    #             .axis(format='%m/%d', labelAngle=-45)
    #             .axis(labelAngle=-45)
    #             .title('주차'),
    #         color=open_close_color
    #     )

    #     rule = base.mark_rule().encode(
    #         alt.Y('low:Q')
    #             .title('관람객')
    #             .scale(zero=False),
    #         alt.Y2('high:Q')
    #     )

    #     bar = base.mark_bar().encode(
    #         alt.Y('open:Q'),
    #         alt.Y2('close:Q')
    #     )
    # #################################################
        # rule + bar

        # st.altair_chart(rule + bar, use_container_width=True)

    ##########################################################
        points = alt.Chart(S_df_selection_t).mark_point(
            filled=True,
            color='white'
        ).encode(
            x=alt.X('mean(관람객)').title('주차별 관람객'),
            y=alt.Y('주차').sort(
                field='주차',
                op='mean',
                order='descending',
            

                
            ),
            color=alt.value("#4682b4")
        # ).properties(
        #     width=400,
        #     height=250
        )

        error_bars = points.mark_rule().encode(
            # x='ci0(관람객)',
            # x2='ci1(관람객)',
            x='max(관람객)',
            x2='min(관람객)',
            # configure_line(color="red")
            # 
        ).properties(
            width=400,
            height=850
        )
    except:
        pass






    # ).configure_errorbar(color="red")
    # ).configure_errorbar())
    # ).configure_errorbar(color(['r','r','b','r']))

    
    # st.altair_chart(points + error_bars, use_container_width=True)

###############################################################


    # bar = alt.Chart(S_df_selection_t).mark_bar(cornerRadius=10, height=20).encode(
    #     x=alt.X('min(관람객):Q').scale(domain=[0, S_df_selection_t['관람객'].max()]).title('관람객'),
    #     x2='max(관람객):Q',
    #     y=alt.Y('주차:O').title(None),
    #     color=alt.value("#116EA1"),
    # )

    # # bar.configure_title(fontSize=14).configure(background='#D9E9F0')
    # text_min = alt.Chart(S_df_selection_t).mark_text(align='right', dx=-5,color='white', size=13).encode(
    #     x='min(관람객):Q',
    #     y=alt.Y('주차:O'),
    #     text='min(관람객):Q',
    #     # color= "white"
    # ).properties(height=700)

    # text_max = alt.Chart(S_df_selection_t).mark_text(align='left', dx=5,color='white',size=13).encode(
    #     x='max(관람객):Q',
    #     y=alt.Y('주차:O'),
    #     text='max(관람객):Q',
    #     # color="white"
    # )
    # # .properties(colors='white')

    # (bar + text_min + text_max).properties(
    #     title=alt.Title(text='Temperature variation by month', subtitle='Seatle weather, 2012-2015'))
    # # .configure(background='#DDEEFF')
    # # .configure(background='#DDEEFF')
    # # st.altair_chart(bar + text_min + text_max, use_container_width=True).configure(background='#D9E9F0')
    # st.altair_chart(bar + text_min + text_max, use_container_width=True)


##################################
    #     text = "Median of 관람객"
    # text = alt.Chart(S_df_selection_t).mark_text(dx=0, dy=0, align='center',baseline='bottom',color='white', size=15).encode(
    #     # x=alt.X('주차', sort=None), y="Median of 관람객", detail="Median of 관람객", text=alt.Text("Median of 관람객"))
    #     x=alt.X('주차', sort=None), y="Median of 관람객", text=alt.Text("Median of 관람객"))
    
    # st.altair_chart(c+text, use_container_width=True)
    
#     c + c.mark_text().encode(
#     # y=alt.datum(11_500_000),
#     text='관람객:'
# )

    # c.update_layout({
    # ‘plot_bgcolor’: ‘rgba(0, 0, 0, 0)’,
    # ‘paper_bgcolor’: ‘rgba(0, 0, 0, 0)’,
    # })
    # st.altair_chart(c, use_container_width=True)
###################################

    ### 기존작동####
    try: 
        parameter = ['moving_average', 'bol_lower', 'bol_upper']
        colors = ['blue', 'orange', 'orange']
        for param,c in zip(parameter, colors):
            fig_c.add_trace(go.Scatter(
            # name="주별평균관람객",
            x = df_MAX_D_line_RANGE['주차'],
            y = df_MAX_D_line_RANGE['주평균관람객'],
            showlegend = False,
            line_color = 'blue',
            mode='lines+markers+text',
            line={'dash': 'solid'},
            name= "주평균관람객",
            marker_line_width=2, 
            marker_size=10,
            text= df_MAX_D_line_RANGE['주평균관람객'],
            textposition = "top center",
            textfont_size=15,
            opacity = 0.8))
            

            fig_c.add_trace(go.Scatter(
            # name="누적평균관람객",
            x = df_MAX_D_line_RANGE['주차'],
            # y = round(df_MAX_D_line_RANGE['누적관람객']//(주차c*7)),
            y = round(df_MAX_D_line_RANGE['일평균관람객']),

            # y = df_MAX_D_line_RANGE['누계관람'],
            showlegend = False,
            line_color = 'orange',
            mode='lines+markers+text',
            line={'dash': 'solid'},
            name= "일평균관람객",
            marker_line_width=2, 
            marker_size=10,
            text= round(df_MAX_D_line_RANGE['일평균관람객']),
            textposition = "top center",
            textfont_size=15,
            opacity = 0.8)
            
            )
    # https://stackoverflow.com/questions/68138197/how-to-add-labels-to-candlestick-plots
        # 인덱스 레이아웃 변경
        fig_c.update_layout(xaxis_rangeslider_visible=False)
        fig_c.update_layout(yaxis=dict(title=None,showgrid=False,showline=False))
        fig_c.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1,
        ))
        fig_c.update_layout(xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=False)
        )
        fig_c.update_yaxes(showticklabels=False)
    except:
        pass

#     open_close_color = alt.condition(
#     "datum.open <= datum.close",
#     alt.value("#06982d"),
#     alt.value("#ae1325")
# )


    # https://stackoverflow.com/questions/66993546/custom-color-of-plotly-candlesticks
    # fig.show()

    #일단 기존그래프 숨김 _국내전 기준
    # st.plotly_chart(fig_c, use_container_width=True)

#####################################
    # def color_vowel(value):
    #             return f"background-color: gray; font color: black"

    # st.dataframe(잔여추정_T.map(color_vowel, subset=pd.IndexSlice['아샴관람객예상','김정기':'평균']), use_container_width=True) #★ 향후 전시명이 아샴일 경우로 조건문 조절 필요

    # selection_t.groupby(['전시명','주차'])['관람객'].agg(**{'최소값':lambda x : x.min()}).reset_index() #0이 아닌 값중 최소값
    # 잔여주차실적_주차별관람객 = 잔여주차실적.groupby(['전시명','주차'])['관람객'].agg(**{'주차별관람객':lambda x : x.sum()}).reset_index() #0이 아닌 값중 최소값

    # st.dataframe(잔여주차실적)


    # 전시명4 = 잔여추정.index
    # option4 = st.selectbox(
    # '추정에 적용할 전시 선택',
    # (전시명4),
    # )
    # st.write('선택한 전시:', option4)

    # 잔여추정 = 잔여추정.reset_index()
    # # 잔여추정 = 잔여추정.set_index(["전시명"])
    # 잔여추정 = 잔여추정.loc[잔여추정['전시명']==option4]

    # 잔여비율_T = 잔여추정['잔여비율(%)']
    # st.dataframe(잔여비율_T)
    # # # st.text()
    # # 잔여비율_x = 잔여비율_T.at[0,'잔여비율(%)']
    # 잔여비율_T = 잔여비율_T.reset_index()

    # 잔여비율_x = 잔여비율_T.iloc[0].loc['잔여비율(%)']
    # # st.dataframe(잔여비율_x)
    # st.text(잔여비율_x)
    # st.text(당일누적관람객)
    # 당일누적관람객
    # 전체관람객추정 = round(당일누적관람객/(100-잔여비율_x)*100,1)
    # st.text(F"{전체관람객추정}만명")

with tab5:

    st.markdown("General Trend")
    my_config ={"scrollZoom" : False, "displayModeBar":False}
    # st.dataframe(S_df1)
    전시명 = S_df1["전시명"].unique()
    # st.dataframe(df_MAX_D_line_RANGE)
    # st.text(전시명)

    option = st.selectbox(
    'Select Exhibition',
    (전시명), index=7,
    )

    # css = '''
    # <style>
    #     .stSelectbox div[data-baseweb="select"] > div:first-child {
    #         background-color: #FFFFFF;
    #         border-color: #2d408d;
    #         color:#051345;
    #         border-radius:2%;
    #         border-style: solid;
    #         border-color: red;
    #         font-weight : 900;
    #     }
    # </style>
    # '''
    # st.markdown(css, unsafe_allow_html=True)

    st.markdown(f'Selection : {option}')
 
    ## 국가 목록 가져오기
    
    ## 선택 상자 생성
    # selected_country = st.selectbox('국가 선택:', option)
    
    ## 데이터 필터링

    if option == '아샴':
        
        filtered_data = S_df1[S_df1["전시명"] == option]
        # filtered_data = filtered_data.reindex()
        filtered_data["주차"] = filtered_data['일차'].apply(lambda x: (x//7)+1)
        filtered_data = filtered_data[filtered_data['주차'] <= (MAX_Day//7)]
        # st.dataframe(filtered_data)    
    else:
        filtered_data = S_df1[S_df1["전시명"] == option]
        # S_df1[S_df1["전시명"] == option]
        # filtered_data_c = filtered_data.copy()
        filtered_data["주차"] = filtered_data['일차'].apply(lambda x: (x//7)+1)
        # filtered_data = S_df[S_df["전시명"] == option]
    

    
    
    ## 필터링된 데이터 표시
    # st.write(filtered_data)






    # filtered_data_c = filtered_data.copy()
    filtered_data["주차"] = filtered_data['일차'].apply(lambda x: (x//7)+1)
    # st.write(filtered_data)

    S_df_t = filtered_data
    S_df_t = S_df_t.set_index(['전시명'])
    # S_df_t = S_df_t.reset_index()
    # S_df_t = S_df_t.loc[S_df_t['전시명']== option]

    # st.dataframe(S_df_t)
    S_df_selection_t = S_df_t
 
    df_MAX_D_line_MAX = S_df_selection_t.groupby(['전시명','주차'])['관람객'].agg(**{'최대값':lambda x : x.max()}).reset_index()
    df_MAX_D_line_MIN = S_df_selection_t.groupby(['전시명','주차'])['관람객'].agg(**{'최소값':lambda x : x.min()}).reset_index() #0이 아닌 값중 최소값
    df_MAX_D_line_주차별관람객 = S_df_selection_t.groupby(['전시명','주차'])['관람객'].agg(**{'주차별관람객':lambda x : x.sum()}).reset_index() #0이 아닌 값중 최소값
    df_MAX_D_line_fir = S_df_selection_t.groupby(['전시명','주차'])['관람객'].apply(lambda x: x.value_counts().index[0]).reset_index(name="fir")
    df_MAX_D_line_lst = S_df_selection_t.groupby(['전시명','주차'])['관람객'].apply(lambda x: x.value_counts().index[-1]).reset_index(name="lst")
    
    
    

    df_MAX_D_line_MAX = df_MAX_D_line_MAX.set_index(['전시명','주차'])
    df_MAX_D_line_MIN = df_MAX_D_line_MIN.set_index(['전시명','주차'])
    df_MAX_D_line_주차별관람객 = df_MAX_D_line_주차별관람객.set_index(['전시명','주차'])
    df_MAX_D_line_fir = df_MAX_D_line_fir.set_index(['전시명','주차'])
    df_MAX_D_line_lst = df_MAX_D_line_lst.set_index(['전시명','주차'])
    
    df_MAX_D_line_RANGE = pd.merge(df_MAX_D_line_MAX,df_MAX_D_line_MIN, on=['전시명','주차'])
    df_MAX_D_line_RANGE = pd.merge(df_MAX_D_line_RANGE,df_MAX_D_line_fir, on=['전시명','주차'])
    df_MAX_D_line_RANGE = pd.merge(df_MAX_D_line_RANGE,df_MAX_D_line_lst, on=['전시명','주차'])
    df_MAX_D_line_RANGE = pd.merge(df_MAX_D_line_RANGE,df_MAX_D_line_주차별관람객, on=['전시명','주차'])

    df_MAX_D_line_RANGE = df_MAX_D_line_RANGE.reset_index()
    df_MAX_D_line_주차별관람객 = df_MAX_D_line_주차별관람객.reset_index()
    df_MAX_D_line_RANGE['누적관람객'] = df_MAX_D_line_주차별관람객['주차별관람객'].cumsum()
    df_MAX_D_line_RANGE['일평균관람객'] = round(df_MAX_D_line_RANGE['누적관람객']/(df_MAX_D_line_RANGE['주차']*7),0)
    df_MAX_D_line_RANGE['주평균관람객'] = round(df_MAX_D_line_RANGE['주차별관람객']/7,0)
    df_MAX_D_line_RANGE['관람객k'] = round(df_MAX_D_line_RANGE['주차별관람객']/1000,1)

    # st.dataframe(df_MAX_D_line_RANGE)
    st.markdown("General Trend")
    my_config ={"scrollZoom" : False, "displayModeBar":False}
    
    # fig_t2 = make_subplots(specs=[[{"secondary_y":True}]])

    # fig_t2.add_trace(
    #     go.Bar(name="누적관람객",x=df_MAX_D_line_RANGE['주차'],y=df_MAX_D_line_RANGE['누적관람객'],text=df_MAX_D_line_RANGE['누적관람객'], textposition = "inside", textfont_size=15),      
    #      secondary_y=False,
    # )
    # fig_t2.add_trace(
    #      go.Scatter(name="일평균",x=df_MAX_D_line_RANGE['주차'],y=df_MAX_D_line_RANGE['일평균관람객'],mode="lines+markers+text",text=df_MAX_D_line_RANGE['일평균관람객'], textposition = "top center", textfont_size=17, line_color='#75451b', line_width=3),
    #      secondary_y=True,
    # )

    # fig_t2.update_traces(marker_color='rgb(54, 65, 89)', marker_line_color='rgb(54, 65, 89)',
    #                   marker_line_width=1.5, opacity=0.6)
    

    # fig_t2.update_layout(xaxis=dict(showgrid=False),
    #           yaxis=dict(showgrid=False)
    # )
    # fig_t2.update_yaxes(showticklabels=False)
    # fig_t2.update_layout(xaxis_rangeslider_visible=False)
    # fig_t2.update_layout(yaxis=dict(title=None,showgrid=False,showline=False))
    # fig_t2.update_layout(legend=dict(
    # orientation="h",
    # yanchor="bottom",
    # y=1.02,
    # xanchor="right",
    # # bgcolor="nation",
    # x=1,
    # # color='lifeExp'
    # ))

    # st.plotly_chart(fig_t2, use_container_width=True, congig=my_config)

######################test#############################
    # base = alt.Chart(df_MAX_D_line_RANGE).encode(x=alt.X('주차',axis=alt.Axis(labelAngle=325)))
    base = alt.Chart(df_MAX_D_line_RANGE).encode(x=alt.X('주차'))    #,axis=alt.Axis(labels=False)
    line = base.mark_line(color='#75451b').encode(y=alt.Y('일평균관람객:Q', axis=alt.Axis(labels=False))) #axis=alt.Axis(grid=False)
    # bar = base.mark_bar().encode(y='누적관람객:Q')
    bar = base.mark_area(color='rgb(54, 65, 89)').encode(y=alt.Y('주차별관람객:Q', axis=alt.Axis(labels=False), title="주차별관람객(단위:k명)")).properties(height=600)

    
    text1 = alt.Chart(df_MAX_D_line_RANGE).mark_text(dx=0, dy=0, align='center',baseline='bottom',color='white', size=15).encode(
        # x=alt.X('주차', sort=None), y='일평균관람객', detail='일평균관람객', text=alt.Text('일평균관람객:Q'))
        # check
        x=alt.X('주차', sort=None),y=alt.Y('일평균관람객:Q', axis=alt.Axis(labels=False),title=""), text=alt.Text('일평균관람객:Q', format=',.0f'))
        # x=alt.X('주차', sort=None),y=alt.Y('일평균관람객:Q', axis=alt.Axis(labels=False),title=""), text=alt.Text('일평균관람객:Q' +'k'))
 
    text2 = alt.Chart(df_MAX_D_line_RANGE).mark_text(dx=0, dy=0, align='center',baseline='line-top',color='white', size=16).encode(
        # x=alt.X('주차', sort=None), y='일평균관람객', detail='일평균관람객', text=alt.Text('일평균관람객:Q'))
        # x=alt.X('주차', sort=None),y=alt.Y('주차별관람객:Q', axis=alt.Axis(labels=False)), text=alt.Text('관람객k:Q', format=',1f')).transform_calculate(label=f'format(".1f") + "k"')
        x=alt.X('주차', sort=None),y=alt.Y('주차별관람객:Q', axis=alt.Axis(labels=False),title=""), text=alt.Text('관람객k:Q', format='.1f'))
        # x=alt.X('주차', sort=None),y=alt.Y('주차별관람객:Q', axis=alt.Axis(labels=False)), text=alt.Text('관람객k:Q', format=''))
    # .transform_calculate(label=f'format(datum.{'관람객k:Q'},".1f") + " inches"')
    #format=',.0f', ',.1f'

    # st.altair_chart((line+bar+text).resolve_scale(y='independent',), use_container_width=True)
    st.altair_chart((line+bar+text1+text2).resolve_scale(y='independent'), use_container_width=True)

    st.markdown('--------------')
    st.info("History : Bar_Race_Chart _ click button")
    # st.dataframe(S_df1)

    S_df22=S_df1
    # st.dataframe(S_df22)
    S_df22["주차"] = S_df22['일차'].apply(lambda x: (x//7)+1)
    # S_df22 = S_df22[S_df22['관람객'] != 0]

    # st.dataframe(S_df22)

    # S_df22 = S_df22.groupby(['전시명'])['관람객'].cumsum() #0이 아닌 값중 최소값
    # S_df22 = S_df22[S_df22['관람객'] != 0]
    S_df22['누적관람객'] = S_df22.groupby(['전시명'])['관람객'].cumsum()

    date_t = {'일차': range(1,max(S_df22['일차'])+1)}
    date_t = pd.DataFrame(date_t)
    # date_t = date_t.set_index(['일차'])
    # st.dataframe(date_t)

    ########################################################
    S_df22_아샴 = S_df22[S_df22["전시명"]=="아샴"]
    S_df22_아샴 = pd.merge(date_t, S_df22_아샴, on=['일차'], how= 'left')
    S_df22_아샴 = S_df22_아샴.ffill()
    # st.dataframe(S_df22_아샴)

    S_df22_마르지엘라 = S_df22[S_df22["전시명"]=="마르지엘라"]
    S_df22_마르지엘라 = pd.merge(date_t, S_df22_마르지엘라, on=['일차'], how= 'left')
    # S_df22_마르지엘라 = S_df22_마르지엘라.fillna(method='ffill')
    S_df22_마르지엘라 = S_df22_마르지엘라.ffill()
    
    # st.dataframe(S_df22_마르지엘라)

    S_df22_바스키아 = S_df22[S_df22["전시명"]=="바스키아"]
    S_df22_바스키아 = pd.merge(date_t, S_df22_바스키아, on=['일차'], how= 'left')
    S_df22_바스키아 = S_df22_바스키아.ffill()
    # st.dataframe(S_df22_바스키아)

    S_df22_페어리 = S_df22[S_df22["전시명"]=="페어리"]
    S_df22_페어리 = pd.merge(date_t, S_df22_페어리, on=['일차'], how= 'left')
    S_df22_페어리 = S_df22_페어리.ffill()

    S_df22_알렉스 = S_df22[S_df22["전시명"]=="알렉스"]
    S_df22_알렉스 = pd.merge(date_t, S_df22_알렉스, on=['일차'], how= 'left')
    S_df22_알렉스 = S_df22_알렉스.ffill()

    S_df22_오스틴리 = S_df22[S_df22["전시명"]=="오스틴 리"]
    S_df22_오스틴리 = pd.merge(date_t, S_df22_오스틴리, on=['일차'], how= 'left')
    S_df22_오스틴리 = S_df22_오스틴리.ffill()

    S_df22_김정기 = S_df22[S_df22["전시명"]=="김정기"]
    S_df22_김정기 = pd.merge(date_t, S_df22_김정기, on=['일차'], how= 'left')
    S_df22_김정기 = S_df22_김정기.ffill()

    S_df22_드리머 = S_df22[S_df22["전시명"]=="드리머"]
    S_df22_드리머 = pd.merge(date_t, S_df22_드리머, on=['일차'], how= 'left')
    S_df22_드리머 = S_df22_드리머.ffill()
    # st.dataframe(S_df22_김정기)

    # S_df22_제이알 = S_df22[S_df22["전시명"]=="제이알"]
    # S_df22_제이알 = pd.merge(date_t, S_df22_제이알, on=['일차'], how= 'left')
    # S_df22_제이알 = S_df22_제이알.fillna(method='ffill')

    s_df22_m = pd.concat([S_df22_드리머,S_df22_김정기,S_df22_마르지엘라,S_df22_아샴,S_df22_오스틴리,S_df22_알렉스, S_df22_페어리, S_df22_바스키아])



    # #############################################
    bar = px.bar(s_df22_m, x='누적관람객', y="전시명",color='전시명',text='누적관람객', animation_frame='일차', height=600)
    # bar = px.bar(S_df22, x='누적관람객', y="전시명",color='전시명',text='누적관람객', animation_frame='일차',width=370)
    # bar = px.bar(S_df22, x='누적관람객', y="전시명",color='전시명',text='누적관람객', animation_frame='일차',width=370)

    bar.update_layout(xaxis_rangeslider_visible=False)

    # bar.update_yaxes(showticklabels=False)
    #차트 내림차순 재정렬
    bar.update_yaxes(type='category', categoryorder='max ascending')

    bar.update_layout(showlegend=False)
    bar.update_layout(transition = {'duration': 1500})
    # bar.layout.xaxis.rangeslider.visible = False
    # bar.show(config={ 'modeBarButtonsToRemove': ['zoom', 'pan'] })
    # bar.xaxis.fixedrange = True
    bar.layout.xaxis.fixedrange = True
    bar.layout.yaxis.fixedrange = True
    # bar.update_layout(use_container_width=True)
    # st.write(bar, use_container_width=True)
    my_config ={"scrollWhellZoom" : False, "displayModeBar":False, "Pan" : False,"scrollZoom" : False, "MiddleClickDragZoom" : False, "dragmode" : False}
    st.plotly_chart(bar, use_container_width=True,congig=my_config)






css = '''
<style>
.stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
font-size:1.0rem;
}
</style>
'''
st.markdown(css, unsafe_allow_html=True)






##################################################33
# 국내전시 차수별 실적 / 전체관람객 중
# 국내 평균 명 / 전체 (%)
# 아샴 평균 명 / 전체 (%)
# 드리머..
# 김정기..
# 라인그래프 조건부 서식 변경 확인
# 전체 서식, 이모지 포함..
# 주차별 캔들 최대, 최소 값으로
# 일자 진도율 : 몇일차 (진도율%)
# 예상관람객 : 일평균관람객 잔여일차 00일 => 예상관람객 00.0만명
# 주차별 아샴 최대 최소 관람객 캔들 차트..
# 아샴일평균 하단에 막대 그래프 추이 표시
# 차트 범례 위치 변경
    # https://plotly.com/python/legend/#legend-position