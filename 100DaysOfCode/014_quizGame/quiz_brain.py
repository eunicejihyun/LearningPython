import html as h


class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        # pulls up next question in list
        new_q = self.question_list[self.question_number]
        q_text = h.unescape(new_q.text)
        self.question_number += 1
        return f"Q{self.question_number}\n {q_text} True or False? "
        # user_response = input(f"").lower()
        # self.check_answer(user_response, new_q.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
