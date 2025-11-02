# OSINT Tool - Complete Usage Guide

## Table of Contents
1. [Getting Started](#getting-started)
2. [Basic Commands](#basic-commands)
3. [Advanced Features](#advanced-features)
4. [Real-World Scenarios](#real-world-scenarios)
5. [Tips and Best Practices](#tips-and-best-practices)

## Getting Started

### First Run
```bash
# Activate virtual environment
source osint_env/bin/activate

# Create config template
python3 osint_tool.py

# Edit config.json with your API keys
nano config.json
```

### Verify Installation
```bash
# Check help menu
python3 osint_cli.py --help

# Test with username check (no API needed)
python3 osint_cli.py username --check test_user
```

## Basic Commands

### 1. Username Enumeration
Check if a username exists across 20+ platforms:

```bash
# Basic check
python3 osint_cli.py username --check johndoe

# Results show:
# ✅ Found - Platform exists
# ❌ Not found - No account with that username
# ⚠️ Timeout - Check manually
```

**Platforms checked:**
- Twitter, Instagram, Facebook, GitHub
- Reddit, YouTube, TikTok, LinkedIn
- Pinterest, Medium, Twitch, Snapchat
- Telegram, Discord, Patreon, Spotify
- Vimeo, Behance, Dribbble, SoundCloud

### 2. Social Media Profile Analysis

**Twitter Analysis:**
```bash
# Basic profile
python3 osint_tool.py --twitter-user username

# With posting pattern analysis
python3 osint_tool.py --twitter-user username --analyze-posts
```

**Reddit Analysis:**
```bash
# Basic profile
python3 osint_tool.py --reddit-user username

# With posting pattern analysis
python3 osint_tool.py --reddit-user username --analyze-posts
```

**Output includes:**
- Account creation date
- Follower/karma counts
- Bio/description
- Location (if provided)
- Verification status
- Posting patterns (time, frequency)
- Estimated timezone

### 3. Email Analysis
```bash
python3 osint_cli.py email --analyze john.doe@example.com
```

**Extracts:**
- Username from email
- Domain information
- Possible real names
- Email hashes (MD5, SHA256)
- Disposable email detection
- Common provider identification

### 4. Phone Number Analysis
```bash
python3 osint_cli.py phone --analyze "+1-555-123-4567"
```

**Identifies:**
- Country code
- Country name
- Number length
- Formatted number

### 5. Image Analysis

**Extract EXIF data:**
```bash
# Local image
python3 osint_tool.py --extract-exif photo.jpg

# Image from URL
python3 osint_tool.py --image-url https://example.com/image.jpg
```

**EXIF data includes:**
- GPS coordinates (if available)
- Camera make and model
- Timestamp
- Image dimensions
- Software used
- Google Maps link (for GPS data)

**Reverse geocode GPS coordinates:**
```bash
python3 osint_tool.py --extract-exif photo.jpg --reverse-geocode
```

### 6. Geolocation

**IP Address Lookup:**
```bash
python3 osint_tool.py --lookup-ip 8.8.8.8
```

**Reverse Geocoding:**
```bash
python3 osint_tool.py --geocode 40.7128 -74.0060
```

**Output:**
- Country, city, region
- Coordinates
- Timezone
- ISP information
- Organization

### 7. URL Analysis
```bash
# Analyze URL
python3 osint_cli.py url --analyze "https://example.com/page?utm_source=twitter"

# Expand shortened URL
python3 osint_cli.py url --expand "https://bit.ly/abc123"
```

**Extracts:**
- Domain and path
- Query parameters
- Tracking parameters (utm, fbclid, etc.)
- Shortened URL detection

### 8. Hash Identification
```bash
python3 osint_cli.py hash --identify "5d41402abc4b2a76b9719d911017c592"
```

Identifies: MD5, SHA1, SHA256, SHA512, NTLM, MySQL hashes

## Advanced Features

### Full Investigation
Combine multiple techniques for comprehensive analysis:

```bash
python3 osint_cli.py investigate \
    --username johndoe \
    --email john.doe@example.com \
    --phone "+1-555-123-4567" \
    --generate-report
```

**Generates:**
- Text report with all findings
- Timestamp-named file
- Organized by analysis type

### Batch Analysis
Analyze multiple targets at once:

```bash
# Edit batch_analysis.py with your targets
nano batch_analysis.py

# Run batch analysis
python3 batch_analysis.py
```

**Outputs:**
- Text report
- JSON file for further processing

### Posting Pattern Analysis
Identify activity patterns and potential timezone:

```bash
python3 osint_tool.py --twitter-user username --analyze-posts
```

**Reveals:**
- Most active hours (UTC)
- Most active days
- Activity distribution
- Estimated timezone
- Long gaps in activity

## Real-World Scenarios

### Scenario 1: Verifying Identity
**Goal:** Verify if an online profile is legitimate

```bash
# 1. Check username across platforms
python3 osint_cli.py username --check suspected_user

# 2. Analyze each found platform
python3 osint_tool.py --twitter-user suspected_user
python3 osint_tool.py --reddit-user suspected_user

# 3. Compare information consistency
# - Creation dates
# - Bio/descriptions
# - Posted locations
```

### Scenario 2: Photo Verification
**Goal:** Verify where a photo was taken

```bash
# 1. Extract EXIF data
python3 osint_tool.py --extract-exif suspicious_photo.jpg --reverse-geocode

# 2. Check GPS coordinates
# 3. Verify timestamp with claimed location
# 4. Check camera metadata for consistency
```

### Scenario 3: Cybersecurity Investigation
**Goal:** Track down source of malicious activity

```bash
# 1. Analyze IP address
python3 osint_tool.py --lookup-ip 192.168.1.1

# 2. Check associated email
python3 osint_cli.py email --analyze attacker@example.com

# 3. Search for username patterns
python3 osint_cli.py username --check suspected_handle

# 4. Generate comprehensive report
python3 osint_cli.py investigate --username suspected_handle --email attacker@example.com --generate-report
```

### Scenario 4: Content Attribution
**Goal:** Find original source of content

```bash
# 1. Extract image metadata
python3 osint_tool.py --image-url https://suspicious-site.com/image.jpg

# 2. Analyze URLs in post
python3 osint_cli.py url --analyze "https://bit.ly/abc123"

# 3. Check poster's history
python3 osint_tool.py --reddit-user poster --analyze-posts
```

## Tips and Best Practices

### 1. API Rate Limits
**Twitter:**
- 300 requests per 15 minutes
- Space out requests

**Reddit:**
- 60 requests per minute
- Use delays between calls

**Free Geolocation APIs:**
- 1000-2500 requests per day
- Monitor usage

### 2. Data Privacy
```bash
# Never commit config.json
git add .gitignore
git status  # Verify config.json not tracked

# Keep investigation reports private
# Store in separate secure location
```

### 3. Efficient Investigation Workflow

**Step 1: Start Broad**
```bash
# Username enumeration
python3 osint_cli.py username --check target_user
```

**Step 2: Focus on Active Platforms**
```bash
# Analyze found profiles
python3 osint_tool.py --twitter-user target_user --analyze-posts
```

**Step 3: Cross-Reference**
- Compare information across platforms
- Look for contradictions
- Verify timestamps and locations

**Step 4: Document Everything**
```bash
# Generate comprehensive report
python3 osint_cli.py investigate --username target_user --generate-report
```

### 4. Handling False Positives
- Multiple people may use same username
- Verify with additional identifiers:
  - Bio information
  - Profile pictures
  - Creation dates
  - Posting patterns
  - Location mentions

### 5. Legal Considerations
✅ **DO:**
- Use for academic research
- Verify information with authorization
- Document methodology
- Respect privacy laws

❌ **DON'T:**
- Harass or stalk individuals
- Violate platform ToS
- Share private information
- Use for illegal purposes

### 6. Automation Tips

**Create custom scripts:**
```python
from osint_tool import TwitterOSINT
from advanced_utils import UsernameEnumerator

# Your custom workflow
def my_investigation(username):
    # Check platforms
    platforms = UsernameEnumerator.check_username(username)
    
    # Analyze Twitter if found
    if platforms.get('twitter', {}).get('exists'):
        twitter = TwitterOSINT()
        profile = twitter.search_user(username)
        return profile
```

### 7. Error Handling
```bash
# If API fails, check:
# 1. API keys in config.json
# 2. Internet connection
# 3. Rate limits
# 4. API service status

# Enable debug mode (if implemented)
python3 osint_tool.py --twitter-user username --debug
```

### 8. Organizing Results
```bash
# Create investigation folder
mkdir investigations/case_001
cd investigations/case_001

# Run analysis
python3 ../../osint_cli.py investigate \
    --username target \
    --generate-report

# Add notes
nano notes.md
```

### 9. Verification Checklist
- [ ] Cross-reference multiple sources
- [ ] Verify timestamps are logical
- [ ] Check location consistency
- [ ] Compare writing styles
- [ ] Validate image metadata
- [ ] Check for bot-like patterns
- [ ] Document confidence level

### 10. Performance Optimization
```bash
# For large investigations:
# 1. Use batch processing
python3 batch_analysis.py

# 2. Schedule during off-peak hours
# 3. Implement caching for repeated queries
# 4. Save intermediate results
```

## Troubleshooting

### Common Issues

**1. Config file not found:**
```bash
python3 osint_tool.py  # Creates template
```

**2. Module not found:**
```bash
pip install -r requirements.txt
```

**3. API authentication failed:**
- Verify API keys in config.json
- Check key permissions
- Ensure keys haven't expired

**4. No results found:**
- Username may not exist
- Check spelling
- Try variations (_, -, no spaces)

**5. Rate limit exceeded:**
- Wait before retry
- Reduce request frequency
- Check API tier limits

## Getting Help

- **Documentation:** README.md
- **Examples:** See batch_analysis.py
- **Issues:** Check API status pages
- **Academic Use:** Include proper citations

## Project Submission Checklist

For your college project:
- [ ] Code is well-commented
- [ ] README.md is complete
- [ ] Usage examples provided
- [ ] Ethical guidelines included
- [ ] config.json in .gitignore
- [ ] Requirements.txt included
- [ ] Sample outputs documented
- [ ] Limitations discussed
- [ ] Future improvements listed
- [ ] References cited

Good luck with your project! 🎓
