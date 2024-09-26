from llama_index.core import VectorStoreIndex
import json

class Index:

    def index_documents(documents):

        EXTRACT_CONTEXT_PROMPT = (
            "Assume that the context is always related to programming, software development, or computer science. "
            "Given the content of the following documents, summarize the key technical topics and expand with additional information "
            ""
        )

        index = VectorStoreIndex.from_documents(documents)

 
        context_response = index.as_query_engine(temperature=0.5).query(EXTRACT_CONTEXT_PROMPT).response
        print(context_response)

  
        GENERATE_2_QUESTIONS_PROMPT = (
            f"Assume that the context is always related to programming, software development, or computer science. "
            "Based on the following content: {context_response}, generate 2 multiple-choice questions in Portuguese, in JSON format. "
            "Each question should be technical and designed to test understanding in programming or computer science. "
            "Provide: "
            "1. A question statement "
            "2. Four answer alternatives (a, b, c, d), ensuring only one correct answer "
            "3. The index of the correct alternative (a, b, c, or d) "
            "4. A brief explanation of why the selected answer is correct."
            "The JSON format should be as follows: "
            "{"
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

        # Step 4: Query again to generate the quiz based on the relevant content
        quiz_response = index.as_query_engine(temperature=0.2).query(GENERATE_2_QUESTIONS_PROMPT).response

        return json.loads(quiz_response)
        

        
        