
---

# 3️⃣ tools/cloudwatch_tool.py

```python
import boto3

def fetch_logs(log_group, limit=20):
    client = boto3.client("logs")
    response = client.filter_log_events(
        logGroupName=log_group,
        limit=limit
    )
    logs = [event["message"] for event in response["events"]]
    return "\n".join(logs)
