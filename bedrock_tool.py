import boto3
import json

def analyze_logs_with_llm(log_text):
    client = boto3.client("bedrock-runtime")

    prompt = f"""
You are a DevOps AI Agent.
Analyze the following logs and:
1. Identify root cause
2. Suggest fix
3. Provide prevention steps

Logs:
{log_text}
"""
    response = client.invoke_model(
        modelId="anthropic.claude-3-sonnet",
        body=json.dumps({
            "prompt": prompt,
            "max_tokens_to_sample": 500
        })
    )
    return response["body"].read().decode()
