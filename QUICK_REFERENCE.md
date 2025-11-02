# Mr. Holmes - Quick Reference Card

```
🔍 "Elementary, my dear Watson!" 🔎
```

## Installation
```bash
chmod +x install.sh
./install.sh
source osint_env/bin/activate
```

## Configuration
```bash
python mr_holmes.py  # Shows help & creates config.json
nano config.json     # Add API keys
```

## Most Common Commands

### 🔎 Username Investigation (NO API NEEDED!)
```bash
# Check 20+ platforms instantly
python mr_holmes.py username --check USERNAME

# Twitter profile
python mr_holmes.py --twitter-user USERNAME

# Reddit profile  
python mr_holmes.py --reddit-user USERNAME
```

### 📧 Contact Intelligence
```bash
# Email analysis
python mr_holmes.py email --analyze EMAIL@DOMAIN.COM

# Phone investigation
python mr_holmes.py phone --analyze "+1-555-1234"
```

### 📷 Image Forensics
```bash
# Extract EXIF
python mr_holmes.py --extract-exif image.jpg

# With GPS reverse lookup
python mr_holmes.py --extract-exif image.jpg --reverse-geocode

# From URL
python mr_holmes.py --image-url https://example.com/img.jpg
```

### 🌍 Geolocation Tracking
```bash
# IP lookup
python mr_holmes.py --lookup-ip 8.8.8.8

# Coordinates
python mr_holmes.py --geocode 40.7128 -74.0060
```

### 🕵️ Full Investigation
```bash
python mr_holmes.py investigate \
    --username USER \
    --email EMAIL \
    --generate-report
```

## File Structure
```
mr_holmes.py       → Main entry point
osint_tool.py      → Social media tool
osint_cli.py       → CLI interface
advanced_utils.py  → Additional utilities
sherlock_logo.py   → ASCII art
config.json        → API credentials (DON'T COMMIT!)
```

## API Keys Needed (Get Free)
- **Twitter**: developer.twitter.com
- **Reddit**: reddit.com/prefs/apps
- **IP Geo**: ipgeolocation.io (1K/day free)
- **Geocoding**: opencagedata.com (2.5K/day free)

## Common Options
```
--analyze-posts       # Pattern analysis
--reverse-geocode     # GPS to location
--generate-report     # Save results
```

## Output Files
```
investigation_*.txt   # Text reports
batch_report_*.json   # JSON data
temp_image.jpg        # Downloaded images
```

## Tips
1. Always activate venv first: `source osint_env/bin/activate`
2. Check .gitignore before committing
3. Respect rate limits (wait between requests)
4. Save results regularly
5. Document your methodology

## Help Commands
```bash
python3 osint_cli.py --help
python3 osint_tool.py --help
```

## Emergency Troubleshooting
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall

# Recreate config
rm config.json
python3 osint_tool.py

# Check Python version (need 3.8+)
python3 --version
```

## For Your Project Report
**Remember to include:**
- Ethical considerations section
- API limitations discussion
- Privacy protection measures
- Legal compliance notes
- Use case examples
- Future improvements
- References and citations

## Rate Limits (Free Tiers)
| Service | Limit |
|---------|-------|
| Twitter | 300/15min |
| Reddit | 60/min |
| IP Geo | 1000/day |
| OpenCage | 2500/day |

## Security Reminders
- ✅ config.json in .gitignore
- ✅ Use virtual environment
- ✅ Keep reports private
- ✅ Don't share API keys
- ❌ Don't commit sensitive data

---
**Tool:** Mr. Holmes OSINT Investigation Tool
**Motto:** "Elementary, my dear Watson!"
**Version:** 2.0
**Purpose:** Educational/Research

🔍 The game is afoot! 🔎
