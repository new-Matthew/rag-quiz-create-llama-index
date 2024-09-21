from llama_index.core import VectorStoreIndex
import json

class Index:

    def index_documents(documents):

        GENERATE_2_QUESTIONS_PROMPT = (
            'Its only role is to generate 2 questions, in json format, based on the content of the uploaded files. '
            'Both the values of the statement, the alternatives and explanations of the answers must be in Portuguese. '
            'Instructions for the fields that must be in json:'
            '{'
                '"question_1": {'
                    '"question_statement": "<fill_with_question_statement>", '
                    '"alternatives": {'
                        '"a": "<fill_with_alternative_A_statement>", '
                        '"b": "<fill_with_alternative_B_statement>", '
                        '"c": "<fill_with_alternative_C_statement>", '
                        '"d": "<fill_with_alternative_D_statement>"'
                    '}, '
                    '"correct_alternative_index": "<fill_with_the_letter_of_the_correct_alternative>", '
                    '"explanation": "<fill_with_explanation_of_why_the_answer_is_this>"'
                '}, '
                '"question_2": {'
                    '"question_statement": "<fill_with_question_statement>", '
                    '"alternatives": {'
                        '"a": "<fill_with_alternative_A_statement>", '
                        '"b": "<fill_with_alternative_B_statement>", '
                        '"c": "<fill_with_alternative_C_statement>", '
                        '"d": "<fill_with_alternative_D_statement>"'
                    '}, '
                    '"correct_alternative_index": "<fill_with_the_letter_of_the_correct_alternative>", '
                    '"explanation": "<fill_with_explanation_of_why_the_answer_is_this>"'
                '}'
            '}'
        )

        index = VectorStoreIndex.from_documents(documents)

        response_quiz = index.as_query_engine().query(GENERATE_2_QUESTIONS_PROMPT).response
        print(response_quiz)
        return json.loads(response_quiz)
        

        
        