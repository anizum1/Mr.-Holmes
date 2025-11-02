#!/usr/bin/env python3
"""
Mr. Holmes - Comprehensive OSINT Investigation Tool
"Elementary, my dear Watson!"
"""

import argparse
import sys
from datetime import datetime
from advanced_utils import (
    UsernameEnumerator, EmailAnalyzer, PhoneAnalyzer, 
    URLAnalyzer, TimelineAnalyzer, HashIdentifier, generate_report
)

def print_banner():
    """Print Mr. Holmes banner"""
    banner = """
    ███╗   ███╗██████╗     ██╗  ██╗ ██████╗ ██╗     ███╗   ███╗███████╗███████╗
    ████╗ ████║██╔══██╗    ██║  ██║██╔═══██╗██║     ████╗ ████║██╔════╝██╔════╝
    ██╔████╔██║██████╔╝    ███████║██║   ██║██║     ██╔████╔██║█████╗  ███████╗
    ██║╚██╔╝██║██╔══██╗    ██╔══██║██║   ██║██║     ██║╚██╔╝██║██╔══╝  ╚════██║
    ██║ ╚═╝ ██║██║  ██║    ██║  ██║╚██████╔╝███████╗██║ ╚═╝ ██║███████╗███████║
    ╚═╝     ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝╚══════╝╚══════╝
    
    ═══════════════════════════════════════════════════════════════════════════
    🔎 "Elementary, my dear Watson. The game is afoot!" 🔍
    Advanced OSINT Investigation Tool | Educational/Research Purpose Only
    ═══════════════════════════════════════════════════════════════════════════
    """
    print(banner)

def main():
    print_banner()
    
    parser = argparse.ArgumentParser(
        description='Mr. Holmes - Advanced OSINT Investigation Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
═══════════════════════════════════════════════════════════════════════════
ELEMENTARY INVESTIGATION TECHNIQUES:

🔍 Social Media Intelligence:
  python mr_holmes.py social --twitter elonmusk --analyze-posts
  python mr_holmes.py social --reddit spez --analyze-posts

👤 Username Investigation:
  python mr_holmes.py username --check johndoe

📧 Email Analysis:
  python mr_holmes.py email --analyze john.doe@example.com

📱 Phone Investigation:
  python mr_holmes.py phone --analyze "+1-555-123-4567"

📷 Image Forensics:
  python mr_holmes.py image --file photo.jpg --extract-gps
  python mr_holmes.py image --url https://example.com/image.jpg

🌍 Geolocation Tracking:
  python mr_holmes.py geo --ip 8.8.8.8
  python mr_holmes.py geo --coords 40.7128 -74.0060

🔗 URL Analysis:
  python mr_holmes.py url --analyze https://example.com/page?utm_source=twitter
  python mr_holmes.py url --expand https://bit.ly/abc123

🔐 Hash Identification:
  python mr_holmes.py hash --identify 5d41402abc4b2a76b9719d911017c592

🕵️ Full Investigation:
  python mr_holmes.py investigate --username johndoe --email john@example.com --generate-report

═══════════════════════════════════════════════════════════════════════════
"When you have eliminated the impossible, whatever remains,
however improbable, must be the truth." - Sherlock Holmes
═══════════════════════════════════════════════════════════════════════════
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Command to execute')
    
    # Social Media Command
    social = subparsers.add_parser('social', help='Social media analysis')
    social.add_argument('--twitter', type=str, help='Twitter username')
    social.add_argument('--reddit', type=str, help='Reddit username')
    social.add_argument('--analyze-posts', action='store_true', help='Analyze posting patterns')
    
    # Username Enumeration Command
    username = subparsers.add_parser('username', help='Username enumeration')
    username.add_argument('--check', type=str, required=True, help='Username to check')
    
    # Email Analysis Command
    email = subparsers.add_parser('email', help='Email analysis')
    email.add_argument('--analyze', type=str, required=True, help='Email address to analyze')
    
    # Phone Analysis Command
    phone = subparsers.add_parser('phone', help='Phone number analysis')
    phone.add_argument('--analyze', type=str, required=True, help='Phone number to analyze')
    
    # Image Analysis Command
    image = subparsers.add_parser('image', help='Image analysis')
    image.add_argument('--file', type=str, help='Image file path')
    image.add_argument('--url', type=str, help='Image URL')
    image.add_argument('--extract-gps', action='store_true', help='Extract GPS coordinates')
    
    # Geolocation Command
    geo = subparsers.add_parser('geo', help='Geolocation lookup')
    geo.add_argument('--ip', type=str, help='IP address to lookup')
    geo.add_argument('--coords', nargs=2, type=float, metavar=('LAT', 'LON'), help='Coordinates')
    
    # URL Analysis Command
    url_parser = subparsers.add_parser('url', help='URL analysis')
    url_parser.add_argument('--analyze', type=str, help='URL to analyze')
    url_parser.add_argument('--expand', type=str, help='Expand shortened URL')
    
    # Hash Identification Command
    hash_parser = subparsers.add_parser('hash', help='Hash identification')
    hash_parser.add_argument('--identify', type=str, required=True, help='Hash to identify')
    
    # Investigation Command (combines multiple features)
    investigate = subparsers.add_parser('investigate', help='Full profile investigation')
    investigate.add_argument('--username', type=str, help='Username to investigate')
    investigate.add_argument('--email', type=str, help='Email address')
    investigate.add_argument('--phone', type=str, help='Phone number')
    investigate.add_argument('--generate-report', action='store_true', help='Generate report')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    # Execute commands
    if args.command == 'username':
        results = UsernameEnumerator.check_username(args.check)
        if args.check:
            print(f"\n💾 Results can be saved to file if needed")
    
    elif args.command == 'email':
        print(f"\n📧 Analyzing email: {args.analyze}")
        result = EmailAnalyzer.analyze_email(args.analyze)
        print_results(result, "Email Analysis")
    
    elif args.command == 'phone':
        print(f"\n📱 Analyzing phone: {args.analyze}")
        result = PhoneAnalyzer.analyze_phone(args.analyze)
        print_results(result, "Phone Analysis")
    
    elif args.command == 'url':
        if args.analyze:
            print(f"\n🔗 Analyzing URL: {args.analyze}")
            result = URLAnalyzer.analyze_url(args.analyze)
            print_results(result, "URL Analysis")
        
        if args.expand:
            print(f"\n🔗 Expanding URL: {args.expand}")
            expanded = URLAnalyzer.expand_short_url(args.expand)
            if expanded:
                print(f"   Expanded URL: {expanded}")
            else:
                print("   ❌ Failed to expand URL")
    
    elif args.command == 'hash':
        print(f"\n🔐 Identifying hash: {args.identify}")
        hash_types = HashIdentifier.identify_hash(args.identify)
        print(f"   Possible hash types: {', '.join(hash_types)}")
    
    elif args.command == 'social':
        # Run the main OSINT tool
        print("\n🔍 Running social media analysis...")
        print("   Use: python osint_tool.py for social media features")
    
    elif args.command == 'image':
        print("\n📷 Running image analysis...")
        print("   Use: python osint_tool.py --extract-exif for image features")
    
    elif args.command == 'geo':
        print("\n🌍 Running geolocation...")
        print("   Use: python osint_tool.py for geolocation features")
    
    elif args.command == 'investigate':
        print("\n🔍 Starting full investigation...")
        investigation_data = {}
        
        if args.username:
            print(f"\n👤 Checking username: {args.username}")
            investigation_data['username_check'] = UsernameEnumerator.check_username(args.username)
        
        if args.email:
            print(f"\n📧 Analyzing email: {args.email}")
            investigation_data['email_analysis'] = EmailAnalyzer.analyze_email(args.email)
        
        if args.phone:
            print(f"\n📱 Analyzing phone: {args.phone}")
            investigation_data['phone_analysis'] = PhoneAnalyzer.analyze_phone(args.phone)
        
        if args.generate_report and investigation_data:
            filename = f"investigation_{args.username or 'unknown'}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            generate_report(investigation_data, filename)

def print_results(data: dict, title: str):
    """Pretty print results"""
    print("\n" + "="*70)
    print(f"📊 {title}")
    print("="*70)
    
    def print_dict(d, indent=0):
        for key, value in d.items():
            if isinstance(value, dict):
                print("  " * indent + f"🔹 {key.replace('_', ' ').title()}:")
                print_dict(value, indent + 1)
            elif isinstance(value, list):
                if value:
                    print("  " * indent + f"🔹 {key.replace('_', ' ').title()}: {', '.join(map(str, value))}")
            else:
                print("  " * indent + f"🔹 {key.replace('_', ' ').title()}: {value}")
    
    print_dict(data)
    print("="*70 + "\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Investigation interrupted!")
        print("🔍 \"Perhaps another time, Watson.\"")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Confound it! An error: {str(e)}")
        print("🔍 \"The plot thickens, Watson.\"")
        sys.exit(1)
