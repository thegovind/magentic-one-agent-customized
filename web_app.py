#!/usr/bin/env python3
"""
Flask web application for the Lumen Magentic-One Agent frontend.
Provides a user-friendly web interface for interacting with the agent.
"""

import os
import json
from flask import Flask, render_template, request, jsonify, redirect, url_for

# Try to import the agent, fallback to demo mode if dependencies not available
try:
    from magentic_one_agent import MagenticOneAgent
    AGENT_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Agent dependencies not available: {e}")
    AGENT_AVAILABLE = False
    MagenticOneAgent = None

from config.lumen_branding import LumenBrandConfig

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'lumen-agent-dev-key')

# Initialize configurations
brand_config = LumenBrandConfig()
agent = None

def get_agent():
    """Get or create agent instance."""
    global agent
    if not AGENT_AVAILABLE:
        return None
    if agent is None:
        try:
            agent = MagenticOneAgent()
        except ValueError as e:
            # If Azure credentials not configured, return None
            print(f"Warning: Could not initialize agent: {e}")
            return None
    return agent

@app.route('/')
def index():
    """Main landing page."""
    return render_template('index.html', brand_config=brand_config)

@app.route('/query')
def query_page():
    """Query submission page."""
    return render_template('query.html', brand_config=brand_config)

@app.route('/api/query', methods=['POST'])
def handle_query():
    """API endpoint to handle agent queries."""
    try:
        data = request.json
        query_text = data.get('query', '').strip()
        query_type = data.get('query_type', 'general')
        partner_info = data.get('partner_info', {})
        
        if not query_text:
            return jsonify({'error': 'Query text is required'}), 400
        
        # Get agent instance
        agent_instance = get_agent()
        if not agent_instance:
            # Return a demo response if agent not available
            return jsonify({
                'response': f"""
{brand_config.get_header()}

Thank you for your query about: "{query_text}"

**Demo Mode Active** - Azure credentials not configured.

This is a demonstration of how the Lumen Magentic-One Agent would respond to your query. In a production environment with proper Azure AI configuration, you would receive:

• Comprehensive analysis of your query
• Specific recommendations for your partner profile
• Technical guidance and best practices
• Scaling strategies and growth opportunities
• Direct access to Lumen's technology expertise

Query Type: {query_type.title()}
Partner Information: {partner_info.get('partner_name', 'Not specified')}

{brand_config.get_footer()}
                """.strip(),
                'demo_mode': True
            })
        
        # Handle different query types
        if query_type == 'scaling':
            response = agent_instance.get_partner_scaling_recommendations(partner_info)
        elif query_type == 'technical':
            urgency = data.get('urgency', 'medium')
            response = agent_instance.handle_technical_support(query_text, urgency)
        else:
            response = agent_instance.handle_customer_query(query_text, partner_info)
        
        return jsonify({'response': response, 'demo_mode': False})
        
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

@app.route('/api/partner-info', methods=['POST'])
def save_partner_info():
    """API endpoint to save partner information."""
    try:
        partner_info = request.json
        # In a real application, this would save to a database
        # For demo purposes, we just return success
        return jsonify({'success': True, 'message': 'Partner information saved successfully'})
    except Exception as e:
        return jsonify({'error': f'Failed to save partner info: {str(e)}'}), 500

@app.route('/demo')
def demo_page():
    """Demo scenarios page."""
    return render_template('demo.html', brand_config=brand_config)

@app.route('/about')
def about_page():
    """About page with agent information."""
    return render_template('about.html', brand_config=brand_config)

@app.errorhandler(404)
def not_found(error):
    """404 error handler."""
    return render_template('error.html', 
                         error_code=404, 
                         error_message="Page not found",
                         brand_config=brand_config), 404

@app.errorhandler(500)
def internal_error(error):
    """500 error handler."""
    return render_template('error.html', 
                         error_code=500, 
                         error_message="Internal server error",
                         brand_config=brand_config), 500

if __name__ == '__main__':
    print("🚀 Starting Lumen Magentic-One Agent Web Interface")
    print("=" * 60)
    print(f"Brand: {brand_config.company_name}")
    print(f"Primary Color: {brand_config.primary_color}")
    print("=" * 60)
    
    # Check if agent can be initialized
    if AGENT_AVAILABLE:
        test_agent = get_agent()
        if test_agent:
            print("✅ Azure AI agent initialized successfully")
        else:
            print("⚠️  Running in demo mode - Azure credentials not configured")
            print("   Set PROJECT_ENDPOINT environment variable for full functionality")
    else:
        print("⚠️  Running in demo mode - Azure AI dependencies not installed")
        print("   Install azure-ai-projects and azure-ai-agents for full functionality")
    
    print("🌐 Starting web server...")
    app.run(host='0.0.0.0', port=5000, debug=True)