##### 기본 정보 불러오기 #####
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
from matplotlib import font_manager

@st.cache_resource
def load_font(font_path):
    return font_manager.FontProperties(fname=font_path)

##### 기능 구현 함수 불러오기 #####
def button_click(state):
    st.session_state.state = state

def cos_sim_index(index_num,cosine_sim,filtered_df):
    selected_similarities = cosine_sim[int(index_num)]
    similarities_with_index = [(similarity, index) for index, similarity in enumerate(selected_similarities) if index != int(index_num)]
    similarities_with_index.append((1.0, int(index_num)))  # Add similarity of 1.0 for the selected index
    sorted_similarities = sorted(similarities_with_index, key=lambda x: x[0], reverse=True)
    top_6_similar_jobs = [filtered_df.iloc[index].tolist() for similarity, index in sorted_similarities[:6]]

    df = pd.DataFrame(data = top_6_similar_jobs,columns=['Unnamed: 0', '사이트', '검색 키워드', '기업이름', '포지션이름', '포지션이름 전처리', '포지션 세부 ', '마감일', '상시 채용 여부', '경력_min', '경력_max', '학력', '학력 세부정보', '스킬', '제출서류', '채용절차', '채용형태', '채용형태_전처리', '채용형태_전처리 세부', '급여', '근무시간', '근무장소', '근무장소 시', '근무장소 구', '경기도 구 ', '근무형태', '주요업무', '인재상', '자격요건', 'Hard Skill', 'Soft Skill', 'Tool', '우대사항', 'hard plus', 'soft plus', 'tool plus', '복지', '기업소개', '표준산업분류', '주요사업', '주요사업.1', '산업군', '산업군 전처리', '설립', '사원 수', '기업 평균 연봉', '기업유형', '기업 유형 전처리', '기업 유형 전처리 _세부', '매출액', '접수방법', '총점', '복지 및 급여', '업무와 삶의 균형', '사내문화', '승진 기회', '경영진', '기업추천율', 'CEO 지지율', '성장 가능성', '하이라이트+태그', '퇴사', '입사', '링크', 'DA', '통계', 'ML', 'DL', '시각화', '데이터 가공', '빅데이터', '클라우드', '파이프라인', '그로스해킹', '로그', '마케팅', '도메인', '프로그래밍언어', '의사소통', '논리적/분석적 사고', '문제해결능력', '프로세스', '리더십', '책임감', '적극적', '의지/열정', '창의력', '비즈니스', '액션도출', 'Agile', '영어', '관심/경험', 'Tool1', 'SQL', 'Python', 'R', '시각화 툴', '로그분석', 'BigData', 'Cloud', 'database', '개발', 'MLtool', 'DLtool', 'DA plus', '통계 plus', 'ML plus', 'DL plus', '시각화 plus', '데이터 가공 plus', '빅데이터 plus', '파이프라인 plus', '그로스해킹 plus', '로그 plus', '마케팅 plus', '의사소통 plus', '리더십 plus', '문제해결능력 plus', 'Agile plus', '학력 plus', '창의력 plus', '적극적 plus', '논리적/분석적 사고 plus', '관심/경험 plus', '영어 plus', '전공', '공모전', '프로젝트 경험', '논문', 'tool plus1', 'SQL plus', 'Python plus', 'R plus', '시각화 툴 plus', '로그분석 plus', 'BigData plus', 'Cloud plus', 'database plus', '개발 plus', 'MLTool plus', 'DLTool plus']
    )

    df=df[['기업이름', '포지션이름', '마감일', 
            '상시 채용 여부', '경력_min', '경력_max',]]
    return df

def cos_sim_index_plus(index_num,cosine_sim,filtered_df_plus):
    selected_similarities = cosine_sim[int(index_num)]
    similarities_with_index = [(similarity, index) for index, similarity in enumerate(selected_similarities) if index != int(index_num)]
    similarities_with_index.append((1.0, int(index_num)))  # Add similarity of 1.0 for the selected index
    sorted_similarities = sorted(similarities_with_index, key=lambda x: x[0], reverse=True)
    top_6_similar_jobs = [filtered_df_plus.iloc[index].tolist() for similarity, index in sorted_similarities[:6]]

    df_plus = pd.DataFrame(data = top_6_similar_jobs,columns=['Unnamed: 0','Unnamed: 0', '사이트', '검색 키워드', '기업이름', '포지션이름', '포지션이름 전처리', '포지션 세부 ', '마감일', '상시 채용 여부', '경력_min', '경력_max', '학력', '학력 세부정보', '스킬', '제출서류', '채용절차', '채용형태', '채용형태_전처리', '채용형태_전처리 세부', '급여', '근무시간', '근무장소', '근무장소 시', '근무장소 구', '경기도 구 ', '근무형태', '주요업무', '인재상', '자격요건', 'Hard Skill', 'Soft Skill', 'Tool', '우대사항', 'hard plus', 'soft plus', 'tool plus', '복지', '기업소개', '표준산업분류', '주요사업', '주요사업.1', '산업군', '산업군 전처리', '설립', '사원 수', '기업 평균 연봉', '기업유형', '기업 유형 전처리', '기업 유형 전처리 _세부', '매출액', '접수방법', '총점', '복지 및 급여', '업무와 삶의 균형', '사내문화', '승진 기회', '경영진', '기업추천율', 'CEO 지지율', '성장 가능성', '하이라이트+태그', '퇴사', '입사', '링크', 'DA', '통계', 'ML', 'DL', '시각화', '데이터 가공', '빅데이터', '클라우드', '파이프라인', '그로스해킹', '로그', '마케팅', '도메인', '프로그래밍언어', '의사소통', '논리적/분석적 사고', '문제해결능력', '프로세스', '리더십', '책임감', '적극적', '의지/열정', '창의력', '비즈니스', '액션도출', 'Agile', '영어', '관심/경험', 'Tool1', 'SQL', 'Python', 'R', '시각화 툴', '로그분석', 'BigData', 'Cloud', 'database', '개발', 'MLtool', 'DLtool', 'DA', '통계', 'ML', 'DL', '시각화', '데이터 가공', '빅데이터', '파이프라인', '그로스해킹', '로그', '마케팅', '의사소통 plus', '리더십 plus', '문제해결능력 plus', 'Agile plus', '학력 plus', '창의력 plus', '적극적 plus', '논리적/분석적 사고 plus', '관심/경험 plus', '영어 plus', '전공', '공모전', '프로젝트 경험', '논문', 'tool plus1', 'SQL plus', 'Python plus', 'R plus', '시각화 툴 plus', '로그분석 plus', 'BigData plus', 'Cloud plus', 'database plus', '개발 plus', 'MLTool plus', 'DLTool plus'])

    df_plus=df_plus[['기업이름', '포지션이름', '마감일', 
        '상시 채용 여부', '경력_min', '경력_max', ]]
    return df_plus

##### 메인 함수 #####
def main():

    st.set_page_config(page_title='채용공고추천',layout='wide')
    font_prop = load_font("NanumGothic.ttf")
    # Session state 초기화
    if 'state' not in st.session_state:
        st.session_state.state = None
    if 'base_df' not in st.session_state:
        st.session_state.base_df  = None
    if 'woodae_df' not in st.session_state:
        st.session_state.woodae_df  = None

    # 데이터셋 불러오기
    df = pd.read_csv('전처리통합최종.csv')
    df_plus=pd.read_csv('hs_plus.csv')
    df_tool=pd.read_csv('tool1.csv')
    df_remote=pd.read_csv('remote.csv')

    # 프로그램 타이틀
    st.header('개인형 맞춤 채용 공고 추천')
    
    # 텝 생성하기
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["공고 추천", "SOFT SKILL","도메인","TOOL","채용 트렌드"])
    
    # 추천시스템
    with tab1:   
        col1, col2 = st.columns(2)

        # 사용자 입력 받기
        with col1:
            st.subheader('HARD SKILL을 선택하세요')
            with st.expander("See explanation"):
                st.write('''
        DA : 데이터 분석 자체에 대한 경험

        통계 : 통계 분석, 통계적 지식, 회귀 분석, 정량적 분석 등

        머신러닝 : 머신러닝, 모델링, 분류/예측 모델링, 시계열 데이터 활용

        딥러닝 : 딥러닝, 알고리즘, 프레임워크, 검색 알고리즘, 추천 알고리즘, 자연어 처리, 차원 모델링

        시각화 : 데이터 시각화, BI Tool 활용, 대시보드 구축

        데이터 가공 : 데이터 수집, 데이터 추출, 데이터 처리

        빅데이터 : 빅데이터 분석, 빅데이터 처리, 대용량 데이터 분산처리 경험

        클라우드 : 클라우드 서비스 플랫폼 (AWS, GA4, Google Cloud Platform 등)

        파이프라인 : 데이터마트, 데이터 웨어하우스, 데이터 레이크 구축 및 데이터 파이프라인 설계 경험

        그로스 해킹 : Funnel 분석, Cohort 분석, AARRR, Retention, A/B테스트 등 마케팅 및 비즈니스 분석에 필요한 분석 기법 활용 경험

        로그 : App/Web 유저 데이터, 사용자 행동 데이터, 로그 데이터

        마케팅 : 마케팅 경험, 프로덕트 분석, 비즈니스 분석.''')
    
            hardskill=st.multiselect(
                'select hard skill',
                ['DA', '통계', 'ML', 'DL', '시각화', '데이터 가공',
                    '빅데이터', '클라우드', '파이프라인', '그로스해킹', '로그', '마케팅']
                )
            # st.write('You selected:', hardskill)
        with col2:
            st.subheader('경력을 선택하세요')
            with st.expander("See explanation"):
                st.write('''만 경력을 기준으로 선택해 주세요.''')
            option = st.selectbox(
                "경력 기간",
                ("1", "2", "3","4","5","6","7"),
                index=None
            )
            # st.write('You selected:', option)

        # To do
        # 버튼 크기 키우고 가운데로!
        col1, col2,col3 = st.columns([2.5, 1, 2])
        with col2:
            st.markdown(
                """
            <style>
            button {
                height: 60px;       
            }
            </style>
            """,
                unsafe_allow_html=True,
            )

            st.button("\n 추천 받기 \n",on_click=button_click,args=("추천시작",))
    
        st.markdown("---")

        if st.session_state.state=="추천시작":
            col1, col2= st.columns(2)
            with col1:
                # 1.기본 추천 

                # 1.1 하드스킬 필터링
                filtered_df = df[(df[hardskill] == 1).all(axis=1) & (df['경력_min'] < int(option))]
                first_row = filtered_df.iloc[0]
                index = filtered_df.index[0]
                
                #To do 0
                #1.2 경력 필터링

                # 바이너리 컬럼 필터링
                selected_columns = ['Unnamed: 0', 'DA', '통계', 'ML', 'DL', '시각화', '데이터 가공',
                '빅데이터', '클라우드', '파이프라인', '그로스해킹', '로그', '마케팅']
                new_df = filtered_df[selected_columns]

                cosine_sim = cosine_similarity(new_df)
                df_recom = cos_sim_index(index,cosine_sim,filtered_df)
                st.subheader('유사 공고 상위 6개')
                df_recom["조회기업선택"] = False  
                st.session_state.base_df = st.data_editor(
                    df_recom,
                    column_config={
                        "조회기업선택": st.column_config.CheckboxColumn(
                            "희망하는 회사는?",
                            help="Select your **favorite** widgets",
                            default=False,
                        )
                    },
                    key="base",
                    hide_index=True,)
                print(df_recom)
                print(st.session_state.base_df)
                st.button('상세 기업 정보 조회(기본)',on_click=button_click,args=("상세기업정보_기본",))
            with col2:
                # 2.우대사항 추천 

                # 우대사항
                #2.1 하드스킬 필터링
                filtered_df_plus = df_plus[(df_plus[hardskill] == 1).all(axis=1)]
                first_row_plus = filtered_df_plus.iloc[0]
                index_plus = filtered_df_plus.index[0]

                #To do
                #2.2 경력 필터링

                selected_columns = ['Unnamed: 0', 'DA', '통계', 'ML', 'DL', '시각화', '데이터 가공',
                    '빅데이터', '클라우드', '파이프라인', '그로스해킹', '로그', '마케팅']
                new_df_plus = filtered_df_plus[selected_columns]

                cosine_sim = cosine_similarity(new_df_plus)
                df_plus_recom = cos_sim_index_plus(index_plus,cosine_sim,filtered_df_plus)
                st.subheader('우대사항 6개')
                df_plus_recom["조회기업선택"] = False  
                st.session_state.woodae = st.data_editor(
                    df_plus_recom,
                    column_config={
                        "조회기업선택": st.column_config.CheckboxColumn(
                            "희망하는 회사는?",
                            help="Select your **favorite** widgets",
                            default=False,
                        )
                    },
                    hide_index=True,)
                st.button('상세 기업 정보 조회(우대)',on_click=button_click,args=("상세기업정보_우대",))
        elif st.session_state.state=="상세기업정보_기본":
            st.subheader("상세 기업 정보")
            # print(df_recom)
            # print(st.session_state.base_df)
            company_name = st.session_state.base_df.loc[st.session_state.base_df["조회기업선택"],"기업이름"].reset_index().loc[0,"기업이름"]
            position_name = st.session_state.base_df.loc[st.session_state.base_df["조회기업선택"],"포지션이름"].reset_index().loc[0,"포지션이름"]
            magam = st.session_state.base_df.loc[st.session_state.base_df["조회기업선택"],"마감일"].reset_index().loc[0,"마감일"]
            df_final = df[(df["기업이름"]==company_name) & (df["포지션이름"]==position_name)& (df["마감일"]==magam)]
            # 여기서부터 상세 정보를 꾸미세요
                        
            selected_info = df_final.iloc[0]
            company_name = selected_info['기업이름']
            scores = selected_info[['총점', '복지 및 급여', '업무와 삶의 균형', '사내문화', '승진 기회']]
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.bar(scores.index, scores.values, color='yellowgreen')
            ax.set_title(f'{company_name} 직원 만족도 지표', fontproperties=font_prop)
            ax.set_xticklabels(labels = scores.index,fontproperties=font_prop)
            
            ax.set_xlabel('')
            ax.set_ylabel('만족도', fontproperties=font_prop)
            ax.set_ylim(0, 5)  # 만족도는 0에서 5 사이의 값
            
            st.pyplot(fig)

            st.divider()

            selected_info = df_final.iloc[0]
            company_name = selected_info['기업이름']

            scores1 = selected_info[['기업추천율', 'CEO 지지율', '성장 가능성']]

            fig1, ax1 = plt.subplots(figsize=(12,6))
            bars1 = ax1.bar(scores1.index, scores1.values, color='olivedrab')

            # for bar in bars1:
            #     # height = bar.get_height()
            #     # # ax1.text(bar.get_x() + bar.get_width() / 2, height, '%d%%' % height, ha='center', va='bottom')

            ax1.set_title(f'{company_name} 기업 평가 지표', fontproperties=font_prop)
            ax1.set_xlabel('')
            ax1.set_xticklabels(labels = scores1.index,fontproperties=font_prop)
            ax1.set_ylabel('기업 평가', fontproperties=font_prop)
            ax1.set_ylim(0, 100) 

            # 그래프 출력
            st.pyplot(fig1)

            st.divider()

           #기업명

            df_name=selected_info['기업이름']
            st.subheader("기업명")
            st.write(df_name)

            st.divider()  

            # 주요업무
            df_work=selected_info['주요업무']
            st.subheader("주요 업무")
            st.write(df_work)

            st.divider()  

            # 자격요건
            df_intro=selected_info['자격요건']
            st.subheader("자격 요건")
            st.write(df_intro)

            st.divider()  

            # 자격요건
            df_pplus=selected_info['우대사항']
            st.subheader("우대 사항")
            st.write(df_pplus)

            st.divider()  

            # 매출액
            df_rev=selected_info['매출액']
            st.subheader("매출액")
            st.write(df_rev)

            st.divider()  

            # 사원수 
            df_ppl=selected_info['사원 수']
            st.header("사원 수")
            st.write(df_ppl,"명")

            st.divider()  

            # 기업평균연봉
            df_income=selected_info['기업 평균 연봉']
            st.subheader("기업 평균 연봉")
            st.write(df_income,"만원")

            st.divider()  

            # 퇴사입사자 수 
            df_out=selected_info['퇴사']
            df_in=selected_info['입사']
            st.subheader("작년 퇴사/입사자 수")
            st.write(df_out,"/",df_in)

            st.divider()  

            
        elif st.session_state.state=="상세기업정보_우대":
            st.subheader("상세 기업 정보_우대")
            company_name = st.session_state.woodae.loc[st.session_state.woodae["조회기업선택"],"기업이름"].reset_index().loc[0,"기업이름"]
            position_name = st.session_state.woodae.loc[st.session_state.woodae["조회기업선택"],"포지션이름"].reset_index().loc[0,"포지션이름"]
            magam = st.session_state.woodae.loc[st.session_state.woodae["조회기업선택"],"마감일"].reset_index().loc[0,"마감일"]
            df_final = df_plus[(df_plus["기업이름"]==company_name) & (df_plus["포지션이름"]==position_name)& (df_plus["마감일"]==magam)]
            # 여기서부터 상세 정보를 꾸미세요
                                    
            selected_info = df_final.iloc[0]
            company_name = selected_info['기업이름']
            scores = selected_info[['총점', '복지 및 급여', '업무와 삶의 균형', '사내문화', '승진 기회']]
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.bar(scores.index, scores.values, color='yellowgreen')
            ax.set_title(f'{company_name} 직원 만족도 지표', fontproperties=font_prop)
            ax.set_xticklabels(labels = scores.index,fontproperties=font_prop)
            ax.set_xlabel('')
            ax.set_ylabel('만족도', fontproperties=font_prop)
            ax.set_ylim(0, 5)  # 만족도는 0에서 5 사이의 값
            
            st.pyplot(fig)

            st.divider()

            selected_info = df_final.iloc[0]
            company_name = selected_info['기업이름']

            scores1 = selected_info[['기업추천율', 'CEO 지지율', '성장 가능성']]

            fig1, ax1 = plt.subplots(figsize=(12,6))
            bars1 = ax1.bar(scores1.index, scores1.values, color='olivedrab')

            for bar in bars1:
                height = bar.get_height()
                ax1.text(bar.get_x() + bar.get_width() / 2, height, '%d%%' % height, ha='center', va='bottom')

            ax1.set_title(f'{company_name} 기업 평가 지표', fontproperties=font_prop)
            ax1.set_xticklabels(labels = scores1.index,fontproperties=font_prop)
            ax1.set_xlabel('')
            ax1.set_ylabel('기업 평가', fontproperties=font_prop)
            ax1.set_ylim(0, 100) 

            # 그래프 출력
            st.pyplot(fig1)

            st.divider()

           #기업명

            df_name=selected_info['기업이름']
            st.subheader("기업명")
            st.write(df_name)

            st.divider()  

            # 주요업무
            df_work=selected_info['주요업무']
            st.subheader("주요 업무")
            st.write(df_work)

            st.divider()  

            # 자격요건
            df_intro=selected_info['자격요건']
            st.subheader("자격 요건")
            st.write(df_intro)

            st.divider()  

            # 자격요건
            df_pplus=selected_info['우대사항']
            st.subheader("우대 사항")
            st.write(df_pplus)

            st.divider()  

            # 매출액
            df_rev=selected_info['매출액']
            st.subheader("매출액")
            st.write(df_rev)

            st.divider()  

            # 사원수 
            df_ppl=selected_info['사원 수']
            st.header("사원 수")
            st.write(df_ppl,"명")

            st.divider()  

            # 기업평균연봉
            df_income=selected_info['기업 평균 연봉']
            st.subheader("기업 평균 연봉")
            st.write(df_income,"만원")

            st.divider()  

            # 퇴사입사자 수 
            df_out=selected_info['퇴사']
            df_in=selected_info['입사']
            st.subheader("작년 퇴사/입사자 수")
            st.write(df_out,"/",df_in)

            st.divider()  
    #트렌드 보여주기

    #기타 필터링
    with tab2:


        st.header('SOFT SKILL')
        softskill=st.multiselect(
            'SOFT SKILL 선택',
            ['의사소통', '논리적/분석적 사고', '문제해결능력', '프로세스', '리더십', '책임감', 
            '적극적', '의지/열정', '창의력', '비즈니스', '액션도출', 'Agile', '영어', '관심/경험']
            )
       
        start1=st.button('관련 공고 확인하기',key='1')
            
        
    
        
        if start1:
            filtered_softskill= df[(df[softskill] == 1).all(axis=1)]

            
            filtered_softskill=filtered_softskill[['기업이름', '포지션이름', '마감일', '경력_min', '경력_max', '채용형태', 
                 '근무장소 시', '근무장소 구','주요업무',  '자격요건', '우대사항','복지', '기업소개', '표준산업분류','사원 수', '기업 평균 연봉','기업유형',
                    '매출액','하이라이트+태그', '퇴사', '입사', '링크']]
            st.dataframe(data=filtered_softskill)

    with tab3:
        st.header('도메인')
        domain=st.multiselect(
            '관심 도메인 선택',
            ['제조', '항공', '마케팅', '정보 보안', '금융', '채용', '응용 소프트웨어 개발', '컨설팅', '의료',
    '에너지', '이커머스', '모빌리티', '엔터테인먼트', '유통', '건강', '가전', '패션', '정보 서비스업',
    '게임', '여행', '애견', '교육', '배달', '식품', '물류', '출판', '투자', '통신', '부동산',
    '없음', '리서치', '축산', '환경', '시스템 소프트웨어 개발', '스포츠', '화장품', '소셜 네트워크',
    '클라우드 컴퓨팅'])
    
        start2=st.button('관련 공고 확인하기',key='2')
        if start2:
            filtered_domain=df.loc[df["산업군 전처리"].isin(domain),:]

            filtered_domain=filtered_domain[['기업이름', '포지션이름', '마감일', '경력_min', '경력_max', '채용형태', 
                '근무장소 시', '근무장소 구','주요업무',  '자격요건', '우대사항','복지', '기업소개', '표준산업분류','사원 수', '기업 평균 연봉','기업유형',
                    '매출액','하이라이트+태그', '퇴사', '입사', '링크']]
                    
            st.dataframe(data=filtered_domain)

    with tab4:
        st.header('TOOL')
        tool=st.multiselect('TOOL 선택',
                            ['sql','r','python','tableau','redash','powerbi','lookerstudio','googleanalytics','amplitude','hadoop','hive'
                            ,'airflow','bigquery','aws','spark','pytorch','tensorflow']
        )
        start3=st.button('관련 공고 확인하기',key='3')

        if start3:
            filtered_tool=df_tool.loc[df_tool["Tool"].isin(tool),:]
            filtered_tool=filtered_tool[['기업이름', '포지션이름', '마감일', '경력_min', '경력_max', '채용형태', 
                 '근무장소 시', '근무장소 구','주요업무',  '자격요건', '우대사항','복지', '기업소개', '표준산업분류','사원 수', '기업 평균 연봉','기업유형',
                    '매출액','하이라이트+태그', '퇴사', '입사', '링크']]
            st.dataframe(data=filtered_tool)

    with tab5:
        st.subheader("데이터 분석가에게 주로 요구되는 학력이에요!")
        st.image("학력.png")
        st.divider()

        st.subheader("데이터 분석에게 요구되는 경력이에요!")
        st.image("경력.png")


        st.subheader("데이터 분석가에게 요구되는 자격요건 중, ‘Hard Skill’이에요!")
        st.image("hardskill.png")
        st.divider()

        st.subheader("데이터 분석가에게 요구되는 자격요건 중, ‘Soft Skill’이에요!")
        st.image("softskill.png")
        st.divider()

        st.subheader("데이터 분석가에게 요구되는 자격요건 중, ‘Tool’이에요!")
        st.image("Tool.png")
        st.divider()

        st.subheader("데이터 분석가를 채용하는 기업의 근무지역이에요!")
        st.image("지역.png")
        st.divider()
       

        st.subheader("데이터 분석가는 이 시간에 일해요!")
        st.subheader("탄력근무제, 선택적 근무시간제 등 상세한 내용을 공고에서 확인하세요!")
        st.image("근무시간.png")
        st.divider()
        st.subheader("잠깐! 재택 근무가 가능한 회사가 있어요")
 
        start5=st.button('재택 가능 공고 확인',key='5')
    
        if start5:
            
            filtered_remote=df_remote[(df_remote['재택여부'] == 1)]
            filtered_remote=filtered_remote[['기업이름', '포지션이름', '마감일', '경력_min', '경력_max', '채용형태', 
                 '근무장소 시', '근무장소 구','주요업무',  '자격요건', '우대사항','복지', '기업소개', '표준산업분류','사원 수', '기업 평균 연봉','기업유형',
                    '매출액','하이라이트+태그', '퇴사', '입사', '링크']]
            st.dataframe(data=filtered_remote)
        st.divider()

        st.subheader("데이터 분석가를 원하는 산업군이에요!")
        st.image("워드클라우드.png")

        st.subheader("당신을 기다리는 기업의 주요 사업이에요!")
        st.image("주요사업.png")

        st.subheader("각 유형별 기업에 근무하는 사원들의 평가예요!")
        st.image("기업유형평가.png")
        st.divider()
        st.subheader("상세한 평가는 여기서 볼 수 있어요!")
        st.image("기업유형세부평가.png")
        st.divider()


    
        

        
        start4=st.button('재택 가능 공고 확인',key='4')
    
        if start4:
            
            filtered_remote=df_remote[(df_remote['재택여부'] == 1)]
            filtered_remote=filtered_remote[['기업이름', '포지션이름', '마감일', '경력_min', '경력_max', '채용형태', 
                 '근무장소 시', '근무장소 구','주요업무',  '자격요건', '우대사항','복지', '기업소개', '표준산업분류','사원 수', '기업 평균 연봉','기업유형',
                    '매출액','하이라이트+태그', '퇴사', '입사', '링크']]
            st.dataframe(data=filtered_remote)




if __name__=="__main__":
    main()


