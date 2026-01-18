from dotenv import load_dotenv
# from langchain.llms import OpenAI
from langchain_openai import OpenAI
import streamlit as st

#llm  = OpenAI(openai_api_key= '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')
# dotenv를 안쓸 때, 이렇게 해도 됨.

load_dotenv()

# llm=OpenAI()
# result= llm.predict('hi!')
# print(result)



from langchain_openai import ChatOpenAI

chat_model = ChatOpenAI()

content = st.text_input('시의 주제를 제시해주세요.')


if st.button('시작성 요청하기'):
    with st.spinner('waiting...'):
        result2=chat_model.predict(content+'에 대한 시를 써줘.')
        st.write(result2)








# st.title('인공지능 시인')
# title = st.text_input('시의 주제를 제시해주세요')
# st.write('시의주제는 ', title)