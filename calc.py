print("Calculator started. Type 'quit' to exit.")

while True:
    age = input("\nHow old are you? ")
    
    if age.lower() == "quit":
        print("Goodbye!")
        break
    
    age = int(age)
    
    print("\n--- Age check ---")
    if age >= 60:
        print("You're a senior Citizen! Respect.")
    elif age >= 18:
        print("You're an adult in Kenya. You can vote!")
    else:
        print("You're still a youth. Keep coding")
    
    print("Thanks for using calculator!")
