import os

# SNS topic ARN
SNS_TOPIC_ARN = os.getenv("SNS_TOPIC_ARN", "arn:aws:sns:ap-south-1:123456789012:ai-agent-alerts")
