
import streamlit as st

import altair as alt
from altair.expr import datum
import pandas as pd
import numpy as np
import streamlit as st
import datetime
from streamlit_plotly_events import plotly_events
import streamlit as st
import plotly.express as px
import pandas as pd
from altair import datum
import warnings
# warnings.filterwarnings("ignore")
from streamlit_extras.metric_cards import style_metric_cards
import seaborn as sns 
import pickle
from pathlib import Path
import streamlit_authenticator as stauth
from streamlit_navigation_bar import st_navbar
# import bcrypt
import streamlit_highcharts as hct
import plotly.graph_objects as go
# import matplotlib.pyplot as plt 
import os
# import matplotlib.font_manager as fm

st.set_page_config(
    page_title = "FINANCIAL Data Dashboard",
    page_icon = "Active",        
    layout="wide"
    )
hide_streamlit_markers=False

st.markdown("<h1 style='text-align: center; color: white;'>Financial Summary Report</h1>", unsafe_allow_html=True)

names = ["koo","sun","myung"]
usernames = ["kkoo","sun","myung"]

file_path = Path(__file__).parent / "hashed_pw.pkl"

with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)


authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "FINANCIAL Data Dashboard", "addfd", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")


if authentication_status == False:
    st.error("error check")
if authentication_status == None:
    st.error("please enter your name and pw")
if authentication_status:
    # st.header("hellow")
    cols = st.columns(20)
    with cols[19]:
        authenticator.logout("logout","main")    

    @st.cache_data
    # 엑셀 파일 읽어오기 함수
    def get_data_from_excel():
            df_all = pd.read_excel(
                        io = 'C:/Users/USER/Desktop/test_db/tstdata.xlsx',
                        engine = 'openpyxl',
                        sheet_name ='T',
                        skiprows = 0,
                        usecols='a:m'
            )
            return df_all

    get_data_from_excel()
    df_all = get_data_from_excel()

    #순환참조 오류 제거
    pd.options.mode.chained_assignment = None

    #데이트 프레임 열 type 지정
    df_all = df_all.astype({'대분류':'str','중분류':'str', '세분류':'str', '세세분류':'str', '보고반영':'str', '기준일':'str','회계연도':'str','전기월':'int', '계정코드':'str', 'bs분류':'str', '계정명':'str', '코스트센터내역':'str'})
    df_all = df_all.reset_index()
    df_all = df_all.astype({'회계연도':'str'})

    cols = st.columns(2)
    with cols[0]:

        # 기준년도, 기준월 INPUT BOX 입력 받기
        기준년도 = st.text_input("년도", "2024")
        비교년도 = int(기준년도)-1
    with cols[1]:    
        기준월 = st.text_input("월", 9)

    targets =[f"{비교년도}",f"{기준년도}"]


    st.markdown("------")

    #부호 조정 함수
    def 금액작업(row):
        if row['중분류'] == '매출':
            val = round(row['금액']*-1)
        elif row['중분류'] == '기부금':
            val = round(row['금액']*-1)
        elif row['중분류'] == '부채':
            val = round(row['금액']*-1)
        else :
            val = round(row['금액']*1)

        return val

    # 함수적용
    df_all['금액2'] = df_all.apply(금액작업, axis=1)

    # 손익구분열 작성
    def 손익구분(row):
        if '매출' in row:
            return '매출'
        elif '기부금' in row:
            return '기부금'
        elif '자산' in row:
            return 'BS'
        elif '부채' in row:
            return 'BS'
        else:
            return '비용'

    # 함수 적용
    df_all['손익구분'] =df_all['중분류'].apply(손익구분)

    # 손익구분 텍스트 만들어 dataframe에 입력
    손익구분 = df_all['손익구분']
    df_all.drop(labels=['손익구분'], axis=1,inplace = True)
    df_all.insert(0, '손익구분', 손익구분)

    # st.dataframe(df_all,use_container_width=True)

    # 계정 소팅 기준
    cost_SORT1 = ['매출','사업비','인건비','일반관리비','건물관리비','지급임차료']
    cost_SORT2 = ['매출','사업비','매출이익','인건비','일반관리비','건물관리비','지급임차료','영업이익']

    # 빈 dataframe 생성
    df_tem = pd.DataFrame()
    df_손익_공연2_누계 = pd.DataFrame()
    df_손익_전시_누계 = pd.DataFrame()
    df_손익_전체_누계 = pd.DataFrame()

    df_손익_공연_월별 = pd.DataFrame()
    df_손익_전시_월별 = pd.DataFrame()
    df_손익_전체_월별 = pd.DataFrame()


    # 빈 alt chart 생성
    c_전체매출 = alt.Chart()
    c_공연매출 = alt.Chart()
    c_전시매출 = alt.Chart()

    c_전체비용 = alt.Chart()
    c_공연비용 = alt.Chart()
    c_전시비용 = alt.Chart()


    ####### 이하 일단 작동 확인 후 재정리 필요#################

    cond_전체 = (df_all['손익구분'] !='BS')
    cond_공연 = (df_all['코스트센터내역'] =='공연')&(df_all['손익구분'] !='BS')
    cond_전시 = (df_all['코스트센터내역'] =='전시')&(df_all['손익구분'] !='BS')
    global 누계손익, 월별손익, bs, 월별bs

    def templit(key, df_all, df_tem, cost_SORT1, cost_SORT2, cond):
        if key == "누계손익":
            df_all = df_all.loc[(df_all['회계연도'].isin(targets)) & (df_all['전기월']<=int(기준월))]

            df_tem = df_all[cond]
            df_tem = df_tem[df_tem['대분류']!='재무상태']
            df_tem = df_tem.groupby(['중분류','회계연도'])['금액2'].sum().unstack().reset_index() # -> 월을 그룹대상에서 빼야 당초 조회 월 누계로 작동

            df_tem["전년비"] = df_tem[f"{기준년도}"]-df_tem[f"{비교년도}"]
            # st.header("공연손익요약")
            df_tem = df_tem.set_index('중분류')
            df_tem = df_tem.reindex(cost_SORT1)

            df_tem.loc["매출이익"] = df_tem.iloc[0] - df_tem.iloc[1]
            df_tem = df_tem.reindex(cost_SORT2)
            df_tem.loc["영업이익"] = df_tem.iloc[2] - df_tem.iloc[3] - df_tem.iloc[4] - df_tem.iloc[5]- df_tem.iloc[6]
            # 인덱스순서 커스텀
            df_tem = df_tem.reindex(cost_SORT2)
            df_tem = round(df_tem/1000000)
            df_tem = df_tem.style.applymap(
                lambda _: "background-color: gray; ", subset=(['매출이익','영업이익'], slice(None))
            ).format('{:,.0f}')


            return df_tem
        elif key =="월별손익":
            df_all = df_all.loc[(df_all['회계연도'].isin(targets)) & (df_all['전기월']<=int(기준월))]
            df_tem = df_all[cond]
            # df_tem = df_tem(df_tem['대분류']!='재무상태')
            df_tem=df_tem.pivot_table(index='중분류', columns=["회계연도","전기월"], values="금액2",aggfunc="sum")
            df_tem = df_tem.reindex(cost_SORT1)

            df_tem.loc["매출이익"] = df_tem.iloc[0] - df_tem.iloc[1]
            df_tem = df_tem.reindex(cost_SORT2)
            df_tem.loc["영업이익"] =  df_tem.iloc[2] - df_tem.iloc[3] - df_tem.iloc[4] - df_tem.iloc[5]- df_tem.iloc[6]
            # 인덱스순서 커스텀
            df_tem = df_tem.reindex(cost_SORT2)
            listVars=df_tem.columns.get_level_values(0)
            
            df_tem.insert(0,'23년',df_tem.loc[:,listVars=='2023'].sum(axis=1).fillna(''))
            df_tem.rename(columns={'':'누계'}, inplace=True)
            listVars=df_tem.columns.get_level_values(0)
            df_tem.insert(1,'24년',df_tem.loc[:,listVars=='2024'].sum(axis=1).fillna(''))
            df_tem.rename(columns={'':'누계'}, inplace=True)


            증감 = df_tem['24년'] - df_tem['23년']
            df_tem.insert(2,'증감',증감)
            df_tem.rename(columns={'':'증감'}, inplace=True)




            df_tem = round(df_tem/1000000)
            
            return df_tem


##재무상태 def#######
    def bs_templit(df_all):
        # if key == "누계손익":
            df_all = df_all.loc[(df_all['회계연도'].isin(targets)) & (df_all['전기월']<=int(기준월))]

            # df_tem = df_all[cond]
            df_tem_bs = df_all[df_all['대분류']=='재무상태']
            df_tem_bs = df_tem_bs.groupby(['보고반영','회계연도'])['금액2'].cumsum()

            # df_tem_bs = df_tem_bs.unstack().reset_index() # -> 월을 그룹대상에서 빼야 당초 조회 월 누계로 작동

            # df_tem_bs["전년비"] = df_tem_bs[f"{기준년도}"]-df_tem_bs[f"{비교년도}"]
            # st.header("공연손익요약")
            # df_tem_bs = df_tem_bs.set_index('보고반영')
            # st.dataframe(df_tem_bs)
            # df_tem = df_tem.reindex(cost_SORT1)

            # df_tem.loc["매출이익"] = df_tem.iloc[0] - df_tem.iloc[1]
            # df_tem = df_tem.reindex(cost_SORT2)
            # df_tem.loc["영업이익"] = df_tem.iloc[2] - df_tem.iloc[3] - df_tem.iloc[4] - df_tem.iloc[5]- df_tem.iloc[6]
            # # 인덱스순서 커스텀
            # df_tem = df_tem.reindex(cost_SORT2)
            # df_tem = round(df_tem/1000000)
            # df_tem = df_tem.style.applymap(
            #     lambda _: "background-color: gray; ", subset=(['매출이익','영업이익'], slice(None))
            # ).format('{:,.0f}')


            return df_tem_bs




    ##############이후 function 앞으로 배치

    domain_1 =['2023', '2024', '전년비']
    range_1 = ['gray', 'white', 'red']



    sort_sale222 = ['티켓','대관','광고협찬','이자','배당','카페임대','기타']
    cost_SORT = ['사업비','인건비','일반관리비','건물관리비','지급임차료']

    df_tem_ch = pd.DataFrame()

    # st.dataframe(df_all)




    def mk_def(k1):
            df_tem_ch = df_all.loc[(df_all['회계연도'].isin(targets)) & (df_all['전기월']<=int(기준월))]
            df_tem_ch['금액3'] = df_tem_ch['금액2']/1000000
            if (str(k1).count("매출") >= 1 and k1 =="매출"):
                df_tem_ch = df_tem_ch.pivot_table(index=['보고반영','중분류','손익구분'], columns=["회계연도"], values="금액3",aggfunc="sum")
            elif (str(k1).count("매출") >= 1 and k1 !="매출"):
                df_tem_ch = df_tem_ch.pivot_table(index=['보고반영','중분류','손익구분','코스트센터내역'], columns=["회계연도"], values="금액3",aggfunc="sum")
            
            elif (str(k1).count("비용") >= 1 and k1 =="비용"):
                df_tem_ch = df_tem_ch.pivot_table(index=['중분류','손익구분'], columns=["회계연도"], values="금액3",aggfunc="sum")
            elif (str(k1).count("비용") >= 1 and k1 !="비용"):
                df_tem_ch = df_tem_ch.pivot_table(index=['중분류','손익구분','코스트센터내역'], columns=["회계연도"], values="금액3",aggfunc="sum")
            
            
            df_tem_ch['전년비'] = df_tem_ch['2024'] - df_tem_ch['2023']
            df_tem_ch = df_tem_ch.stack().reset_index()
            df_tem_ch.rename(columns={0:'금액3'}, inplace=True)

            
            df_tem_ch = df_tem_ch.reset_index()
            return df_tem_ch

    def chart(k1, df_tem_ch, k3, k4, k5):
        df_tem_ch = mk_def(k1)
        if k1 == "매출":
            df_tem_ch = df_tem_ch[df_tem_ch['손익구분'] == "매출"]
            c2= alt.Chart(df_tem_ch).mark_bar().encode(
                x=alt.X('회계연도:O', title=""),
                y=alt.Y('금액3:Q'),
                color=alt.Color('회계연도:O', scale=alt.Scale(domain=domain_1, range=range_1), legend = None),
                ).properties(width=130)
            text = c2.mark_text(
                    dy = alt.ExprRef(alt.expr.if_(alt.datum.금액3 >= 0, -10, 10)),
                    fontSize=18).encode(text=alt.Text("금액3:Q", format=",.0f"))
            k = alt.layer(c2, text, data=df_tem_ch).facet(
                column=alt.Column( "보고반영:N",sort = k3 )).configure_facet(spacing=50).configure_mark(    
                        )
            return k

        if k1 == "공연매출":
            df_tem_ch = df_tem_ch[(df_tem_ch['손익구분']==k5) & (df_tem_ch['코스트센터내역']==k4)]
            
            c_공연매출= alt.Chart(df_tem_ch).mark_bar().encode(
                x=alt.X('회계연도:O', title=""),
                y=alt.Y('금액3:Q'),
                color=alt.Color('회계연도:O', scale=alt.Scale(domain=domain_1, range=range_1), legend = None),
                ).properties(width=130)
            text = c_공연매출.mark_text(
                    dy = alt.ExprRef(alt.expr.if_(alt.datum.금액3 >= 0, -10, 10)),
                    fontSize=18).encode(text=alt.Text("금액3:Q", format=",.0f"))
            c_공연매출_ch = alt.layer(c_공연매출, text, data=df_tem_ch).facet(
                column=alt.Column( "보고반영:N",sort = k3 )).configure_facet(spacing=50).configure_mark(    
                        )
            return c_공연매출_ch

        if k1 == "전시매출":
            df_tem_ch = df_tem_ch[(df_tem_ch['손익구분']==k5) & (df_tem_ch['코스트센터내역']==k4)]

            c_전시매출= alt.Chart(df_tem_ch).mark_bar().encode(
                x=alt.X('회계연도:O', title=""),
                y=alt.Y('금액3:Q'),
                color=alt.Color('회계연도:O', scale=alt.Scale(domain=domain_1, range=range_1), legend = None),
                ).properties(width=130)
            text = c_전시매출.mark_text(
                    dy = alt.ExprRef(alt.expr.if_(alt.datum.금액3 >= 0, -10, 10)),
                    fontSize=18).encode(text=alt.Text("금액3:Q", format=",.0f"))
            c_전시매출_ch = alt.layer(c_전시매출, text, data=df_tem_ch).facet(
                column=alt.Column( "보고반영:N",sort = k3 )).configure_facet(spacing=50).configure_mark(    
                        )
            return c_전시매출_ch



        if k1 == "비용":
            df_tem_ch = df_tem_ch[df_tem_ch['손익구분'] == k5]

            c2= alt.Chart(df_tem_ch).mark_bar().encode(
                x=alt.X('회계연도:O', title=""),
                y=alt.Y('금액3:Q'),
                color=alt.Color('회계연도:O', scale=alt.Scale(domain=domain_1, range=range_1), legend = None),
                ).properties(width=280)
            text = c2.mark_text(
                    dy = alt.ExprRef(alt.expr.if_(alt.datum.금액3 >= 0, -10, 10)),
                    fontSize=18).encode(text=alt.Text("금액3:Q", format=",.0f"))
            k = alt.layer(c2, text, data=df_tem_ch).facet(
                column=alt.Column("중분류:N",sort = cost_SORT )).configure_facet(spacing=50).configure_mark(    
                        )

            return k
        
        if k1 == "공연비용":
            df_tem_ch = df_tem_ch[(df_tem_ch['손익구분']==k5) & (df_tem_ch['코스트센터내역']== k4)]
            c_공연비용= alt.Chart(df_tem_ch).mark_bar().encode(
                x=alt.X('회계연도:O', title=""),
                y=alt.Y('금액3:Q'),
                color=alt.Color('회계연도:O', scale=alt.Scale(domain=domain_1, range=range_1), legend = None),
                ).properties(width=280)
            text = c_공연비용.mark_text(
                    dy = alt.ExprRef(alt.expr.if_(alt.datum.금액3 >= 0, -10, 10)),
                    fontSize=18).encode(text=alt.Text("금액3:Q", format=",.0f"))
            c_공연비용_ch = alt.layer(c_공연비용, text, data=df_tem_ch).facet(
                column=alt.Column("중분류:N",sort = cost_SORT )).configure_facet(spacing=50).configure_mark(    
                        )

            return c_공연비용_ch




        
        if k1 == "전시비용":
            df_tem_ch = df_tem_ch[(df_tem_ch['손익구분']==k5) & (df_tem_ch['코스트센터내역']==k4)]

            c_전시비용= alt.Chart(df_tem_ch).mark_bar().encode(
                x=alt.X('회계연도:O', title=""),
                y=alt.Y('금액3:Q'),
                color=alt.Color('회계연도:O', scale=alt.Scale(domain=domain_1, range=range_1), legend = None),
                ).properties(width=280)
            text = c_전시비용.mark_text(
                    dy = alt.ExprRef(alt.expr.if_(alt.datum.금액3 >= 0, -10, 10)),
                    fontSize=18).encode(text=alt.Text("금액3:Q", format=",.0f"))
            c_전시비용_ch = alt.layer(c_전시비용, text, data=df_tem_ch).facet(
                column=alt.Column("중분류:N",sort = cost_SORT )).configure_facet(spacing=50).configure_mark(    
                        )

            return c_전시비용_ch









    tab1, tab2, tab3, tab4, tab5 = st.tabs(['🏳 DASHBOARD', '🏳 PL_Graph','🏳 PL', '🏳 PL trend', '🏳 B/S'])
    with tab1:

        df_tem_bs = bs_templit(df_all)
        st.dataframe(df_tem_bs)

        cfdata = {'전년동기현금': [30], '기부금증감': [0],'영업활동효과': [0],'미지금이연등': [0],'당기말현금': [0], }



        pd.DataFrame(cfdata)
        st.error("전년동기대비 Cashflow 변동")
        st.dataframe(cfdata,use_container_width=True)
        st.text("")

        col1b, col2b = st.columns(2)
        with col1b:
            st.error("서머리")
            col1, col2, col3 = st.columns(3)
            # st.text("11")
            with col1:
                df_손익_전체_누계 = templit("월별손익", df_all, df_tem , cost_SORT1, cost_SORT2, cond_전체)
                # st.dataframe(df_손익_전체_누계,use_container_width=True)
                # st.dataframe(df_손익_전체_누계)
                st.header("전체")
                # st.markdown('<p class="blank-font"></p>', unsafe_allow_html=True)
                st.text('')
                st.metric("매출", f"{df_손익_전체_누계.iloc[0,1]:,.0f}",f"{df_손익_전체_누계.iloc[0,2]:,.0f}")
                st.text('')
                st.metric("사업비", f"{df_손익_전체_누계.iloc[1,1]:,.0f}",f"{df_손익_전체_누계.iloc[1,2]:,.0f}")
                st.text('')
                # st.markdown('#')
                st.metric("매출이익", f"{df_손익_전체_누계.iloc[2,1]:,.0f}",f"{df_손익_전체_누계.iloc[2,2]:,.0f}")
                판매관리비 = df_손익_전체_누계.iloc[3,1]+df_손익_전체_누계.iloc[4,1]+df_손익_전체_누계.iloc[5,1]+df_손익_전체_누계.iloc[6,1]
                판매관리비_증감 = df_손익_전체_누계.iloc[3,2]+df_손익_전체_누계.iloc[4,2]+df_손익_전체_누계.iloc[5,2]+df_손익_전체_누계.iloc[6,2]
                st.text('')
                st.metric("판매관리비",f"{판매관리비:,.0f}" ,f"{판매관리비_증감:,.0f}")
                st.text('')
                전체영업이익 = df_손익_전체_누계.iloc[7,1]
                st.metric("영업이익", f"{df_손익_전체_누계.iloc[7,1]:,.0f}",f"{df_손익_전체_누계.iloc[7,2]:,.0f}")
                st.text('')
                임차제외_영업이익 = df_손익_전체_누계.iloc[7,1]+df_손익_전체_누계.iloc[6,1]
                임차제외_영업이익_증감 = df_손익_전체_누계.iloc[7,2]+df_손익_전체_누계.iloc[6,2]
                st.metric("임차료제외영업이익", f"{임차제외_영업이익:,.0f}",f"{임차제외_영업이익_증감:,.0f}")

 
            with col2:
                df_손익_공연2_누계 = templit("월별손익", df_all, df_tem , cost_SORT1, cost_SORT2, cond_공연)
                # st.dataframe(df_손익_공연2_누계,use_container_width=True)
                
                st.header("공연")
                st.text('')
                st.metric("매출", f"{df_손익_공연2_누계.iloc[0,1]:,.0f}",f"{df_손익_공연2_누계.iloc[0,2]:,.0f}")
                st.text('')
                st.metric("사업비", f"{df_손익_공연2_누계.iloc[1,1]:,.0f}",f"{df_손익_공연2_누계.iloc[1,2]:,.0f}")
                st.text('')
                st.metric("매출이익", f"{df_손익_공연2_누계.iloc[2,1]:,.0f}",f"{df_손익_공연2_누계.iloc[2,2]:,.0f}")
                공연_판매관리비 = df_손익_공연2_누계.iloc[3,1]+df_손익_공연2_누계.iloc[4,1]+df_손익_공연2_누계.iloc[5,1]+df_손익_공연2_누계.iloc[6,1]
                공연_판매관리비_증감 = df_손익_공연2_누계.iloc[3,2]+df_손익_공연2_누계.iloc[4,2]+df_손익_공연2_누계.iloc[5,2]+df_손익_공연2_누계.iloc[6,2]
                st.text('')
                st.metric("판매관리비",f"{공연_판매관리비:,.0f}" ,f"{공연_판매관리비_증감:,.0f}")
                st.text('')
                st.metric("영업이익", f"{df_손익_공연2_누계.iloc[7,1]:,.0f}",f"{df_손익_공연2_누계.iloc[7,2]:,.0f}")
                st.text('')
                임차제외_영업이익_공연 = df_손익_공연2_누계.iloc[7,1]+df_손익_공연2_누계.iloc[6,1]
                임차제외_영업이익_증감_공연 = df_손익_공연2_누계.iloc[7,2]+df_손익_공연2_누계.iloc[6,2]
                st.metric("임차료제외영업이익", f"{임차제외_영업이익_공연:,.0f}",f"{임차제외_영업이익_증감_공연:,.0f}")

            with col3:
                df_손익_전시_누계 = templit("월별손익", df_all, df_tem , cost_SORT1, cost_SORT2, cond_전시)
                st.header("전시")
                st.text('')
                st.metric("매출", f"{df_손익_전시_누계.iloc[0,1]:,.0f}",f"{df_손익_전시_누계.iloc[0,2]:,.0f}")
                st.text('')
                st.metric("사업비", f"{df_손익_전시_누계.iloc[1,1]:,.0f}",f"{df_손익_전시_누계.iloc[1,2]:,.0f}")
                st.text('')
                st.metric("매출이익", f"{df_손익_전시_누계.iloc[2,1]:,.0f}",f"{df_손익_전시_누계.iloc[2,2]:,.0f}")
                전시_판매관리비 = df_손익_전시_누계.iloc[3,1]+df_손익_전시_누계.iloc[4,1]+df_손익_전시_누계.iloc[5,1]+df_손익_전시_누계.iloc[6,1]
                전시_판매관리비_증감 = df_손익_전시_누계.iloc[3,2]+df_손익_전시_누계.iloc[4,2]+df_손익_전시_누계.iloc[5,2]+df_손익_전시_누계.iloc[6,2]
                st.text('')
                st.metric("판매관리비",f"{전시_판매관리비:,.0f}" ,f"{전시_판매관리비_증감:,.0f}")
                st.text('')
                st.metric("영업이익", f"{df_손익_전시_누계.iloc[7,1]:,.0f}",f"{df_손익_전시_누계.iloc[7,2]:,.0f}")
                st.text('')
                임차제외_영업이익_전시 = df_손익_전시_누계.iloc[7,1]+df_손익_전시_누계.iloc[6,1]
                임차제외_영업이익_증감_전시 = df_손익_전시_누계.iloc[7,2]+df_손익_전시_누계.iloc[6,2]
                st.metric("임차료제외영업이익", f"{임차제외_영업이익_전시:,.0f}",f"{임차제외_영업이익_증감_전시:,.0f}")

            with col2b:
                st.error(f"{기준년도}년 손익 Cash영향 (단위:억원)")
                df_all_wf = df_all[df_all['대분류']=='손익']
                df_all_wf = df_all_wf.loc[(df_all_wf['회계연도'].isin(targets)) & (df_all_wf['전기월']<=int(기준월))]

                df_tem = df_all_wf[cond_전체]
                df_tem = df_tem.groupby(['중분류','회계연도'])['금액2'].sum().unstack().reset_index() # -> 월을 그룹대상에서 빼야 당초 조회 월 누계로 작동
                df_tem = df_tem[['중분류',f'{기준년도}']]
                df_tem = df_tem.set_index('중분류')
                sort_wf = ['기부금','매출','사업비','인건비','일반관리비','건물관리비','지급임차료']
                df_tem = df_tem.reindex(sort_wf)
                df_tem[f'{기준년도}_N'] = 0
                df_tem = df_tem.reset_index()

                def 금액작업(row):
                    if row['중분류'] == '매출':
                        val = round(row['2024']/100000000)
                    elif row['중분류'] == '기부금':
                        val = round(row['2024']/100000000)
                    else :
                        val = round(row['2024']/100000000*-1)

                    return val

                # 함수적용
                df_tem[f'{기준년도}_N'] = df_tem.apply(금액작업, axis=1)
                df_tem = df_tem.set_index('중분류')
                기부금 = df_tem.iloc[0,1]
                # st.text(기부금)
                cashflow = 전체영업이익/100 + 기부금
                

                fig = go.Figure(go.Waterfall(
                    name ="손익흐름", orientation='v',
                    x= df_tem.index, y=df_tem[f'{기준년도}_N'], 
                    text=df_tem['2024_N'],textposition='outside',
                    texttemplate='%{text:,}',
                    increasing={'marker':{"color":"White"}},
                    decreasing={'marker':{"color":"#967078"}},
                    
                ))
                # https://docs.streamlit.io/develop/api-reference/widgets/st.color_picker
                fig.update_layout(height=800,title_text=f"전체현금흐름 영향 : {cashflow}억",
                
                font=dict(
                    size=18,  # Set the font size here
                    color="white",
                    # format=",.0f",
                )
                )
                fig.update_yaxes(showticklabels=False)
                fig.update_layout(
                xaxis = dict(
                tickfont = dict(size=15)),
                title_font_size = 25)
                st.plotly_chart(fig, use_container_width=True)
        st.text("목표대비 실적 그래프")

    with tab2:
        st.text("전체, 공연, 전시별 누적그래프")
        st.text("전체, 공연, 전시별 월별 트랜드그래프")    
    
    with tab3:
        div = st.selectbox("구분손익", ["전체", "공연", "전시"])
        col1, col2, col3 = st.columns(3)

        if div == "전체":
            st.header("전체손익")
            df_손익_전체_누계 = templit("누계손익", df_all, df_tem , cost_SORT1, cost_SORT2, cond_전체)
            st.dataframe(df_손익_전체_누계,use_container_width=True)
        if div == "공연":
            st.header("공연손익")    
            df_손익_공연2_누계 = templit("누계손익", df_all, df_tem , cost_SORT1, cost_SORT2, cond_공연)
            st.dataframe(df_손익_공연2_누계,use_container_width=True)
        # if st.button("전시"):
        if div == "전시":
            st.header("전시손익")    
            df_손익_전시_누계 = templit("누계손익", df_all, df_tem , cost_SORT1, cost_SORT2, cond_전시)
            st.dataframe(df_손익_전시_누계,use_container_width=True)
        
        if "initial_rerun_done" not in st.session_state:
            st.session_state.initial_rerun_done = True
            st.rerun()
            
    with tab4:
        div2 = st.selectbox("구분손익 ", ["전체", "공연", "전시"])
        if div2 == "전체":
            st.header("전체손익")
            df_손익_전체_누계 = templit("월별손익", df_all, df_tem , cost_SORT1, cost_SORT2, cond_전체)
            st.dataframe(df_손익_전체_누계,use_container_width=True)
        if div2 == "공연":
            st.header("공연손익")    
            df_손익_공연2_누계 = templit("월별손익", df_all, df_tem , cost_SORT1, cost_SORT2, cond_공연)
            st.dataframe(df_손익_공연2_누계,use_container_width=True)
        if div2 == "전시":
            st.header("전시손익")    
            df_손익_전시_누계 = templit("월별손익", df_all, df_tem , cost_SORT1, cost_SORT2, cond_전시)
            st.dataframe(df_손익_전시_누계,use_container_width=True)
        if "initial_rerun_done" not in st.session_state:
            st.session_state.initial_rerun_done = True
            st.rerun()

    with tab5:

        st.markdown('--------------')
        st.header("재무상태")

        st.error("bs테이블")

        df_all_bs = df_all[df_all['손익구분'] == "BS"]

        # ★감가상각누계액 제외 조건 반영 필요 ->
        df_all_bs['누적금액'] = df_all_bs.groupby('보고반영')['금액2'].cumsum() #를 함수로 변환



        st.dataframe(df_all_bs,use_container_width=True)
        df_all_bs_보고반영 = df_all_bs.groupby(by=['중분류','세분류','bs분류'])['금액2'].sum()
        st.text("groupby 1차")
        st.dataframe(df_all_bs_보고반영, use_container_width= True)

        df_all_bs = df_all_bs.reset_index()
        df_all_bs_약식 = df_all_bs.pivot_table(index=['중분류','세분류',"bs분류"], columns=["기준일"], values="금액2",aggfunc="sum")
        st.dataframe(df_all_bs_약식,use_container_width=True)

        df_all_bs_약식 = round(df_all_bs_약식/1000000)
        st.dataframe(df_all_bs_약식,use_container_width=True)

        기준일 = str(기준년도) + "-" + str(기준월.rjust(2,'0')) + "-" + "01"
        비교일 = str(비교년도) + "-" + str(기준월.rjust(2,'0')) + "-" + "01"

        st.text(기준일)
        st.text(비교일)

        st.text("시점기준 불러오기")
        listVars_bs=df_all_bs_약식.columns.get_level_values(0)


        df_all_bs_약식.insert(0,f'{기준일}누계',df_all_bs_약식.loc[:,listVars_bs <= 기준일].sum(axis=1).fillna(''))
        listVars_bs=df_all_bs_약식.columns.get_level_values(0)
        df_all_bs_약식.insert(1,f'{비교일}누계',df_all_bs_약식.loc[:,listVars_bs <= 비교일].sum(axis=1).fillna(''))
        증감 = df_all_bs_약식[f'{기준일}누계'] - df_all_bs_약식[f'{비교일}누계']
        df_all_bs_약식.insert(2,'증감',증감)
        df_all_bs_약식 = df_all_bs_약식.sort_index(ascending=False)


        st.dataframe(df_all_bs_약식, use_container_width=True)

        st.text("누계만 발라내기 - bs분류 일치화 필요")

        df_all_bs_약식_누계 = df_all_bs_약식[[f'{비교일}누계',f'{기준일}누계','증감']]
        df_all_bs_약식_누계.columns = df_all_bs_약식_누계.columns.str.replace('-01누계', '누계')

        df_all_bs_약식_누계_요약 = df_all_bs_약식_누계.groupby(by=['중분류','세분류']).sum([f'{비교일}누계',[f'{기준일}누계']])
        df_all_bs_약식_누계_요약_증감대상 = df_all_bs_약식_누계_요약
        st.text("중분류합계 테스트")

        df_all_bs_약식_누계_요약.insert(0,'bs분류',"")
        st.dataframe(df_all_bs_약식_누계_요약,use_container_width=True)

        # df_all_bs_약식_누계 = round(df_all_bs_약식_누계/1000000)
        df_all_bs_약식_누계_임시 = df_all_bs_약식_누계
        st.dataframe(df_all_bs_약식_누계,use_container_width=True)

        st.text("중분류합계 테스트 - 합계테이블 병합 테스트")
        df_all_bs_약식_누계 = df_all_bs_약식_누계.reset_index()

        df_all_bs_약식_누계_요약 = df_all_bs_약식_누계_요약.reset_index()
        df_all_bs_약식_누계_병합 = pd.concat([df_all_bs_약식_누계,df_all_bs_약식_누계_요약])


        df_all_bs_약식_누계_병합 = df_all_bs_약식_누계_병합.set_index(['중분류','세분류','bs분류'])
        df_all_bs_약식_누계_병합 = df_all_bs_약식_누계_병합.sort_index(axis=0, level=[0,1,2],ascending=[False,False,True])


        st.dataframe(df_all_bs_약식_누계_병합,use_container_width=True)



        df_all_bs_약식_누계_병합 = df_all_bs_약식_누계_병합.reset_index()


        st.text("t전")
        st.dataframe(df_all_bs_약식_누계_병합,use_container_width=True)


        df_all_bs_약식_누계_병합_서식대상 = df_all_bs_약식_누계_병합[df_all_bs_약식_누계_병합['bs분류']==""]

        st.text("서식대상 필터 테스트")

        st.dataframe(df_all_bs_약식_누계_병합_서식대상, use_container_width= True)


        # 조건 1은 콜_행사가, 콜_수량합계 열에, 조건 2는 풋_행사가, 풋_수량합계 열에 적용 


        st.text("서식대상 필터 테스트_apply후")
        df_all_bs_약식_누계_병합 = df_all_bs_약식_누계_병합.style.applymap(
                    lambda x: f"background-color: gray; ", subset = (df_all_bs_약식_누계_병합_서식대상[df_all_bs_약식_누계_병합_서식대상['bs분류'] ==""].index,slice(None))
                    # lambda _: "background-color: gray; ", subset=(['bs중분류','영업이익'], slice(None))
                ).format(precision=0, thousands=',')


        st.dataframe(df_all_bs_약식_누계_병합,use_container_width=True)




        # 증감내역 작성 테스트
        #row string test

        증감텍스트_list = df_all_bs_약식_누계_병합_서식대상['세분류'].unique()
        st.text(증감텍스트_list)

        row_s1 = df_all_bs_약식_누계_병합_서식대상.iloc[0].to_string()
        st.text(row_s1)


        # row_s2 = '   '.join(df_all_bs_약식_누계_병합_서식대상.iloc[0,1:].astype(str).format(precision=0, thousands=',')) -> .format(precision=0, thousands=',')) : error AttributeError: 'Series' object has no attribute 'format'
        row_s2 = '   '.join(df_all_bs_약식_누계.iloc[0,1:].astype(str))
        st.text(row_s2)

        ####################################################################################################
        st.text("df전체 텍스트 테스트")
        # st.text(k)

        # ss =[]
        # def text_f(k):
        #     ss = '   '.join(df_all_bs_약식_누계_병합_서식대상.iloc[k].astype(str))
        #     # return k_t
        #     ss = ss + ss[k]
        #     # st.text(ss)

        # for k in range(0,3):
        #     text_f(k)


        # st.text("df전체 텍스트 테스트")
        # st.text(ss)
        ####################################################################################################
        ##작동###
        # ss = df_all_bs_약식_누계_병합_서식대상.iloc[:,1:].to_string(header=False, index=False,index_names=False).split('\n')
        # vals = ['.'.join(ele.split()) for ele in ss]
        # st.text(ss)


        # df_all_bs_약식_누계_요약_증감내역 = pd.DataFrame()
        df_all_bs_약식_누계_요약_증감내역 = df_all_bs_약식_누계_요약
        df_all_bs_약식_누계_요약_증감대상 = df_all_bs_약식_누계_임시.reset_index()
        df_all_bs_약식_누계_요약_증감내역['증감내역'] = ""
        ##작동###

        # global t_구분
        # t_구분 =""
        # t_구분 ="비유동자산"

            
        df_all_bs_약식_비유동자산 = df_all_bs_약식_누계_요약_증감대상[df_all_bs_약식_누계_요약_증감대상['세분류']=="비유동자산"]
        st.dataframe(df_all_bs_약식_비유동자산,use_container_width=True)

        ss = df_all_bs_약식_비유동자산.iloc[:,2:].to_string(header=False, index=False,index_names=False).split('\n')
        vals = ['.'.join(ele.split()) for ele in ss]


        st.dataframe(df_all_bs_약식_누계_임시,use_container_width=True)
        # st.text(type(ss))
        st.text(ss)


        df_all_bs_약식_누계_요약_증감내역 = df_all_bs_약식_누계_요약_증감내역.set_index('세분류')

        df_all_bs_약식_누계_요약_증감내역.at["비유동자산", '증감내역'] = ss
        st.dataframe(df_all_bs_약식_누계_요약_증감내역,use_container_width=True)

        # st.dataframe(df_all_bs_약식_누계_요약_증감내역,use_container_width=True)

        ####################################333
        # t_구분 ="유동자산"
            
        df_all_bs_약식_유동자산 = df_all_bs_약식_누계_요약_증감대상[df_all_bs_약식_누계_요약_증감대상['세분류']== "유동자산"]
        ss = df_all_bs_약식_유동자산.iloc[:,2:].to_string(header=False, index=False,index_names=False).split('\n')
        vals = ['.'.join(ele.split()) for ele in ss]

        st.dataframe(df_all_bs_약식_유동자산,use_container_width=True)

        # st.dataframe(df_all_bs_약식_누계_임시,use_container_width=True)
        # st.text(type(ss))
        # st.text(ss)


        # df_all_bs_약식_누계_요약_증감내역 = df_all_bs_약식_누계_요약
        # df_all_bs_약식_누계_요약_증감내역 = df_all_bs_약식_누계_요약_증감내역.set_index(['중분류','세분류'])
        # df_all_bs_약식_누계_요약_증감내역['증감'] = ""

        # st.dataframe(df_all_bs_약식_누계_요약_증감내역,use_container_width=True)

        df_all_bs_약식_누계_요약_증감내역.at["유동자산", '증감내역'] = ss

        # for t_구분 in ['유동자산','비유동자산']:
        #     증감입력(t_구분)



        ########################################
        st.markdown(df_all_bs_약식_누계_요약_증감내역.to_html(escape=False),unsafe_allow_html=True)

        df_all_bs_약식_누계_요약_증감내역 = df_all_bs_약식_누계_요약_증감내역.reset_index()
        # df_all_bs_약식_누계_요약_증감내역 = df_all_bs_약식_누계_요약_증감내역.reindex([1,0,3,4])

        # gd = GridOptionsBuilder.from_dataframe(df_all_bs_약식_누계_요약_증감내역)
        # gd.configure_pagination(enabled=True)
        # gd.configure_default_column(editable=True,groupable=True,)

        # const gridOptions = {
        #     columnDefs: [
        #         simple currency formatter
        #         { field: 'price', valueFormatter: p => '$' + params.value },
        #         # simple UPPER CASE formatter
        #         # { field: 'code', valueFormatter: p => params.value.toUpperCase() }
        #     ],
        # }


        # st.header("증감내역")
        # def configure_ag_grid():
        # gb = GridOptionsBuilder.from_dataframe(df_all_bs_약식_누계_요약_증감내역)
        # gridOptions = gb.build()
        # gb.configure_grid_options(autoHeight=True)
            # gb.configure_column("2023-09누계", 
            #                 type=["numericColumn","numberColumnFilter","customNumericFormat"], 
            #                 valueGetter="data.09누계.toLocaleString('en-US', {style: 'currency', currency: 'USD', maximumFractionDigits:1})")  
            # gb.configure_column('MySum', type=['numericColumn'], valueGetter='(Number(data.EMPLVL) * 5.23).toFixed(1)', editable='false', resizable=False, sortable=False)
            # gb.configure_columns(df_all_bs_약식_누계_요약_증감내역, wrapText=True, autoHeight=True, width=150)
            # gb.configure_column('2023-09누계', type=['numericColumn'], valueGetter='', editable='false', resizable=False, sortable=False)
            # gb.configure_column("2023-09누계", header_name=("2023-09누계"), editable=True, type=["numericColumn","numberColumnFilter","customNumericFormat"], precision=0)
            # gb.configure_column({'2023-09누계', valueGetter: params})
            #★ 천단위 컴마 표시 방법 STUDY필요

            # gb.configure_columns('2023-09누계', wrapText=True, autoHeight=True, width=150, type=['numericColumn'], precision=1)
            # gb.configure_column('2023-09누계', type=['numericColumn'], valueGetter='2023-09누계', editable='false', resizable=False, sortable=False)
            # gb.configure_column("2023-09누계", header_name=("2023-09누계"), editable=True, type=["numericColumn","numberColumnFilter","customNumericFormat"], precision=0)
            # gb.configure_column('2023-09누계', type=['numericColumn'], valueGetter='(Number(df_all_bs_약식_누계_요약_증감내역.2023-09누계)', editable='false', resizable=False, sortable=False)
            # gb.configure_column("2023-09누계", header_name="2023-09누계", editable=True, type="numericColumn", precision=0)

            # gb.configure_column('MySum', type=['numericColumn'], valueGetter='(Number(data.EMPLVL) * 5.23).toFixed(1)', editable='false', resizable=False, sortable=False)
            # gb.configure_columns('2023-09누계',type=['numericColumn'],valueGetter='Number(de-DE)', editable='false', resizable=False, sortable=False)
            # gb.configure_columns(df_all_bs_약식_누계_요약_증감내역, wrapText=True, autoHeight=True, width=150,header_name='2023-09누계',type=['numericColumn','numberColumnFilter','customNumericFormat','customNumericFormat'], precision=1)
        # gb.configure_columns('2023-09누계', wrapText=True, autoHeight=True, width=150, type='numericColumn', precision=0)
        # op = gb.configure_column('2023-09누계', header_name=('2023-09누계'), editable=True, type=["numericColumn","numberColumnFilter","customNumericFormat"], precision=0)
        # op = gb.configure_column('2023-09누계', header_name=('2023-09누계'), editable=True, type="numericColumn", precision=0)
        # gb.configure_column('2023-09누계', wrapText=False, autoHeight=True, width=150, type=['numericColumn'], precision=0)
        # }

        # AgGrid(gb)
        # AgGrid(gb)
        # st.text(gb)


        # configure_ag_grid()

        # AgGrid(df_all_bs_약식_누계_요약_증감내역, gridOptions=op)



        # gb = GridOptionsBuilder.from_dataframe(df_all_bs_약식_누계_요약_증감내역)



        # gb = GridOptionsBuilder.from_dataframe(df_all_bs_약식_누계_요약_증감내역)

        # columnDefs=[
        #                     {
        #                         "field": "1",
        #                         "editable": True,
        #                         "type": "numeric",
        #                         "valueFormatter": {
        #                             "function": "d3.format('(,.1f')(params.value)"
        #                         },
        #                     },
        #                     {
        #                         "field": "2",
        #                         "editable": True,
        #                         "type": "numeric",
        #                         "valueFormatter": {
        #                             "function": "d3.format('(,.1f')(params.value)"
        #                         },
        #                     },
        #                     {
        #                         "field": "3",
        #                         "editable": True,
        #                         "type": "numeric",
        #                         "valueFormatter": {
        #                             "function": "d3.format('(,.1f')(params.value)"
        #                         },
        #                     },
        #                     {
        #                         "field": "Sum",
        #                         "valueGetter": {
        #                             "function": "params.data['1']+params.data['2']+params.data['3']);"
        #                         },
        #                     },
        # ]


        # op = gb.configure_column('2023-09누계', header_name=('2023-09누계'), editable=True, type="numericColumn", precision=0)


        df_all_bs_약식_누계_요약_증감내역 = df_all_bs_약식_누계_요약_증감내역.astype({'2023-09누계':'int'}) 
        st.dataframe(df_all_bs_약식_누계_요약_증감내역,use_container_width=True)


        # gb.configure_column("2023-09누계", 
        #                     type=["numericColumn","numberColumnFilter","customNumericFormat"], 
        #                     valueGetter="data.AMT.toLocaleString('en-US', {style: 'currency', currency: 'USD', maximumFractionDigits:1})") 

        # https://streamlit-aggrid.readthedocs.io/en/docs/GridOptionsBuilder.html

        df_all_bs_약식_누계.columns = df_all_bs_약식_누계.columns.str.replace('-', '.')
        df_all_bs_약식_누계.columns = df_all_bs_약식_누계.columns.str.replace('누계', '')

        # df_tt = df_all_bs_약식_누계_요약_증감내역
        df_tt = df_all_bs_약식_누계
        # gb = GridOptionsBuilder.from_dataframe(df_all_bs_약식_누계_요약_증감내역,editable=True)
        # gb = GridOptionsBuilder.from_dataframe(df_tt,editable=True)
        st.text("xddddd")

        # gb = GridOptionsBuilder.from_dataframe(df_tt)
        # gb.configure_pagination(enabled=True)
        # gb.configure_column('202309누계', header_name='202309누계', editable=True, type=["numericColumn"], precision=0)
        # AgGrid(gb,gridOptions=gridOptions)

        # gb.configure_column("증감내역",wrapText = True, autoSizeColumns = True, wrapHeaderText=  True, autoHeaderHeight= True,autoHeight = True)
        # gb.configure_columns(autoSizeColumns = True)
        # https://www.restack.io/docs/streamlit-knowledge-streamlit-aggrid-column-width-guide#clvmvev7103v0hjp2dxm8cxxr
        # gb.configure_column(
        #     field="증감내역",
        #     header_name="증감내역 Plant",
        #     flex=1
        # )
        # gridOptions = {'autoSizeColumns': ['allColumns']}


        # gb.configure_grid_options(
        #     autoGroupColumnDef=dict(
        #         flex=1,
        #     )
        # )


        # gb.configure_grid_options(
        #     autoGroupColumnDef=dict(
        #         flex=1,
        #         minWidth=300, 
        #         pinned="left", 
        #         cellRendererParams=dict(suppressCount=True)
        #     )
        # )

        # gb.configure_column("증감내역",autoHeight = True)
        # gb.configure_default_column(editable=True, groupable=True)
        # gb.configure_selection(selection_mode = 'multiple',use_checkbox=False)

        # gridoptions = gb.build()

        # grid_table = AgGrid(df_tt, gridOptions=gridOptions)
                            
        # # grid_table = AgGrid(df_tt, flex=1, gridOptions=gridOptions, wrapText=  True,
        #                         update_mode=GridUpdateMode.SELECTION_CHANGED | GridUpdateMode.VALUE_CHANGED,
        #                         # height=650, width = 8000,
        #                         allow_unsafe_jscode=True)

        st.dataframe(df_tt,use_container_width=True)



        # https://blog.streamlit.io/building-a-pivottable-report-with-streamlit-and-ag-grid/




        # grid_table = AgGrid(df, columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS)
        # AgGrid(df_all_bs_약식_누계_요약_증감내역, gridOptions=op)
        # AgGrid(df_all_bs_약식_누계_요약_증감내역, gridOptions= gridOptions)
        # st.dataframe(df_all_bs_약식_누계_요약_증감내역.to_html(escape=False),use_container_width=True)

        # gb = GridOptionsBuilder.from_dataframe(df_all_bs_약식_누계_요약_증감내역,editable=True)


        # grid_options = {
        #     "columnDefs": [
        #         {
        #             "headerName": "2023-09누계",
        #             "field": "2023-09누계",
        #             "editable": True,
        #             "type" : "numericColumn",
        #             "wrapText" : True,
        #         },
        #         {
        #             "headerName": "2024-09누계",
        #             "field": "2024-09누계",
        #             "editable": True,
        #             "type" : "numericColumn",
        #             "wrapText" : True,
        #         },
        #     ],
        # }
        # st.header("ㅅㅅㅅㅅㅅㅅ22222")



        # AgGrid(df_all_bs_약식_누계_요약_증감내역, gridOptions=grid_options)
        # grid_return = AgGrid(df_all_bs_약식_누계_요약_증감내역, grid_options)


        # new_df = grid_return["data"]
        # st.header("ㅅㅅㅅㅅㅅㅅ")
        # st.write(new_df,unsafe_allow_html=True)
        # grid_return


        st.text("new_data test")
        df_all_bs_약식_누계_요약_증감내역.columns = df_all_bs_약식_누계_요약_증감내역.columns.str.replace('-', '')
        df_all_bs_약식_누계_요약_증감내역.columns = df_all_bs_약식_누계_요약_증감내역.columns.str.replace('누계', '')
        df_all_bs_약식_누계_요약_증감내역.columns = df_all_bs_약식_누계_요약_증감내역.columns.str.replace('202409', '_2024년')
        df_all_bs_약식_누계_요약_증감내역.columns = df_all_bs_약식_누계_요약_증감내역.columns.str.replace('202309', '_2023년')

        # df_all_bs_약식_누계_요약_증감내역 = df_all_bs_약식_누계_요약_증감내역.columns.str.replace(pat=r'[^\w]',repl=r' ',regex=True)
        # df = pd.DataFrame(df_all_bs_약식_누계_요약_증감내역)
        df = df_all_bs_약식_누계_요약_증감내역
        st.dataframe(df)
        # gb = GridOptionsBuilder.from_dataframe(df_all_bs_약식_누계_요약_증감내역,editable=True)

        # gb.configure_column('2023-09누계', wrapText=True, autoHeight=True, width=150, type=['numericColumn'], precision=1)
        # gb.configure_column("2023-09누계", type=["customCurrencyFormat"], custom_currency_symbol="%")
        # gb.configure_column('2023-09누계', type=['numericColumn'], valueGetter='(Number(data.EMPLVL) * 5.23).toFixed(1)', editable='false', resizable=False, sortable=False)
        # gb.configure_column("2023-09누계", 
        #                     type=["numericColumn","numberColumnFilter","customNumericFormat"], 
        #                     valueGetter="data.2023-09누계.toLocaleString('en-US', {style: 'currency', currency: 'USD'})") 
        # gb.configure_column("2023-09누계", header_name=("2023-09누계"), editable=True, type=["numericColumn","numberColumnFilter","customNumericFormat"], precision=0)
        # gb.configure_column("2023-09누계", type=["customNumericFormat"], customNumericFormat='{,}')
        # https://discuss.streamlit.io/t/format-date-time-in-aggrid/23658/5
        # gb.configure_column("2023-09누계", 
        #                     type=["numericColumn","numberColumnFilter","customNumericFormat"], 
        #                     valueFormatter="data.2023-09누계.toLocaleString('en-US');") 


        # gb = GridOptionsBuilder.from_dataframe(df)

        ### ok 작동
        # gb.configure_column("증감", 
        #                     type=["numericColumn","numberColumnFilter","customNumericFormat"], 
        #                     valueFormatter="data.증감.toLocaleString('en-US');") 
        st.text(df.columns[5])
        # tt = df.columns[3]




        # tt = list(df.columns[2:6])
        # st.text(tt)
        # for i in tt:
        #     gb.configure_column(i, 
        #                     type=["numericColumn","numberColumnFilter","customNumericFormat"], 
        #                     # valueFormatter=f"data.{tt}.toLocaleString('en-US');") 
        #                     valueFormatter=f"data.{i}.toLocaleString('en-US');") 


        # vgo = gb.build()
        # AgGrid(df, gridOptions=vgo)


        # gb = GridOptionsBuilder.from_dataframe(df)

        # tt = df.columns[4]
        # st.text(tt)
        # gb.configure_column(df.columns[4], 
        #                     type=["numericColumn","numberColumnFilter","customNumericFormat"], 
        #                     # valueFormatter=f"data.{tt}.toLocaleString('en-US');") 
        #                     valueFormatter=f"data.{tt}.toLocaleString('en-US');") 


        # vgo = gb.build()
        # AgGrid(df, gridOptions=vgo)

        tt = str(df.columns[4])
        st.text(tt)
        # gb.configure_columns(df.columns[4], 
        #                     type=["numericColumn","numberColumnFilter","customNumericFormat"], 
        #                     valueFormatter=f"data.{tt}.toLocaleString('en-US');") 
        # vgo = gb.build()
        # AgGrid(df, gridOptions=vgo)


        # gb.configure_column("Env_Oran", type=["customCurrencyFormat"], custom_currency_symbol="%")
        # https://www.ag-grid.com/javascript-data-grid/column-definitions/
        # gb.configure_column("team", rowGroup=True, hide=True)

        # grid = AgGrid(df,
        #             gridOptions=gb.build(),            
        #             updateMode=GridUpdateMode.VALUE_CHANGED,
        #             allow_unsafe_jscode=True)

        # https://discuss.streamlit.io/t/python-streamlit-ag-grid-dynamic-edit/61158/2
        # https://discuss.streamlit.io/t/streamlit-aggrid-version-creating-an-aggrid-with-columns-with-embedded-urls/39640/2
        df_all_bs_약식 = df_all_bs_약식.reset_index()


        st.text("test3")
        df = pd.DataFrame(df_all_bs_약식_누계_요약_증감내역)
        # gb = GridOptionsBuilder.from_dataframe(df_all_bs_약식_누계_요약_증감내역,editable=True)


        # grid = AgGrid(df,
        #             gridOptions=gb.build(),
        #             updateMode=GridUpdateMode.VALUE_CHANGED,
        #             allow_unsafe_jscode=True)




        # st.text("test4")


        # data = {
        #     "Name": ["Alice", "Bob", "Charlie"],
        #     "Age": [25, 30, 35],
        #     "link": [
        #         "https://example.com/alice",
        #         "https://example.com/bob",
        #         "https://example.com/charlie",
        #     ],
        # }

        # df = pd.DataFrame(data)
        # gb = GridOptionsBuilder.from_dataframe(df,
        #                                         editable=True)

        # cell_renderer =  JsCode("""
        #                         function(params) {return `<a href=${params.value} target="_blank">${params.value}</a>`}
        #                         """)


        # gb.configure_column(
        #     "link",
        #     headerName="link",
        #     width=100,
        #     cellRenderer=JsCode("""
        #         class UrlCellRenderer {
        #         init(params) {
        #             this.eGui = document.createElement('a');
        #             this.eGui.innerText = 'SomeText';
        #             this.eGui.setAttribute('href', params.value);
        #             this.eGui.setAttribute('style', "text-decoration:none");
        #             this.eGui.setAttribute('target', "_blank");
        #         }
        #         getGui() {
        #             return this.eGui;
        #         }
        #         }
        #     """)
        # )

        # grid = AgGrid(df,
        #             gridOptions=gb.build(),
        #             updateMode=GridUpdateMode.VALUE_CHANGED,
        #             allow_unsafe_jscode=True)



        # st.text("test5")

        # # 회사 데이터 구조를 DataFrame으로 변환
        # data = [
        #     {"company": "Company A", "hq": "HQ 1", "team": "Team 1-1", "part": "Part 1-1"},
        #     {"company": "Company A", "hq": "HQ 1", "team": "Team 1-1", "part": "Part 1-2"},
        #     {"company": "Company A", "hq": "HQ 1", "team": "Team 1-1", "part": "Part 1-3"},
        #     {"company": "Company A", "hq": "HQ 1", "team": "Team 1-2", "part": "Part 2-1"},
        #     {"company": "Company A", "hq": "HQ 1", "team": "Team 1-3", "part": "Part 2-2"},
        #     {"company": "Company A", "hq": "HQ 2", "team": "Team 2-1", "part": "Part 2-3"},
        #     {"company": "Company A", "hq": "HQ 2", "team": "Team 2-2", "part": "Part 3-1"},
        #     {"company": "Company B", "hq": "HQ 3", "team": "Team 3-1", "part": "Part 3-2"},
        #     {"company": "Company B", "hq": "HQ 3", "team": "Team 3-2", "part": "Part 3-3"},
        #     {"company": "Company B", "hq": "HQ 4", "team": "Team 4-1", "part": "Part 4-1"},
        #     {"company": "Company B", "hq": "HQ 4", "team": "Team 4-2", "part": "Part 4-2"},
        #     {"company": "Company B", "hq": "HQ 4", "team": "Team 4-3", "part": "Part 4-3"},
        # ]

        # df = pd.DataFrame(data)
        # st.dataframe(df, use_container_width=True)
        # # Ag-Grid 설정
        # gb = GridOptionsBuilder.from_dataframe(df)
        # gb.configure_default_column(groupable=True)
        # gb.configure_column("company", rowGroup=True, hide=True)
        # gb.configure_column("hq", rowGroup=True, hide=True)
        # gb.configure_column("team", rowGroup=True, hide=True)
        # #gb.configure_column("part", rowGroup=True, hide=True)
        # gb.configure_column("part", header_name="Team", min_width=250)

        # gridOptions = gb.build()

        # st.header("Company Structure")

        # AgGrid(df, gridOptions=gridOptions, enable_enterprise_modules=True)



        # st.text('test6')

        # df = pd.DataFrame({'col1': [1000, 2000, 3000], 'col2': [4000, 5000, 6000]})

        # gb = GridOptionsBuilder.from_dataframe(df)
        # gb.configure_column("col2", 
        #                     type=["numericColumn","numberColumnFilter","customNumericFormat"], 
        #                     valueFormatter="data.col2.toLocaleString('en-US');") 
        # vgo = gb.build()
        # AgGrid(df, gridOptions=vgo)




        #####레퍼 사이트
        # https://streamlit-aggrid.readthedocs.io/en/docs/Usage.html


        # df_all_bs_약식_누계_요약_증감내역.at[1,'증감'] = ss  # at[0,'증감'] ==> 에러 ==> at을 함수화 불가
        # df_all_bs_약식_누계_요약_증감내역.loc[df_all_bs_약식_누계_요약_증감내역['세분류']=='유동자산'].at['증감'] = ss  # loc로 일단 안됨

        # df_all_bs_약식_누계_요약_증감내역.at[('자산','유동자산')]['증감'] = ss #-> 에러
        # df_all_bs_약식_누계_요약_증감내역.loc[('자산','유동자산'), '증감'] = ss




        # df_all_bs_약식 = df_all_bs_약식.set_index('중분류')

        # df_all_bs_약식 = df_all_bs_약식.sort_index(ascending=False)
        df_all_bs_약식 = df_all_bs_약식.sort_index(ascending=False)

        df_all_bs_약식 = df_all_bs_약식.sort_values(기준일,ascending=False)


        #자산 sort

        # df_all_bs_약식.reindex()
        df_all_bs_약식_s = df_all_bs_약식.reset_index()

        st.text("요약BS")

        st.dataframe(df_all_bs_약식_s, use_container_width=True)



        st.dataframe(df_all_bs_약식_s)


        df_all_bs_약식.rename(columns = {기준일 : 기준일[0:7], 비교일 : 비교일[0:7]}, inplace = True)
        st.dataframe(df_all_bs_약식,use_container_width=True)


        st.dataframe(df_all_bs_약식,use_container_width=True)



        # df_all_bs_약식["기준일"].head()
        # st.text("헤더 일부제거")
        # st.dataframe(df_all_bs_약식,use_container_width=True)



        # st.text("찍어서 보기 - 18년 3월말 가수금")
        # df_all_bs_약식= df_all_bs_약식.reset_index()
        # ttt = df_all_bs_약식[df_all_bs_약식['보고반영']=="가수금"]['2016-07-01']

        # st.text(ttt)

