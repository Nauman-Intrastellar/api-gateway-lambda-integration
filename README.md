# API Gateway and Lambda Integration

## Architecture Diagram

![API Gateway and Lambda Integration](architecture-diagram/api-gateway-lambda-integration.png)

---

lambda_function.py

```py
import json

def lambda_handler(event, context):
    return "Hey There!, Welcome."
```
