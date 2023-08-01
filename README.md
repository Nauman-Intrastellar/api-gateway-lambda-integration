# API Gateway and Lambda Integration

## Architecture Diagram

![API Gateway and Lambda Integration](architecture-diagram/api-gateway-lambda-integration.png)

---

## GET Method

### Lambda Function

lambda_function.py

```py
import json

def lambda_handler(event, context):
    return "Hey There!, Welcome."
```

### API Gateway - GET Method

Deployed API

[https://igu65hixj4.execute-api.us-east-1.amazonaws.com/Dev/heytherelambda](https://igu65hixj4.execute-api.us-east-1.amazonaws.com/Dev/heytherelambda)

---

## POST Method

### Lambda Function

lambda_function.py

```py
import json

def lambda_handler(event, context):
    print(event)
    return 'Hi There, ' + event['Name']
```

### API Gateway - Post Method

Deployed API

[https://cidp9rf265.execute-api.us-east-1.amazonaws.com/Dev/api-lambda-post-resource](https://cidp9rf265.execute-api.us-east-1.amazonaws.com/Dev/api-lambda-post-resource)

---
