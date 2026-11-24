from backend import run_travel_agent

user_input = input("Enter travel request: ")

result = run_travel_agent(user_input)

print(result["answer"])
