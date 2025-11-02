#!/usr/bin/env python3
"""
Batch Analysis Script
Analyze multiple targets at once and generate comprehensive report
"""

import json
from datetime import datetime
from osint_tool import TwitterOSINT, RedditOSINT, MetadataExtractor
from advanced_utils import UsernameEnumerator, EmailAnalyzer, generate_report

def batch_username_analysis(usernames: list) -> dict:
    """Analyze multiple usernames"""
    results = {}
    
    for username in usernames:
        print(f"\n{'='*60}")
        print(f"Analyzing: {username}")
        print('='*60)
        
        # Check across platforms
        platform_results = UsernameEnumerator.check_username(username)
        
        # Try Twitter
        try:
            twitter = TwitterOSINT()
            twitter_data = twitter.search_user(username)
            if twitter_data:
                platform_results['twitter_profile'] = twitter_data
        except:
            pass
        
        # Try Reddit
        try:
            reddit = RedditOSINT()
            reddit_data = reddit.search_user(username)
            if reddit_data:
                platform_results['reddit_profile'] = reddit_data
        except:
            pass
        
        results[username] = platform_results
    
    return results

def batch_email_analysis(emails: list) -> dict:
    """Analyze multiple email addresses"""
    results = {}
    
    for email in emails:
        print(f"\nAnalyzing email: {email}")
        results[email] = EmailAnalyzer.analyze_email(email)
    
    return results

def main():
    """Example batch analysis"""
    
    # Define targets
    targets = {
        'usernames': ['example_user1', 'example_user2'],
        'emails': ['test1@example.com', 'test2@example.com']
    }
    
    print("="*60)
    print("BATCH OSINT ANALYSIS")
    print(f"Started: {datetime.now().isoformat()}")
    print("="*60)
    
    all_results = {}
    
    # Analyze usernames
    if targets['usernames']:
        print("\n\n📊 ANALYZING USERNAMES...")
        all_results['username_analysis'] = batch_username_analysis(targets['usernames'])
    
    # Analyze emails
    if targets['emails']:
        print("\n\n📧 ANALYZING EMAILS...")
        all_results['email_analysis'] = batch_email_analysis(targets['emails'])
    
    # Generate report
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_filename = f"batch_report_{timestamp}.txt"
    generate_report(all_results, report_filename)
    
    # Also save as JSON
    json_filename = f"batch_report_{timestamp}.json"
    with open(json_filename, 'w') as f:
        json.dump(all_results, f, indent=2)
    
    print(f"\n✅ Analysis complete!")
    print(f"   Text report: {report_filename}")
    print(f"   JSON report: {json_filename}")

if __name__ == "__main__":
    main()
