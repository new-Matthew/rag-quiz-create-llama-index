from infra.loader_pdf import Loader
from infra.pdf_url import url_list
from infra.index_documents import Index


class GenerateQuiz:

    def generate_quiz():

        quiz_response = []

        for count in range(len(url_list)):
            pdf_loader = Loader.loader(url_list[count])
            quiz_response.append(Index.index_documents(pdf_loader))

        return quiz_response



