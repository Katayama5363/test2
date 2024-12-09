import boto3
import json

def lambda_handler(event, context):
    modelId = "anthropic.claude-3-haiku-20240307-v1:0"


    message = event['queryStringParameters']['message']
    sp = """
   AWSのサービス名を記載するので、そのサービスの解説をお願いします。
   IT未経験の人でもわかるように噛み砕いた説明をして下さい。
   またITの専門用語が出てくる場合は、その用語の解説も簡単にいれてください。
    """

    bedrock = boto3.client('bedrock-runtime',region_name="us-east-1")
    body = json.dumps(
        {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 4000,
            "system": sp,
            "messages": [{"role": "user","content": message}]
        }   
    )
    
    # Bedrockの呼び出し
    response = bedrock.invoke_model(body=body,modelId=modelId)
    
    # Bedrock呼出し結果の抽出
    response_body = json.loads(response.get('body').read())
    answer = response_body["content"][0]["text"]

    # 結果の出力
    print(answer)

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',  
        },
        'body': answer
    }
