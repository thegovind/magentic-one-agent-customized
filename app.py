from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, Any
import os
import uvicorn
from magentic_one_agent import MagenticOneAgent
from config.lumen_branding import LumenBrandConfig

app = FastAPI(
    title="Lumen Magentic-One Agent API",
    description="Lumen-customized Magentic-One Agent for customer support and channel partner scaling",
    version="1.0.0"
)

brand_config = LumenBrandConfig()

class QueryRequest(BaseModel):
    query: str
    partner_info: Optional[Dict[str, Any]] = None

class TechnicalSupportRequest(BaseModel):
    technical_issue: str
    urgency: str = "medium"

class PartnerScalingRequest(BaseModel):
    partner_profile: Dict[str, Any]

class AgentResponse(BaseModel):
    response: str
    status: str = "success"

@app.get("/")
async def root():
    """Root endpoint with Lumen branding."""
    return {
        "message": "Lumen Magentic-One Agent API",
        "company": brand_config.company_name,
        "industry": brand_config.industry,
        "primary_color": brand_config.primary_color,
        "tagline": brand_config.tagline,
        "version": "1.0.0",
        "mode": "oneshot",
        "features": [
            "Customer Support Specialization",
            "Channel Partner Scaling",
            "Lumen Brand Integration",
            "Technology Industry Focus"
        ]
    }

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "lumen-magentic-one-agent"}

@app.post("/query", response_model=AgentResponse)
async def handle_query(request: QueryRequest):
    """Handle general customer support queries."""
    try:
        agent = MagenticOneAgent()
        response = agent.handle_customer_query(request.query, request.partner_info)
        agent.cleanup()
        
        return AgentResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")

@app.post("/technical-support", response_model=AgentResponse)
async def handle_technical_support(request: TechnicalSupportRequest):
    """Handle technical support requests."""
    try:
        agent = MagenticOneAgent()
        response = agent.handle_technical_support(request.technical_issue, request.urgency)
        agent.cleanup()
        
        return AgentResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing technical support: {str(e)}")

@app.post("/partner-scaling", response_model=AgentResponse)
async def handle_partner_scaling(request: PartnerScalingRequest):
    """Handle partner scaling recommendations."""
    try:
        agent = MagenticOneAgent()
        response = agent.get_partner_scaling_recommendations(request.partner_profile)
        agent.cleanup()
        
        return AgentResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing scaling request: {str(e)}")

@app.get("/branding")
async def get_branding():
    """Get Lumen branding configuration."""
    return {
        "color_scheme": brand_config.get_color_scheme(),
        "brand_identity": brand_config.get_brand_identity(),
        "css_variables": brand_config.get_css_variables()
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=False)
