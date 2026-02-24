from strands import Agent, Tool
from tools.cloudwatch_tool import fetch_logs
from tools.bedrock_tool import analyze_logs_with_llm
from tools.sns_tool import send_alert
from config.settings import SNS_TOPIC_ARN

cloudwatch_tool = Tool(
    name="cloudwatch_fetcher",
    func=fetch_logs,
    description="Fetches logs from CloudWatch log group"
)

llm_tool = Tool(
    name="log_analyzer",
    func=analyze_logs_with_llm,
    description="Analyzes logs and returns root cause + fix"
)

alert_tool = Tool(
    name="sns_alert",
    func=lambda msg: send_alert(SNS_TOPIC_ARN, msg),
    description="Sends alert via SNS"
)

agent = Agent(
    name="DevOpsLogAnalyzer",
    tools=[cloudwatch_tool, llm_tool, alert_tool],
    instructions="Fetch logs, analyze with LLM, and send actionable recommendations."
)

def run_agent(log_group):
    result = agent.run(log_group)
    alert_tool.run(result)
    return result
