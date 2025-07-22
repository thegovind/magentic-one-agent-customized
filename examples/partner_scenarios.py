"""
Example scenarios demonstrating the Lumen Magentic-One Agent capabilities
for different channel partner use cases.
"""

from magentic_one_agent import MagenticOneAgent

def demo_cloud_infrastructure_partner():
    """Demo scenario for a cloud infrastructure partner looking to scale."""
    print("🌩️  CLOUD INFRASTRUCTURE PARTNER SCALING DEMO")
    print("=" * 60)
    
    agent = MagenticOneAgent()
    
    partner_info = {
        "partner_name": "CloudTech Solutions",
        "partner_tier": "Gold",
        "focus_area": "Cloud Infrastructure",
        "region": "North America"
    }
    
    query = """
    We're a Gold-tier partner specializing in cloud infrastructure. Our current 
    customer base is primarily mid-market companies, but we want to expand into 
    enterprise accounts. What Lumen solutions and strategies would help us scale 
    our operations and win larger deals?
    """
    
    try:
        response = agent.handle_customer_query(query, partner_info)
        print(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        agent.cleanup()

def demo_network_services_partner():
    """Demo scenario for a network services partner with technical issues."""
    print("\n🌐 NETWORK SERVICES PARTNER TECHNICAL SUPPORT DEMO")
    print("=" * 60)
    
    agent = MagenticOneAgent()
    
    partner_info = {
        "partner_name": "NetConnect Pro",
        "partner_tier": "Platinum",
        "focus_area": "Network Services",
        "region": "Europe"
    }
    
    technical_issue = """
    We're experiencing intermittent connectivity issues with our SD-WAN 
    deployment for a major client. The issues seem to occur during peak 
    traffic hours and are affecting business-critical applications. 
    We need immediate guidance on troubleshooting and resolution.
    """
    
    try:
        response = agent.handle_technical_support(technical_issue, urgency="high")
        print(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        agent.cleanup()

def demo_security_solutions_partner():
    """Demo scenario for a security solutions partner seeking growth opportunities."""
    print("\n🔒 SECURITY SOLUTIONS PARTNER GROWTH DEMO")
    print("=" * 60)
    
    agent = MagenticOneAgent()
    
    partner_info = {
        "partner_name": "SecureEdge Technologies",
        "partner_tier": "Silver",
        "focus_area": "Security Solutions",
        "region": "Asia Pacific"
    }
    
    query = """
    As a Silver-tier security partner, we're looking to expand our cybersecurity 
    offerings. We currently focus on endpoint protection but want to move into 
    network security and threat intelligence. What Lumen security solutions 
    would complement our existing portfolio, and how can we position ourselves 
    for rapid growth in the APAC market?
    """
    
    try:
        response = agent.handle_customer_query(query, partner_info)
        print(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        agent.cleanup()

def demo_managed_services_partner():
    """Demo scenario for a managed services partner onboarding."""
    print("\n🛠️  MANAGED SERVICES PARTNER ONBOARDING DEMO")
    print("=" * 60)
    
    agent = MagenticOneAgent()
    
    partner_info = {
        "partner_name": "TotalCare MSP",
        "partner_tier": "Standard",
        "focus_area": "Managed Services",
        "region": "North America"
    }
    
    query = """
    We're a new Standard-tier partner specializing in managed services for 
    small and medium businesses. We're just getting started with Lumen and 
    need guidance on the best way to onboard, what training we should prioritize, 
    and how to quickly start generating revenue with Lumen solutions.
    """
    
    try:
        response = agent.handle_customer_query(query, partner_info)
        print(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        agent.cleanup()

def demo_scaling_recommendations():
    """Demo the dedicated scaling recommendations feature."""
    print("\n📈 DEDICATED SCALING RECOMMENDATIONS DEMO")
    print("=" * 60)
    
    agent = MagenticOneAgent()
    
    partner_profile = {
        "partner_name": "Innovation Networks",
        "partner_tier": "Gold",
        "focus_area": "Hybrid Cloud Solutions",
        "region": "North America",
        "current_revenue": "$2M annually",
        "target_growth": "50% in 12 months",
        "customer_segments": ["Mid-market", "Enterprise"]
    }
    
    try:
        response = agent.get_partner_scaling_recommendations(partner_profile)
        print(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        agent.cleanup()

if __name__ == "__main__":
    print("🚀 LUMEN MAGENTIC-ONE AGENT - PARTNER SCENARIO DEMOS")
    print("=" * 70)
    print("Demonstrating various channel partner use cases and scaling scenarios")
    print("=" * 70)
    
    demo_cloud_infrastructure_partner()
    demo_network_services_partner()
    demo_security_solutions_partner()
    demo_managed_services_partner()
    demo_scaling_recommendations()
    
    print("\n✅ All demo scenarios completed!")
    print("For more information, see the README.md file.")
