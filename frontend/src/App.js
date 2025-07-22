import React, { useState } from 'react';
import {
  Container,
  Paper,
  Typography,
  TextField,
  Button,
  Box,
  Card,
  CardContent,
  Grid,
  Alert,
  CircularProgress,
  Chip,
  AppBar,
  Toolbar
} from '@mui/material';
import {
  Support,
  TrendingUp,
  Business,
  Chat,
  Send
} from '@mui/icons-material';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import axios from 'axios';
import './App.css';

const lumenTheme = createTheme({
  palette: {
    primary: {
      main: '#3b82f6',
      light: '#60a5fa',
      dark: '#1e40af',
    },
    secondary: {
      main: '#f59e0b',
    },
    background: {
      default: '#f8fafc',
      paper: '#ffffff',
    },
  },
  typography: {
    fontFamily: '"Segoe UI", "Roboto", "Helvetica Neue", Arial, sans-serif',
    h3: {
      fontWeight: 700,
    },
    h4: {
      fontWeight: 600,
    },
  },
});

const API_BASE_URL = 'https://lumen-magentic-one-agent-tjfsshob.fly.dev';

function App() {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [activeTab, setActiveTab] = useState('support');

  const handleSubmit = async (endpoint, data) => {
    setLoading(true);
    setError('');
    setResponse('');

    try {
      const result = await axios.post(`${API_BASE_URL}/${endpoint}`, data, {
        headers: {
          'Content-Type': 'application/json',
        },
        timeout: 30000,
      });
      setResponse(result.data.response);
    } catch (err) {
      if (err.code === 'ECONNABORTED') {
        setError('Request timeout. The backend service may be starting up. Please try again in a moment.');
      } else if (err.response) {
        setError(`Error: ${err.response.status} - ${err.response.data?.detail || 'Server error'}`);
      } else if (err.request) {
        setError('Unable to connect to the backend service. The service may be starting up or experiencing issues.');
      } else {
        setError(`Error: ${err.message}`);
      }
    } finally {
      setLoading(false);
    }
  };

  const handleSupportQuery = () => {
    if (!query.trim()) return;
    handleSubmit('query', { query, partner_info: null });
  };

  const handleTechnicalSupport = () => {
    if (!query.trim()) return;
    handleSubmit('technical-support', { 
      technical_issue: query, 
      urgency: 'medium' 
    });
  };

  const handlePartnerScaling = () => {
    if (!query.trim()) return;
    const partnerProfile = {
      partner_name: 'Demo Partner',
      partner_tier: 'Gold',
      focus_area: 'Cloud Infrastructure',
      region: 'North America',
      current_challenge: query
    };
    handleSubmit('partner-scaling', { partner_profile: partnerProfile });
  };

  return (
    <ThemeProvider theme={lumenTheme}>
      <div className="App">
        <AppBar position="static" sx={{ background: 'linear-gradient(135deg, #3b82f6 0%, #1e40af 100%)' }}>
          <Toolbar>
            <Business sx={{ mr: 2 }} />
            <Typography variant="h6" component="div" sx={{ flexGrow: 1, fontWeight: 700 }}>
              Lumen Magentic-One Agent
            </Typography>
            <Chip 
              label="Technology Industry" 
              variant="outlined" 
              sx={{ color: 'white', borderColor: 'white' }}
            />
          </Toolbar>
        </AppBar>

        <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
          <Paper 
            elevation={8} 
            sx={{ 
              p: 4, 
              borderRadius: 3,
              background: 'linear-gradient(145deg, #ffffff 0%, #f8fafc 100%)',
              boxShadow: '0 20px 40px rgba(59, 130, 246, 0.1)'
            }}
          >
            <Box textAlign="center" mb={4}>
              <Typography 
                variant="h3" 
                component="h1" 
                gutterBottom
                sx={{ 
                  background: 'linear-gradient(135deg, #3b82f6 0%, #1e40af 100%)',
                  backgroundClip: 'text',
                  WebkitBackgroundClip: 'text',
                  WebkitTextFillColor: 'transparent',
                  mb: 2
                }}
              >
                Lumen Technologies
              </Typography>
              <Typography variant="h5" color="text.secondary" gutterBottom>
                AI-Powered Customer Support and Channel Partner Scaling
              </Typography>
              <Typography variant="body1" color="text.secondary">
                Oneshot mode | Technology Industry Focus | Channel Partner Optimization
              </Typography>
            </Box>

            <Grid container spacing={3} mb={4}>
              <Grid item xs={12} md={4}>
                <Card 
                  sx={{ 
                    height: '100%',
                    cursor: 'pointer',
                    border: activeTab === 'support' ? '2px solid #3b82f6' : '1px solid #e2e8f0',
                    '&:hover': { boxShadow: '0 8px 25px rgba(59, 130, 246, 0.15)' }
                  }}
                  onClick={() => setActiveTab('support')}
                >
                  <CardContent sx={{ textAlign: 'center', p: 3 }}>
                    <Support sx={{ fontSize: 48, color: '#3b82f6', mb: 2 }} />
                    <Typography variant="h6" gutterBottom>
                      Customer Support
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                      Get expert technical assistance and troubleshooting guidance
                    </Typography>
                  </CardContent>
                </Card>
              </Grid>

              <Grid item xs={12} md={4}>
                <Card 
                  sx={{ 
                    height: '100%',
                    cursor: 'pointer',
                    border: activeTab === 'technical' ? '2px solid #3b82f6' : '1px solid #e2e8f0',
                    '&:hover': { boxShadow: '0 8px 25px rgba(59, 130, 246, 0.15)' }
                  }}
                  onClick={() => setActiveTab('technical')}
                >
                  <CardContent sx={{ textAlign: 'center', p: 3 }}>
                    <Chat sx={{ fontSize: 48, color: '#3b82f6', mb: 2 }} />
                    <Typography variant="h6" gutterBottom>
                      Technical Support
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                      Advanced technical issue resolution and expert guidance
                    </Typography>
                  </CardContent>
                </Card>
              </Grid>

              <Grid item xs={12} md={4}>
                <Card 
                  sx={{ 
                    height: '100%',
                    cursor: 'pointer',
                    border: activeTab === 'scaling' ? '2px solid #3b82f6' : '1px solid #e2e8f0',
                    '&:hover': { boxShadow: '0 8px 25px rgba(59, 130, 246, 0.15)' }
                  }}
                  onClick={() => setActiveTab('scaling')}
                >
                  <CardContent sx={{ textAlign: 'center', p: 3 }}>
                    <TrendingUp sx={{ fontSize: 48, color: '#3b82f6', mb: 2 }} />
                    <Typography variant="h6" gutterBottom>
                      Partner Scaling
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                      Strategic growth recommendations and scaling optimization
                    </Typography>
                  </CardContent>
                </Card>
              </Grid>
            </Grid>

            <Box mb={3}>
              <TextField
                fullWidth
                multiline
                rows={4}
                variant="outlined"
                label={
                  activeTab === 'support' ? 'Describe your support question...' :
                  activeTab === 'technical' ? 'Describe your technical issue...' :
                  'Describe your scaling challenge...'
                }
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                sx={{
                  '& .MuiOutlinedInput-root': {
                    '&:hover fieldset': {
                      borderColor: '#3b82f6',
                    },
                    '&.Mui-focused fieldset': {
                      borderColor: '#3b82f6',
                    },
                  },
                }}
              />
            </Box>

            <Box display="flex" gap={2} mb={3}>
              <Button
                variant="contained"
                size="large"
                startIcon={loading ? <CircularProgress size={20} color="inherit" /> : <Send />}
                onClick={
                  activeTab === 'support' ? handleSupportQuery :
                  activeTab === 'technical' ? handleTechnicalSupport :
                  handlePartnerScaling
                }
                disabled={loading || !query.trim()}
                sx={{
                  background: 'linear-gradient(135deg, #3b82f6 0%, #1e40af 100%)',
                  px: 4,
                  py: 1.5,
                  '&:hover': {
                    background: 'linear-gradient(135deg, #1e40af 0%, #1e3a8a 100%)',
                  }
                }}
              >
                {loading ? 'Processing...' : 
                 activeTab === 'support' ? 'Get Support' :
                 activeTab === 'technical' ? 'Get Technical Help' :
                 'Get Scaling Advice'}
              </Button>
              
              <Button
                variant="outlined"
                size="large"
                onClick={() => {
                  setQuery('');
                  setResponse('');
                  setError('');
                }}
                sx={{
                  borderColor: '#3b82f6',
                  color: '#3b82f6',
                  '&:hover': {
                    borderColor: '#1e40af',
                    backgroundColor: 'rgba(59, 130, 246, 0.04)',
                  }
                }}
              >
                Clear
              </Button>
            </Box>

            {error && (
              <Alert severity="warning" sx={{ mb: 3 }}>
                {error}
              </Alert>
            )}

            {response && (
              <Paper 
                elevation={2} 
                sx={{ 
                  p: 3, 
                  backgroundColor: '#f8fafc',
                  border: '1px solid #e2e8f0',
                  borderRadius: 2
                }}
              >
                <Typography variant="h6" gutterBottom sx={{ color: '#3b82f6', fontWeight: 600 }}>
                  Lumen Agent Response:
                </Typography>
                <Typography variant="body1" sx={{ whiteSpace: 'pre-wrap', lineHeight: 1.6 }}>
                  {response}
                </Typography>
              </Paper>
            )}

            <Box mt={4} textAlign="center">
              <Typography variant="body2" color="text.secondary">
                Powered by Lumen Technologies • Magentic-One Agent • Oneshot Mode
              </Typography>
            </Box>
          </Paper>
        </Container>
      </div>
    </ThemeProvider>
  );
}

export default App;
