from llama_index.core import VectorStoreIndex
import json

class Index:

    def index_documents(documents):

        GENERATE_2_QUESTIONS_PROMPT = (

            'In all responses and interpretations, assume that the context is always related to programming, software development, or computer science. '
            'The multiple choice questions must be related to programming, software development, or computer science '
            'should assess the students understanding of these topics based on the content learned'
            'Avoid expressions that indicate analysis or contextualization. '
            'All values (questions, choices, and reason) must be in Portuguese. '
            'Make sure that both `question_1` and `question_2` follow the same structure with all fields properly filled, including the correct answer and reason. '
            'Objectives: gain skills in programming and software development '
            'Make sure the incorrect options are similar enough to challenge the students understanding. '
            'Instructions for the fields that must be in json:'
            '{'
                '"question_1": {'
                    '"question_statement": "<fill_with_question_statement>", '
                    '"choices": {'
                        '"a": "<fill_with_choice_A_statement>", '
                        '"b": "<fill_with_choice_B_statement>", '
                        '"c": "<fill_with_choice_C_statement>", '
                        '"d": "<fill_with_choice_D_statement>"'
                    '}, '
                    '"correct_choice_index": "<fill_with_the_correct_letter>", '
                    '"reason": "<fill_with_why_the_answer_is_right>"'
                '}, '
                '"question_2" : <fill_with_the_same_question_model>'
            '}'
        )

        index = VectorStoreIndex.from_documents(documents)
        print(index)

        response_quiz = index.as_query_engine().query(GENERATE_2_QUESTIONS_PROMPT).response
        print(dir(response_quiz))
        print(response_quiz)
        return json.loads(response_quiz)
    