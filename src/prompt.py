from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from store_index import get_vector_document
from langchain.chains import RetrievalQA
import os



prompt_template="""
Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""

vector_document = get_vector_document()


PROMPT=PromptTemplate(template=prompt_template, input_variables=["context", "question"])

chain_type_kwargs={"prompt": PROMPT}

model_name = "llama-2-7b-chat.ggmlv3.q4_0.bin"
model_path =os.path.join(os.getcwd(),"model/",model_name)

llm=CTransformers(model=model_path,
                  model_type="llama",
                  config={'max_new_tokens':512,
                          'temperature':0.8})

qa=RetrievalQA.from_chain_type(
    llm=llm, 
    chain_type="stuff", 
    retriever=vector_document.as_retriever(search_kwargs={'k': 2}),
    return_source_documents=True, 
    chain_type_kwargs=chain_type_kwargs)