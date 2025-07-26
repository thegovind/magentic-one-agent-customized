# Lumen Magentic-One Agent - Customer Support & Channel Partner Scaling

A customized Magentic-One Agent template specifically designed for Lumen Technologies' customer support and channel partner scaling needs. This agent operates in oneshot mode without MCP Tools or Agent-to-Agent (A2A) capabilities, providing comprehensive support for technology industry partners.

**✨ NEW: Complete Web Frontend Interface Available!** See [Frontend Setup Guide](FRONTEND_SETUP.md) for the web interface.

## 🎯 Overview

This agent is tailored for Lumen's technology industry focus, helping channel partners scale their operations through expert guidance, technical support, and strategic insights. The agent maintains Lumen's brand identity with the signature #3b82f6 primary color theme throughout all interactions.

## 🌐 Web Interface

The complete web frontend provides:
- **Professional UI** with Lumen branding
- **Interactive Query Forms** for different support types
- **Demo Scenarios** with real partner examples
- **Responsive Design** for all devices
- **Real-time Processing** with loading states

**Quick Start Web Interface:**
```bash
pip install -r requirements.txt
python web_app.py
# Visit http://localhost:5000
```

See [FRONTEND_SETUP.md](FRONTEND_SETUP.md) for complete frontend documentation.

## ✨ Key Features

### 🏢 Lumen Brand Integration
- **Primary Color**: #3b82f6 (Lumen Blue)
- **Brand Voice**: Professional, innovative, customer-focused
- **Visual Identity**: Consistent Lumen branding across all responses
- **Company Alignment**: Technology industry specialization

### 🤝 Customer Support Specialization
- **Channel Partner Support**: Comprehensive guidance for Lumen partners
- **Technical Assistance**: Expert troubleshooting and technical guidance
- **Scaling Solutions**: Strategic recommendations for partner growth
- **Product Knowledge**: Deep expertise in Lumen's technology portfolio

### 📈 Channel Partner Scaling Features
- **Multi-tenant Support**: Handle multiple channel partners
- **Partner-specific Customization**: Tailored responses based on partner profile
- **Growth Analytics**: Performance tracking and scaling metrics
- **Onboarding Workflows**: Streamlined partner enablement process

### ⚡ Oneshot Mode Configuration
- **Direct Execution**: Single-shot response generation
- **No MCP Tools**: Simplified operation without Model Context Protocol
- **No A2A**: No Agent-to-Agent orchestration required
- **Immediate Value**: Complete responses in single interactions

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Azure AI Projects access
- Azure credentials configured

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/thegovind/magentic-one-agent-customized.git
   cd magentic-one-agent-customized
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   ```bash
   export PROJECT_ENDPOINT="your-azure-ai-project-endpoint"
   export MODEL_DEPLOYMENT_NAME="gpt-4"  # Optional, defaults to gpt-4
   ```

4. **Run the agent**:
   ```bash
   python magentic_one_agent.py
   ```

## 📋 Configuration

### Environment Variables
- `PROJECT_ENDPOINT`: Your Azure AI Project endpoint (required)
- `MODEL_DEPLOYMENT_NAME`: AI model deployment name (optional, defaults to "gpt-4")

### Lumen Branding Configuration
The agent uses Lumen's brand configuration defined in `config/lumen_branding.py`:

```python
primary_color = "#3b82f6"      # Lumen Blue
company_name = "Lumen Technologies"
industry = "Technology"
tagline = "Enabling amazing things"
```

## 🎯 Use Cases

### 1. Channel Partner Scaling Consultation
```python
agent = MagenticOneAgent()
partner_info = {
    "partner_name": "TechSolutions Inc",
    "partner_tier": "Gold",
    "focus_area": "Cloud Infrastructure",
    "region": "North America"
}

response = agent.get_partner_scaling_recommendations(partner_info)
```

### 2. Technical Support
```python
technical_issue = "Integration challenges with Lumen's SD-WAN solution"
response = agent.handle_technical_support(technical_issue, urgency="high")
```

### 3. General Customer Support
```python
query = "What Lumen solutions are best for small business cloud services?"
response = agent.handle_customer_query(query)
```

## 🏗️ Architecture

### Core Components

1. **MagenticOneAgent**: Main agent class with Lumen customizations
2. **LumenBrandConfig**: Brand identity and theming configuration
3. **CustomerSupportTemplates**: Pre-built templates for common scenarios
4. **Oneshot Mode**: Direct execution without multi-agent orchestration

### File Structure
```
magentic-one-agent-customized/
├── magentic_one_agent.py          # Main agent implementation
├── config/
│   ├── __init__.py
│   └── lumen_branding.py          # Lumen brand configuration
├── templates/
│   ├── __init__.py
│   └── support_templates.py       # Support query templates
├── requirements.txt               # Python dependencies
└── README.md                     # This file
```

## 🎨 Customization

### Brand Theming
Modify `config/lumen_branding.py` to adjust:
- Color schemes
- Brand messaging
- Visual elements
- Company information

### Support Templates
Extend `templates/support_templates.py` to add:
- New query templates
- Industry-specific scenarios
- Custom response formats
- Partner tier variations

### Agent Behavior
Customize `magentic_one_agent.py` to modify:
- Response formatting
- Context enhancement
- Escalation criteria
- Partner profiling

## 🔧 Technical Configuration

### Oneshot Mode Settings
- **MCP Tools**: Disabled (`use_mcp_tools: False`)
- **A2A Communication**: Disabled (`use_a2a: False`)
- **Execution Mode**: Single-shot responses
- **Tool Integration**: None (simplified operation)

### Azure AI Integration
- Uses Azure AI Projects SDK
- Supports GPT-4 and other Azure OpenAI models
- Integrates with Azure identity management
- Scalable cloud-based execution

## 📊 Partner Scaling Features

### Multi-tenant Architecture
- Partner-specific configurations
- Isolated data handling
- Customized response templates
- Tier-based feature access

### Analytics and Reporting
- Partner performance tracking
- Scaling progress metrics
- ROI measurement tools
- Success benchmarking

### Growth Enablement
- Market expansion strategies
- Operational scaling guidance
- Technology roadmap planning
- Resource optimization

## 🛠️ Development

### Adding New Features
1. Extend the `MagenticOneAgent` class
2. Add new templates in `templates/support_templates.py`
3. Update brand configuration if needed
4. Test with sample partner scenarios

### Testing
```bash
# Run the example usage
python magentic_one_agent.py

# Test with custom scenarios
python -c "
from magentic_one_agent import MagenticOneAgent
agent = MagenticOneAgent()
response = agent.handle_customer_query('Your test query here')
print(response)
"
```

## 📈 Success Metrics

### Partner Satisfaction
- Response accuracy and relevance
- Time to resolution
- Partner feedback scores
- Escalation rates

### Scaling Effectiveness
- Partner growth rates
- Revenue expansion
- Market penetration
- Operational efficiency

### Technical Performance
- Response time
- System availability
- Error rates
- Resource utilization

## 🔒 Security & Compliance

### Data Protection
- Partner information encryption
- Secure credential management
- Access control and authentication
- Audit logging

### Compliance
- Industry standard compliance
- Data residency requirements
- Privacy protection
- Regulatory adherence

## 🆘 Support & Troubleshooting

### Common Issues
1. **Authentication Errors**: Verify Azure credentials and PROJECT_ENDPOINT
2. **Model Access**: Ensure proper model deployment permissions
3. **Response Quality**: Check partner context information completeness
4. **Performance**: Monitor Azure resource allocation

### Getting Help
- Review Azure AI Projects documentation
- Check Lumen partner portal resources
- Contact technical support team
- Submit issues via GitHub

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📞 Contact

For questions about this Lumen Magentic-One Agent customization:
- Technical Issues: Submit GitHub issues
- Partner Support: Contact your dedicated partner manager
- General Inquiries: Lumen partner portal

---

**Lumen Technologies** | Empowering Digital Transformation
