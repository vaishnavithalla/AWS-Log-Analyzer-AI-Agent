from agents.log_analyzer_agent import run_agent

if __name__ == "__main__":
    log_group = "/aws/lambda/my-app"
    result = run_agent(log_group)
    print("\n=== AI INCIDENT REPORT ===\n")
    print(result)
