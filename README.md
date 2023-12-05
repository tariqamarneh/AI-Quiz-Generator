# AI-Quiz-Generator
The AI Quiz Generator is an application that employs the OpenAI GPT-3.5 Turbo model to craft multiple-choice questions on a specified topic. Seamlessly integrated with Streamlit, this tool provides a user-friendly interface for specifying the desired topic and the number of questions needed. Using a template prompt, the application generates questions, choices, and correct answers.

To use the quiz generator, simply input the topic and desired number of questions. After answering the questions, the application provides both the quiz score and the correct answers. With the added convenience of Streamlit, the entire process is made accessible and intuitive, enhancing the overall user experience.

## Installation

Follow the steps below to set up and run the project on your local machine:
1. Clone the repository to your local machine using the following command:
```
git clone https://github.com/tariqamarneh/AI-Quiz-Generato.git
```
2. Navigate to the project directory:
```
cd AI-Quiz-Generato
```
3. Install the required dependencies by running the following commands:
```
pip install -r requirements.txt
```
4. Run the website locally using the following command (replace <api-key> with you openAI API_key):
```
streamlit run main.py <api-key>
```

## Usage
1. **Open the Website**: using streamlit run main.py <api-key>.

2. **Choose the topic**: Enter the topic name that you want to get a quiz about.

3. **specify number of questions**: Enter the number of questions.

4. **Start Quiz**: Click on start quiz to generate the questions.

5. **Answer the questions**: Every question has four choices, and one correct answer.

6. **Submit Answers**: Once you answered all of the questions, click on submit  Answers to get the result.
