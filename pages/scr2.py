import requests
from bs4 import BeautifulSoup
import streamlit as st
import pandas as pd
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
from pathlib import Path
from datetime import datetime

st.set_page_config(
    page_title = "News Crawling",
    page_icon = "Active",        
    layout="wide"
    )
hide_streamlit_markers=False


st.markdown("<h1 style='text-align: center; color: white;'>Recent Press Summary</h1>", unsafe_allow_html=True)

titles = []
rinks = []
times = []
presses = []

df_news_b = pd.DataFrame()
df_news_0 = pd.DataFrame()
df_news_1 = pd.DataFrame()
df_news_2 = pd.DataFrame()
df_news_3 = pd.DataFrame()
df_news_4 = pd.DataFrame()
df_news_5 = pd.DataFrame()

# search_word = '롯데뮤지엄'

search_word = st.text_input("키워드 입력","롯데뮤지엄")

# url = f'https://m.search.naver.com/search.naver?where=m_news&sm=mtb_nmr&query={search_word}&sort=0&nso=so:r,p:all'
# for x in range(0,10):
for x in range(0,2):
    # url =  f'https://m.search.naver.com/search.naver?where=m_news&query={search_word}&sm=mtb_opt&sort=1&photo=0&field=0&pd=0&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Add%2Cp%3Aall&is_sug_officeid=0&office_category=0&service_area=0&start=15x{x}+1'
    # url =  f'https://m.search.naver.com/search.naver?where=m_news&sm=mtb_pge&query={search_word}&sort=1&photo=0&field=0&pd=0&ds=&de=&cluster_rank=97&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all&start=15x{x}+1'
    # url =  f'https://m.search.naver.com/search.naver?where=m_news&sm=mtb_pge&query={search_word}&sort=1&photo=0&field=0&pd=0&ds=&de=&cluster_rank=97&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all&start=15{x+1}'
    # url = f'https://m.search.naver.com/search.naver?where=m_news&query={search_word}&sm=mtb_opt&sort=1&photo=0&field=0&pd=0&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Add%2Cp%3Aall&is_sug_officeid=0&office_category=0&service_area=0' #&start=15x{x}+1
    # url = f'https://m.search.naver.com/search.naver?where=m_news&query={search_word}&sm=mtb_opt&sort=1&photo=0&field=0&pd=0&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all&start=15{x}+1&%3Add%2Cp%3Aall&is_sug_officeid=0&office_category=0&service_area=0' #&start=15{x}+1
    # url = f'https://m.search.naver.com/search.naver?where=m_news&query={search_word}&sm=mtb_opt&sort=1&photo=0&field=0&pd=0&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all&start=15x{x}+1' #&start=15{x}+1
    url = f'https://m.search.naver.com/search.naver?where=m_news&query={search_word}&sm=mtb_opt&sort=1&photo=0&field=0&pd=0&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all&start={15*x+1}&service_area=0&sort=1'
## url =  f'https://m.search.naver.com/search.naver?where=m_news&sm=mtb_pge&query={search_word}&sort=1&photo=0&field=0&pd=0&ds=&de=&cluster_rank=97&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all&start=15'
# url = 'https://m.search.naver.com/search.naver?sm=mtb_hty.top&where=m_news&ssc=tab.m_news.all&oquery=&query=%EB%A1%AF%EB%8D%B0%EB%AE%A4%EC%A7%80%EC%97%84&nso=so%3Add%2Cp%3Aall&mynews=0&office_category=0&office_section_code=0&office_type=0&pd=0&photo=0&service_area=0&sort=1'
# https://m.search.naver.com/search.naver?where=m_news&sm=mtb_pge&query=롯데뮤지엄&sort=1&photo=0&field=0&pd=0&ds=&de=&cluster_rank=97&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all&start=1
# https://m.search.naver.com/search.naver?where=m_news&sm=mtb_pge&query=삼성전자&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=97&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all&start={15x+1의 정수 기입(시작 페이지)}
# url = f'https://m.search.naver.com/search.naver?sm=mtp_hty.top&where=m&query={search_word}'
    try: 
        req = requests.get(url)
        html = req.text
        # st.text(html)
        soup = BeautifulSoup(html,'html.parser')
        search_result = soup.select_one('#news_result_list')
        news_links1 = search_result.select('.bx > .news_wrap > a')
        # presses = search_result.select('.bx > .news_wrap > .news_info > .info_group > a > .thumb_box')
        presses1 = search_result.select('.bx > .news_wrap > .news_info > .info_group > a')
        # times1 = search_result.select('.bx > .news_wrap > .news_info > .info_group > .info')
        times1 = search_result.select('.bx > .news_wrap > .news_info > .info_group > .info')
        # times2 = soup.find_all('span',class_='info')
        times2 = search_result.find_all('span',class_='info')


        # st.text(f'times2:{len(times2)}')
        # st.text(f'times2:{times2}')
        # st.text(f'times1:{len(times1)}')

        for time11 in times2:
            s = time11.get_text()
            if s != "네이버뉴스":
                # st.text(s)
                times.append(s)
                

        # st.text(f'times1:{times1}')
        # /html/body/div[2]/div[1]/section/div[1]/div/ul/li[1]/div/div[1]/div[2]/span[2]
        # times2 = soup.find_all(".info")
        # # times1 = soup.find_all("info")
        # st.text(f'times2:{times2}')
        # /html/body/div[2]/div[1]/section/div[1]/div/ul/li[1]/div/div[1]/div[2]/a/text()
        # /html/body/div[2]/div[1]/section/div[1]/div/ul/li[1]/div/div[1]/div[2]/a/text()
        # st.text(search_result)

        # times : 시간 추가 방법 확인 필요

        for title in news_links1:
            titles.append(title.get_text())
        # st.text(titles)

        for rink in news_links1:
            rinks.append(rink.get("href"))

        # st.text(len(times1))
        # for time in times1:
        #     times.append(time.get_text())
        # st.text(f'times1:{times1}')

        # st.text(f'time: {times}')

        # st.text(f'언론사수{len(presses1)}')
        for press in presses1:
            try:
                press = press.get_text()
                ss = press.split("</span>")
                # st.text(ss)
                presses.append(ss)
            except:
                pass


        # for rink in news_links1:
        #     rinks.append(rink.get("href"))
        # # https://charimlab.tistory.com/entry/ep01-%EC%9B%B9%ED%81%AC%EB%A1%A4%EB%A7%81-6-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%8A%AC%EB%9D%BC%EC%9D%B4%EC%8B%B1%EA%B3%BC-for%EB%AC%B8%EC%9C%BC%EB%A1%9C-%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%A5%BC-%EC%A0%95%EC%A0%9C%ED%95%98%EB%8B%A4-with-%ED%8C%8C%EC%9D%B4%EC%8D%AC
        # # times1 = times1[::2]
        # st.text(f'시간수{len(times1)}')
        # for time in times1:
        #     # try:
        #     # if times1.index(time) % 2 == 1:
        #     time = time.get_text()
        #     ts = time
        #     st.text(ts)
        #     ts = time.split("before")
        #     times.append(ts)
            # st.text(times)
            # except:
            #     pass
            # presses.append(ss)
        # st.text(presses)


        # for press in presses:
        #     presses.append(press.getText)
        #     st.text(press)

        # for press in presses:
        #     presses.append(press.string)
        #     st.text(presses)


        # for news_time in news_times:
        #     times.append(news_time.get_text())
        #     # st.text(times)


    # st.text(f'언론사수: {len(presses)}')
    # st.text(f'링크수: {len(rinks)}')
    # st.text(f'기사수 : {len(titles)}')
    # st.text(f'시간수 : {len(times)}')

    except:
        pass

# df_news = pd.DataFrame({'시간':times,'언론사':presses, 'text':titles, 'rinks': rinks})
    if x == 0:
        # df_news = f'df_news_{x}'
        df_news_b = pd.DataFrame({'언론사':presses, '시간':times, 'text':titles, 'rinks': rinks})
        # df_news = df_news.sort_values(by='시간', axis=0, ascending=True)
        # # df_news = df_news.drop_duplicates(subset='text')
        # df_news = st.data_editor(
        #     df_news,
        #     column_config={
        #         "rinks": st.column_config.LinkColumn(
        #             "App Creator", display_text= "기사보기"
        #         ),
        #     },
        #     hide_index=True,use_container_width=True
        # )
        # st.dataframe(df_news_b)
    else:
        df_news = f'df_news_{x}'
        df_news = pd.DataFrame({'언론사':presses, '시간':times, 'text':titles, 'rinks': rinks})
        # df_news_b = df_news_b.append(df_news)
        df_news_b = pd.concat([df_news_b, df_news], ignore_index=True)
        # df_news = df_news.sort_values(by='시간', axis=0, ascending=True)
        # df_news = df_news.drop_duplicates(subset='text')
        # df_news = st.data_editor(
        #     df_news,
        #     column_config={
        #         "rinks": st.column_config.LinkColumn(
        #             "App Creator", display_text= "기사보기"
        #         ),
        #     },
        #     hide_index=True,use_container_width=True
        # )

now = datetime.now()
st.text(f'최근 {len(df_news_b)}개 기사  [ {now}기준 ]')
# st.text(f'최근 {len(df_news_b)}개 기사')
# st.text(f'최근 {len(df_news_b)}개 기사')

# df_news_b = st.data_editor(
#     df_news_b,
#     column_config={
#         "rinks": st.column_config.LinkColumn(
#             "App Creator", display_text= "기사보기"
#         ),
#     },
#     hide_index=True,use_container_width=True
# )




# text_w = []
# for i in(0,45):
#     text_w = text_w.add(df_news_b['text'].iloc[i])

text_w = df_news_b['text'].values.tolist()
# st.text(text_w)
# [x.encode('utf-8') for x in text_w]
# wc = WordCloud().fit_words(text_w)
# text_w = str(text_w)
# for item in text_w:
#     unique_string = [n.encode('utf-8') for n in text_w]
#     unique_string=(" ").join(unique_string)




# st.text(text_w)
# DATA_IN_PATH = os.path.realpath(__file__)
# DATA_IN_PATH = './parent_folder'
file_path = Path(__file__).parent / 'NanumSquareOTF_acEB.otf'
# st.text(file_path)
# wordcloud = WordCloud(width = 1000, height = 500).generate(unique_string)
wordcloud = WordCloud(font_path=os.path.join(file_path)).generate(" ".join(text_w))
# https://velog.io/@leejong/AI-WordCloud-%ED%95%9C%EA%B8%80-%ED%8F%B0%ED%8A%B8-%EB%AC%B8%EC%A0%9C-%ED%95%B4%EA%B2%B0
# plt.figure(figsize=(10,6))
plt.imshow(wordcloud)
plt.axis("off")
# plt.savefig("your_file_name"+".png", bbox_inches='tight')
plt.show()
# plt.close()
st.pyplot(plt)



st.text(f'최근 {len(df_news_b)}개 기사')

df_news_b = st.data_editor(
    df_news_b,
    column_config={
        "rinks": st.column_config.LinkColumn(
            "App Creator", display_text= "기사보기"
        ),
    },
    hide_index=True,use_container_width=True
)


# wordcloud = WordCloud(width=1000, height=500, regexp=r"\w[\w' ]+").generate("+".join(text_w))

# st.image(wordcloud.to_array())

# fig, ax = plt.subplots()
# text.lineplot(x='x', y='y', data=text, ax=ax)
# st.pyplot(fig)

# st.pyplot()


    # st.dataframe(df_news,use_container_width=True)
    # st.dataframe(df_news, hide_index= True, use_container_width=True)
    # https://docs.streamlit.io/develop/api-reference/data/st.column_config/st.column_config.linkcolumn




# # https://stackoverflow.com/questions/42263946/how-to-create-a-table-with-clickable-hyperlink-in-pandas-jupyter-notebook
# # https://www.geeksforgeeks.org/how-to-create-a-table-with-clickable-hyperlink-to-a-local-file-in-pandas/
# # st.text(titles)
# st.text(len(titles))



# df_news['text'] = df_news['text'].apply(lambda x: f'<a href="http://softhints.com/tutorial/{x}">{x}</a>')
# df = df_news.to_html(escape=False)
# st.dataframe(df)

# # df = pd.DataFrame(['https://google.com', 'https://duckduckgo.com'])

# # def make_clickable(val):
# #     return '<a href="{}">{}</a>'.format(val,val)

# # df = df.style.format(make_clickable)
# # st.dataframe(df)

# # def make_clickable(url, name):
# #     return '<a href="{}" rel="noopener noreferrer" target="_blank">{}</a>'.format(url,name)

# # df_news['rink'] = df_news.apply(lambda x: make_clickable(x['text'], x['rinks']), axis=1)

# # def make_clickable(val):
# #     return f'<a target="_blank" href="{val}">{val}</a>'

# # df = df_news.style.format({'url': make_clickable})

# # def make_clickable(val):
# #     return f'<a href="{val}">{val}</a>'
# # # https://github.com/softhints/Pandas-Tutorials/blob/master/styling/create-clickable-link-pandas-dataframe-jupyterlab.ipynb

# # # df = df_news.style
# # st.dataframe(df)

# # https://github.com/softhints/Pandas-Tutorials/blob/master/styling/create-clickable-link-pandas-dataframe-jupyterlab.ipynb