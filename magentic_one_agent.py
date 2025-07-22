import time
import json
import os
from azure.ai.projects import AIProjectClient
from azure.ai.agents import AgentClient
from azure.ai.agents.models import MessageTextContent, ListSortOrder
from azure.identity import DefaultAzureCredential
from config.lumen_branding import LumenBrandConfig
from templates.support_templates import CustomerSupportTemplates

class MagenticOneAgent:
    """
    Lumen-customized Magentic-One Agent for customer support and channel partner scaling.
    Configured for oneshot mode without MCP Tools or A2A capabilities.
    """
    
    def __init__(self):
        self.brand_config = LumenBrandConfig()
        self.support_templates = CustomerSupportTemplates()
        self.project_endpoint = os.environ.get("PROJECT_ENDPOINT")
        self.model_deployment_name = os.environ.get("MODEL_DEPLOYMENT_NAME", "gpt-4")
        
        if not self.project_endpoint:
            raise ValueError("PROJECT_ENDPOINT environment variable is required")
        
        self.project_client = AIProjectClient(
            endpoint=self.project_endpoint,
            credential=DefaultAzureCredential()
        )
        
        self.agent_client = self.project_client.agents
        self.agent = None
        self.thread = None
        
    def initialize_agent(self):
        """Initialize the Lumen customer support agent with oneshot configuration."""
        
        instructions = f"""
        You are a specialized customer support agent for Lumen, a leading technology company.
        
        BRAND IDENTITY:
        - Company: Lumen Technologies
        - Industry: Technology/Telecommunications
        - Primary Color: {self.brand_config.primary_color}
        - Brand Voice: Professional, helpful, solution-oriented
        
        CORE MISSION:
        You help Lumen's channel partners scale their operations by providing expert guidance,
        technical support, and strategic insights for technology solutions.
        
        OPERATING MODE: ONESHOT
        - Provide complete, comprehensive responses in a single interaction
        - Do not use multi-agent orchestration or MCP tools
        - Focus on delivering immediate value and actionable solutions
        
        CUSTOMER SUPPORT SPECIALIZATION:
        1. Channel Partner Support: Help partners understand Lumen's technology offerings
        2. Technical Guidance: Provide detailed technical assistance and troubleshooting
        3. Scaling Solutions: Recommend strategies for partner growth and efficiency
        4. Product Knowledge: Deep expertise in Lumen's technology portfolio
        
        RESPONSE GUIDELINES:
        - Always maintain Lumen's professional brand voice
        - Provide specific, actionable recommendations
        - Include relevant technical details when appropriate
        - Offer escalation paths for complex issues
        - Focus on partner success and scaling opportunities
        
        ESCALATION CRITERIA:
        - Complex technical issues requiring engineering team involvement
        - Contract or pricing discussions
        - Strategic partnership opportunities
        - Issues requiring executive attention
        
        Remember: You represent Lumen's commitment to partner success and technological excellence.
        """
        
        self.agent = self.agent_client.create_agent(
            model=self.model_deployment_name,
            name="lumen-customer-support-agent",
            instructions=instructions,
            tools=[],
            tool_resources=None
        )
        
        print(f"Created Lumen customer support agent with ID: {self.agent.id}")
        return self.agent
    
    def create_support_session(self):
        """Create a new customer support session thread."""
        self.thread = self.agent_client.threads.create()
        print(f"Created support session thread with ID: {self.thread.id}")
        return self.thread
    
    def handle_customer_query(self, query: str, partner_info: dict = None):
        """
        Handle a customer support query in oneshot mode.
        
        Args:
            query: The customer's question or issue
            partner_info: Optional partner context information
        """
        if not self.agent:
            self.initialize_agent()
        
        if not self.thread:
            self.create_support_session()
        
        enhanced_query = self._enhance_query_with_context(query, partner_info)
        
        message = self.agent_client.threads.messages.create(
            thread_id=self.thread.id,
            role="user",
            content=enhanced_query
        )
        
        run = self.agent_client.threads.runs.create_and_poll(
            thread_id=self.thread.id,
            assistant_id=self.agent.id
        )
        
        print(f"Run completed with status: {run.status}")
        
        if run.status == "completed":
            messages = self.agent_client.threads.messages.list(
                thread_id=self.thread.id,
                order=ListSortOrder.DESC
            )
            
            for message in messages.data:
                if message.role == "assistant":
                    for content_item in message.content:
                        if isinstance(content_item, MessageTextContent):
                            return self._format_response(content_item.text.value)
        
        return "I apologize, but I encountered an issue processing your request. Please try again or contact our support team for assistance."
    
    def _enhance_query_with_context(self, query: str, partner_info: dict = None):
        """Enhance the query with partner context and Lumen-specific information."""
        context_parts = [f"Customer Query: {query}"]
        
        if partner_info:
            context_parts.append("Partner Context:")
            if partner_info.get("partner_name"):
                context_parts.append(f"- Partner: {partner_info['partner_name']}")
            if partner_info.get("partner_tier"):
                context_parts.append(f"- Tier: {partner_info['partner_tier']}")
            if partner_info.get("focus_area"):
                context_parts.append(f"- Focus Area: {partner_info['focus_area']}")
            if partner_info.get("region"):
                context_parts.append(f"- Region: {partner_info['region']}")
        
        context_parts.append("\nPlease provide a comprehensive response that addresses the query while considering Lumen's technology offerings and the partner's scaling needs.")
        
        return "\n".join(context_parts)
    
    def _format_response(self, response_text: str):
        """Format the response with Lumen branding and structure."""
        formatted_response = f"""
{self.brand_config.get_header()}

{response_text}

{self.brand_config.get_footer()}
        """.strip()
        
        return formatted_response
    
    def get_partner_scaling_recommendations(self, partner_profile: dict):
        """Provide specific scaling recommendations for channel partners."""
        scaling_query = self.support_templates.get_scaling_template(partner_profile)
        return self.handle_customer_query(scaling_query, partner_profile)
    
    def handle_technical_support(self, technical_issue: str, urgency: str = "medium"):
        """Handle technical support requests with appropriate urgency."""
        tech_query = self.support_templates.get_technical_template(technical_issue, urgency)
        return self.handle_customer_query(tech_query)
    
    def cleanup(self):
        """Clean up resources."""
        if hasattr(self, 'project_client'):
            self.project_client.close()

def main():
    """Example usage of the Lumen Magentic-One Agent."""
    agent = MagenticOneAgent()
    
    try:
        partner_info = {
            "partner_name": "TechSolutions Inc",
            "partner_tier": "Gold",
            "focus_area": "Cloud Infrastructure",
            "region": "North America"
        }
        
        query = "We're looking to expand our cloud services offering to small businesses. What Lumen solutions would be best for this market segment, and how can we scale our operations efficiently?"
        
        print("Lumen Customer Support Agent - Processing Query...")
        print("=" * 60)
        
        response = agent.handle_customer_query(query, partner_info)
        print(response)
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        agent.cleanup()

if __name__ == "__main__":
    main()
