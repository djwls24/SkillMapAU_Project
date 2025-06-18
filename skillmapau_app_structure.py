
# skillmapau_app_structure.py
# 간단한 Flask 앱 구조 예시

from flask import Flask, request, jsonify
from skill_matcher import match_skills

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    user_skills = set(data.get('skills', []))
    results = match_skills(user_skills)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
