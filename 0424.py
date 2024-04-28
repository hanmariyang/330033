import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
import io
import base64
plt.rcParams['font.family'] = 'AppleGothic'




st.set_page_config(page_title='recc',layout='wide')

df = pd.read_csv('/Users/jeong-yula/Desktop/streamlit/전처리통합최종.csv')
df_plus=pd.read_csv('/Users/jeong-yula/Desktop/streamlit/hs_plus.csv')
df_tool=pd.read_csv('/Users/jeong-yula/Desktop/streamlit/tool2.csv')
# hardskill_df=pd.read_csv('/Users/jeong-yula/Desktop/streamlit/hardskill.csv')




tab1, tab2, tab3, tab4 = st.tabs(["recommend", "trend", "etc","기업 정보"])

with tab1:   
    # col1, col2 = st.columns(2)

    st.header('Hard Skill')
    st.write("DA : 데이터 분석 자체에 대한 경험")
    st.write("통계 : 통계 분석, 통계적 지식, 회귀 분석, 정량적 분석 등")
    st.write("머신러닝 : 머신러닝, 모델링, 분류/예측 모델링, 시계열 데이터 활용")
    st.write("딥러닝 : 딥러닝, 알고리즘, 프레임워크, 검색 알고리즘, 추천 알고리즘, 자연어 처리, 차원 모델링")
    st.write("시각화 : 데이터 시각화, BI Tool 활용, 대시보드 구축")
    st.write("데이터 가공 : 데이터 수집, 데이터 추출, 데이터 처리")
    st.write("빅데이터 : 빅데이터 분석, 빅데이터 처리, 대용량 데이터 분산처리 경험")
    st.write("클라우드 : 클라우드 서비스 플랫폼 (AWS, GA4, Google Cloud Platform 등)")
    st.write("파이프라인 : 데이터마트, 데이터 웨어하우스, 데이터 레이크 구축 및 데이터 파이프라인 설계 경험")
    st.write("그로스 해킹 : Funnel 분석, Cohort 분석, AARRR, Retention, A/B테스트 등 마케팅 및 비즈니스 분석에 필요한 분석 기법 활용 경험")
    st.write("로그 : App/Web 유저 데이터, 사용자 행동 데이터, 로그 데이터")
    st.write("마케팅 : 마케팅 경험, 프로덕트 분석, 비즈니스 분석")
        
    hardskill=st.multiselect(
        'select hard skill',
        ['DA', '통계', 'ML', 'DL', '시각화', '데이터 가공',
            '빅데이터', '클라우드', '파이프라인', '그로스해킹', '로그', '마케팅']
        )





    st.header('경력')
    option = st.selectbox(
        "경력 기간",
        ("1", "2", "3","4","5","6","7"),
        index=None
    )

    st.write('You selected:', option)




    start=st.button('추천 받기')

    if start:
    # df_filtered=df.loc[df['Tool'].isin(lang),:]
        filtered_df = df[(df[hardskill] == 1).any(axis=1)]
        first_row = filtered_df.iloc[0]
        index = filtered_df.index[0]


    # st.dataframe(data=filtered_df)

        selected_columns = ['Unnamed: 0', 'DA', '통계', 'ML', 'DL', '시각화', '데이터 가공',
        '빅데이터', '클라우드', '파이프라인', '그로스해킹', '로그', '마케팅']
        new_df = filtered_df[selected_columns]





        from sklearn.metrics.pairwise import cosine_similarity



        cosine_sim = cosine_similarity(new_df)


        def cos_sim_index(index_num):
            selected_similarities = cosine_sim[int(index_num)]
            similarities_with_index = [(similarity, index) for index, similarity in enumerate(selected_similarities) if index != int(index_num)]
            similarities_with_index.append((1.0, int(index_num)))  # Add similarity of 1.0 for the selected index
            sorted_similarities = sorted(similarities_with_index, key=lambda x: x[0], reverse=True)
            top_6_similar_jobs = [filtered_df.iloc[index].tolist() for similarity, index in sorted_similarities[:6]]


            df = pd.DataFrame(data = top_6_similar_jobs,columns=['Unnamed: 0', '사이트', '검색 키워드', '기업이름', '포지션이름', '포지션이름 전처리', '포지션 세부 ', '마감일', '상시 채용 여부', '경력_min', '경력_max', '학력', '학력 세부정보', '스킬', '제출서류', '채용절차', '채용형태', '채용형태_전처리', '채용형태_전처리 세부', '급여', '근무시간', '근무장소', '근무장소 시', '근무장소 구', '경기도 구 ', '근무형태', '주요업무', '인재상', '자격요건', 'Hard Skill', 'Soft Skill', 'Tool', '우대사항', 'hard plus', 'soft plus', 'tool plus', '복지', '기업소개', '표준산업분류', '주요사업', '주요사업.1', '산업군', '산업군 전처리', '설립', '사원 수', '기업 평균 연봉', '기업유형', '기업 유형 전처리', '기업 유형 전처리 _세부', '매출액', '접수방법', '총점', '복지 및 급여', '업무와 삶의 균형', '사내문화', '승진 기회', '경영진', '기업추천율', 'CEO 지지율', '성장 가능성', '하이라이트+태그', '퇴사', '입사', '링크', 'DA', '통계', 'ML', 'DL', '시각화', '데이터 가공', '빅데이터', '클라우드', '파이프라인', '그로스해킹', '로그', '마케팅', '도메인', '프로그래밍언어', '의사소통', '논리적/분석적 사고', '문제해결능력', '프로세스', '리더십', '책임감', '적극적', '의지/열정', '창의력', '비즈니스', '액션도출', 'Agile', '영어', '관심/경험', 'Tool1', 'SQL', 'Python', 'R', '시각화 툴', '로그분석', 'BigData', 'Cloud', 'database', '개발', 'MLtool', 'DLtool', 'DA plus', '통계 plus', 'ML plus', 'DL plus', '시각화 plus', '데이터 가공 plus', '빅데이터 plus', '파이프라인 plus', '그로스해킹 plus', '로그 plus', '마케팅 plus', '의사소통 plus', '리더십 plus', '문제해결능력 plus', 'Agile plus', '학력 plus', '창의력 plus', '적극적 plus', '논리적/분석적 사고 plus', '관심/경험 plus', '영어 plus', '전공', '공모전', '프로젝트 경험', '논문', 'tool plus1', 'SQL plus', 'Python plus', 'R plus', '시각화 툴 plus', '로그분석 plus', 'BigData plus', 'Cloud plus', 'database plus', '개발 plus', 'MLTool plus', 'DLTool plus']
            )

            df=df[['사이트', '검색 키워드', '기업이름', '포지션이름', '포지션이름 전처리', '포지션 세부 ', '마감일', 
                    '상시 채용 여부', '경력_min', '경력_max', '학력', '학력 세부정보', '스킬', '제출서류', '채용절차', '채용형태', 
                    '채용형태_전처리', '채용형태_전처리 세부', '급여', '근무시간', '근무장소', '근무장소 시', '근무장소 구', '경기도 구 ', '근무형태',
                        '주요업무', '인재상', '자격요건', 'Hard Skill', 'Soft Skill', 'Tool', '우대사항', 'hard plus', 'soft plus', 'tool plus', 
                        '복지', '기업소개', '표준산업분류', '주요사업', '주요사업.1', '산업군', '산업군 전처리', '설립', '사원 수', '기업 평균 연봉', '기업유형',
                        '기업 유형 전처리', '기업 유형 전처리 _세부', '매출액', '접수방법', '총점', '복지 및 급여', '업무와 삶의 균형', '사내문화', '승진 기회', 
                    '경영진', '기업추천율', 'CEO 지지율', '성장 가능성', '하이라이트+태그', '퇴사', '입사', '링크'
                    ,'DA', '통계', 'ML', 'DL', '시각화', '데이터 가공',
                '빅데이터', '클라우드', '파이프라인', '그로스해킹', '로그', '마케팅']]

            st.header('상위5개')
            st.dataframe(data=df)


        cos_sim_index(index)

        # 우대사항
        filtered_df_plus = df_plus[(df_plus[hardskill] == 1).all(axis=1)]
        first_row_plus = filtered_df_plus.iloc[0]
        index_plus = filtered_df_plus.index[0]


        selected_columns = ['Unnamed: 0', 'DA', '통계', 'ML', 'DL', '시각화', '데이터 가공',
            '빅데이터', '클라우드', '파이프라인', '그로스해킹', '로그', '마케팅']
        new_df_plus = filtered_df_plus[selected_columns]


        cosine_sim = cosine_similarity(new_df_plus)


        def cos_sim_index(index_num):
            selected_similarities = cosine_sim[int(index_num)]
            similarities_with_index = [(similarity, index) for index, similarity in enumerate(selected_similarities) if index != int(index_num)]
            similarities_with_index.append((1.0, int(index_num)))  # Add similarity of 1.0 for the selected index
            sorted_similarities = sorted(similarities_with_index, key=lambda x: x[0], reverse=True)
            top_6_similar_jobs = [filtered_df_plus.iloc[index].tolist() for similarity, index in sorted_similarities[:6]]


            df_plus = pd.DataFrame(data = top_6_similar_jobs,columns=['Unnamed: 0','Unnamed: 0', '사이트', '검색 키워드', '기업이름', '포지션이름', '포지션이름 전처리', '포지션 세부 ', '마감일', '상시 채용 여부', '경력_min', '경력_max', '학력', '학력 세부정보', '스킬', '제출서류', '채용절차', '채용형태', '채용형태_전처리', '채용형태_전처리 세부', '급여', '근무시간', '근무장소', '근무장소 시', '근무장소 구', '경기도 구 ', '근무형태', '주요업무', '인재상', '자격요건', 'Hard Skill', 'Soft Skill', 'Tool', '우대사항', 'hard plus', 'soft plus', 'tool plus', '복지', '기업소개', '표준산업분류', '주요사업', '주요사업.1', '산업군', '산업군 전처리', '설립', '사원 수', '기업 평균 연봉', '기업유형', '기업 유형 전처리', '기업 유형 전처리 _세부', '매출액', '접수방법', '총점', '복지 및 급여', '업무와 삶의 균형', '사내문화', '승진 기회', '경영진', '기업추천율', 'CEO 지지율', '성장 가능성', '하이라이트+태그', '퇴사', '입사', '링크', 'DA', '통계', 'ML', 'DL', '시각화', '데이터 가공', '빅데이터', '클라우드', '파이프라인', '그로스해킹', '로그', '마케팅', '도메인', '프로그래밍언어', '의사소통', '논리적/분석적 사고', '문제해결능력', '프로세스', '리더십', '책임감', '적극적', '의지/열정', '창의력', '비즈니스', '액션도출', 'Agile', '영어', '관심/경험', 'Tool1', 'SQL', 'Python', 'R', '시각화 툴', '로그분석', 'BigData', 'Cloud', 'database', '개발', 'MLtool', 'DLtool', 'DA', '통계', 'ML', 'DL', '시각화', '데이터 가공', '빅데이터', '파이프라인', '그로스해킹', '로그', '마케팅', '의사소통 plus', '리더십 plus', '문제해결능력 plus', 'Agile plus', '학력 plus', '창의력 plus', '적극적 plus', '논리적/분석적 사고 plus', '관심/경험 plus', '영어 plus', '전공', '공모전', '프로젝트 경험', '논문', 'tool plus1', 'SQL plus', 'Python plus', 'R plus', '시각화 툴 plus', '로그분석 plus', 'BigData plus', 'Cloud plus', 'database plus', '개발 plus', 'MLTool plus', 'DLTool plus']
        )

            df_plus=df_plus[['사이트', '검색 키워드', '기업이름', '포지션이름', '포지션이름 전처리', '포지션 세부 ', '마감일', 
                '상시 채용 여부', '경력_min', '경력_max', '학력', '학력 세부정보', '스킬', '제출서류', '채용절차', '채용형태', 
                '채용형태_전처리', '채용형태_전처리 세부', '급여', '근무시간', '근무장소', '근무장소 시', '근무장소 구', '경기도 구 ', '근무형태',
                    '주요업무', '인재상', '자격요건', 'Hard Skill', 'Soft Skill', 'Tool', '우대사항', 'hard plus', 'soft plus', 'tool plus', 
                    '복지', '기업소개', '표준산업분류', '주요사업', '주요사업.1', '산업군', '산업군 전처리', '설립', '사원 수', '기업 평균 연봉', '기업유형',
                    '기업 유형 전처리', '기업 유형 전처리 _세부', '매출액', '접수방법', '총점', '복지 및 급여', '업무와 삶의 균형', '사내문화', '승진 기회', 
                '경영진', '기업추천율', 'CEO 지지율', '성장 가능성', '하이라이트+태그', '퇴사', '입사', '링크']]

            st.header('우대사항 5개')
            st.dataframe(data=df_plus)


        cos_sim_index(index_plus)




with tab2:
   st.header("Trend")

   with st.container():
      st.write("This is inside the container")

   # You can call any Streamlit command, including custom components:
   st.bar_chart(np.random.randn(50, 3))

   st.write("This is outside the container")


with tab3:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header('Soft Skill')
        softskill=st.multiselect(
            'soft skill 선택',
            ['의사소통', '논리적/분석적 사고', '문제해결능력', '프로세스', '리더십', '책임감', 
             '적극적', '의지/열정', '창의력', '비즈니스', '액션도출', 'Agile', '영어', '관심/경험']
            )
        start1=st.button('관련 공고 확인하기',key='1')
        if start1:
            filtered_softskill= df[(df[softskill] == 1).all(axis=1)]

            
            filtered_softskill=filtered_softskill[['사이트', '검색 키워드', '기업이름', '포지션이름', '포지션이름 전처리', '포지션 세부 ', '마감일', 
                   '상시 채용 여부', '경력_min', '경력_max', '학력', '학력 세부정보', '스킬', '제출서류', '채용절차', '채용형태', 
                   '채용형태_전처리', '채용형태_전처리 세부', '급여', '근무시간', '근무장소', '근무장소 시', '근무장소 구', '경기도 구 ', '근무형태',
                     '주요업무', '인재상', '자격요건', 'Hard Skill', 'Soft Skill', 'Tool', '우대사항', 'hard plus', 'soft plus', 'tool plus', 
                     '복지', '기업소개', '표준산업분류', '주요사업', '주요사업.1', '산업군', '산업군 전처리', '설립', '사원 수', '기업 평균 연봉', '기업유형',
                       '기업 유형 전처리', '기업 유형 전처리 _세부', '매출액', '접수방법', '총점', '복지 및 급여', '업무와 삶의 균형', '사내문화', '승진 기회', 
                   '경영진', '기업추천율', 'CEO 지지율', '성장 가능성', '하이라이트+태그', '퇴사', '입사', '링크']]
            st.dataframe(data=filtered_softskill)


    with col2:
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

            filtered_domain=filtered_domain[['사이트', '검색 키워드', '기업이름', '포지션이름', '포지션이름 전처리', '포지션 세부 ', '마감일', 
                   '상시 채용 여부', '경력_min', '경력_max', '학력', '학력 세부정보', '스킬', '제출서류', '채용절차', '채용형태', 
                   '채용형태_전처리', '채용형태_전처리 세부', '급여', '근무시간', '근무장소', '근무장소 시', '근무장소 구', '경기도 구 ', '근무형태',
                     '주요업무', '인재상', '자격요건', 'Hard Skill', 'Soft Skill', 'Tool', '우대사항', 'hard plus', 'soft plus', 'tool plus', 
                     '복지', '기업소개', '표준산업분류', '주요사업', '주요사업.1', '산업군', '산업군 전처리', '설립', '사원 수', '기업 평균 연봉', '기업유형',
                       '기업 유형 전처리', '기업 유형 전처리 _세부', '매출액', '접수방법', '총점', '복지 및 급여', '업무와 삶의 균형', '사내문화', '승진 기회', 
                   '경영진', '기업추천율', 'CEO 지지율', '성장 가능성', '하이라이트+태그', '퇴사', '입사', '링크']]
                    
            st.dataframe(data=filtered_domain)


    with col3:
        st.header('TOOL')
        tool=st.multiselect('Tool 선택',
                            ['sql','r','python','tableau','redash','powerbi','lookerstudio','googleanalytics','amplitude','hadoop','hive'
                             ,'airflow','bigquery','aws','spark','pytorch','tensorflow']
        )
        start3=st.button('관련 공고 확인하기',key='3')

        if start3:
            filtered_tool=df_tool.loc[df_tool["Tool"].isin(tool),:]
            filtered_tool=filtered_tool[['사이트', '검색 키워드', '기업이름', '포지션이름', '포지션이름 전처리', '포지션 세부 ', '마감일', 
                   '상시 채용 여부', '경력_min', '경력_max', '학력', '학력 세부정보', '스킬', '제출서류', '채용절차', '채용형태', 
                   '채용형태_전처리', '채용형태_전처리 세부', '급여', '근무시간', '근무장소', '근무장소 시', '근무장소 구', '경기도 구 ', '근무형태',
                     '주요업무', '인재상', '자격요건', 'Hard Skill', 'Soft Skill', 'Tool', '우대사항', 'hard plus', 'soft plus', 'tool plus', 
                     '복지', '기업소개', '표준산업분류', '주요사업', '주요사업.1', '산업군', '산업군 전처리', '설립', '사원 수', '기업 평균 연봉', '기업유형',
                       '기업 유형 전처리', '기업 유형 전처리 _세부', '매출액', '접수방법', '총점', '복지 및 급여', '업무와 삶의 균형', '사내문화', '승진 기회', 
                   '경영진', '기업추천율', 'CEO 지지율', '성장 가능성', '하이라이트+태그', '퇴사', '입사', '링크']]
            
            st.dataframe(data=filtered_tool)

with tab4:

    df_etc=df[['기업이름','포지션이름','마감일','채용형태','근무장소','기업소개','자격요건','우대사항','복지','주요업무',
           '설립', '사원 수', '기업 평균 연봉', '기업유형',
                       '기업 유형 전처리', '기업 유형 전처리 _세부', '매출액', '접수방법', '총점', '복지 및 급여', '업무와 삶의 균형', '사내문화', '승진 기회', 
                   '경영진', '기업추천율', 'CEO 지지율', '성장 가능성',
                   '퇴사','입사']]
    
    
    
    selected_info = df_etc.iloc[5]
    company_name = selected_info['기업이름']
    scores = selected_info[['총점', '복지 및 급여', '업무와 삶의 균형', '사내문화', '승진 기회']]
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(scores.index, scores.values, color='green')
    ax.set_title(f'{company_name} 직원 만족도 지표')
    ax.set_xlabel('지표')
    ax.set_ylabel('만족도')
    ax.set_ylim(0, 5)  # 만족도는 0에서 5 사이의 값
    
    st.pyplot(fig)

    
    company_name = selected_info['기업이름']
    scores1 = selected_info[['기업추천율','CEO 지지율','성장 가능성']]
    fig1, ax = plt.subplots(figsize=(8, 4))
    ax.bar(scores1.index, scores.values, color='green')
    ax.set_title(f'{company_name} 기업 평가 지표(%) ')
    ax.set_xlabel('지표')
    ax.set_ylabel('기업 평가')
    ax.set_ylim(0, 100) 
    
    st.pyplot(fig1)


    # st.write(selected_info)

    # columns = ['총점', '복지 및 급여', '업무와 삶의 균형', '사내문화', '승진 기회']
    # values = selected_info[['총점', '복지 및 급여', '업무와 삶의 균형', '사내문화', '승진 기회']]

    # # 바 차트를 그리기 위해 데이터를 딕셔너리 형태로 변환
    # data = {columns[i]: values[i] for i in range(len(columns))}



#     #기업명
#     df_name=selected_info['기업이름']
#     st.header("기업명")
#     st.write(df_name)

#     st.divider()  

#     # 주요업무
#     df_work=selected_info['주요업무']
#     st.header("주요 업무")
#     st.write(df_work)

#     st.divider()  

#     # 자격요건
#     df_intro=selected_info['자격요건']
#     st.header("자격 요건")
#     st.write(df_intro)


#     st.divider()  

#     # 자격요건
#     df_pplus=selected_info['우대사항']
#     st.header("우대 사항")
#     st.write(df_pplus)

#     st.divider()  

#     # 매출액
#     df_rev=selected_info['매출액']
#     st.header("매출액")
#     st.write(df_rev)

#     st.divider()  

#     # 사원수 
#     df_ppl=selected_info['사원 수']
#     st.header("사원 수")
#     st.write(df_ppl,"명")

#     st.divider()  

#     # 기업평균연봉
#     df_income=selected_info['기업 평균 연봉']
#     st.header("기업 평균 연봉")
#     st.write(df_income,"만원")

#     st.divider()  

#     # 퇴사입사자 수 
#     df_out=selected_info['퇴사']
#     df_in=selected_info['입사']
#     st.header("작년 퇴사/입사자 수")
#     st.write(df_out,"/",df_in)

#     st.divider()  


#     st.header("기업 평점")

#     bar_chart_data = pd.DataFrame({
#         'aspect': ['총점', '복지 및 급여', '워라밸', '사내문화', '승진 기회'],
#         'score': selected_info[['총점', '복지 및 급여', '업무와 삶의 균형', '사내문화', '승진 기회']]
#     })

#     # 바 차트 생성
#     bar_chart = alt.Chart(bar_chart_data).mark_bar(color='gray').encode(
#         x=alt.X('aspect:N', title=None, axis=alt.Axis(labelAngle=0)),
#         y=alt.Y('score:Q', title='Score'),
#         tooltip=['aspect:N', 'score:Q']
#     ).properties(
#         width=alt.Step(80),
#         height=400
#     )

#     st.altair_chart(bar_chart, use_container_width=True)

#     st.divider()  

#     chart_data = pd.DataFrame({
#     'aspect': ['기업추천율', 'CEO 지지율', '성장 가능성'],
#     'score': selected_info[['기업추천율', 'CEO 지지율', '성장 가능성']]
# })

#     # 선 그래프 생성
#     line_chart = alt.Chart(chart_data).mark_bar().encode(
#         x=alt.X('aspect:N', title=None, axis=alt.Axis(labelAngle=0)),
#         y=alt.Y('score:Q', title='Score (%)'),
#         tooltip=['aspect:N', 'score:Q']
#     ).properties(
#         width=alt.Step(80),
#         height=400
#     )


#     st.altair_chart(line_chart, use_container_width=True)

