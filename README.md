# AWS-Log-Analyzer-AI-Agent

AWS Log Analyzer AI Agent 🚀

**Description**: An AI-powered DevOps agent that fetches CloudWatch logs, analyzes them using AWS Bedrock LLMs, and optionally sends alerts via SNS.

## Features
- Real-time log analysis
- Root cause identification
- Actionable recommendations
- Optional automated remediation
- Cloud-native, modular, production-ready

## Setup

```bash
# Create virtual environment
python -m venv venv
.\venv\Scripts\Activate  # Windows PowerShell
source venv/bin/activate  # Linux/macOS

# Install dependencies
pip install -r requirements.txt

# Configure AWS credentials
aws configure
