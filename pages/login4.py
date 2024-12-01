
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

import pickle
from pathlib import Path
import streamlit_authenticator as stauth
from streamlit_navigation_bar import st_navbar
# import bcrypt



st.set_page_config(
    page_title = "FINANCIAL Data Dashboard",
    page_icon = "Active",        
    layout="wide"
    )
hide_streamlit_markers=False

# st.set_page_config(initial_sidebar_state="collapsed")
###############################################################################################

# def round_value(input_value):
#     if input_value.values > 1:
#         a = float(round(input_value, 2))
#     else:
#         a = float(round(input_value, 8))
#     return a



#######################################################################################33

# page_test = st_navbar(["Home", "Documentation", "Examples", "Community", "About"])
# st.write(page_test)


names = ["koo","sun","myung"]
usernames = ["kkoo","sun","myung"]

file_path = Path(__file__).parent / "hashed_pw.pkl"

with file_path.open("rb") as file:
    # hashed_passwords = pickle.load(file, encoding = 'utf-8')
    hashed_passwords = pickle.load(file)


authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "FINANCIAL Data Dashboard", "addfd", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")
# st.text(hashed_passwords)

if authentication_status == False:
    st.error("error check")
if authentication_status == None:
    st.error("please enter your name and pw")
if authentication_status:
    # st.header("hellow")
    cols = st.columns(20)
    with cols[19]:
        authenticator.logout("logout","main")    

    # tab1, tab2, tab3, tab4, tab5 = st.tabs(['🏳 DASHBOARD', '🏳 PL', '🏳 BS', '🏳 PROCESSING', '🏳 DETECT'])
    # with tab3:
    #     tab1, tab2, tab3, tab4, tab5 = st.tabs(['🏳 Trend', '🏳 Weekly', '🏳 Average', '🏳 Forcasting', '🏳 History'])
    

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
            # st.dataframe(df_tem_ch)
            # st.dataframe(df_tem_ch)
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

    # col1, col2, col3 = st.columns(3)

    # # Widget (Cryptocurrency selection box)
    # col1_selection = st.sidebar.selectbox('Price 1', df.symbol, list(df.symbol).index('BTCBUSD') )
    # col2_selection = st.sidebar.selectbox('Price 2', df.symbol, list(df.symbol).index('ETHBUSD') )
    # col3_selection = st.sidebar.selectbox('Price 3', df.symbol, list(df.symbol).index('BNBBUSD') )

    # # DataFrame of selected Cryptocurrency
    # col1_df = df[df.symbol == col1_selection]
    # col2_df = df[df.symbol == col2_selection]
    # col3_df = df[df.symbol == col3_selection]

    # # Apply a custom function to conditionally round values
    # col1_price = round_value(col1_df.weightedAvgPrice)
    # col2_price = round_value(col2_df.weightedAvgPrice)
    # col3_price = round_value(col3_df.weightedAvgPrice)

    # # Select the priceChangePercent column
    # col1_percent = f'{float(col1_df.priceChangePercent)}%'
    # col2_percent = f'{float(col2_df.priceChangePercent)}%'
    # col3_percent = f'{float(col3_df.priceChangePercent)}%'

    # # Create a metrics price box
    # col1.metric(col1_selection, col1_price, col1_percent)
    # col2.metric(col2_selection, col2_price, col2_percent)
    # col3.metric(col3_selection, col3_price, col3_percent)
    # st.header('**All Price**')
    # # st.dataframe(df)

    # st.info('Credit: Created by Chanin Nantasenamat (aka [Data Professor](https://youtube.com/dataprofessor/))')



    st.header('손익')
    with st.expander("🔍전체손익"):    

        choice = st.radio(
                "Table or Monthly Table",
                ["전체Table","전체Monthly Table","전체매출차트", "전체비용차트"],
            )
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        

        if choice == "전체Table":  
            df_손익_전체_누계 = templit("누계손익", df_all, df_tem , cost_SORT1, cost_SORT2, cond_전체)
            st.dataframe(df_손익_전체_누계, use_container_width=True)

        if choice == "전체Monthly Table":  
            df_손익_전체_누계 = templit("월별손익", df_all, df_tem , cost_SORT1, cost_SORT2, cond_전체)
            st.dataframe(df_손익_전체_누계, use_container_width=True)


        if choice == "전체매출차트":  
            st.text("매출차트")
            c_전체매출 = chart("매출", df_tem_ch, sort_sale222, "전체", "매출")
            
            st.altair_chart(c_전체매출, use_container_width=True)

        if choice == "전체비용차트":  
            st.text("비용차트")
            chart_비용 = chart("비용", df_tem_ch, cost_SORT,"전체", "비용")
            st.altair_chart(chart_비용, use_container_width=True)


        else:
            pass

    with st.expander("🔍공연손익"):    
        
        choice2 = st.radio(
                "Table or Monthly Table",
                ["공연Table","공연Monthly Table","공연매출차트", "공연비용차트"],
                # key="{진행기간}th day Graph",
            )
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        

        if choice2 == "공연Table":  
            df_손익_공연2_누계 = templit("누계손익", df_all, df_tem , cost_SORT1, cost_SORT2, cond_공연)
            st.dataframe(df_손익_공연2_누계, use_container_width=True)

        if choice2 == "공연Monthly Table":  
            df_손익_공연_월별 = templit("월별손익", df_all, df_tem , cost_SORT1, cost_SORT2, cond_공연)
            st.dataframe(df_손익_공연_월별, use_container_width=True)

        if choice2 == "공연매출차트":  
            st.text("매출차트")
            # st.dataframe(df_tem_ch)
            st.text("ttt")
            c_공연매출_ch = chart("공연매출", df_tem_ch, sort_sale222, "공연", "매출")
            # st.altair_chart(chart_매출, use_container_width=True)
            st.altair_chart(c_공연매출_ch, use_container_width=True)


        if choice2 == "공연비용차트":  
            st.text("비용차트")
            c_공연비용_ch = chart("공연비용", df_tem_ch, cost_SORT, "공연", "비용")
            st.altair_chart(c_공연비용_ch, use_container_width=True)


        else:
            pass

        ##공연전시별 매출_비용 차트 추가 필요
        ##매출/비용별 월별 추이?

    with st.expander("🔍전시손익"):    

        choice3 = st.radio(
                "Table or Monthly Table",
                ["전시Table","전시Monthly Table","전시매출차트","전시비용차트"]
                # key="{진행기간}th day Graph",
            )
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        

        if choice3 == "전시Table":  
            df_손익_전시_누계 = templit("누계손익", df_all, df_tem , cost_SORT1, cost_SORT2, cond_전시)
            st.dataframe(df_손익_전시_누계, use_container_width=True)

        if choice3 == "전시Monthly Table":  
            df_손익_전시_월별 = templit("월별손익", df_all, df_tem , cost_SORT1, cost_SORT2, cond_전시)
            st.dataframe(df_손익_전시_월별, use_container_width=True)
        
        if choice3 == "전시매출차트":  
            st.text("매출차트")
            # st.dataframe(df_tem_ch)
            # st.text("ttt")
            c_전시매출_ch = chart("전시매출", df_tem_ch, sort_sale222, "전시", "매출")
            # st.altair_chart(chart_매출, use_container_width=True)
            st.altair_chart(c_전시매출_ch, use_container_width=True)


        if choice3 == "전시비용차트":  
            st.text("비용차트")
            c_전시비용_ch = chart("전시비용", df_tem_ch, cost_SORT, "전시", "비용")
            st.altair_chart(c_전시비용_ch, use_container_width=True)


        # if choice2 == "전시비용차트":  
        #     st.text("비용차트")
        #     chart_비용 = chart("전시비용", df_tem_ch, cost_SORT, "공연")
        #     st.altair_chart(chart_비용, use_container_width=True)
        # else:
            # pass

        ##공연전시별 매출_비용 차트 추가 필요
        ##매출/비용별 월별 추이?











    # st.sidebar.title("logout")
    # # Pass the list of passwords directly to the 
    # # Hasher constructor and generate the hashes
    # passwords_to_hash = ['fashion@123', 'increff@fashion']

    # print(hashed_passwords)




    # User auth.
    # names = ["abc"]
    # username = ["def"]
    # Load hashed passwords
    # passwords = ['abc123']


    # file_path = "C:/Users/USER/anaconda3/project/visitor3/hashed_pwd.pkl"
    # hashed_passwords = stauth.Hasher(['abc', 'def']).generate()

    # hashed_passwords = stauth.Hasher(passwords).generate()
    # hashed_passwords = stauth.hasher(['abc','a1234']).generate()
    # print(hashed_passwords)



    # file_path = "C:/Users/USER/anaconda3/project/visitor3/hashed_pwd.pkl"
    # with file_path.open("wb") as file:
    #     pickle.dump(hashed_passwords, file)


    # with file_path.open("rb") as file:
    #     hashed_passwords = pickle.load(file)

    # authenticator = stauth.Authenticate(names, username, hashed_passwords, "dashboard", "prototype", cookie_expiry_days=30)

    # name, authentication_status, username = authenticator.login("Login", "main")





    # file_path = Path(__file__).parent / "hashed_pw.pkl"

    # with file_path.open("wb") as file:
    #     pickle.dump(hashed_passwords, file)

    # https://discuss.streamlit.io/t/new-component-streamlit-authenticator-a-secure-authenticaton-module-to-validate-user-credentials-in-a-streamlit-application/18893




    # __login__obj = __login__(auth_token = "courier_auth_token", 
    #                     company_name = "Shims",
    #                     width = 200, height = 250, 
    #                     logout_button_name = 'Logout', hide_menu_bool = False, 
    #                     hide_footer_bool = False, 
    #                     lottie_url = 'https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json')

    # LOGGED_IN = __login__obj.build_login_ui()

    # if LOGGED_IN:

    #     st.markown("Your Streamlit Application Begins here!")