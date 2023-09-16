
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download()


# This code yields a lot of ModuleNotFoundError, so install packages accordingly

from langchain.document_loaders import UnstructuredPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

loader = UnstructuredPDFLoader("sample.pdf")
data = loader.load()

#print(len(data[0].page_content))

text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 0)
texts = text_splitter.split_documents(data)
# len(texts)
# texts[1]

from langchain.vectorstores import Chroma, Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone


OPENAI_API_KEY = "OPENAI_API_KEY"
PINECONE_API_ENV = 'PINECONE_API_ENV'
PINECONE_API_KEY = 'PINECONE_API_KEY'

embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

pinecone.init(
    api_key=PINECONE_API_KEY,
    environment=PINECONE_API_ENV
)
index_name = 'top-teacher'
docsearch = Pinecone.from_texts([t.page_content for t in texts], embeddings, index_name=index_name)

query = "여기에 질문 입력"
docs = docsearch.similarity_search(query)

from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
llm = OpenAI(temperature = 0, openai_api_key = OPENAI_API_KEY, model_name="gpt-3.5-turbo-16k")
chain = load_qa_chain(llm, chain_type ="stuff")

chain.run(input_documents = docs, question = query)
