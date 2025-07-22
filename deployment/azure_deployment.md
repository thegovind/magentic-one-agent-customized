# Azure Deployment Guide for Lumen Magentic-One Agent

This guide provides step-by-step instructions for deploying the Lumen Magentic-One Agent to Azure.

## Prerequisites

- Azure subscription with AI Services enabled
- Azure CLI installed and configured
- Python 3.8+ environment
- Git repository access

## Deployment Steps

### 1. Azure AI Project Setup

```bash
# Create resource group
az group create --name lumen-agent-rg --location eastus

# Create Azure AI Services resource
az cognitiveservices account create \
  --name lumen-ai-services \
  --resource-group lumen-agent-rg \
  --kind AIServices \
  --sku S0 \
  --location eastus
```

### 2. Azure AI Project Configuration

```bash
# Create AI Project
az ml workspace create \
  --name lumen-agent-project \
  --resource-group lumen-agent-rg \
  --location eastus
```

### 3. Environment Configuration

Create a `.env` file with your Azure configuration:

```bash
PROJECT_ENDPOINT=https://your-project.services.ai.azure.com/api/projects/lumen-agent-project
MODEL_DEPLOYMENT_NAME=gpt-4
AZURE_CLIENT_ID=your-client-id
AZURE_CLIENT_SECRET=your-client-secret
AZURE_TENANT_ID=your-tenant-id
```

### 4. Container Deployment

```dockerfile
# Dockerfile for Azure Container Instances
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["python", "magentic_one_agent.py"]
```

Deploy to Azure Container Instances:

```bash
az container create \
  --resource-group lumen-agent-rg \
  --name lumen-agent-container \
  --image your-registry/lumen-agent:latest \
  --environment-variables \
    PROJECT_ENDPOINT=$PROJECT_ENDPOINT \
    MODEL_DEPLOYMENT_NAME=$MODEL_DEPLOYMENT_NAME \
  --secure-environment-variables \
    AZURE_CLIENT_ID=$AZURE_CLIENT_ID \
    AZURE_CLIENT_SECRET=$AZURE_CLIENT_SECRET \
    AZURE_TENANT_ID=$AZURE_TENANT_ID
```

### 5. Function App Deployment (Alternative)

```bash
# Create Function App
az functionapp create \
  --resource-group lumen-agent-rg \
  --consumption-plan-location eastus \
  --runtime python \
  --runtime-version 3.11 \
  --functions-version 4 \
  --name lumen-agent-function \
  --storage-account lumenagentstg
```

### 6. Monitoring and Logging

```bash
# Enable Application Insights
az monitor app-insights component create \
  --app lumen-agent-insights \
  --location eastus \
  --resource-group lumen-agent-rg
```

## Security Configuration

### 1. Managed Identity

```bash
# Enable system-assigned managed identity
az container update \
  --resource-group lumen-agent-rg \
  --name lumen-agent-container \
  --assign-identity
```

### 2. Key Vault Integration

```bash
# Create Key Vault
az keyvault create \
  --name lumen-agent-vault \
  --resource-group lumen-agent-rg \
  --location eastus

# Store secrets
az keyvault secret set \
  --vault-name lumen-agent-vault \
  --name "project-endpoint" \
  --value "$PROJECT_ENDPOINT"
```

## Scaling Configuration

### Auto-scaling Rules

```bash
# Create auto-scaling profile
az monitor autoscale create \
  --resource-group lumen-agent-rg \
  --resource lumen-agent-container \
  --resource-type Microsoft.ContainerInstance/containerGroups \
  --name lumen-agent-autoscale \
  --min-count 1 \
  --max-count 10 \
  --count 2
```

## Monitoring and Alerts

### Performance Metrics

```bash
# Create performance alert
az monitor metrics alert create \
  --name "High CPU Usage" \
  --resource-group lumen-agent-rg \
  --scopes /subscriptions/{subscription-id}/resourceGroups/lumen-agent-rg/providers/Microsoft.ContainerInstance/containerGroups/lumen-agent-container \
  --condition "avg Percentage CPU > 80" \
  --description "Alert when CPU usage exceeds 80%"
```

## Backup and Recovery

### Data Backup

```bash
# Create backup storage account
az storage account create \
  --name lumenagentbackup \
  --resource-group lumen-agent-rg \
  --location eastus \
  --sku Standard_LRS
```

## Troubleshooting

### Common Issues

1. **Authentication Errors**
   - Verify Azure credentials
   - Check managed identity permissions
   - Validate Key Vault access

2. **Performance Issues**
   - Monitor resource utilization
   - Check auto-scaling configuration
   - Review application logs

3. **Connectivity Problems**
   - Verify network security groups
   - Check firewall rules
   - Validate DNS resolution

### Diagnostic Commands

```bash
# Check container logs
az container logs \
  --resource-group lumen-agent-rg \
  --name lumen-agent-container

# Monitor resource usage
az monitor metrics list \
  --resource /subscriptions/{subscription-id}/resourceGroups/lumen-agent-rg/providers/Microsoft.ContainerInstance/containerGroups/lumen-agent-container \
  --metric "Percentage CPU"
```

## Cost Optimization

### Resource Management

```bash
# Schedule container shutdown
az container stop \
  --resource-group lumen-agent-rg \
  --name lumen-agent-container

# Use spot instances for development
az container create \
  --resource-group lumen-agent-rg \
  --name lumen-agent-dev \
  --image your-registry/lumen-agent:latest \
  --priority Spot
```

## Maintenance

### Updates and Patches

```bash
# Update container image
az container create \
  --resource-group lumen-agent-rg \
  --name lumen-agent-container \
  --image your-registry/lumen-agent:latest \
  --restart-policy Always
```

### Health Checks

```bash
# Configure health probe
az container create \
  --resource-group lumen-agent-rg \
  --name lumen-agent-container \
  --image your-registry/lumen-agent:latest \
  --restart-policy Always \
  --probe-type liveness \
  --probe-path /health \
  --probe-port 8000
```

## Production Checklist

- [ ] Azure AI Services configured
- [ ] Container registry setup
- [ ] Environment variables configured
- [ ] Managed identity enabled
- [ ] Key Vault integration complete
- [ ] Monitoring and alerts configured
- [ ] Auto-scaling rules defined
- [ ] Backup strategy implemented
- [ ] Security policies applied
- [ ] Performance testing completed

## Support

For deployment issues:
- Check Azure documentation
- Review container logs
- Contact Azure support
- Submit GitHub issues for template-specific problems
