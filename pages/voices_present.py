from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote
import pandas as pd
import streamlit as st

def get_posts(query):
    texts_l = []
    
    url_query = quote(query)
    url = 'https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query=' + url_query
    

    search_url = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(search_url, 'html.parser')
    blog_tt = soup.find('ul',{'class':'lst_view _fe_view_infinite_scroll_append_target'})
    bloggers = blog_tt.find_all('li',{'class':'bx'})
    for n in bloggers:
        bloger = n.find('div',{'class':'view_wrap'}).find('div',{'class':'user_box_inner'}).get_text()
        texts_l.append(bloger)
    
    df_test = pd.DataFrame(data=texts_l, columns=['text'], index=None)
    st.dataframe(df_test, hide_index=True, use_container_width=True)



get_posts('이수안컴퓨터연구소')

