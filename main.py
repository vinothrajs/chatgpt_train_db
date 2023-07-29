from langchain import OpenAI, SQLDatabase, SQLDatabaseChain

    
def generate_query():
    # OpenAI Key
    API_KEY = "sk-xxxxx"

    # Connect to postgresql
    db = SQLDatabase.from_uri(
        f"postgresql+psycopg2://root:admin@localhost:54320/erp",
    )
    # setup llm
    llm = OpenAI(model_name="gpt-3.5-turbo-16k",temperature=0, openai_api_key=API_KEY)
    
    # Setup the database chain
    db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True)
    
    # Create db chain
    QUERY = """
    Given an input question, first create a syntactically correct postgresql query to run, then look at the results of the query and return the answer.
    Use the following format:

    Question: Question here
    SQLQuery: SQL Query to run
    SQLResult: Result of the SQLQuery
    Answer: Final answer here

    {question}
    """
    print("Type 'exit' to quit")

    while True:
        prompt = input("Enter a prompt: ")

        if prompt.lower() == 'exit':
            print('Exiting...')
            break
        else:
            try:
                question = QUERY.format(question=prompt)
                print(db_chain.run(question))
            except Exception as e:
                print(e)
    
if __name__ == "__main__":
    generate_query();