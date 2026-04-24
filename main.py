from agent.parser import generate_steps

if __name__ == "__main__":
    description = input("Enter test description:\n")

    result = generate_steps(description)

    print("\nGenerated Steps:\n")
    print(result)