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

### API Gateway

Deployed API

* **https://igu65hixj4.execute-api.us-east-1.amazonaws.com/Dev/heytherelambda**

---

## POST Method
