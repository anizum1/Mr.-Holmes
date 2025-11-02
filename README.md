# Mr. Holmes - Advanced OSINT Investigation Tool

```
███╗   ███╗██████╗     ██╗  ██╗ ██████╗ ██╗     ███╗   ███╗███████╗███████╗
████╗ ████║██╔══██╗    ██║  ██║██╔═══██╗██║     ████╗ ████║██╔════╝██╔════╝
██╔████╔██║██████╔╝    ███████║██║   ██║██║     ██╔████╔██║█████╗  ███████╗
██║╚██╔╝██║██╔══██╗    ██╔══██║██║   ██║██║     ██║╚██╔╝██║██╔══╝  ╚════██║
██║ ╚═╝ ██║██║  ██║    ██║  ██║╚██████╔╝███████╗██║ ╚═╝ ██║███████╗███████║
╚═╝     ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝╚══════╝╚══════╝

🔍 "Elementary, my dear Watson. The game is afoot!" 🔎
```

**⚠️ EDUCATIONAL/RESEARCH PURPOSE ONLY**

Mr. Holmes is a powerful Open Source Intelligence (OSINT) investigation tool designed for legitimate research, academic projects, and ethical security analysis. Named after the legendary detective Sherlock Holmes, this tool helps investigators piece together digital clues with precision and thoroughness.

## 🎩 Features

### 🔍 Social Media Intelligence
- ✅ Twitter/X user information lookup
- ✅ Reddit user profile analysis
- ✅ Posting pattern and activity analysis
- ✅ Timeline analysis and timezone estimation
- ✅ Cross-reference multiple accounts

### 📷 Image Forensics
- ✅ EXIF metadata extraction
- ✅ GPS coordinate extraction from images
- ✅ Camera and device information
- ✅ Timestamp analysis from image metadata
- ✅ Download and analyze images from URLs
- ✅ Reverse geocoding integration

### 🌍 Geolocation Intelligence
- ✅ IP address geolocation lookup
- ✅ Reverse geocoding (coordinates to location)
- ✅ Timezone identification
- ✅ ISP and organization information

### 👤 Username Investigation
- ✅ Cross-platform username enumeration (20+ platforms)
- ✅ Account existence verification
- ✅ Social media footprint mapping
- ✅ **Works WITHOUT API keys!**

### 📧 Contact Intelligence
- ✅ Email address analysis and validation
- ✅ Domain information extraction
- ✅ Name extraction from email patterns
- ✅ Phone number analysis and country identification
- ✅ Disposable email detection

### 🔗 URL Analysis
- ✅ URL parameter extraction
- ✅ Tracking parameter identification
- ✅ Shortened URL expansion
- ✅ Domain and path analysis

### 🔐 Cryptographic Analysis
- ✅ Hash type identification (MD5, SHA1, SHA256, etc.)
- ✅ Multiple hash format support

### 📊 Advanced Analytics
- ✅ Activity timeline analysis
- ✅ Posting pattern detection
- ✅ Behavioral analysis
- ✅ Automated report generation
- ✅ Batch processing support
- ✅ Modular architecture for easy extension

## 📋 Prerequisites

- Python 3.8 or higher
- Linux/Unix environment (or WSL on Windows)
- Valid API credentials for social media platforms (optional for some features)

## 🚀 Installation

### Quick Install (Linux)

```bash
# Clone the repository
git clone <your-repo-url>
cd mr-holmes

# Run installation script
chmod +x install.sh
./install.sh

# Activate virtual environment
source osint_env/bin/activate
```

### Manual Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Create config file
python mr_holmes.py
# This creates config.json template

# Add your API credentials to config.json
nano config.json
```

## 🔑 Getting API Credentials

### Twitter/X API
1. Go to https://developer.twitter.com
2. Apply for a developer account
3. Create a new app
4. Get your Bearer Token, API Key, and API Secret

### Reddit API
1. Go to https://www.reddit.com/prefs/apps
2. Create a new application (script type)
3. Note your client_id and client_secret

### Instagram/Facebook (Optional)
1. Go to https://developers.facebook.com
2. Create an app
3. Get Graph API access token
4. Note: Requires business verification for full access

### IP Geolocation API (Free)
1. Go to https://ipgeolocation.io/
2. Sign up for free account
3. Get your API key (free tier: 1000 requests/day)

### OpenCage Geocoding API (Free)
1. Go to https://opencagedata.com/
2. Sign up for free account
3. Get your API key (free tier: 2500 requests/day)

## 📖 Usage

### Quick Start - No API Required!

```bash
# Username enumeration across 20+ platforms (NO API NEEDED!)
python mr_holmes.py username --check johndoe

# This checks: Twitter, Instagram, Facebook, GitHub, Reddit,
# YouTube, TikTok, LinkedIn, Pinterest, Medium, and more!
```

### Social Media Investigation

```bash
# Twitter profile analysis
python mr_holmes.py --twitter-user elonmusk

# Reddit profile with posting pattern analysis
python mr_holmes.py --reddit-user spez --analyze-posts

# Analyze timestamp
python mr_holmes.py --analyze-time "2024-01-15T10:30:00Z"
```

### Image Forensics

```bash
# Extract EXIF from local image
python mr_holmes.py --extract-exif photo.jpg

# Extract EXIF and reverse geocode GPS coordinates
python mr_holmes.py --extract-exif photo.jpg --reverse-geocode

# Analyze image from URL
python mr_holmes.py --image-url https://example.com/image.jpg
```

### Geolocation Tracking

```bash
# IP address lookup
python mr_holmes.py --lookup-ip 8.8.8.8

# Reverse geocode coordinates
python mr_holmes.py --geocode 40.7128 -74.0060
```

### Advanced Investigations

```bash
# Email analysis
python mr_holmes.py email --analyze john.doe@example.com

# Phone number investigation
python mr_holmes.py phone --analyze "+1-555-123-4567"

# URL analysis
python mr_holmes.py url --analyze "https://example.com/page?utm_source=twitter"

# Expand shortened URL
python mr_holmes.py url --expand "https://bit.ly/abc123"

# Hash identification
python mr_holmes.py hash --identify "5d41402abc4b2a76b9719d911017c592"
```

### Full Investigation with Report

```bash
python mr_holmes.py investigate \
    --username johndoe \
    --email john.doe@example.com \
    --phone "+1-555-123-4567" \
    --generate-report
```

## 📁 Project Structure

```
mr-holmes/
├── mr_holmes.py           # Main OSINT tool
├── osint_cli.py          # CLI interface wrapper  
├── advanced_utils.py     # Advanced utilities
├── sherlock_logo.py      # ASCII art and branding
├── batch_analysis.py     # Batch processing script
├── requirements.txt      # Python dependencies
├── config.json           # API credentials (DO NOT COMMIT!)
├── install.sh            # Installation script
├── README.md             # This file
├── USAGE_GUIDE.md        # Detailed usage guide
├── QUICK_REFERENCE.md    # Quick command reference
├── LICENSE               # MIT License
└── .gitignore           # Git ignore file
```

## 🎓 For Academic Projects

This tool is perfect for college final year projects. Here's what makes it stand out:

### ✅ Strengths to Highlight
- **Modular Architecture**: Easy to extend and customize
- **Comprehensive Documentation**: Complete usage guides and examples
- **Ethical Framework**: Built-in ethical guidelines and privacy protection
- **Multiple Data Sources**: Integration with various platforms
- **Real-World Applicable**: Practical use cases in security and research
- **Professional Code**: Well-structured, commented, and maintainable

### 📊 Presentation Tips
1. **Demo username enumeration** - Works immediately without setup
2. **Show image EXIF extraction** - Impressive visual results
3. **Demonstrate report generation** - Professional output
4. **Discuss ethical considerations** - Show responsibility
5. **Explain extensibility** - Future improvements

## ⚖️ Ethical Guidelines

### ✅ DO:
- Use for academic research with proper authorization
- Respect privacy and data protection laws
- Only analyze publicly available information
- Follow platform Terms of Service
- Document your research methodology
- Get informed consent when applicable
- Include proper citations in academic work

### ❌ DON'T:
- Track or stalk individuals
- Violate platform Terms of Service
- Collect data without authorization
- Use for harassment or malicious purposes
- Share private/sensitive information
- Attempt to bypass platform security
- Use for illegal activities

## 📜 Legal Considerations

This tool is designed for educational purposes. Users must:
- ✅ Comply with GDPR, CCPA, and local privacy laws
- ✅ Respect platform Terms of Service
- ✅ Have proper authorization for research
- ✅ Not use for illegal purposes
- ✅ Follow academic/institutional ethics guidelines

## 🔒 Security & Privacy

- **Never commit config.json** to version control
- Keep investigation reports private and secure
- Store sensitive data separately from code
- Use virtual environments for isolation
- Respect rate limits to avoid detection
- Follow responsible disclosure practices

## 📚 Documentation

- **README.md** (this file) - Overview and quick start
- **USAGE_GUIDE.md** - Comprehensive usage instructions
- **QUICK_REFERENCE.md** - Quick command reference
- See examples in `batch_analysis.py` for automation

## 🛠️ Troubleshooting

### Common Issues

**Config file not found:**
```bash
python mr_holmes.py  # Creates template
```

**Module not found:**
```bash
pip install -r requirements.txt
```

**API authentication failed:**
- Verify API keys in config.json
- Check key permissions
- Ensure keys haven't expired

**No results found:**
- Username may not exist
- Check spelling
- Try variations (_, -, no spaces)

**Rate limit exceeded:**
- Wait before retry
- Reduce request frequency
- Check API tier limits

## 🚧 Extending Mr. Holmes

To add a new platform:

1. Create a new class inheriting from `OSINTTool`
2. Implement `search_user()` and `parse_user_data()` methods
3. Add configuration in `create_config_template()`
4. Add command-line argument in `main()`

Example:
```python
class TikTokOSINT(OSINTTool):
    def search_user(self, username: str) -> Optional[Dict]:
        # Implementation
        pass
    
    def parse_user_data(self, data: Dict) -> Dict:
        # Implementation
        pass
```

## 🤝 Contributing

This is an academic project. Contributions are welcome:
1. Fork the repository
2. Create a feature branch
3. Follow ethical guidelines
4. Submit pull request with documentation

## 📄 License

MIT License - See LICENSE file for details

## ⚠️ Disclaimer

This tool is provided for educational and research purposes only. The authors and contributors are not responsible for misuse or any damages caused by this tool. Users are solely responsible for ensuring their use complies with all applicable laws, regulations, and platform Terms of Service.

By using Mr. Holmes, you agree to use it ethically and legally.

## 📞 Contact & Support

For academic inquiries: [Your Email]  
Institution: [Your College Name]  
Project: Final Year Project - OSINT Research

## 🎯 Future Improvements

- [ ] Web-based GUI interface
- [ ] Machine learning for pattern recognition
- [ ] Advanced visualization tools
- [ ] Real-time monitoring capabilities
- [ ] Integration with more platforms
- [ ] Automated threat intelligence
- [ ] Export to multiple formats (PDF, JSON, XML)

## 📖 References

- Twitter API Documentation: https://developer.twitter.com/en/docs
- Reddit API Documentation: https://www.reddit.com/dev/api
- OSINT Framework: https://osintframework.com/
- Sherlock Project: https://github.com/sherlock-project/sherlock

---

```
🔍 "The world is full of obvious things which nobody by any chance ever observes."
                                                          - Sherlock Holmes
```

**Remember**: With great power comes great responsibility. Use Mr. Holmes wisely! 🎩🔍
