from agent.parser import generate_steps
from runner.playwright_runner import run_steps

if __name__ == "__main__":
    description = input("Enter test description:\n")

    steps = generate_steps(description)

    print("\nGenerated Steps:\n", steps)

    success = run_steps(steps)

    if success:
        print("\n✅ Test Passed")
    else:
        print("\n❌ Test Failed")