import json
from difflib import get_close_matches

def load_kownledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def save_knowledge_base(file_path: str, data:dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]

def chat_bot():
    knowledge_base: dict = load_kownledge_base('knowledge_base.json')

    while True:
        user_input: str = input(user.capitalize()+ ': ')

        if user_input.lower() == 'stop':
            print("")
            print("Goodbye! It was a pleasure assisting you. Have a great day! 😊")
            print("")
            break
        elif user_input.lower() == 'bye':
            print("")
            print("Goodbye! It was a pleasure assisting you. Have a great day! 😊")
            print("")
            break
        elif user_input.lower() == 'bye bye':
            print("")
            print("Goodbye! It was a pleasure assisting you. Have a great day! 😊")
            print("")
            break

        best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

        if best_match:
            answer: str = get_answer_for_question(best_match, knowledge_base)
            print(f'MineBot: {answer}')
        else:
            print('MineBot: I don\'t know the answer. Can you teach me ? ')
            new_answer: str = input('Type the answer or "skip" to Skip: ')

            if new_answer.lower() != 'skip':
                if new_answer.lower() != '':
                    knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                    save_knowledge_base('knowledge_base.json', knowledge_base)
                    print('MineBot: Thank You ! I learned a new response !')

print("")
print("HELLO!")
print("")
user = input(str("WHAT IS YOUR NAME: "))
print("")
print("WELCOME "+user.upper()+" !")
print("")
print("---------------------------------------------------------------------------------")
print("")
print("HELLO! THIS IS MINEBOT. HOW CAN I ASSIST YOU TODAY? 😊")
print("")
print("TO EXIT FROM THE TERMIAL OR STOP RESPONSE PLEASE TYPE 'STOP'")
print("")

if __name__ == '__main__':
    chat_bot()