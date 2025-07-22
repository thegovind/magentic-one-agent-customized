class CustomerSupportTemplates:
    """Pre-built templates for common customer support scenarios."""
    
    def __init__(self):
        self.scaling_templates = {
            "cloud_infrastructure": "How can we help partners scale their cloud infrastructure offerings?",
            "network_services": "What network services solutions support rapid partner growth?",
            "security_solutions": "How can partners expand their security services portfolio?",
            "managed_services": "What managed services opportunities exist for scaling partners?"
        }
        
        self.technical_templates = {
            "connectivity": "Technical guidance for connectivity solutions",
            "integration": "Integration support and best practices",
            "troubleshooting": "Troubleshooting technical issues",
            "configuration": "Configuration assistance and optimization"
        }
    
    def get_scaling_template(self, partner_profile: dict):
        """Generate a scaling-focused query template."""
        partner_name = partner_profile.get("partner_name", "Partner")
        focus_area = partner_profile.get("focus_area", "technology solutions")
        partner_tier = partner_profile.get("partner_tier", "Standard")
        region = partner_profile.get("region", "their region")
        
        template = f"""
PARTNER SCALING CONSULTATION REQUEST

Partner Information:
- Name: {partner_name}
- Tier: {partner_tier}
- Focus Area: {focus_area}
- Region: {region}

Request: Please provide comprehensive scaling recommendations including:

1. GROWTH OPPORTUNITIES
   - Market expansion strategies for {focus_area}
   - New service offerings that align with current capabilities
   - Revenue growth potential and timelines

2. OPERATIONAL SCALING
   - Infrastructure requirements for growth
   - Staffing and training recommendations
   - Process optimization strategies

3. LUMEN SOLUTION ALIGNMENT
   - Specific Lumen products/services that support scaling
   - Partnership program benefits for {partner_tier} tier
   - Technical resources and support available

4. IMPLEMENTATION ROADMAP
   - 90-day quick wins
   - 6-month strategic initiatives
   - 12-month transformation goals

5. SUCCESS METRICS
   - KPIs to track scaling progress
   - Benchmarks for {focus_area} in {region}
   - ROI expectations and measurement

Please provide specific, actionable recommendations tailored to this partner's profile and scaling objectives.
        """.strip()
        
        return template
    
    def get_technical_template(self, technical_issue: str, urgency: str = "medium"):
        """Generate a technical support query template."""
        urgency_context = {
            "low": "Standard technical inquiry - no immediate business impact",
            "medium": "Moderate priority - affecting some operations",
            "high": "High priority - significant business impact",
            "critical": "Critical issue - major service disruption"
        }
        
        context = urgency_context.get(urgency, urgency_context["medium"])
        
        template = f"""
TECHNICAL SUPPORT REQUEST

Issue Description: {technical_issue}
Priority Level: {urgency.upper()}
Context: {context}

Please provide:

1. IMMEDIATE ASSESSMENT
   - Root cause analysis
   - Impact assessment
   - Immediate mitigation steps

2. TECHNICAL SOLUTION
   - Step-by-step resolution process
   - Required tools and resources
   - Estimated resolution time

3. PREVENTION STRATEGIES
   - Best practices to prevent recurrence
   - Monitoring and alerting recommendations
   - Maintenance schedules

4. ESCALATION PATH
   - When to escalate to engineering
   - Required information for escalation
   - Emergency contact procedures

5. FOLLOW-UP ACTIONS
   - Post-resolution verification steps
   - Documentation requirements
   - Knowledge base updates

Please provide detailed technical guidance appropriate for the urgency level.
        """.strip()
        
        return template
    
    def get_product_inquiry_template(self, product_category: str, use_case: str):
        """Generate a product inquiry template."""
        template = f"""
PRODUCT CONSULTATION REQUEST

Product Category: {product_category}
Use Case: {use_case}

Please provide comprehensive product guidance including:

1. SOLUTION OVERVIEW
   - Relevant Lumen products for {product_category}
   - Key features and capabilities
   - Competitive advantages

2. USE CASE ALIGNMENT
   - How solutions address {use_case}
   - Implementation considerations
   - Integration requirements

3. BUSINESS VALUE
   - ROI potential and metrics
   - Cost-benefit analysis
   - Time to value expectations

4. TECHNICAL SPECIFICATIONS
   - System requirements
   - Performance characteristics
   - Scalability considerations

5. PARTNER ENABLEMENT
   - Training and certification requirements
   - Sales tools and resources
   - Marketing support available

6. NEXT STEPS
   - Evaluation process
   - Pilot program opportunities
   - Implementation timeline

Please provide detailed product information tailored to this specific use case.
        """.strip()
        
        return template
    
    def get_onboarding_template(self, partner_type: str, business_focus: str):
        """Generate a partner onboarding template."""
        template = f"""
PARTNER ONBOARDING CONSULTATION

Partner Type: {partner_type}
Business Focus: {business_focus}

Please provide comprehensive onboarding guidance including:

1. PARTNERSHIP OVERVIEW
   - Lumen partner program benefits
   - Tier progression opportunities
   - Program requirements and commitments

2. BUSINESS ENABLEMENT
   - Go-to-market strategies for {business_focus}
   - Sales process and methodologies
   - Customer targeting and segmentation

3. TECHNICAL ENABLEMENT
   - Product training requirements
   - Certification pathways
   - Technical resources and documentation

4. OPERATIONAL SETUP
   - Partner portal access and navigation
   - Order management processes
   - Support and escalation procedures

5. MARKETING SUPPORT
   - Co-marketing opportunities
   - Lead generation programs
   - Brand guidelines and assets

6. SUCCESS PLANNING
   - 30-60-90 day milestones
   - Performance metrics and tracking
   - Regular review and optimization

Please provide a detailed onboarding roadmap for this partner profile.
        """.strip()
        
        return template
