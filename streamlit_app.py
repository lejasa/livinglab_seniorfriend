# python -m streamlit run C:\Users\USER\Documents\GitHub\optimizer\streamlit_app.py
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
st.set_page_config(layout='wide')

# 타이틀
st.title('시니어 프렌드')
# 헤더
st.header('고령자 복지 및 생활 정보 서비스')



# 데이터 받아오기
dolbom = pd.read_csv("./data/지역별노인돌봄서비스기관.csv")
chimae = pd.read_csv("./data/지역별치매센터.csv")
job = pd.read_csv("./data/지역별일자리.csv")
health = pd.read_csv("./data/지역별건강증진센터.csv")
protect = pd.read_csv("./data/지역별노인보호기관.csv")
digital = pd.read_csv("./data/지역별디지털배움터.csv")
welfare = pd.read_csv("./data/지역별노인복지시설.csv")
leisure = pd.read_csv("./data/지역별여가및문화생활.csv")

# 홈
def home():
    # 데이터 처리

    # 시도 조건 처리
    sido = dolbom["시도"].unique().tolist()
    sido2 = chimae["시도"].unique().tolist()
    sido3 = job["시도"].unique().tolist()
    sido4 = health["시도"].unique().tolist()
    sido5 = protect["시도"].unique().tolist()
    sido6 = digital["시도"].unique().tolist()
    sido7 = welfare["시도"].unique().tolist()
    sido8 = leisure["시도"].unique().tolist()

    
    sido = list(set.union(set(sido), set(sido2), set(sido3), set(sido4), set(sido5), set(sido6), set(sido7), set(sido8)))
    region = st.sidebar.selectbox("지역을 선택하세요: ", sido )
    dolbom_cond = dolbom["시도"] == region
    chimae_cond = chimae["시도"] == region
    job_cond = job["시도"] == region
    health_cond = health["시도"] == region
    protect_cond = protect["시도"] == region
    digital_cond = digital["시도"] == region
    welfare_cond = welfare["시도"] == region
    leisure_cond = leisure["시도"] == region

    # 시군구 조건 처리
    sigoongoo = dolbom[dolbom_cond]["시군구"].unique().tolist()
    sigoongoo2 = chimae[chimae_cond]["시군구"].unique().tolist()
    sigoongoo3 = job[job_cond]["시군구"].unique().tolist()
    sigoongoo4 = health[health_cond]["시군구"].unique().tolist()
    sigoongoo5 = protect[protect_cond]["시군구"].unique().tolist()
    sigoongoo6 = digital[digital_cond]["시군구"].unique().tolist()
    sigoongoo7 = welfare[welfare_cond]["시군구"].unique().tolist()


    sigoongoo = list(set.union(set(sigoongoo), set(sigoongoo2), set(sigoongoo3), set(sigoongoo4), set(sigoongoo5), set(sigoongoo6), set(sigoongoo7)))
    region_detail = st.sidebar.selectbox("세부지역을 선택하세요: ", sigoongoo )

    dolbom_cond2 = dolbom["시군구"] == region_detail
    chimae_cond2 = chimae["시군구"] == region_detail
    job_cond2 = job["시군구"] == region_detail
    health_cond2 = health["시군구"] == region_detail
    protect_cond2 = protect["시군구"] == region_detail
    digital_cond2 = digital["시군구"] == region_detail
    welfare_cond2 = welfare["시군구"] == region_detail

    dolbom_cond3 = dolbom_cond&dolbom_cond2
    chimae_cond3 = chimae_cond&chimae_cond2
    job_cond3 = job_cond&job_cond2
    health_cond3 = health_cond&health_cond2
    protect_cond3 = protect_cond&protect_cond2
    digital_cond3 = digital_cond&digital_cond2
    welfare_cond3 = welfare_cond&welfare_cond2

    if st.sidebar.button("실행"):
        dolbom[dolbom_cond3].to_csv("./tempor/dolbom.csv")
        chimae[chimae_cond3].to_csv("./tempor/chimae.csv")
        job[job_cond3].to_csv("./tempor/job.csv")
        health[health_cond3].to_csv("./tempor/health.csv")
        protect[protect_cond3].to_csv("./tempor/protect.csv")
        digital[digital_cond3].to_csv("./tempor/digital.csv")
        welfare[welfare_cond3].to_csv("./tempor/welfare.csv")
        leisure[leisure_cond].to_csv("./tempor/leisure.csv")

# 위치정보 상세 (단, data에 위도 경도 컬럼이 있어야 함)
def location_detail(data):
    ICON_URL = "https://cdn-icons-png.flaticon.com/512/1141/1141117.png"
    icon_data = {
    # Icon from Wikimedia, used the Creative Commons Attribution-Share Alike 3.0
    # Unported, 2.5 Generic, 2.0 Generic and 1.0 Generic licenses
    "url": ICON_URL,
    "width": 242,
    "height": 242,
    "anchorY": 242,
}
    data["icon_data"] = None
    for i in data.index:
        data["icon_data"][i] = icon_data
    la, lo = np.mean(data["위도"]),np.mean(data["경도"])
    st.pydeck_chart(pdk.Deck(map_style=None, initial_view_state=pdk.ViewState(longitude=lo, latitude=la, zoom=11, pitch=50), 
    layers= [pdk.Layer(type="IconLayer",data= data,get_icon="icon_data", get_size=4, size_scale=15 ,get_position='[경도, 위도]', pickable=True)] ), use_container_width=True)

# 복지정보
def info():
    df = pd.read_csv("./data/복지정보.csv")
    st.dataframe(df)


# 노인맞춤돌봄서비스 수행기관현황
def dolbom_ft():
    st.markdown("#### 노인 맞춤 돌봄서비스 수행기관")
    df = pd.read_csv("./tempor/dolbom.csv", index_col=0)
    st.dataframe(df)
    if len(df) != 0:
        location_detail(df)


# 전국치매센터 현황
def chimae_ft():
    st.markdown("#### 치매센터 정보")
    df = pd.read_csv("./tempor/chimae.csv", index_col=0)
    st.dataframe(df)
    if len(df) != 0:
        location_detail(df)


# 노인일자리 현황
def job_ft():
    st.markdown("#### 일자리 정보")
    df = pd.read_csv("./tempor/job.csv", index_col=0)
    st.dataframe(df)
    

# 건강증진센터 현황
def health_ft():
    st.markdown('#### 건강 증진센터 정보')
    df = pd.read_csv("./tempor/health.csv", index_col=0)
    li = df["건강증진센터구분"].unique().tolist()
    box = st.selectbox('구분 선택: ', li)
    cond = df["건강증진센터구분"] == box
    st.dataframe(df[cond])
    if len(df[cond]) != 0:
        location_detail(df[cond])


# 노인보호기관 현황
def protect_ft():
    st.markdown('#### 보호기관 정보')
    df = pd.read_csv("./tempor/protect.csv", index_col=0)
    st.dataframe(df)
    if len(df) != 0:
        location_detail(df)


# 노인복지시설 현황
def welfare_ft():
    st.markdown('#### 복지시설 정보')
    df = pd.read_csv("./tempor/welfare.csv", index_col=0)
    st.dataframe(df)

# 여가 및 문화생활
def leisure_ft():
    st.markdown('#### 여가 및 문화생활 정보')
    df = pd.read_csv("./tempor/leisure.csv", index_col=0)
    li = df["구분"].unique().tolist()
    box = st.selectbox('장르 선택: ', li)
    cond = df["구분"] == box
    st.dataframe(df[cond])

# 디지털 배움터 현황
def digital_ft():
    st.markdown('#### 디지털 배움터 정보')
    df = pd.read_csv("./tempor/digital.csv", index_col=0)
    st.dataframe(df)
    if len(df) != 0:
        location_detail(df)


# 메인 화면

home()
page = st.sidebar.selectbox('페이지 선택: ', ['복지 정보','노인 맞춤 돌봄서비스', '전국 치매센터', '일자리', '건강 증진센터', '보호기관', '복지시설', '디지털 배움터', '여가 및 문화생활'])
if page == '복지 정보':
    info()
elif page == '노인 맞춤 돌봄서비스':
    dolbom_ft()
elif page == '전국 치매센터':
    chimae_ft()
elif page == '일자리':
    job_ft()
elif page == '건강 증진센터':
    health_ft()
elif page == '보호기관':
    protect_ft()
elif page == '복지시설':
    welfare_ft()
elif page == '디지털 배움터':
    digital_ft()
elif page == '여가 및 문화생활':
    leisure_ft()








