# import streamlit as st
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt

# st.subheader("cloudword")
# # st.set_option('deprecation.showPyplotGlobalUse', False)
# # st.set_option('deprecation.showPyplotGlobalUse', False)
# # st.set_option('deprecation.showPyplotGlobalUse', False)

# text = "가 나다 마 바사 가 아자 가나다 마바사"

# if text:
#     w = WordCloud().generate()
#     # w = WordCloud().generate_from_frequencies(text)
#     w = ordcloud.fit_words(word_frequence)

#     plt.imshow(w)
#     st.pyplot()


import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# fig_roc = RocCurveDisplay.from_estimator(model, x_test, y_test)
# st.pyplot(fig_roc.figure_)
# fig, ax = plt.figure(figsize=(15,5))
# st.set_option('deprecation.showPyplotGlobalUse', False)
# Create some sample text
text = 'Fun, fun, awesome, awesome, tubular, astounding, superb, great, amazing, amazing, amazing, amazing'

# Create and generate a word cloud image:
wordcloud = WordCloud().generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

wc = WordCloud().fit_words({"A": 2, "B": 2, "C": 3})

st.image(wc.to_array())

# fig, ax = plt.subplots()
# text.lineplot(x='x', y='y', data=text, ax=ax)
# st.pyplot(fig)

st.pyplot()