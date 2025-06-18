
# skill_self_test.py
# 간단한 기술 셀프 진단 퀴즈 CLI

questions = [
    {
        "question": "1. Python에서 리스트의 길이를 구하는 함수는 무엇인가요?",
        "options": ["A. size()", "B. len()", "C. count()", "D. length()"],
        "answer": "B"
    },
    {
        "question": "2. SQL에서 데이터를 조회할 때 사용하는 명령어는?",
        "options": ["A. INSERT", "B. UPDATE", "C. SELECT", "D. DELETE"],
        "answer": "C"
    },
    {
        "question": "3. Git에서 버전 관리를 초기화하는 명령어는?",
        "options": ["A. git start", "B. git begin", "C. git init", "D. git create"],
        "answer": "C"
    },
    {
        "question": "4. HTML에서 링크를 만드는 태그는?",
        "options": ["A. <link>", "B. <a>", "C. <href>", "D. <url>"],
        "answer": "B"
    },
    {
        "question": "5. Java에서 클래스를 정의하는 키워드는?",
        "options": ["A. def", "B. function", "C. class", "D. object"],
        "answer": "C"
    }
]

def run_quiz():
    score = 0
    print("기술 셀프 진단 테스트를 시작합니다. (총 5문항)\n")
    for q in questions:
        print(q["question"])
        for opt in q["options"]:
            print(opt)
        answer = input("정답을 입력하세요 (A/B/C/D): ").strip().upper()
        if answer == q["answer"]:
            score += 1
        print()
    print(f"총 점수: {score}/5")
    if score >= 4:
        print("우수한 기술 이해도를 보유하고 있습니다.")
    elif score == 3:
        print("기술 기초는 갖추었으나 추가 학습이 필요합니다.")
    else:
        print("기초부터 다시 학습해보세요.")

if __name__ == "__main__":
    run_quiz()
