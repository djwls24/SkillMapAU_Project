# 호주 IT 개발자 채용공고 분석 기반 기술 스킬 도출 연구

## 📘 논문 주제
**호주 IT 개발자 채용공고 분석을 통한 기술 스킬 도출 연구**

본 프로젝트는 호주 현지 구인구직 플랫폼인 SEEK 사이트의 채용공고 데이터를 수집 및 분석하여, IT 개발자에게 요구되는 기술 스택을 도출하고, 이를 바탕으로 커리어 설계 방향을 제시하기 위한 연구입니다.

## 🎯 연구 목적
- 호주 IT 채용 시장의 실시간 기술 수요 파악
- 직무별 기술 스택 및 우대 기술 정량 분석
- 구직자의 커리어 설계에 도움을 줄 수 있는 데이터 기반 인사이트 제공

## 📊 데이터 수집 및 분석
- **데이터 출처:** SEEK Australia (https://www.seek.com.au)
- **크롤링 키워드:** "IT Developer", "Software Engineer", "Full Stack", "Data Engineer"
- **총 수집 공고:** 약 500건
- **분석 기법:** 텍스트 마이닝, 키워드 빈도 분석, TF-IDF 분석, 직무별 클러스터링
- **사용 도구:** Python (BeautifulSoup, nltk, scikit-learn, wordcloud, pandas)

## 🔍 주요 분석 결과 요약
- 핵심 기술: Python, Java, AWS, SQL, JavaScript
- 직무별 선호 기술 차이 명확 (예: 백엔드 - Java/Spring, 프론트엔드 - React/TypeScript 등)
- 우대 사항: 클라우드 경험, 협업 툴 사용 능력, 커뮤니케이션 역량 등

## 💡 핵심 코드 예시
> `src/skill_analysis.py` 파일에 주요 분석 코드를 포함했습니다.
- 텍스트 전처리
- 키워드 추출 및 시각화
- TF-IDF 계산
- 상위 기술 키워드 추출

```python
# 예시: 주요 키워드 추출
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(stop_words='english', max_features=100)
tfidf_matrix = vectorizer.fit_transform(job_descriptions)
feature_names = vectorizer.get_feature_names_out()
```

## 📄 포함 파일
- `논문_최종본.docx`: 분석 기반 연구 논문 전체 문서
- `skill_analysis.py`: 채용공고 텍스트 분석용 핵심 코드 파일
- `기술_키워드_워드클라우드.png`: 분석 결과 시각화 자료
- `README.md`: 프로젝트 개요 및 문서

## 📚 참고문헌
- SEEK Australia (https://www.seek.com.au)
- Python Software Foundation (https://www.python.org)
- Scikit-learn documentation (https://scikit-learn.org)
- 한국정보과학회 논문지 외 관련 국내 논문
