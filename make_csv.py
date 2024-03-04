from openai import OpenAI
from langchain_community.document_loaders import PyPDFLoader
import pandas as pd

def extract_pdf_text(file_path):
    loader = PyPDFLoader(file_path)
    pages = loader.load_and_split()
    return pages

client = OpenAI(
    # This is the default and can be omitted
    api_key='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',
)

# openai.api_key ='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'
 
def get_chat_completion(prompt, model="gpt-3.5-turbo"):
  
   # Creating a message as required by the API
   messages = [{"role": "user", "content": prompt}]
  
   # Calling the ChatCompletion API
   response = client.chat.completions.create(
       model=model,
       messages=messages,
       temperature=0.5,
   )

   # Returning the extracted response
   return response.choices[0].message.content

# def main():
#     pgs = extract_pdf_text(r"C:\Users\akuma\VSCode\blooms\QP\SocialScience-SQP.pdf")
#     questions =[]
#     df = pd.DataFrame(columns=['Questions'])
#     for s in pgs:
#         response = get_chat_completion("'"+str(s) + "'\n\nAbove given is the extract of a question paper. List all the questions in the extract. no need to list the options along with the questions")
#         questions.append(response.split('\n'))

#     print(questions)
    
#     for question in questions:
#             df2 = pd.DataFrame({'Questions': question})
#             df = pd.concat([df,df2],ignore_index = True)
    
    
#     df.to_csv('questions.csv',index=False)



# if __name__ == "__main__":
#     main()
def extract_questions_from_pdf(pdf_file_path):
    pgs = extract_pdf_text(pdf_file_path)
    questions = []
    for s in pgs:
        response = get_chat_completion("'" + str(s) + "'\n\nAbove given is the extract of a question paper. List all the questions in the extract. no need to list the options along with the questions")
        questions.extend(response.split('\n'))
    return questions

if __name__ == "__main__":
    questions = extract_questions_from_pdf(r"C:\Users\akuma\VSCode\blooms\QP\SocialScience-SQP.pdf")
    print(questions)


