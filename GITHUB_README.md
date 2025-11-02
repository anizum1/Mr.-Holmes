🔍 Mr. Holmes - Advanced OSINT Investigation Tool
<div align="center">
```
███╗   ███╗██████╗     ██╗  ██╗ ██████╗ ██╗     ███╗   ███╗███████╗███████╗
████╗ ████║██╔══██╗    ██║  ██║██╔═══██╗██║     ████╗ ████║██╔════╝██╔════╝
██╔████╔██║██████╔╝    ███████║██║   ██║██║     ██╔████╔██║█████╗  ███████╗
██║╚██╔╝██║██╔══██╗    ██╔══██║██║   ██║██║     ██║╚██╔╝██║██╔══╝  ╚════██║
██║ ╚═╝ ██║██║  ██║    ██║  ██║╚██████╔╝███████╗██║ ╚═╝ ██║███████╗███████║
╚═╝     ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝╚══════╝╚══════╝
```
"Elementary, my dear Watson. The game is afoot!"
Show Image
Show Image
Show Image
Show Image
A powerful Open Source Intelligence (OSINT) investigation framework inspired by Sherlock Holmes
Features • Installation • Usage • Documentation • Contributing
</div>

🎯 What is Mr. Holmes?
Mr. Holmes is a comprehensive OSINT investigation tool designed for security researchers, investigators, journalists, and academic researchers. Named after the legendary detective, this tool helps piece together digital clues with precision and thoroughness.
🌟 Why Mr. Holmes?

✅ Easy to Use - Intuitive CLI interface with helpful prompts
✅ No Setup Required - Username enumeration works immediately without API keys
✅ Comprehensive - 8+ investigation modules covering social media, images, locations, and more
✅ Professional - Generate detailed reports suitable for academic or professional use
✅ Extensible - Modular architecture makes adding new features simple
✅ Ethical - Built-in guidelines and privacy protection
✅ Well-Documented - Extensive guides and examples included

🚀 Features
<table>
<tr>
<td width="50%">
🕵️ Social Media Intelligence

Twitter/X profile analysis
Reddit user investigation
Posting pattern detection
Timeline analysis
Timezone estimation

📷 Image Forensics

EXIF metadata extraction
GPS coordinate recovery
Camera/device identification
Timestamp analysis
Remote image analysis

</td>
<td width="50%">
🌍 Geolocation

IP address tracking
Reverse geocoding
Location intelligence
ISP identification
Timezone mapping

👤 Identity Intelligence

Cross-platform username search (20+ platforms)
Email analysis & validation
Phone number investigation
Name extraction
Disposable email detection

</td>
</tr>
</table>
🔐 Additional Capabilities

URL Analysis - Track parameters, expand shortened URLs
Hash Identification - Identify MD5, SHA1, SHA256, and more
Batch Processing - Investigate multiple targets simultaneously
Report Generation - Professional documentation output
Pattern Recognition - Behavioral analysis and predictions

🎬 Quick Demo
bash# Instantly check if username exists on 20+ platforms - NO API REQUIRED!
$ python mr_holmes.py username --check johndoe

🔍 Elementary! Beginning username investigation...
─────────────────────────────────────────────────────────
✅ Found         | twitter        | https://twitter.com/johndoe
✅ Found         | github         | https://github.com/johndoe
✅ Found         | reddit         | https://reddit.com/user/johndoe
❌ Not found     | instagram      | https://instagram.com/johndoe
─────────────────────────────────────────────────────────
📊 Summary: Found on 3/20 platforms
💻 Quick Start
Installation (60 seconds)
bash# Clone the repository
git clone https://github.com/yourusername/mr-holmes.git
cd mr-holmes

# Run automatic installation
chmod +x install.sh
./install.sh

# Activate environment
source osint_env/bin/activate
First Investigation
bash# Start investigating immediately - no setup needed!
python mr_holmes.py username --check johndoe

# Or get help
python mr_holmes.py --help
📖 Usage Examples
🔍 Social Media Investigation
bash# Analyze Twitter profile
python mr_holmes.py --twitter-user elonmusk

# Analyze Reddit user with posting patterns
python mr_holmes.py --reddit-user spez --analyze-posts
📷 Image Analysis
bash# Extract location from photo
python mr_holmes.py --extract-exif vacation_photo.jpg --reverse-geocode

# Analyze image from URL
python mr_holmes.py --image-url https://example.com/suspicious_image.jpg
🌍 Geolocation
bash# Track IP address
python mr_holmes.py --lookup-ip 8.8.8.8

# Find location from coordinates
python mr_holmes.py --geocode 40.7128 -74.0060
📧 Contact Intelligence
bash# Analyze email address
python mr_holmes.py email --analyze suspicious@example.com

# Investigate phone number
python mr_holmes.py phone --analyze "+1-555-123-4567"
🕵️ Full Investigation
bash# Comprehensive investigation with automated report
python mr_holmes.py investigate \
    --username johndoe \
    --email john@example.com \
    --phone "+1-555-1234" \
    --generate-report
📚 Documentation

Complete Guide - Comprehensive usage instructions
Quick Reference - Command cheat sheet
API Setup - How to get API keys
Examples - Sample automation scripts

🛠️ Configuration
Some features require API keys (free tiers available):
bash# Create configuration file
python mr_holmes.py

# Edit with your API keys
nano config.json
Free API Sources:

Twitter Developer - Social media data
Reddit Apps - Reddit access
IP Geolocation - 1000 requests/day free
OpenCage - 2500 requests/day free

🎓 Perfect for Academic Projects
Mr. Holmes is ideal for final year projects, research, and cybersecurity courses:
✨ Advantages

Complete Documentation - Ready for project reports
Ethical Framework - Shows responsible development
Real-World Application - Practical security tool
Extensible Design - Easy to add new features
Professional Output - Generate impressive reports

📊 Project Highlights
python# Lines of code: ~2500+
# Modules: 8+
# Supported platforms: 20+
# Features: 25+
# Documentation pages: 4
⚖️ Ethical Use
Mr. Holmes is designed for authorized and ethical use only:
✅ Appropriate Uses

Academic research and education
Authorized security testing
Journalism and fact-checking
Personal account verification
OSINT training and learning

❌ Prohibited Uses

Stalking or harassment
Unauthorized surveillance
Doxxing or privacy invasion
Illegal activities
Terms of Service violations

🤝 Contributing
Contributions are welcome! Here's how:

Fork the repository
Create a feature branch (git checkout -b feature/AmazingFeature)
Commit changes (git commit -m 'Add AmazingFeature')
Push to branch (git push origin feature/AmazingFeature)
Open a Pull Request

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.
🙏 Acknowledgments

Inspired by Sherlock Project
Built with Python and various open-source libraries
Created for educational and research purposes
Thanks to the OSINT community

📞 Support & Contact

🐛 Report Issues: GitHub Issues
💬 Discussions: GitHub Discussions
📧 Email: zanzorofel@proton.me

🗺️ Roadmap

 Web-based GUI interface
 Machine learning pattern detection
 Real-time monitoring
 Advanced visualization
 Mobile app
 Docker containerization
 Cloud deployment option

⭐ Star History
If you find Mr. Holmes useful, please star this repository!

<div align="center">
🔍 "The world is full of obvious things which nobody observes." 🔎
Made with ❤️ for the OSINT community
⬆ Back to Top
</div>
