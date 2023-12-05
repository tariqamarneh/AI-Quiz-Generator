from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate


class ChatBot:
    def __init__(self, api_key):
        self.template = """You are a quiz bot, expert in asking question with 4 choices.
        ask {quantity} questions about a specific topic.
        ONLY return the question and the choices, and between brackets return the answer letter.
        EXACT template: 1)question\\nA)a\\nB)b\\nC)c\\nD)d\\n[B]"""

        self.human_template = "{text}"

        self.chat_prompt = ChatPromptTemplate.from_messages([
            ("system", self.template),
            ("human", self.human_template),
        ])

        self.llm = ChatOpenAI(openai_api_key=api_key)

        self.question = None

        self.QA = None

    def get_question(self, topic, number_of_questions):
        prompt = self.chat_prompt.format_messages(quantity=number_of_questions, text=topic)
        self.question = self.llm.invoke(prompt).content

    def format_questions(self):
        self.QA = {}
        questions = self.question.split('\n\n')
        for q in questions:
            if q.strip():
                answer = q[-2]
                question = q[0:q.index('A)') - 1]
                lines = q.split('\n')
                choices = [lines[i] for i in range(-5, -1, 1)]
                self.QA[question] = [choices, answer]
        return self.QA
