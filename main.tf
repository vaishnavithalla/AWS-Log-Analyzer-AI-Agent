provider "aws" {
  region = "ap-south-1"
}

resource "aws_sns_topic" "alerts" {
  name = "ai-agent-alerts"
}

resource "aws_lambda_function" "auto_remediate" {
  filename         = "lambda.zip"
  function_name    = "AutoRemediate"
  handler          = "lambda_function.lambda_handler"
  runtime          = "python3.10"
  role             = aws_iam_role.lambda_exec.arn
}

resource "aws_iam_role" "lambda_exec" {
  name = "lambda_exec_role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Action    = "sts:AssumeRole"
      Effect    = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
    }]
  })
}

output "sns_topic_arn" {
  value = aws_sns_topic.alerts.arn
}
