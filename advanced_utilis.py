#!/usr/bin/env python3
"""
Advanced OSINT Utilities
Additional analysis tools for the OSINT framework
"""

import re
import hashlib
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import socket
import requests

class UsernameEnumerator:
    """Check username across multiple platforms"""
    
    PLATFORMS = {
        'twitter': 'https://twitter.com/{}',
        'instagram': 'https://www.instagram.com/{}/',
        'facebook': 'https://www.facebook.com/{}',
        'github': 'https://github.com/{}',
        'reddit': 'https://www.reddit.com/user/{}',
        'youtube': 'https://www.youtube.com/@{}',
        'tiktok': 'https://www.tiktok.com/@{}',
        'linkedin': 'https://www.linkedin.com/in/{}',
        'pinterest': 'https://www.pinterest.com/{}',
        'medium': 'https://medium.com/@{}',
        'twitch': 'https://www.twitch.tv/{}',
        'snapchat': 'https://www.snapchat.com/add/{}',
        'telegram': 'https://t.me/{}',
        'discord': 'https://discord.com/users/{}',
        'patreon': 'https://www.patreon.com/{}',
        'spotify': 'https://open.spotify.com/user/{}',
        'vimeo': 'https://vimeo.com/{}',
        'behance': 'https://www.behance.net/{}',
        'dribbble': 'https://dribbble.com/{}',
        'soundcloud': 'https://soundcloud.com/{}'
    }
    
    @staticmethod
    def check_username(username: str) -> Dict[str, Dict]:
        """Check if username exists on various platforms"""
        results = {}
        
        print(f"\n🔍 Checking username '{username}' across platforms...")
        print("-" * 60)
        
        for platform, url_template in UsernameEnumerator.PLATFORMS.items():
            url = url_template.format(username)
            
            try:
                response = requests.get(url, timeout=5, allow_redirects=True)
                
                exists = False
                if response.status_code == 200:
                    # Additional checks for some platforms
                    if platform == 'github':
                        exists = 'Not Found' not in response.text
                    elif platform == 'reddit':
                        exists = 'Sorry, nobody on Reddit goes by that name' not in response.text
                    else:
                        exists = True
                
                results[platform] = {
                    'exists': exists,
                    'url': url,
                    'status_code': response.status_code
                }
                
                status = "✅ Found" if exists else "❌ Not found"
                print(f"{status:15} | {platform:15} | {url}")
                
            except requests.exceptions.RequestException:
                results[platform] = {
                    'exists': None,
                    'url': url,
                    'status_code': 'Timeout/Error'
                }
                print(f"⚠️  Timeout     | {platform:15} | {url}")
        
        print("-" * 60)
        
        found_count = sum(1 for r in results.values() if r['exists'] is True)
        print(f"\n📊 Summary: Found on {found_count}/{len(UsernameEnumerator.PLATFORMS)} platforms\n")
        
        return results

class EmailAnalyzer:
    """Analyze email addresses"""
    
    @staticmethod
    def analyze_email(email: str) -> Dict:
        """Extract information from email address"""
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            return {"error": "Invalid email format"}
        
        username, domain = email.split('@')
        
        info = {
            "email": email,
            "username": username,
            "domain": domain,
            "email_hash_md5": hashlib.md5(email.lower().encode()).hexdigest(),
            "email_hash_sha256": hashlib.sha256(email.lower().encode()).hexdigest(),
            "possible_names": EmailAnalyzer.extract_possible_names(username),
            "domain_info": EmailAnalyzer.get_domain_info(domain)
        }
        
        return info
    
    @staticmethod
    def extract_possible_names(username: str) -> List[str]:
        """Try to extract possible real names from username"""
        names = []
        
        # Split by common separators
        parts = re.split(r'[._-]', username)
        parts = [p for p in parts if p and not p.isdigit()]
        
        if parts:
            names.append(' '.join(parts).title())
            names.append(' '.join(reversed(parts)).title())
        
        return names
    
    @staticmethod
    def get_domain_info(domain: str) -> Dict:
        """Get basic domain information"""
        info = {
            "domain": domain,
            "is_disposable": EmailAnalyzer.is_disposable_email(domain),
            "is_common_provider": domain in [
                'gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com',
                'icloud.com', 'protonmail.com', 'aol.com'
            ]
        }
        
        try:
            ip = socket.gethostbyname(domain)
            info["mx_ip"] = ip
        except:
            info["mx_ip"] = "Unable to resolve"
        
        return info
    
    @staticmethod
    def is_disposable_email(domain: str) -> bool:
        """Check if email domain is disposable"""
        disposable_domains = [
            'tempmail.com', '10minutemail.com', 'guerrillamail.com',
            'mailinator.com', 'throwaway.email', 'temp-mail.org',
            'fakeinbox.com', 'trashmail.com'
        ]
        return domain.lower() in disposable_domains

class PhoneAnalyzer:
    """Analyze phone numbers"""
    
    @staticmethod
    def analyze_phone(phone: str) -> Dict:
        """Extract information from phone number"""
        # Remove common formatting
        cleaned = re.sub(r'[^\d+]', '', phone)
        
        info = {
            "original": phone,
            "cleaned": cleaned,
            "length": len(cleaned.replace('+', ''))
        }
        
        # Try to identify country code
        if cleaned.startswith('+'):
            if cleaned.startswith('+1'):
                info["country"] = "USA/Canada"
                info["country_code"] = "+1"
            elif cleaned.startswith('+44'):
                info["country"] = "United Kingdom"
                info["country_code"] = "+44"
            elif cleaned.startswith('+91'):
                info["country"] = "India"
                info["country_code"] = "+91"
            elif cleaned.startswith('+86'):
                info["country"] = "China"
                info["country_code"] = "+86"
            else:
                info["country"] = "Unknown"
                info["country_code"] = cleaned[:3]
        
        return info

class URLAnalyzer:
    """Analyze URLs for OSINT"""
    
    @staticmethod
    def analyze_url(url: str) -> Dict:
        """Extract information from URL"""
        from urllib.parse import urlparse, parse_qs
        
        parsed = urlparse(url)
        
        info = {
            "url": url,
            "scheme": parsed.scheme,
            "domain": parsed.netloc,
            "path": parsed.path,
            "parameters": parse_qs(parsed.query) if parsed.query else {},
            "fragment": parsed.fragment
        }
        
        # Extract potential tracking parameters
        tracking_params = ['utm_source', 'utm_medium', 'utm_campaign', 
                          'fbclid', 'gclid', 'ref', 'source']
        
        info["tracking_params"] = {
            k: v for k, v in info["parameters"].items() 
            if k in tracking_params
        }
        
        # Check if shortened URL
        short_domains = ['bit.ly', 't.co', 'tinyurl.com', 'goo.gl', 'ow.ly']
        info["is_shortened"] = any(domain in parsed.netloc for domain in short_domains)
        
        return info
    
    @staticmethod
    def expand_short_url(url: str) -> Optional[str]:
        """Expand shortened URL"""
        try:
            response = requests.head(url, allow_redirects=True, timeout=5)
            return response.url
        except:
            return None

class TimelineAnalyzer:
    """Analyze timelines and activity patterns"""
    
    @staticmethod
    def analyze_activity_timeline(timestamps: List[str]) -> Dict:
        """Analyze activity patterns over time"""
        if not timestamps:
            return {"error": "No timestamps provided"}
        
        dates = []
        for ts in timestamps:
            try:
                dt = datetime.fromisoformat(ts.replace('Z', '+00:00'))
                dates.append(dt)
            except:
                continue
        
        if not dates:
            return {"error": "No valid timestamps"}
        
        dates.sort()
        
        # Calculate activity metrics
        first_post = dates[0]
        last_post = dates[-1]
        total_days = (last_post - first_post).days
        
        # Activity by hour
        hours = [d.hour for d in dates]
        hour_distribution = {h: hours.count(h) for h in range(24)}
        
        # Activity by day of week
        days = [d.strftime("%A") for d in dates]
        day_distribution = {d: days.count(d) for d in set(days)}
        
        # Find gaps
        gaps = []
        for i in range(1, len(dates)):
            gap = (dates[i] - dates[i-1]).days
            if gap > 7:  # Gaps longer than a week
                gaps.append({
                    "start": dates[i-1].isoformat(),
                    "end": dates[i].isoformat(),
                    "days": gap
                })
        
        return {
            "first_activity": first_post.isoformat(),
            "last_activity": last_post.isoformat(),
            "total_days_active": total_days,
            "total_posts": len(dates),
            "avg_posts_per_day": len(dates) / max(total_days, 1),
            "most_active_hour": max(hour_distribution, key=hour_distribution.get),
            "most_active_day": max(day_distribution, key=day_distribution.get),
            "activity_by_hour": hour_distribution,
            "activity_by_day": day_distribution,
            "long_gaps": gaps[:5]  # Top 5 longest gaps
        }

class HashIdentifier:
    """Identify hash types"""
    
    HASH_PATTERNS = {
        'MD5': (r'^[a-fA-F0-9]{32}$', 32),
        'SHA1': (r'^[a-fA-F0-9]{40}$', 40),
        'SHA256': (r'^[a-fA-F0-9]{64}$', 64),
        'SHA512': (r'^[a-fA-F0-9]{128}$', 128),
        'NTLM': (r'^[a-fA-F0-9]{32}$', 32),
        'MySQL': (r'^\*[a-fA-F0-9]{40}$', 41)
    }
    
    @staticmethod
    def identify_hash(hash_string: str) -> List[str]:
        """Identify possible hash types"""
        possible_types = []
        
        for hash_type, (pattern, length) in HashIdentifier.HASH_PATTERNS.items():
            if re.match(pattern, hash_string) and len(hash_string) == length:
                possible_types.append(hash_type)
        
        return possible_types if possible_types else ["Unknown"]

def generate_report(data: Dict, output_file: str = "osint_report.txt"):
    """Generate a text report from OSINT data"""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("="*70 + "\n")
        f.write("OSINT ANALYSIS REPORT\n")
        f.write(f"Generated: {datetime.now().isoformat()}\n")
        f.write("="*70 + "\n\n")
        
        def write_dict(d, indent=0):
            for key, value in d.items():
                if isinstance(value, dict):
                    f.write("  " * indent + f"{key.upper()}:\n")
                    write_dict(value, indent + 1)
                elif isinstance(value, list):
                    f.write("  " * indent + f"{key}: {', '.join(map(str, value))}\n")
                else:
                    f.write("  " * indent + f"{key}: {value}\n")
        
        write_dict(data)
        f.write("\n" + "="*70 + "\n")
        f.write("END OF REPORT\n")
        f.write("="*70 + "\n")
    
    print(f"✅ Report saved to: {output_file}")

if __name__ == "__main__":
    print("Advanced OSINT Utilities Module")
    print("Import this module to use advanced features:")
    print("  from advanced_utils import UsernameEnumerator, EmailAnalyzer, PhoneAnalyzer")
