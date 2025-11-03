#!/usr/bin/env python3
"""
Mr. Holmes - Advanced OSINT Investigation Tool
"Elementary, my dear Watson. The game is afoot!"

Complete Integrated Version
Educational/Research Purpose Only
"""

import requests
import json
import argparse
from datetime import datetime, timezone, timedelta
from typing import Dict, List, Optional, Tuple
import sys
import os
import re
import socket
import hashlib
import time
from pathlib import Path

try:
    import exifread
    from PIL import Image
    from PIL.ExifTags import TAGS, GPSTAGS
except ImportError:
    pass

# ============================================================================
# COLORFUL ASCII ART & ANIMATIONS
# ============================================================================

class Colors:
    """ANSI color codes for terminal"""
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    
    # Foreground colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Bright colors
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

def print_animated_logo():
    """Print animated colorful Sherlock Holmes logo with hat"""
    
    # Clear screen for better effect
    os.system('clear' if os.name != 'nt' else 'cls')
    
    logo = f"""
{Colors.BRIGHT_YELLOW}╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║  {Colors.BRIGHT_CYAN}███╗   ███╗██████╗     {Colors.BRIGHT_MAGENTA}██╗  ██╗ ██████╗ ██╗     {Colors.BRIGHT_GREEN}███╗   ███╗███████╗{Colors.BRIGHT_YELLOW}  ║
║  {Colors.BRIGHT_CYAN}████╗ ████║██╔══██╗    {Colors.BRIGHT_MAGENTA}██║  ██║██╔═══██╗██║     {Colors.BRIGHT_GREEN}████╗ ████║██╔════╝{Colors.BRIGHT_YELLOW}  ║
║  {Colors.BRIGHT_CYAN}██╔████╔██║██████╔╝    {Colors.BRIGHT_MAGENTA}███████║██║   ██║██║     {Colors.BRIGHT_GREEN}██╔████╔██║█████╗  {Colors.BRIGHT_YELLOW}  ║
║  {Colors.BRIGHT_CYAN}██║╚██╔╝██║██╔══██╗    {Colors.BRIGHT_MAGENTA}██╔══██║██║   ██║██║     {Colors.BRIGHT_GREEN}██║╚██╔╝██║██╔══╝  {Colors.BRIGHT_YELLOW}  ║
║  {Colors.BRIGHT_CYAN}██║ ╚═╝ ██║██║  ██║    {Colors.BRIGHT_MAGENTA}██║  ██║╚██████╔╝███████╗{Colors.BRIGHT_GREEN}██║ ╚═╝ ██║███████╗{Colors.BRIGHT_YELLOW}  ║
║  {Colors.BRIGHT_CYAN}╚═╝     ╚═╝╚═╝  ╚═╝    {Colors.BRIGHT_MAGENTA}╚═╝  ╚═╝ ╚═════╝ ╚══════╝{Colors.BRIGHT_GREEN}╚═╝     ╚═╝╚══════╝{Colors.BRIGHT_YELLOW}  ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝{Colors.RESET}

{Colors.BRIGHT_YELLOW}                    ═══════════════════════════════════
{Colors.BRIGHT_CYAN}                         {Colors.BG_BLUE}{Colors.BRIGHT_YELLOW}🎩 DETECTIVE SHERLOCK HOLMES 🎩{Colors.RESET}
{Colors.BRIGHT_YELLOW}                    ═══════════════════════════════════{Colors.RESET}

{Colors.BRIGHT_GREEN}                              .▄▄ · ▄▄▄ .▄▄▄  
                              ▐█ ▀. ▀▄.▀·▀▄ █·
                              ▄▀▀▀█▄▐▀▀▪▄▐▀▀▄ 
                              ▐█▄▪▐█▐█▄▄▌▐█•█▌
                               ▀▀▀▀  ▀▀▀ .▀  ▀{Colors.RESET}

{Colors.BRIGHT_YELLOW}                              ╔══════════╗
                              ║{Colors.BRIGHT_CYAN}  /^^^^\\  {Colors.BRIGHT_YELLOW}║
                              ║{Colors.BRIGHT_CYAN} {Colors.BG_CYAN} {Colors.YELLOW}DEER  {Colors.RESET}{Colors.BRIGHT_CYAN} {Colors.BRIGHT_YELLOW}║
                              ║{Colors.BRIGHT_CYAN} {Colors.BG_CYAN}{Colors.YELLOW}STALKER{Colors.RESET}{Colors.BRIGHT_CYAN}{Colors.BRIGHT_YELLOW}║
{Colors.BRIGHT_RED}                              ╠══════════╣{Colors.RESET}
{Colors.BRIGHT_MAGENTA}                              ║  {Colors.BRIGHT_WHITE}👁️  👁️{Colors.BRIGHT_MAGENTA}  ║
                              ║    {Colors.BRIGHT_WHITE}>👃<{Colors.BRIGHT_MAGENTA}   ║
                              ║   {Colors.BRIGHT_WHITE}╰───╯{Colors.BRIGHT_MAGENTA}  ║{Colors.RESET}
{Colors.BRIGHT_BLUE}                              ╠══════════╣
                              ║{Colors.BRIGHT_WHITE}  │╔═══╗│{Colors.BRIGHT_BLUE}  ║
                              ║{Colors.BRIGHT_WHITE}  │║{Colors.BRIGHT_GREEN}🧥{Colors.BRIGHT_WHITE}║│{Colors.BRIGHT_BLUE}  ║
                              ║{Colors.BRIGHT_WHITE}  │║{Colors.BRIGHT_GREEN}🔍{Colors.BRIGHT_WHITE}║│{Colors.BRIGHT_BLUE}  ║
                              ║{Colors.BRIGHT_WHITE}  ├╫───╫┤{Colors.BRIGHT_BLUE}  ║
                              ║{Colors.BRIGHT_WHITE}  ││   ││{Colors.BRIGHT_BLUE}  ║
                              ╚══╩═════╩══╝{Colors.RESET}
{Colors.BRIGHT_YELLOW}                               │     │
                              {Colors.BRIGHT_RED}🥾{Colors.BRIGHT_YELLOW}     {Colors.BRIGHT_RED}🥾{Colors.RESET}

{Colors.BRIGHT_CYAN}    ╔═══════════════════════════════════════════════════════════════╗
    ║  {Colors.BRIGHT_WHITE}"Elementary, my dear Watson. The game is afoot!"{Colors.BRIGHT_CYAN}      ║
    ╚═══════════════════════════════════════════════════════════════╝{Colors.RESET}

{Colors.BRIGHT_GREEN}    🔍 {Colors.BRIGHT_WHITE}Advanced OSINT Investigation Framework{Colors.BRIGHT_GREEN} 🔎{Colors.RESET}
{Colors.BRIGHT_YELLOW}    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.RESET}
{Colors.BRIGHT_MAGENTA}    👤 Social Media Intel  {Colors.BRIGHT_CYAN}📷 Image Forensics  {Colors.BRIGHT_GREEN}🌍 Geolocation{Colors.RESET}
{Colors.BRIGHT_YELLOW}    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.RESET}

{Colors.BRIGHT_RED}    🚬 {Colors.DIM}Puff... puff... {Colors.BRIGHT_RED}💨 {Colors.BRIGHT_WHITE}"The evidence never lies..."{Colors.RESET}
    
{Colors.BRIGHT_BLUE}    ╔══════════════════════════════════════════════════════════════╗
    ║  {Colors.BRIGHT_YELLOW}Version 2.0  {Colors.BRIGHT_WHITE}|  {Colors.BRIGHT_GREEN}Educational/Research Only  {Colors.BRIGHT_WHITE}|  {Colors.BRIGHT_CYAN}2024{Colors.BRIGHT_BLUE}     ║
    ╚══════════════════════════════════════════════════════════════╝{Colors.RESET}
"""
    
    print(logo)
    
    # Animated typing effect for the quote
    quote = f"\n{Colors.BRIGHT_YELLOW}    ┌{'─' * 66}┐{Colors.RESET}"
    print(quote)
    
    message = "    │  \"When you have eliminated the impossible, whatever remains,   │"
    for char in message:
        print(f"{Colors.BRIGHT_WHITE}{char}{Colors.RESET}", end='', flush=True)
        time.sleep(0.01)
    
    print(f"\n{Colors.BRIGHT_WHITE}    │   however improbable, must be the truth.\" - Sherlock Holmes   │{Colors.RESET}")
    print(f"{Colors.BRIGHT_YELLOW}    └{'─' * 66}┘{Colors.RESET}\n")

def print_investigating_animation():
    """Show investigating animation"""
    frames = [
        f"{Colors.BRIGHT_CYAN}🔍 Investigating...     {Colors.RESET}",
        f"{Colors.BRIGHT_GREEN}🔍 Investigating..      {Colors.RESET}",
        f"{Colors.BRIGHT_YELLOW}🔍 Investigating.       {Colors.RESET}",
        f"{Colors.BRIGHT_MAGENTA}🔍 Investigating        {Colors.RESET}"
    ]
    
    for _ in range(3):
        for frame in frames:
            print(f"\r{frame}", end='', flush=True)
            time.sleep(0.2)
    print("\r" + " " * 30 + "\r", end='')

def print_success(message):
    """Print success message"""
    print(f"{Colors.BRIGHT_GREEN}✅ {message}{Colors.RESET}")

def print_error(message):
    """Print error message"""
    print(f"{Colors.BRIGHT_RED}❌ {message}{Colors.RESET}")

def print_info(message):
    """Print info message"""
    print(f"{Colors.BRIGHT_CYAN}ℹ️  {message}{Colors.RESET}")

def print_warning(message):
    """Print warning message"""
    print(f"{Colors.BRIGHT_YELLOW}⚠️  {message}{Colors.RESET}")

def print_detective_quote():
    """Print random Sherlock Holmes quote"""
    quotes = [
        "The world is full of obvious things which nobody observes.",
        "You see, but you do not observe. The distinction is clear.",
        "Data! Data! Data! I can't make bricks without clay!",
        "It is a capital mistake to theorize before one has data.",
        "Nothing clears up a case so much as stating it to another person.",
        "There is nothing more deceptive than an obvious fact.",
        "I never guess. It is a shocking habit—destructive to the logical faculty.",
        "The little things are infinitely the most important."
    ]
    import random
    quote = random.choice(quotes)
    print(f"\n{Colors.BRIGHT_YELLOW}🔍 Sherlock says:{Colors.BRIGHT_WHITE} \"{quote}\"{Colors.RESET}\n")

def print_pipe_smoke():
    """Animated pipe smoke"""
    smoke_frames = [
        f"{Colors.BRIGHT_WHITE}  🚬 ~~{Colors.RESET}",
        f"{Colors.BRIGHT_WHITE}  🚬 ~~~{Colors.RESET}",
        f"{Colors.BRIGHT_WHITE}  🚬 ~~~ ~{Colors.RESET}",
        f"{Colors.BRIGHT_WHITE}  🚬 ~~~{Colors.RESET}",
    ]
    
    print(f"\n{Colors.BRIGHT_CYAN}    Sherlock lights his pipe and ponders...{Colors.RESET}")
    for _ in range(2):
        for frame in smoke_frames:
            print(f"\r{frame}", end='', flush=True)
            time.sleep(0.3)
    print("\r" + " " * 20)

# ============================================================================
# CONFIGURATION MANAGEMENT
# ============================================================================

class OSINTTool:
    def __init__(self):
        self.config = self.load_config()
        
    def load_config(self) -> Dict:
        """Load API credentials from config file"""
        try:
            with open('config.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print_warning("config.json not found. Creating template...")
            self.create_config_template()
            sys.exit(1)
    
    def create_config_template(self):
        """Create a template config file"""
        template = {
            "twitter": {
                "bearer_token": "YOUR_TWITTER_BEARER_TOKEN",
                "api_key": "YOUR_API_KEY",
                "api_secret": "YOUR_API_SECRET"
            },
            "reddit": {
                "client_id": "YOUR_CLIENT_ID",
                "client_secret": "YOUR_CLIENT_SECRET",
                "user_agent": "Mr. Holmes OSINT Tool v2.0"
            },
            "instagram": {
                "access_token": "YOUR_ACCESS_TOKEN"
            },
            "facebook": {
                "access_token": "YOUR_ACCESS_TOKEN"
            },
            "ipgeolocation": {
                "api_key": "YOUR_IPGEOLOCATION_API_KEY",
                "note": "Get free key from https://ipgeolocation.io/"
            },
            "opencage": {
                "api_key": "YOUR_OPENCAGE_API_KEY",
                "note": "Get free key from https://opencagedata.com/"
            }
        }
        with open('config.json', 'w') as f:
            json.dump(template, f, indent=4)
        print_success("Created config.json template. Please add your API credentials.")

# ============================================================================
# TWITTER/X OSINT
# ============================================================================

class TwitterOSINT(OSINTTool):
    def __init__(self):
        super().__init__()
        self.base_url = "https://api.twitter.com/2"
        
    def search_user(self, username: str) -> Optional[Dict]:
        """Search for user information"""
        headers = {
            "Authorization": f"Bearer {self.config['twitter']['bearer_token']}"
        }
        
        params = {
            "user.fields": "created_at,description,location,public_metrics,verified,profile_image_url"
        }
        
        try:
            response = requests.get(
                f"{self.base_url}/users/by/username/{username}",
                headers=headers,
                params=params
            )
            
            if response.status_code == 200:
                return self.parse_user_data(response.json())
            else:
                print_error(f"Twitter API Error: {response.status_code}")
                return None
        except Exception as e:
            print_error(f"Exception: {str(e)}")
            return None
    
    def get_recent_tweets(self, user_id: str, max_results: int = 10) -> List[Dict]:
        """Get recent tweets from user"""
        headers = {
            "Authorization": f"Bearer {self.config['twitter']['bearer_token']}"
        }
        
        params = {
            "max_results": max_results,
            "tweet.fields": "created_at,geo,public_metrics,entities"
        }
        
        try:
            response = requests.get(
                f"{self.base_url}/users/{user_id}/tweets",
                headers=headers,
                params=params
            )
            
            if response.status_code == 200:
                return response.json().get('data', [])
            return []
        except Exception as e:
            print_error(f"Error getting tweets: {str(e)}")
            return []
    
    def parse_user_data(self, data: Dict) -> Dict:
        """Parse and extract relevant information"""
        user = data.get('data', {})
        
        info = {
            "platform": "Twitter",
            "username": user.get('username'),
            "name": user.get('name'),
            "user_id": user.get('id'),
            "created_at": user.get('created_at'),
            "location": user.get('location', 'Not specified'),
            "bio": user.get('description', 'No bio'),
            "verified": user.get('verified', False),
            "followers": user.get('public_metrics', {}).get('followers_count', 0),
            "following": user.get('public_metrics', {}).get('following_count', 0),
            "tweet_count": user.get('public_metrics', {}).get('tweet_count', 0),
            "profile_image": user.get('profile_image_url', '')
        }
        
        return info

# ============================================================================
# REDDIT OSINT
# ============================================================================

class RedditOSINT(OSINTTool):
    def __init__(self):
        super().__init__()
        self.base_url = "https://oauth.reddit.com"
        self.token = self.get_access_token()
        
    def get_access_token(self) -> str:
        """Get OAuth token"""
        auth = requests.auth.HTTPBasicAuth(
            self.config['reddit']['client_id'],
            self.config['reddit']['client_secret']
        )
        
        data = {'grant_type': 'client_credentials'}
        headers = {'User-Agent': self.config['reddit']['user_agent']}
        
        try:
            response = requests.post(
                'https://www.reddit.com/api/v1/access_token',
                auth=auth,
                data=data,
                headers=headers
            )
            
            if response.status_code == 200:
                return response.json()['access_token']
            else:
                print_error(f"Failed to get Reddit token: {response.status_code}")
                return ""
        except Exception as e:
            print_error(f"Exception getting token: {str(e)}")
            return ""
    
    def search_user(self, username: str) -> Optional[Dict]:
        """Search for Reddit user information"""
        headers = {
            'Authorization': f'bearer {self.token}',
            'User-Agent': self.config['reddit']['user_agent']
        }
        
        try:
            response = requests.get(
                f"{self.base_url}/user/{username}/about",
                headers=headers
            )
            
            if response.status_code == 200:
                return self.parse_user_data(response.json())
            else:
                print_error(f"Reddit Error: {response.status_code}")
                return None
        except Exception as e:
            print_error(f"Exception: {str(e)}")
            return None
    
    def get_user_posts(self, username: str, limit: int = 25) -> List[Dict]:
        """Get recent posts from user"""
        headers = {
            'Authorization': f'bearer {self.token}',
            'User-Agent': self.config['reddit']['user_agent']
        }
        
        try:
            response = requests.get(
                f"{self.base_url}/user/{username}/submitted",
                headers=headers,
                params={'limit': limit}
            )
            
            if response.status_code == 200:
                return response.json().get('data', {}).get('children', [])
            return []
        except Exception as e:
            print_error(f"Error getting posts: {str(e)}")
            return []
    
    def parse_user_data(self, data: Dict) -> Dict:
        """Parse Reddit user data"""
        user = data.get('data', {})
        
        created = datetime.fromtimestamp(user.get('created_utc', 0))
        
        info = {
            "platform": "Reddit",
            "username": user.get('name'),
            "user_id": user.get('id'),
            "created_at": created.isoformat(),
            "karma_post": user.get('link_karma', 0),
            "karma_comment": user.get('comment_karma', 0),
            "is_gold": user.get('is_gold', False),
            "is_mod": user.get('is_mod', False),
            "verified": user.get('verified', False),
            "total_karma": user.get('total_karma', 0)
        }
        
        return info

# ============================================================================
# IMAGE ANALYSIS
# ============================================================================

class ImageAnalyzer:
    """Extract EXIF data and analyze images"""
    
    @staticmethod
    def extract_exif(image_path: str) -> Dict:
        """Extract EXIF data from image"""
        if not os.path.exists(image_path):
            return {"error": "File not found"}
        
        result = {
            "filename": os.path.basename(image_path),
            "file_size": os.path.getsize(image_path),
            "exif_data": {},
            "gps_data": None
        }
        
        try:
            image = Image.open(image_path)
            exif_data = image._getexif()
            
            if exif_data:
                for tag_id, value in exif_data.items():
                    tag = TAGS.get(tag_id, tag_id)
                    
                    if tag == "GPSInfo":
                        gps_data = {}
                        for gps_tag_id in value:
                            gps_tag = GPSTAGS.get(gps_tag_id, gps_tag_id)
                            gps_data[gps_tag] = value[gps_tag_id]
                        result["gps_data"] = gps_data
                    else:
                        result["exif_data"][tag] = str(value)
                
                if result["gps_data"]:
                    coords = ImageAnalyzer.parse_gps_coordinates(result["gps_data"])
                    if coords:
                        result["latitude"] = coords[0]
                        result["longitude"] = coords[1]
                        result["coordinates"] = f"{coords[0]}, {coords[1]}"
                        result["google_maps"] = f"https://www.google.com/maps?q={coords[0]},{coords[1]}"
            
            result["format"] = image.format
            result["mode"] = image.mode
            result["size"] = f"{image.width}x{image.height}"
            
        except Exception as e:
            result["error"] = str(e)
        
        return result
    
    @staticmethod
    def parse_gps_coordinates(gps_data: Dict) -> Optional[Tuple[float, float]]:
        """Convert GPS EXIF data to decimal coordinates"""
        try:
            def convert_to_degrees(value):
                d, m, s = value
                return float(d) + float(m) / 60.0 + float(s) / 3600.0
            
            lat = convert_to_degrees(gps_data.get('GPSLatitude', [0, 0, 0]))
            lon = convert_to_degrees(gps_data.get('GPSLongitude', [0, 0, 0]))
            
            if gps_data.get('GPSLatitudeRef', 'N') == 'S':
                lat = -lat
            if gps_data.get('GPSLongitudeRef', 'E') == 'W':
                lon = -lon
            
            return (lat, lon)
        except:
            return None
    
    @staticmethod
    def download_image(url: str, save_path: str = "temp_image.jpg") -> str:
        """Download image from URL"""
        try:
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                with open(save_path, 'wb') as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)
                return save_path
        except Exception as e:
            print_error(f"Error downloading image: {str(e)}")
        return ""

# ============================================================================
# GEOLOCATION ANALYZER
# ============================================================================

class GeolocationAnalyzer(OSINTTool):
    """Analyze geolocation data"""
    
    def lookup_ip(self, ip_address: str) -> Optional[Dict]:
        """Lookup IP address geolocation"""
        api_key = self.config.get('ipgeolocation', {}).get('api_key', '')
        
        if not api_key or api_key == "YOUR_IPGEOLOCATION_API_KEY":
            return {"error": "IP Geolocation API key not configured"}
        
        try:
            url = f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={ip_address}"
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                return {
                    "ip": data.get('ip'),
                    "country": data.get('country_name'),
                    "city": data.get('city'),
                    "region": data.get('state_prov'),
                    "latitude": data.get('latitude'),
                    "longitude": data.get('longitude'),
                    "timezone": data.get('time_zone', {}).get('name'),
                    "isp": data.get('isp'),
                    "organization": data.get('organization')
                }
        except Exception as e:
            return {"error": str(e)}
        
        return None
    
    def reverse_geocode(self, latitude: float, longitude: float) -> Optional[Dict]:
        """Reverse geocode coordinates to location"""
        api_key = self.config.get('opencage', {}).get('api_key', '')
        
        if not api_key or api_key == "YOUR_OPENCAGE_API_KEY":
            return {"error": "OpenCage API key not configured"}
        
        try:
            url = f"https://api.opencagedata.com/geocode/v1/json"
            params = {
                'q': f"{latitude},{longitude}",
                'key': api_key
            }
            response = requests.get(url, params=params)
            
            if response.status_code == 200:
                data = response.json()
                if data['results']:
                    result = data['results'][0]
                    return {
                        "formatted_address": result.get('formatted'),
                        "country": result.get('components', {}).get('country'),
                        "city": result.get('components', {}).get('city'),
                        "state": result.get('components', {}).get('state'),
                        "postcode": result.get('components', {}).get('postcode'),
                        "timezone": result.get('annotations', {}).get('timezone', {}).get('name')
                    }
        except Exception as e:
            return {"error": str(e)}
        
        return None

# ============================================================================
# USERNAME ENUMERATOR
# ============================================================================

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
        
        print(f"\n{Colors.BRIGHT_CYAN}╔════════════════════════════════════════════════════════════════╗{Colors.RESET}")
        print(f"{Colors.BRIGHT_CYAN}║  {Colors.BRIGHT_YELLOW}🔍 Checking username '{username}' across platforms...{Colors.BRIGHT_CYAN}           ║{Colors.RESET}")
        print(f"{Colors.BRIGHT_CYAN}╚════════════════════════════════════════════════════════════════╝{Colors.RESET}")
        print(f"{Colors.BRIGHT_YELLOW}{'─' * 70}{Colors.RESET}")
        
        for platform, url_template in UsernameEnumerator.PLATFORMS.items():
            url = url_template.format(username)
            
            try:
                response = requests.get(url, timeout=5, allow_redirects=True)
                
                exists = False
                if response.status_code == 200:
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
                
                if exists:
                    print(f"{Colors.BRIGHT_GREEN}✅ Found      {Colors.RESET}| {Colors.BRIGHT_CYAN}{platform:15}{Colors.RESET} | {Colors.BRIGHT_WHITE}{url}{Colors.RESET}")
                else:
                    print(f"{Colors.BRIGHT_RED}❌ Not found  {Colors.RESET}| {Colors.DIM}{platform:15}{Colors.RESET} | {Colors.DIM}{url}{Colors.RESET}")
                
            except requests.exceptions.RequestException:
                results[platform] = {
                    'exists': None,
                    'url': url,
                    'status_code': 'Timeout/Error'
                }
                print(f"{Colors.BRIGHT_YELLOW}⚠️  Timeout    {Colors.RESET}| {Colors.BRIGHT_MAGENTA}{platform:15}{Colors.RESET} | {Colors.DIM}{url}{Colors.RESET}")
        
        print(f"{Colors.BRIGHT_YELLOW}{'─' * 70}{Colors.RESET}")
        
        found_count = sum(1 for r in results.values() if r['exists'] is True)
        print(f"\n{Colors.BRIGHT_GREEN}📊 Summary: Found on {found_count}/{len(UsernameEnumerator.PLATFORMS)} platforms{Colors.RESET}\n")
        
        return results

# ============================================================================
# EMAIL ANALYZER
# ============================================================================

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

# ============================================================================
# PHONE ANALYZER
# ============================================================================

class PhoneAnalyzer:
    """Analyze phone numbers"""
    
    @staticmethod
    def analyze_phone(phone: str) -> Dict:
        """Extract information from phone number"""
        cleaned = re.sub(r'[^\d+]', '', phone)
        
        info = {
            "original": phone,
            "cleaned": cleaned,
            "length": len(cleaned.replace('+', ''))
        }
        
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

# ============================================================================
# URL ANALYZER
# ============================================================================

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
        
        tracking_params = ['utm_source', 'utm_medium', 'utm_campaign', 
                          'fbclid', 'gclid', 'ref', 'source']
        
        info["tracking_params"] = {
            k: v for k, v in info["parameters"].items() 
            if k in tracking_params
        }
        
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

# ============================================================================
# HASH IDENTIFIER
# ============================================================================

class HashIdentifier:
    """Identify hash types"""
    
    HASH_PATTERNS = {
        'MD5': (r'^[a-fA-F0-9]{32}$', 32),
        'SHA1': (r'^[a-fA-F0-9]{40}$', 40),
        'SHA256': (r'^[a-fA-F0-9]{64}$', 64),
        'SHA512': (r'^[a-fA-F0-9]{128}$', 128),
        'NTLM': (r'^[a-fA-F0-9]{32}$', 32),
        'MySQL': (r'^\*[a-fA-F0-9]{40}$', 41)
    }$', 32),
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

# ============================================================================
# METADATA EXTRACTOR
# ============================================================================

class MetadataExtractor:
    """Extract metadata from publicly available information"""
    
    @staticmethod
    def analyze_timezone(timestamp: str) -> Dict:
        """Analyze timezone information from timestamp"""
        try:
            dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
            return {
                "utc_time": dt.isoformat(),
                "timestamp": dt.timestamp(),
                "day_of_week": dt.strftime("%A"),
                "hour": dt.hour,
                "date": dt.strftime("%Y-%m-%d"),
                "time": dt.strftime("%H:%M:%S")
            }
        except:
            return {"error": "Invalid timestamp"}
    
    @staticmethod
    def analyze_posting_patterns(posts: List[Dict]) -> Dict:
        """Analyze posting patterns to infer timezone/activity"""
        if not posts:
            return {"error": "No posts provided"}
        
        hours = []
        days = []
        
        for post in posts:
            timestamp = None
            
            if isinstance(post, dict):
                if 'created_at' in post:
                    timestamp = post['created_at']
                elif 'data' in post and 'created_utc' in post['data']:
                    timestamp = datetime.fromtimestamp(
                        post['data']['created_utc']
                    ).isoformat()
            
            if timestamp:
                try:
                    dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
                    hours.append(dt.hour)
                    days.append(dt.strftime("%A"))
                except:
                    continue
        
        if hours:
            most_active_hour = max(set(hours), key=hours.count)
            most_active_day = max(set(days), key=days.count)
            
            return {
                "most_active_hour_utc": most_active_hour,
                "most_active_day": most_active_day,
                "total_posts_analyzed": len(hours),
                "activity_by_hour": {h: hours.count(h) for h in sorted(set(hours))},
                "activity_by_day": {d: days.count(d) for d in set(days)},
                "estimated_timezone": MetadataExtractor.estimate_timezone(most_active_hour)
            }
        
        return {"error": "No valid timestamps"}
    
    @staticmethod
    def estimate_timezone(most_active_hour: int) -> str:
        """Estimate timezone based on activity patterns"""
        if 9 <= most_active_hour <= 23:
            offset = most_active_hour - 15
            if offset > 0:
                return f"Likely UTC+{offset} to UTC+{offset+3}"
            else:
                return f"Likely UTC{offset} to UTC{offset+3}"
        else:
            return "Unable to estimate (unusual activity pattern)"

# ============================================================================
# REPORT GENERATOR
# ============================================================================

def generate_report(data: Dict, output_file: str = "holmes_report.txt"):
    """Generate a text report from OSINT data"""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("="*80 + "\n")
        f.write("MR. HOLMES - OSINT INVESTIGATION REPORT\n")
        f.write(f"Generated: {datetime.now().isoformat()}\n")
        f.write("="*80 + "\n\n")
        
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
        f.write("\n" + "="*80 + "\n")
        f.write("\"Elementary, my dear Watson!\" - Case Closed\n")
        f.write("="*80 + "\n")
    
    print_success(f"Report saved to: {output_file}")

# ============================================================================
# RESULT PRINTER
# ============================================================================

def print_results(data: Dict, title: str = "Results"):
    """Pretty print results - Holmes style"""
    print(f"\n{Colors.BRIGHT_YELLOW}{'═' * 70}{Colors.RESET}")
    print(f"{Colors.BRIGHT_CYAN}🔍 CASE FILE: {Colors.BRIGHT_WHITE}{title}{Colors.RESET}")
    print(f"{Colors.BRIGHT_YELLOW}{'═' * 70}{Colors.RESET}")
    
    def print_dict(d, indent=0):
        for key, value in d.items():
            if isinstance(value, dict):
                print("  " * indent + f"{Colors.BRIGHT_MAGENTA}📋 {key.replace('_', ' ').title()}:{Colors.RESET}")
                print_dict(value, indent + 1)
            elif isinstance(value, list):
                if value:
                    print("  " * indent + f"{Colors.BRIGHT_GREEN}📋 {key.replace('_', ' ').title()}: {Colors.BRIGHT_WHITE}{', '.join(map(str, value))}{Colors.RESET}")
            else:
                print("  " * indent + f"{Colors.BRIGHT_CYAN}📋 {key.replace('_', ' ').title()}: {Colors.BRIGHT_WHITE}{value}{Colors.RESET}")
    
    print_dict(data)
    print(f"{Colors.BRIGHT_YELLOW}{'═' * 70}{Colors.RESET}")
    print(f"{Colors.BRIGHT_GREEN}🔎 \"The facts, Watson, just the facts.\"{Colors.RESET}")
    print(f"{Colors.BRIGHT_YELLOW}{'═' * 70}{Colors.RESET}\n")

# ============================================================================
# MAIN APPLICATION
# ============================================================================

def main():
    """Main application entry point"""
    
    # Print animated logo
    print_animated_logo()
    
    parser = argparse.ArgumentParser(
        description=f'{Colors.BRIGHT_CYAN}Mr. Holmes - Advanced OSINT Investigation Tool{Colors.RESET}',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
{Colors.BRIGHT_YELLOW}═══════════════════════════════════════════════════════════════════════════{Colors.RESET}
{Colors.BRIGHT_CYAN}ELEMENTARY INVESTIGATION TECHNIQUES:{Colors.RESET}

{Colors.BRIGHT_GREEN}🔎 Username Investigation (NO API REQUIRED!):{Colors.RESET}
  python mr_holmes.py username --check johndoe

{Colors.BRIGHT_MAGENTA}🐦 Social Media Intelligence:{Colors.RESET}
  python mr_holmes.py twitter --user elonmusk
  python mr_holmes.py reddit --user spez --analyze-posts

{Colors.BRIGHT_CYAN}📷 Image Forensics:{Colors.RESET}
  python mr_holmes.py image --file photo.jpg
  python mr_holmes.py image --file photo.jpg --reverse-geocode
  python mr_holmes.py image --url https://example.com/image.jpg

{Colors.BRIGHT_YELLOW}🌍 Geolocation Tracking:{Colors.RESET}
  python mr_holmes.py geo --ip 8.8.8.8
  python mr_holmes.py geo --coords 40.7128 -74.0060

{Colors.BRIGHT_GREEN}📧 Contact Intelligence:{Colors.RESET}
  python mr_holmes.py email --analyze john@example.com
  python mr_holmes.py phone --analyze "+1-555-1234"

{Colors.BRIGHT_BLUE}🔗 URL Analysis:{Colors.RESET}
  python mr_holmes.py url --analyze https://example.com/page
  python mr_holmes.py url --expand https://bit.ly/abc123

{Colors.BRIGHT_RED}🔐 Hash Identification:{Colors.RESET}
  python mr_holmes.py hash --identify 5d41402abc4b2a76b9719d911017c592

{Colors.BRIGHT_MAGENTA}🕵️ Full Investigation:{Colors.RESET}
  python mr_holmes.py investigate --username USER --email EMAIL --report

{Colors.BRIGHT_YELLOW}═══════════════════════════════════════════════════════════════════════════
{Colors.BRIGHT_WHITE}"When you have eliminated the impossible, whatever remains,
however improbable, must be the truth." - Sherlock Holmes{Colors.RESET}
{Colors.BRIGHT_YELLOW}═══════════════════════════════════════════════════════════════════════════{Colors.RESET}
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Investigation command')
    
    # Username command
    username_parser = subparsers.add_parser('username', help='Username enumeration')
    username_parser.add_argument('--check', type=str, required=True, help='Username to investigate')
    
    # Twitter command
    twitter_parser = subparsers.add_parser('twitter', help='Twitter investigation')
    twitter_parser.add_argument('--user', type=str, required=True, help='Twitter username')
    twitter_parser.add_argument('--analyze-posts', action='store_true', help='Analyze posting patterns')
    
    # Reddit command
    reddit_parser = subparsers.add_parser('reddit', help='Reddit investigation')
    reddit_parser.add_argument('--user', type=str, required=True, help='Reddit username')
    reddit_parser.add_argument('--analyze-posts', action='store_true', help='Analyze posting patterns')
    
    # Image command
    image_parser = subparsers.add_parser('image', help='Image forensics')
    image_parser.add_argument('--file', type=str, help='Image file path')
    image_parser.add_argument('--url', type=str, help='Image URL')
    image_parser.add_argument('--reverse-geocode', action='store_true', help='Reverse geocode GPS data')
    
    # Geo command
    geo_parser = subparsers.add_parser('geo', help='Geolocation')
    geo_parser.add_argument('--ip', type=str, help='IP address')
    geo_parser.add_argument('--coords', nargs=2, type=float, metavar=('LAT', 'LON'), help='Coordinates')
    
    # Email command
    email_parser = subparsers.add_parser('email', help='Email analysis')
    email_parser.add_argument('--analyze', type=str, required=True, help='Email address')
    
    # Phone command
    phone_parser = subparsers.add_parser('phone', help='Phone analysis')
    phone_parser.add_argument('--analyze', type=str, required=True, help='Phone number')
    
    # URL command
    url_parser = subparsers.add_parser('url', help='URL analysis')
    url_parser.add_argument('--analyze', type=str, help='URL to analyze')
    url_parser.add_argument('--expand', type=str, help='Expand shortened URL')
    
    # Hash command
    hash_parser = subparsers.add_parser('hash', help='Hash identification')
    hash_parser.add_argument('--identify', type=str, required=True, help='Hash to identify')
    
    # Investigate command
    investigate_parser = subparsers.add_parser('investigate', help='Full investigation')
    investigate_parser.add_argument('--username', type=str, help='Username')
    investigate_parser.add_argument('--email', type=str, help='Email address')
    investigate_parser.add_argument('--phone', type=str, help='Phone number')
    investigate_parser.add_argument('--report', action='store_true', help='Generate report')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        print_detective_quote()
        return
    
    # Execute commands
    try:
        if args.command == 'username':
            print(f"\n{Colors.BRIGHT_GREEN}🔍 Elementary! Beginning username investigation...{Colors.RESET}")
            print_investigating_animation()
            results = UsernameEnumerator.check_username(args.check)
            print_detective_quote()
            
        elif args.command == 'twitter':
            print(f"\n{Colors.BRIGHT_BLUE}🐦 Investigating Twitter profile: @{args.user}{Colors.RESET}")
            print_investigating_animation()
            twitter = TwitterOSINT()
            result = twitter.search_user(args.user)
            
            if result:
                print_results(result, f"Twitter Profile: @{args.user}")
                
                if args.analyze_posts:
                    print(f"{Colors.BRIGHT_MAGENTA}📊 Observing behavioral patterns...{Colors.RESET}")
                    print_pipe_smoke()
                    posts = twitter.get_recent_tweets(result['user_id'])
                    if posts:
                        patterns = MetadataExtractor.analyze_posting_patterns(posts)
                        print_results(patterns, "Activity Pattern Analysis")
                        print(f"{Colors.BRIGHT_GREEN}🔍 \"Habits, Watson, are the key to understanding people.\"{Colors.RESET}")
        
        elif args.command == 'reddit':
            print(f"\n{Colors.BRIGHT_RED}🤖 Investigating Reddit profile: u/{args.user}{Colors.RESET}")
            print_investigating_animation()
            reddit = RedditOSINT()
            result = reddit.search_user(args.user)
            
            if result:
                print_results(result, f"Reddit Profile: u/{args.user}")
                
                if args.analyze_posts:
                    print(f"{Colors.BRIGHT_MAGENTA}📊 Studying the subject's patterns...{Colors.RESET}")
                    posts = reddit.get_user_posts(args.user)
                    if posts:
                        patterns = MetadataExtractor.analyze_posting_patterns(posts)
                        print_results(patterns, "Activity Pattern Analysis")
        
        elif args.command == 'image':
            if args.file:
                print(f"\n{Colors.BRIGHT_CYAN}📷 Examining photographic evidence: {args.file}{Colors.RESET}")
                print(f"{Colors.BRIGHT_YELLOW}🔎 Searching for hidden clues...{Colors.RESET}")
                print_investigating_animation()
                analyzer = ImageAnalyzer()
                result = analyzer.extract_exif(args.file)
                print_results(result, "Image Forensic Analysis")
                
                if args.reverse_geocode and 'latitude' in result and 'longitude' in result:
                    print(f"{Colors.BRIGHT_GREEN}🌍 Pinpointing the location...{Colors.RESET}")
                    geo = GeolocationAnalyzer()
                    location = geo.reverse_geocode(result['latitude'], result['longitude'])
                    if location:
                        print_results(location, "Location Identified")
            
            elif args.url:
                print(f"\n{Colors.BRIGHT_CYAN}🌐 Acquiring evidence from: {args.url}{Colors.RESET}")
                print_investigating_animation()
                analyzer = ImageAnalyzer()
                temp_path = analyzer.download_image(args.url)
                if temp_path:
                    result = analyzer.extract_exif(temp_path)
                    print_results(result, "Remote Image Analysis")
                    os.remove(temp_path)
                    print(f"{Colors.BRIGHT_GREEN}🔍 \"Evidence collected and analyzed, Watson!\"{Colors.RESET}")
        
        elif args.command == 'geo':
            if args.ip:
                print(f"\n{Colors.BRIGHT_YELLOW}🌍 Tracing network address: {args.ip}{Colors.RESET}")
                print(f"{Colors.BRIGHT_CYAN}🔎 Cross-referencing databases...{Colors.RESET}")
                print_investigating_animation()
                geo = GeolocationAnalyzer()
                result = geo.lookup_ip(args.ip)
                if result:
                    print_results(result, "IP Geolocation Intelligence")
            
            elif args.coords:
                lat, lon = args.coords
                print(f"\n{Colors.BRIGHT_YELLOW}📍 Reverse geocoding coordinates: {lat}, {lon}{Colors.RESET}")
                print(f"{Colors.BRIGHT_CYAN}🔎 Consulting my maps...{Colors.RESET}")
                print_investigating_animation()
                geo = GeolocationAnalyzer()
                result = geo.reverse_geocode(lat, lon)
                if result:
                    print_results(result, "Location Intelligence")
        
        elif args.command == 'email':
            print(f"\n{Colors.BRIGHT_MAGENTA}📧 Analyzing correspondence: {args.analyze}{Colors.RESET}")
            print(f"{Colors.BRIGHT_CYAN}🔎 Examining the evidence...{Colors.RESET}")
            print_investigating_animation()
            result = EmailAnalyzer.analyze_email(args.analyze)
            print_results(result, "Email Intelligence")
        
        elif args.command == 'phone':
            print(f"\n{Colors.BRIGHT_GREEN}📱 Tracing communication device: {args.analyze}{Colors.RESET}")
            print(f"{Colors.BRIGHT_CYAN}🔎 Cross-referencing databases...{Colors.RESET}")
            print_investigating_animation()
            result = PhoneAnalyzer.analyze_phone(args.analyze)
            print_results(result, "Phone Intelligence")
        
        elif args.command == 'url':
            if args.analyze:
                print(f"\n{Colors.BRIGHT_BLUE}🔗 Following the digital trail: {args.analyze}{Colors.RESET}")
                print(f"{Colors.BRIGHT_CYAN}🔎 Examining breadcrumbs...{Colors.RESET}")
                print_investigating_animation()
                result = URLAnalyzer.analyze_url(args.analyze)
                print_results(result, "URL Analysis")
            
            if args.expand:
                print(f"\n{Colors.BRIGHT_BLUE}🔗 Revealing the true destination: {args.expand}{Colors.RESET}")
                print(f"{Colors.BRIGHT_CYAN}🔎 Unmasking the redirect...{Colors.RESET}")
                print_investigating_animation()
                expanded = URLAnalyzer.expand_short_url(args.expand)
                if expanded:
                    print(f"{Colors.BRIGHT_GREEN}✅ Destination revealed: {expanded}{Colors.RESET}")
                else:
                    print(f"{Colors.BRIGHT_RED}❌ The trail has gone cold{Colors.RESET}")
        
        elif args.command == 'hash':
            print(f"\n{Colors.BRIGHT_RED}🔐 Deciphering the cipher: {args.identify}{Colors.RESET}")
            print(f"{Colors.BRIGHT_CYAN}🔎 Consulting my references...{Colors.RESET}")
            print_investigating_animation()
            hash_types = HashIdentifier.identify_hash(args.identify)
            print(f"{Colors.BRIGHT_GREEN}📋 Identification: {', '.join(hash_types)}{Colors.RESET}")
        
        elif args.command == 'investigate':
            print(f"\n{Colors.BRIGHT_MAGENTA}🕵️  Commencing full investigation...{Colors.RESET}")
            print(f"{Colors.BRIGHT_CYAN}🔎 Gathering all available evidence...{Colors.RESET}")
            print_pipe_smoke()
            investigation_data = {}
            
            if args.username:
                print(f"\n{Colors.BRIGHT_YELLOW}👤 Investigating subject: {args.username}{Colors.RESET}")
                investigation_data['username_check'] = UsernameEnumerator.check_username(args.username)
            
            if args.email:
                print(f"\n{Colors.BRIGHT_MAGENTA}📧 Analyzing correspondence: {args.email}{Colors.RESET}")
                investigation_data['email_analysis'] = EmailAnalyzer.analyze_email(args.email)
            
            if args.phone:
                print(f"\n{Colors.BRIGHT_GREEN}📱 Tracing communications: {args.phone}{Colors.RESET}")
                investigation_data['phone_analysis'] = PhoneAnalyzer.analyze_phone(args.phone)
            
            if args.report and investigation_data:
                filename = f"holmes_case_{args.username or 'unknown'}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                print(f"\n{Colors.BRIGHT_BLUE}📝 Preparing case file: {filename}{Colors.RESET}")
                generate_report(investigation_data, filename)
                print(f"\n{Colors.BRIGHT_GREEN}✅ Case closed! Report filed.{Colors.RESET}")
                print(f"{Colors.BRIGHT_YELLOW}🔍 \"Elementary, my dear Watson!\"{Colors.RESET}")
        
        # Final quote
        if args.command != 'investigate':
            print_detective_quote()
    
    except KeyboardInterrupt:
        print(f"\n\n{Colors.BRIGHT_RED}⚠️  Investigation interrupted!{Colors.RESET}")
        print(f"{Colors.BRIGHT_YELLOW}🔍 \"Perhaps another time, Watson.\"{Colors.RESET}\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.BRIGHT_RED}❌ Confound it! An error occurred: {str(e)}{Colors.RESET}")
        print(f"{Colors.BRIGHT_YELLOW}🔍 \"The plot thickens, Watson.\"{Colors.RESET}\n")
        sys.exit(1)

# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n{Colors.BRIGHT_RED}❌ Critical error: {str(e)}{Colors.RESET}\n")
        sys.exit(1)
