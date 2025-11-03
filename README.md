# 🔍 Mr. Holmes - Complete Single File Edition

```
███╗   ███╗██████╗     ██╗  ██╗ ██████╗ ██╗     ███╗   ███╗███████╗███████╗
████╗ ████║██╔══██╗    ██║  ██║██╔═══██╗██║     ████╗ ████║██╔════╝██╔════╝
██╔████╔██║██████╔╝    ███████║██║   ██║██║     ██╔████╔██║█████╗  ███████╗
██║╚██╔╝██║██╔══██╗    ██╔══██║██║   ██║██║     ██║╚██╔╝██║██╔══╝  ╚════██║
██║ ╚═╝ ██║██║  ██║    ██║  ██║╚██████╔╝███████╗██║ ╚═╝ ██║███████╗███████║
╚═╝     ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝╚══════╝╚══════╝

🎩 "Elementary, my dear Watson. The game is afoot!" 🔍
```

## ✨ Single File Edition Features

**Everything in ONE file - `mr_holmes.py`!**

- 🎨 **Colorful, Animated ASCII Art** - Dynamic Sherlock Holmes with deerstalker hat
- 🚬 **Pipe Smoking Animation** - Watch Sherlock think!
- 🔍 **All Investigation Modules** - Complete OSINT toolkit
- 🎩 **Detective-Themed Interface** - Immersive investigation experience
- 📊 **Professional Output** - Color-coded results
- ⚡ **Zero Dependencies** (except config.json for API keys)

## 🚀 Quick Start

### Installation

```bash
# 1. Download mr_holmes.py
wget https://anizum1/Mr.-Holmes/mr_holmes.py

# 2. Install dependencies
pip install requests Pillow exifread

# 3. Make executable
chmod +x mr_holmes.py

# 4. Run for first time (creates config.json)
python mr_holmes.py

# 5. Edit config.json with your API keys (optional for many features)
nano config.json
```

### First Investigation (No API Required!)

```bash
# Check username across 20+ platforms - instant results!
python mr_holmes.py username --check johndoe
```

## 🎨 Visual Features

### Animated Logo
- **Colorful ASCII art** with ANSI color codes
- **Sherlock Holmes character** with iconic deerstalker hat
- **Magnifying glass** and detective imagery
- **Pipe smoking animation** 🚬
- **Dynamic text effects** with typing animation

### Color Scheme
- 🔵 **Cyan/Blue** - Information and headers
- 🟢 **Green** - Success and confirmations
- 🟡 **Yellow** - Warnings and highlights
- 🔴 **Red** - Errors and critical info
- 🟣 **Magenta** - Special notices
- ⚪ **White** - Data and results

## 📖 Usage Examples

### 🔎 Username Investigation (NO API!)
```bash
python mr_holmes.py username --check johndoe
```
**Output:** Colorful platform-by-platform results with ✅ ❌ indicators

### 🐦 Twitter Investigation
```bash
# Basic profile
python mr_holmes.py twitter --user elonmusk

# With activity analysis
python mr_holmes.py twitter --user elonmusk --analyze-posts
```
**Includes:** Animated investigating sequence, pipe smoke, Sherlock quotes!

### 🤖 Reddit Investigation
```bash
python mr_holmes.py reddit --user spez --analyze-posts
```

### 📷 Image Forensics
```bash
# Local image with GPS extraction
python mr_holmes.py image --file photo.jpg --reverse-geocode

# Remote image analysis
python mr_holmes.py image --url https://example.com/image.jpg
```

### 🌍 Geolocation
```bash
# IP address lookup
python mr_holmes.py geo --ip 8.8.8.8

# Reverse geocoding
python mr_holmes.py geo --coords 40.7128 -74.0060
```

### 📧 Email Analysis
```bash
python mr_holmes.py email --analyze john.doe@example.com
```

### 📱 Phone Analysis
```bash
python mr_holmes.py phone --analyze "+1-555-123-4567"
```

### 🔗 URL Analysis
```bash
# Analyze URL structure
python mr_holmes.py url --analyze "https://example.com/page?utm_source=twitter"

# Expand shortened URL
python mr_holmes.py url --expand "https://bit.ly/abc123"
```

### 🔐 Hash Identification
```bash
python mr_holmes.py hash --identify "5d41402abc4b2a76b9719d911017c592"
```

### 🕵️ Full Investigation
```bash
python mr_holmes.py investigate \
    --username johndoe \
    --email john@example.com \
    --phone "+1-555-1234" \
    --report
```

## 🎭 Sherlock Holmes Theme Elements

### Visual Indicators
- 🎩 **Deerstalker Hat** on logo
- 🔍 **Magnifying Glass** for investigations
- 🚬 **Pipe** with smoke animation
- 👁️ **Eyes** watching for clues
- 🧥 **Coat** - proper detective attire
- 🥾 **Boots** - ready for fieldwork

### Sherlock Quotes (Random)
- "The world is full of obvious things which nobody observes."
- "You see, but you do not observe. The distinction is clear."
- "Data! Data! Data! I can't make bricks without clay!"
- "It is a capital mistake to theorize before one has data."
- And more...

### Terminology
- **"Elementary!"** - For simple findings
- **"The game is afoot!"** - Starting investigations
- **"Case file"** - Reports and results
- **"Examining evidence"** - Processing data
- **"The plot thickens"** - Complex situations

## 🔧 Configuration

### config.json Structure
```json
{
    "twitter": {
        "bearer_token": "YOUR_TOKEN"
    },
    "reddit": {
        "client_id": "YOUR_ID",
        "client_secret": "YOUR_SECRET",
        "user_agent": "Mr. Holmes OSINT Tool v2.0"
    },
    "ipgeolocation": {
        "api_key": "YOUR_KEY"
    },
    "opencage": {
        "api_key": "YOUR_KEY"
    }
}
```

## 📊 Features Summary

| Feature | API Required | Description |
|---------|-------------|-------------|
| 👤 Username Check | ❌ No | Check 20+ platforms |
| 🐦 Twitter | ✅ Yes | Profile & activity analysis |
| 🤖 Reddit | ✅ Yes | User investigation |
| 📷 Image EXIF | ❌ No | Metadata extraction |
| 🌍 IP Lookup | ✅ Yes | Geolocation |
| 📧 Email | ❌ No | Email analysis |
| 📱 Phone | ❌ No | Phone investigation |
| 🔗 URL | ❌ No | URL analysis |
| 🔐 Hash | ❌ No | Hash identification |

## 🎨 Terminal Requirements

**For best visual experience:**
- Terminal with ANSI color support
- UTF-8 encoding
- Recommended: iTerm2 (Mac), Windows Terminal, GNOME Terminal

**Terminals tested:**
- ✅ Linux (GNOME Terminal, Konsole, xterm)
- ✅ macOS (Terminal.app, iTerm2)
- ✅ Windows (Windows Terminal, Git Bash)
- ⚠️ Windows CMD (limited color support)

## 🚨 Troubleshooting

### Colors not showing?
```bash
# Check terminal color support
echo $TERM

# Should show: xterm-256color or similar
```

### Module import errors?
```bash
pip install requests Pillow exifread
```

### Config file issues?
```bash
# Delete and recreate
rm config.json
python mr_holmes.py
```

## 📝 File Structure

**EVERYTHING is in `mr_holmes.py`!**

**Sections:**
1. Colors & ASCII Art (Lines 1-300)
2. Core Classes (Lines 301-800)
3. Investigation Modules (Lines 801-1200)
4. Utilities (Lines 1201-1500)
5. Main Application (Lines 1501-end)

**Total:** ~1,500 lines of detective goodness! 🕵️

## 🎓 For Your College Project

**Single file advantages:**
- ✅ Easy to understand flow
- ✅ No module confusion
- ✅ Simple deployment
- ✅ All code visible
- ✅ Easy to demo

**Presentation tips:**
1. Start with the animated logo (impressive!)
2. Show username check (works immediately)
3. Demonstrate color-coded output
4. Highlight Sherlock Holmes theme
5. Show report generation

## ⚖️ Ethical Use

**This tool is for:**
- ✅ Educational projects
- ✅ Authorized research
- ✅ Security testing (with permission)
- ✅ Journalism
- ✅ Personal account verification

**NOT for:**
- ❌ Stalking or harassment
- ❌ Privacy invasion
- ❌ Illegal activities
- ❌ Unauthorized surveillance

## 📄 License

MIT License - Educational/Research Purpose Only

## 🎩 Credits

**Inspired by:**
- Sherlock Holmes (Sir Arthur Conan Doyle)
- Sherlock Project
- OSINT community

**Created for:** Educational purposes and legitimate security research

## 🆘 Support

For issues or questions:
1. Check the inline comments in `mr_holmes.py`
2. Review the help menu: `python mr_holmes.py --help`
3. Test each module independently
4. Ensure config.json is properly formatted

## 🎉 What Makes This Special?

1. **🎨 Animated & Colorful** - Not your boring CLI tool!
2. **🎩 Unique Theme** - Sherlock Holmes detective experience
3. **📦 Single File** - No complex project structure
4. **⚡ Instant Features** - Username check works without setup
5. **🔍 Complete Toolkit** - 8+ investigation modules
6. **📊 Professional Output** - Color-coded, organized results
7. **🚬 Fun Animations** - Pipe smoke, thinking animations
8. **💬 Sherlock Quotes** - Random detective wisdom

## 🔮 Future Enhancements

Ideas for extending this single file:
- [ ] More animation frames
- [ ] Sound effects (optional)
- [ ] More Sherlock quotes
- [ ] Additional color themes
- [ ] Progress bars for long operations
- [ ] Interactive mode
- [ ] ASCII art results visualization

---

<div align="center">

## 🔍 "The game is afoot!" 🔎

**One file. Infinite investigations.**

```
       🎩
      👁️👁️
      >👃<
      ╰─╯
     🧥🔍🧥
      │ │
     🥾 🥾

"Elementary, my dear Watson!"
```

Made with ❤️ for the OSINT community

</div>
