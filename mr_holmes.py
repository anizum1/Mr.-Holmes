#!/usr/bin/env python3
"""
Mr. Holmes - Main Entry Point
"Elementary, my dear Watson!"
"""

import sys
import os

# Import the logo module
try:
    from sherlock_logo import print_logo
    print_logo()
except:
    print("""
    ███╗   ███╗██████╗     ██╗  ██╗ ██████╗ ██╗     ███╗   ███╗███████╗███████╗
    ████╗ ████║██╔══██╗    ██║  ██║██╔═══██╗██║     ████╗ ████║██╔════╝██╔════╝
    ██╔████╔██║██████╔╝    ███████║██║   ██║██║     ██╔████╔██║█████╗  ███████╗
    ██║╚██╔╝██║██╔══██╗    ██╔══██║██║   ██║██║     ██║╚██╔╝██║██╔══╝  ╚════██║
    ██║ ╚═╝ ██║██║  ██║    ██║  ██║╚██████╔╝███████╗██║ ╚═╝ ██║███████╗███████║
    ╚═╝     ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝╚══════╝╚══════╝
    
    🔍 "Elementary, my dear Watson!" 🔎
    """)

# Check which module to run based on arguments
if len(sys.argv) > 1:
    command = sys.argv[1]
    
    # Username, email, phone, url, hash, investigate commands go to CLI
    if command in ['username', 'email', 'phone', 'url', 'hash', 'investigate']:
        print("\n🔍 Loading investigation modules...")
        import osint_cli
        osint_cli.main()
    
    # Social media, image, geo commands go to main tool
    elif command in ['--twitter-user', '--reddit-user', '--extract-exif', 
                      '--image-url', '--lookup-ip', '--geocode', '--analyze-time',
                      '--analyze-posts', '--reverse-geocode', '-h', '--help']:
        print("\n🔍 Initializing OSINT tools...")
        import osint_tool
        osint_tool.main()
    
    else:
        print("\n❌ Unknown command. Use --help for assistance.")
        print("\n📚 Quick Start:")
        print("   python mr_holmes.py username --check johndoe")
        print("   python mr_holmes.py --twitter-user username")
        print("   python mr_holmes.py --extract-exif image.jpg")
        print("   python mr_holmes.py --help")
else:
    # No arguments - show help
    print("\n🔍 Mr. Holmes - Advanced OSINT Investigation Tool")
    print("=" * 70)
    print("\n📋 Available Commands:")
    print("\n🔎 QUICK INVESTIGATIONS (No API Required):")
    print("   python mr_holmes.py username --check USERNAME")
    print("   python mr_holmes.py email --analyze EMAIL")
    print("   python mr_holmes.py phone --analyze PHONE")
    print("   python mr_holmes.py url --analyze URL")
    print("   python mr_holmes.py hash --identify HASH")
    print("\n🕵️ SOCIAL MEDIA (Requires API):")
    print("   python mr_holmes.py --twitter-user USERNAME")
    print("   python mr_holmes.py --reddit-user USERNAME")
    print("   python mr_holmes.py --twitter-user USERNAME --analyze-posts")
    print("\n📷 IMAGE FORENSICS:")
    print("   python mr_holmes.py --extract-exif image.jpg")
    print("   python mr_holmes.py --extract-exif image.jpg --reverse-geocode")
    print("   python mr_holmes.py --image-url https://example.com/img.jpg")
    print("\n🌍 GEOLOCATION:")
    print("   python mr_holmes.py --lookup-ip 8.8.8.8")
    print("   python mr_holmes.py --geocode 40.7128 -74.0060")
    print("\n📊 FULL INVESTIGATION:")
    print("   python mr_holmes.py investigate --username USER --email EMAIL --generate-report")
    print("\n📖 For detailed help:")
    print("   python mr_holmes.py --help")
    print("   python mr_holmes.py username --help")
    print("\n" + "=" * 70)
    print("🔍 \"The game is afoot, Watson!\"")
    print("=" * 70 + "\n")
