from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings


# Loading the pdf file
def load_pdf(data_dir):
    loader = DirectoryLoader(data_dir,
                             glob="*.pdf",
                             loader_cls=PyPDFLoader)
    
    documents = loader.load()
    return documents


#Create the Text Chunks
def text_splitter(extracted_data):
    splitted_text = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 20)
    text_chunks = splitted_text.split_documents(extracted_data)
    
    return text_chunks


#download Embedding Model
def download_hugging_face_embedding():
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embedding