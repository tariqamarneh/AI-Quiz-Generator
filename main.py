import streamlit as st
from backend import ChatBot
import sys


def quiz_app(apikey):
    st.title("Quiz App")
    if "questions" not in st.session_state:
        st.session_state["questions"] = {}

    # Get the input from the user
    topic = st.text_input("Enter a topic:")
    num_questions = st.number_input("Enter the number of questions:", min_value=1, step=1)

    # Check if the start button clicked or the number of questions changed from 1
    # To avoid rerun while choosing the answers
    if st.button("Start Quiz") or num_questions > 1:

        # Check if questions not generated
        if not st.session_state["questions"]:
            client = ChatBot(apikey)
            client.get_question(topic, num_questions)

            # Check if the topic is valid else error message
            try:
                st.session_state["questions"] = client.format_questions()
            except ValueError:
                st.error('Enter a valid topic')
                exit()

        # Display questions and collect answers from the user
        user_answers = {}
        for q, (c, a) in st.session_state["questions"].items():
            st.markdown(f"**{q}**")
            user_answers[q] = st.radio("Select your answer:", c, key=q)
            st.markdown("---")

        # Show user selected answers and the correct answer after submission
        if st.button("Submit Answers"):
            st.success("Answers Submitted!")
            st.subheader("Your Answers:")

            # Calculate and print the score, and check if the score is above 0.5 or not
            score = 0
            for question, answer in user_answers.items():
                if answer.startswith(st.session_state["questions"][question][1]):
                    score = score + 1
                st.write(f"{question}: {answer}")
                st.write(f"The correct answer is: ", st.session_state["questions"][question][1])
            if score/num_questions >= 0.5:
                st.success(f"You score is: {score}/{num_questions}")
            else:
                st.error(f"You score is: {score}/{num_questions}")
        if st.button('Close'):
            st.rerun()


if __name__ == "__main__":
    # Check if there are exactly two arguments, the script name and the API_key
    if len(sys.argv) != 2:
        print("Usage: python main.py <api_key>")
    else:
        api_key = sys.argv[1]
        quiz_app(api_key)
