#!/usr/bin/env python3
"""
Mr. Holmes - Advanced OSINT Investigation Tool
"The world is full of obvious things which nobody observes"
Educational/Research Purpose Only
"""

import requests
import json
import argparse
from datetime import datetime, timezone
from typing import Dict, List, Optional, Tuple
import sys
import os
from pathlib import Path
import re
from sherlock_logo import print_logo, print_magnifying_glass

try:
    import exifread
    from PIL import Image
    from PIL.ExifTags import TAGS, GPSTAGS
except ImportError:
    print("⚠️  Some image analysis features require additional packages.")
    print("Run: pip install Pillow exifread")

class OSINTTool:
    def __init__(self):
        self.config = self.load_config()
        
    def load_config(self) -> Dict:
        """Load API credentials from config file"""
        try:
            with open('config.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print("⚠️  config.json not found. Creating template...")
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
                "user_agent": "OSINT Tool v2.0"
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
        print("✅ Created config.json template. Please add your API credentials.")

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
                print(f"❌ Error: {response.status_code} - {response.text}")
                return None
        except Exception as e:
            print(f"❌ Exception: {str(e)}")
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
            print(f"❌ Exception getting tweets: {str(e)}")
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
                print(f"❌ Failed to get Reddit token: {response.status_code}")
                return ""
        except Exception as e:
            print(f"❌ Exception getting token: {str(e)}")
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
                print(f"❌ Error: {response.status_code}")
                return None
        except Exception as e:
            print(f"❌ Exception: {str(e)}")
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
            print(f"❌ Exception getting posts: {str(e)}")
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
            # Using PIL
            image = Image.open(image_path)
            exif_data = image._getexif()
            
            if exif_data:
                for tag_id, value in exif_data.items():
                    tag = TAGS.get(tag_id, tag_id)
                    
                    # Handle GPS data separately
                    if tag == "GPSInfo":
                        gps_data = {}
                        for gps_tag_id in value:
                            gps_tag = GPSTAGS.get(gps_tag_id, gps_tag_id)
                            gps_data[gps_tag] = value[gps_tag_id]
                        result["gps_data"] = gps_data
                    else:
                        # Convert to string to handle various data types
                        result["exif_data"][tag] = str(value)
                
                # Extract GPS coordinates if available
                if result["gps_data"]:
                    coords = ImageAnalyzer.parse_gps_coordinates(result["gps_data"])
                    if coords:
                        result["latitude"] = coords[0]
                        result["longitude"] = coords[1]
                        result["coordinates"] = f"{coords[0]}, {coords[1]}"
                        result["google_maps"] = f"https://www.google.com/maps?q={coords[0]},{coords[1]}"
            
            # Get basic image info
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
                """Convert GPS coordinates to degrees"""
                d, m, s = value
                return float(d) + float(m) / 60.0 + float(s) / 3600.0
            
            lat = convert_to_degrees(gps_data.get('GPSLatitude', [0, 0, 0]))
            lon = convert_to_degrees(gps_data.get('GPSLongitude', [0, 0, 0]))
            
            # Check for hemisphere
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
            print(f"❌ Error downloading image: {str(e)}")
        return ""

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
            
            # Handle different post structures
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
        # Most people are active during daytime (9 AM - 11 PM local time)
        # This is a rough estimation
        if 9 <= most_active_hour <= 23:
            offset = most_active_hour - 15  # Assuming peak activity at 3 PM
            if offset > 0:
                return f"Likely UTC+{offset} to UTC+{offset+3}"
            else:
                return f"Likely UTC{offset} to UTC{offset+3}"
        else:
            return "Unable to estimate (unusual activity pattern)"
    
    @staticmethod
    def extract_urls_from_text(text: str) -> List[str]:
        """Extract URLs from text"""
        url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        return re.findall(url_pattern, text)
    
    @staticmethod
    def extract_mentions(text: str) -> Dict:
        """Extract mentions and hashtags"""
        mentions = re.findall(r'@(\w+)', text)
        hashtags = re.findall(r'#(\w+)', text)
        
        return {
            "mentions": mentions,
            "hashtags": hashtags,
            "mention_count": len(mentions),
            "hashtag_count": len(hashtags)
        }

def print_results(data: Dict, title: str = "Results"):
    """Pretty print results - Holmes style"""
    print("\n" + "="*70)
    print(f"🔍 CASE FILE: {title}")
    print("="*70)
    
    def print_dict(d, indent=0):
        for key, value in d.items():
            if isinstance(value, dict):
                print("  " * indent + f"📋 {key.replace('_', ' ').title()}:")
                print_dict(value, indent + 1)
            elif isinstance(value, list):
                print("  " * indent + f"📋 {key.replace('_', ' ').title()}: {', '.join(map(str, value))}")
            else:
                print("  " * indent + f"📋 {key.replace('_', ' ').title()}: {value}")
    
    print_dict(data)
    print("="*70)
    print("🔎 \"The facts, Watson, just the facts.\"")
    print("="*70 + "\n")

def main():
    parser = argparse.ArgumentParser(
        description='Social Media OSINT Tool - Enhanced Version',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Social Media Analysis
  python osint_tool.py --twitter-user elonmusk
  python osint_tool.py --reddit-user spez
  python osint_tool.py --twitter-user elonmusk --analyze-posts
  
  # Image Analysis
  python osint_tool.py --extract-exif image.jpg
  python osint_tool.py --extract-exif image.jpg --reverse-geocode
  
  # Geolocation
  python osint_tool.py --lookup-ip 8.8.8.8
  python osint_tool.py --geocode 40.7128 -74.0060
  
  # Timestamp Analysis
  python osint_tool.py --analyze-time "2024-01-15T10:30:00Z"

Note: Requires valid API credentials in config.json
        """
    )
    
    # Social Media Arguments
    parser.add_argument('--twitter-user', type=str, help='Twitter username to analyze')
    parser.add_argument('--reddit-user', type=str, help='Reddit username to analyze')
    parser.add_argument('--analyze-posts', action='store_true', help='Analyze posting patterns')
    
    # Image Analysis Arguments
    parser.add_argument('--extract-exif', type=str, help='Extract EXIF from image file')
    parser.add_argument('--image-url', type=str, help='Download and analyze image from URL')
    
    # Geolocation Arguments
    parser.add_argument('--lookup-ip', type=str, help='Lookup IP address geolocation')
    parser.add_argument('--geocode', nargs=2, type=float, metavar=('LAT', 'LON'), 
                       help='Reverse geocode coordinates')
    parser.add_argument('--reverse-geocode', action='store_true', 
                       help='Reverse geocode GPS data from EXIF')
    
    # Metadata Arguments
    parser.add_argument('--analyze-time', type=str, help='Analyze timestamp (ISO format)')
    
    args = parser.parse_args()
    
    if not any(vars(args).values()):
        parser.print_help()
        return
    
    # Twitter search
    if args.twitter_user:
        print(f"🐦 Elementary! Investigating Twitter profile: @{args.twitter_user}")
        print_magnifying_glass() if 'print_magnifying_glass' in dir() else None
        twitter = TwitterOSINT()
        result = twitter.search_user(args.twitter_user)
        
        if result:
            print_results(result, f"Twitter Profile: @{args.twitter_user}")
            
            if args.analyze_posts:
                print("📊 Observing behavioral patterns...")
                posts = twitter.get_recent_tweets(result['user_id'])
                if posts:
                    patterns = MetadataExtractor.analyze_posting_patterns(posts)
                    print_results(patterns, "Activity Pattern Analysis")
                    print("🔍 \"Habits, Watson, are the key to understanding people.\"")
    
    # Reddit search
    if args.reddit_user:
        print(f"🤖 Investigating Reddit profile: u/{args.reddit_user}")
        reddit = RedditOSINT()
        result = reddit.search_user(args.reddit_user)
        
        if result:
            print_results(result, f"Reddit Profile: u/{args.reddit_user}")
            
            if args.analyze_posts:
                print("📊 Studying the subject's patterns...")
                posts = reddit.get_user_posts(args.reddit_user)
                if posts:
                    patterns = MetadataExtractor.analyze_posting_patterns(posts)
                    print_results(patterns, "Activity Pattern Analysis")
    
    # Image EXIF extraction
    if args.extract_exif:
        print(f"📷 Examining photographic evidence: {args.extract_exif}")
        print("🔎 Searching for hidden clues...")
        analyzer = ImageAnalyzer()
        result = analyzer.extract_exif(args.extract_exif)
        print_results(result, "Image Forensic Analysis")
        
        if args.reverse_geocode and 'latitude' in result and 'longitude' in result:
            print("🌍 Pinpointing the location...")
            geo = GeolocationAnalyzer()
            location = geo.reverse_geocode(result['latitude'], result['longitude'])
            if location:
                print_results(location, "Location Identified")
    
    # Image URL analysis
    if args.image_url:
        print(f"🌐 Acquiring evidence from: {args.image_url}")
        analyzer = ImageAnalyzer()
        temp_path = analyzer.download_image(args.image_url)
        if temp_path:
            result = analyzer.extract_exif(temp_path)
            print_results(result, "Remote Image Analysis")
            os.remove(temp_path)
            print("🔍 \"Evidence collected and analyzed, Watson!\"")
    
    # IP lookup
    if args.lookup_ip:
        print(f"🌍 Tracing network address: {args.lookup_ip}")
        print("🔎 Cross-referencing databases...")
        geo = GeolocationAnalyzer()
        result = geo.lookup_ip(args.lookup_ip)
        if result:
            print_results(result, "IP Geolocation Intelligence")
    
    # Reverse geocoding
    if args.geocode:
        lat, lon = args.geocode
        print(f"📍 Reverse geocoding coordinates: {lat}, {lon}")
        print("🔎 Consulting my maps...")
        geo = GeolocationAnalyzer()
        result = geo.reverse_geocode(lat, lon)
        if result:
            print_results(result, "Location Intelligence")
    
    # Timestamp analysis
    if args.analyze_time:
        print(f"🕐 Analyzing temporal evidence: {args.analyze_time}")
        extractor = MetadataExtractor()
        result = extractor.analyze_timezone(args.analyze_time)
        print_results(result, "Chronological Analysis")

if __name__ == "__main__":
    main()
