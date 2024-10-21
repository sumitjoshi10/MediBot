from src.helper import load_pdf,text_splitter,download_hugging_face_embedding
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

load_dotenv()
KEY = os.getenv("PINECONE_API_KEY")
INDEX = os.getenv("PINECONE_INDEX_NAME")


data_folder = os.path.join(os.getcwd(),"data/")

extracted_data = load_pdf(data_folder)

text_chunks = text_splitter(extracted_data)

embedding = download_hugging_face_embedding()


#Creating Embeddings for Each of The Text Chunks & storing
vectorstore = PineconeVectorStore.from_texts(pinecone_api_key=KEY,
                                             index_name=INDEX,
                                             embedding=embedding,
                                             texts=[text.page_content for text in text_chunks])

