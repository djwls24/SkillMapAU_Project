
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer

def crawl_seek_sample(keyword="developer", pages=5):
    headers = {'User-Agent': 'Mozilla/5.0'}
    base_url = "https://www.seek.com.au"
    job_data = []

    for page in range(1, pages + 1):
        url = f"{base_url}/jobs?page={page}&keywords={keyword}"
        resp = requests.get(url, headers=headers)
        if resp.status_code != 200:
            continue
        soup = BeautifulSoup(resp.text, 'html.parser')
        jobs = soup.find_all("article")
        for job in jobs:
            title = job.find("a")
            if title:
                job_data.append(title.text.strip())

    return job_data

def clean_text(texts):
    cleaned = [re.sub(r'[^a-zA-Z ]', '', t).lower() for t in texts]
    return cleaned

def preprocess_keywords(texts):
    vectorizer = TfidfVectorizer(stop_words='english', max_features=100)
    X = vectorizer.fit_transform(texts)
    feature_names = vectorizer.get_feature_names_out()
    freqs = X.sum(axis=0).A1
    keywords_freq = dict(zip(feature_names, freqs))
    return sorted(keywords_freq.items(), key=lambda x: x[1], reverse=True)

def visualize_keywords(keywords_freq, top_n=20):
    top_keywords = dict(keywords_freq[:top_n])

    # Bar plot
    plt.figure(figsize=(10, 6))
    plt.bar(top_keywords.keys(), top_keywords.values())
    plt.title("Top Keywords in Job Postings")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("/mnt/data/skill_barplot.png")
    plt.close()

    # WordCloud
    wc = WordCloud(width=800, height=400, background_color='white')
    wc.generate_from_frequencies(dict(keywords_freq))
    wc.to_file("/mnt/data/wordcloud.png")

def main():
    print("크롤링 중...")
    job_titles = crawl_seek_sample("it developer", pages=5)
    df = pd.DataFrame(job_titles, columns=["title"])
    df.to_csv("/mnt/data/seek_jobs_raw.csv", index=False)

    print("텍스트 전처리 중...")
    cleaned = clean_text(df['title'].tolist())
    print("키워드 분석 중...")
    keywords_freq = preprocess_keywords(cleaned)
    print("시각화 생성 중...")
    visualize_keywords(keywords_freq)
    print("완료.")

if __name__ == "__main__":
    main()
