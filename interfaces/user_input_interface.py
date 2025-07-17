from query_interpreter import interpret_query

def get_user_input():
    while True:
        user_input = input("Enter your query: ")
        if user_input.lower() == "exit":
            break

        results = interpret_query(user_input)

        print("Query Results: ")

        for row in results:
            print(row)

if __name__ == "__main__":
    get_user_input()