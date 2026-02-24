import boto3

def send_alert(topic_arn, message):
    client = boto3.client("sns")
    client.publish(
        TopicArn=topic_arn,
        Message=message,
        Subject="AI DevOps Alert"
    )
