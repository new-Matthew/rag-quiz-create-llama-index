from llama_index.core import VectorStoreIndex
import json

class Index:

    def index_documents(documents):

        EXTRACT_CONTEXT_PROMPT = (
            "Assume that the context is always related to programming, software development, or computer science. "
            "Given the content of the following documents, summarize the key technical topics and expand with additional information "
            "Given the contents of the following documents, which describe a software system or a business scenario involving software"
            "summarize the key technical topics and generate additional relevant programming-related information "
            "that would help in understanding how to design, implement, or improve the described system."
            "For the duration of this conversation, always assume that the context is programming-related, specifically software development and coding."
            "Even if I use terms that could have multiple meanings (like 'object,' 'method,' 'state,' or 'inheritance'), interpret them as they relate to programming, particularly class, objects."
            "continue with response"
        )

        index = VectorStoreIndex.from_documents(documents)

 
        context_response = index.as_query_engine(temperature=0.9).query(EXTRACT_CONTEXT_PROMPT).response
        print(context_response)
        print(documents)

  
        GENERATE_4_QUESTIONS_PROMPT = (
            'In all responses and interpretations, assume that the context is always related to programming, software development, or computer science.'
            'The questions must be related to programming, software development, or computer science, and should assess the students understanding of these topics based on the content learned'
            'Based on the following content: {context_response}, generate 4 questions in Portuguese, in JSON format. '
            'Both the values of the statement, the choices and reasons of the answers must be in Portuguese. '
            'Make sure that both `question_1` `question_2` `question_3` `question_4` follow the same structure with all fields properly filled, including the correct answer and reasoning. '
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

        # Step 4: Query again to generate the quiz based on the relevant content
        quiz_response = index.as_query_engine(temperature=0.3).query(GENERATE_4_QUESTIONS_PROMPT).response
        print(documents)
        return json.loads(quiz_response)
        

        
        