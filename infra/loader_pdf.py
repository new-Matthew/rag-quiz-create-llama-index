from llama_index.readers.remote_depth import RemoteDepthReader

class Loader:

    def loader(url_list):

        pdf_loader = RemoteDepthReader()
        documents = pdf_loader.load_data(url=url_list)
        return documents  
