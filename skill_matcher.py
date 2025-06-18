
import pandas as pd

def load_skill_data(csv_path='skill_frequency.csv'):
    return pd.read_csv(csv_path)

def recommend_job(user_skills, skill_data):
    skill_data['match'] = skill_data['Skill'].apply(lambda s: s in user_skills)
    matched_skills = skill_data[skill_data['match']]
    score = len(matched_skills)
    recommendations = matched_skills[['Skill', 'Frequency']]
    return recommendations.sort_values(by='Frequency', ascending=False), score

if __name__ == "__main__":
    user_skills = ['Python', 'SQL', 'AWS', 'Docker']
    skill_data = load_skill_data()
    recommendations, score = recommend_job(user_skills, skill_data)

    print(f"총 {score}개의 기술이 매칭되었습니다. 추천 기술 목록:")
    print(recommendations)
