# Lumen Magentic-One Agent - Frontend Setup Guide

## 🎯 Overview

This guide explains how to set up and run the frontend web interface for the Lumen Magentic-One Agent. The frontend provides a professional, branded user experience for interacting with the AI agent through a modern web interface.

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### 1. Install Dependencies

```bash
# Install required packages
pip install -r requirements.txt
```

### 2. Run the Web Application

```bash
# Start the Flask development server
python web_app.py
```

The web interface will be available at:
- **Local**: http://127.0.0.1:5000
- **Network**: http://0.0.0.0:5000

## 📁 Frontend Architecture

```
magentic-one-agent-customized/
├── web_app.py                  # Flask web application
├── templates/                  # HTML templates
│   ├── base.html              # Base template with navigation
│   ├── index.html             # Homepage
│   ├── query.html             # Query interface
│   ├── demo.html              # Demo scenarios
│   ├── about.html             # About page
│   └── error.html             # Error pages
├── static/                    # Static assets
│   ├── css/
│   │   └── style.css          # Lumen-branded CSS
│   └── js/
│       ├── main.js            # Common JavaScript
│       └── query.js           # Query page functionality
└── requirements.txt           # Python dependencies
```

## 🎨 Features

### Homepage (`/`)
- Modern landing page with Lumen branding
- Feature highlights and statistics
- Call-to-action buttons to engage users

### Query Interface (`/query`)
- Interactive form with multiple query types:
  - **General Inquiry**: Basic questions
  - **Partner Scaling**: Growth strategies
  - **Technical Support**: Priority-based assistance
  - **Partner Onboarding**: New partner guidance
- Partner information collection
- Real-time query processing

### Demo Scenarios (`/demo`)
- Pre-built partner scenarios:
  - Cloud Infrastructure Partner (Gold Tier)
  - Network Services Partner (Platinum Tier)
  - Security Solutions Partner (Silver Tier)
  - Managed Services Partner (Standard Tier)
- One-click scenario testing

### About Page (`/about`)
- Comprehensive agent information
- Technical specifications
- System architecture overview
- Success metrics and support contact

## 🔧 Configuration

### Environment Variables

The frontend supports both production mode (with Azure AI) and demo mode:

```bash
# For production with Azure AI
export PROJECT_ENDPOINT="https://your-project.services.ai.azure.com/api/projects/your-project-name"
export MODEL_DEPLOYMENT_NAME="gpt-4"  # Optional

# For demo mode (no configuration needed)
# The application will automatically run in demo mode if Azure dependencies are not available
```

### Demo Mode

The frontend automatically runs in demo mode when:
- Azure AI dependencies are not installed
- `PROJECT_ENDPOINT` environment variable is not set
- Azure credentials are not configured

Demo mode features:
- Full UI functionality
- Sample responses with Lumen branding
- "Demo Mode" indicator in responses
- All interactive features working

## 🎯 Query Types

### 1. General Inquiry
Basic questions about Lumen solutions, partnerships, or general support needs.

**Example**: "What Lumen solutions are best for small business cloud services?"

### 2. Partner Scaling
Strategic recommendations for business growth, market expansion, and operational scaling.

**Example**: "Help us scale our cloud infrastructure services for the SMB market."

### 3. Technical Support
Priority-based technical assistance with urgency levels:
- Low: General inquiry
- Medium: Standard priority (default)
- High: Business impact
- Critical: Service disruption

**Example**: "SD-WAN connectivity issues affecting business-critical applications."

### 4. Partner Onboarding
New partner guidance, training resources, and program information.

**Example**: "We're a new partner specializing in managed services. What should we prioritize?"

## 🎨 Lumen Branding

The frontend implements consistent Lumen Technologies branding:

- **Primary Color**: `#3b82f6` (Lumen Blue)
- **Typography**: Professional, clean fonts
- **Brand Voice**: Innovative, customer-focused
- **Logo**: "LUMEN - Enabling amazing things"

## 🔒 Security Features

- Input validation and sanitization
- CSRF protection via Flask's built-in security
- Error handling with user-friendly messages
- No sensitive data logging in demo mode

## 📱 Responsive Design

The frontend is fully responsive and works on:
- Desktop computers
- Tablets
- Mobile phones
- Different screen orientations

## 🛠️ Development

### File Structure
- `web_app.py`: Main Flask application with routes and API endpoints
- `templates/`: Jinja2 HTML templates with inheritance
- `static/css/style.css`: Comprehensive CSS with Lumen branding
- `static/js/`: Interactive JavaScript functionality

### Adding New Features

1. **New Pages**: Create HTML template in `templates/` and add route in `web_app.py`
2. **New Styling**: Add CSS rules in `static/css/style.css`
3. **New Interactions**: Add JavaScript in `static/js/`

### API Endpoints

- `POST /api/query`: Submit queries to the agent
- `POST /api/partner-info`: Save partner information
- Error handling: 404, 500 with branded error pages

## 🧪 Testing

### Manual Testing
1. Visit each page and verify layout
2. Test query submission with different types
3. Verify responsive design on different screen sizes
4. Test error scenarios (invalid input, network issues)

### Browser Compatibility
- Modern browsers (Chrome, Firefox, Safari, Edge)
- JavaScript enabled
- CSS Grid and Flexbox support

## 📊 Performance

- Optimized CSS and JavaScript
- Minimal external dependencies
- Fast page loading
- Responsive API endpoints

## 🆘 Troubleshooting

### Common Issues

**Web server won't start**
```bash
# Check if port 5000 is available
lsof -i :5000

# Use different port
export FLASK_RUN_PORT=8000
python web_app.py
```

**Templates not loading**
- Ensure `templates/` directory exists in the same folder as `web_app.py`
- Check file permissions

**Static files not serving**
- Ensure `static/` directory exists
- Verify CSS and JS file paths

**Agent not responding**
- Check if running in demo mode (expected behavior)
- Verify Azure credentials if using production mode

### Debug Mode

For development, Flask debug mode is enabled by default:
- Automatic reloading on file changes
- Detailed error messages
- Interactive debugger

## 🚀 Production Deployment

For production deployment:

1. **Disable debug mode** in `web_app.py`:
   ```python
   app.run(host='0.0.0.0', port=5000, debug=False)
   ```

2. **Use production WSGI server**:
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 web_app:app
   ```

3. **Configure environment variables**:
   ```bash
   export PROJECT_ENDPOINT="your-production-endpoint"
   export FLASK_SECRET_KEY="your-secret-key"
   ```

4. **Set up reverse proxy** (nginx/Apache) for static file serving

## 📞 Support

- **Technical Issues**: Submit GitHub issues
- **Feature Requests**: Create pull requests
- **General Questions**: Contact Lumen partner support

---

**Lumen Technologies** | Empowering Digital Transformation