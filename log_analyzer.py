#!/usr/bin/env python3
"""
Log Analyzer Simulation Tool
Purpose: Demonstrates file reading, pattern matching, and data aggregation.
Safe for Termux: Uses only standard libraries.
"""

import re
import os
from collections import Counter

def create_dummy_log(filename):
    """Creates a sample log file to test the analyzer."""
    print(f"[+] Creating dummy log file: {filename}...")
    
    dummy_logs = [
        "2026-05-01 10:00:01 INFO User login successful from 192.168.1.5",
        "2026-05-01 10:00:05 WARNING Failed login attempt from 10.0.0.22",
        "2026-05-01 10:00:10 ERROR Database connection timeout",
        "2026-05-01 10:00:15 INFO User logout from 192.168.1.5",
        "2026-05-01 10:00:20 WARNING Failed login attempt from 10.0.0.22",
        "2026-05-01 10:00:25 INFO New connection from 172.16.0.10",
        "2026-05-01 10:00:30 ERROR File not found: config.json",
        "2026-05-01 10:00:35 WARNING Failed login attempt from 10.0.0.22",
        "2026-05-01 10:00:40 INFO System backup started",
        "2026-05-01 10:00:45 ERROR Disk space critical on /dev/sda1"
    ]
    
    with open(filename, 'w') as f:
        f.write('\n'.join(dummy_logs))
    
    print(f"[✓] Created {filename} with {len(dummy_logs)} lines.")

def analyze_log(filename):
    """Reads the log file and extracts patterns."""
    if not os.path.exists(filename):
        print(f"[!] Error: File '{filename}' not found.")
        return

    print(f"\n[+] Analyzing {filename}...")
    
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    error_pattern = r'ERROR'
    warning_pattern = r'WARNING'
    
    ips_found = []
    error_count = 0
    warning_count = 0
    
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            
        for line in lines:
            # Find IPs
            matches = re.findall(ip_pattern, line)
            ips_found.extend(matches)
            
            # Count Errors/Warnings
            if re.search(error_pattern, line):
                error_count += 1
            if re.search(warning_pattern, line):
                warning_count += 1
                
    except Exception as e:
        print(f"[!] Error reading file: {e}")
        return

    # Display Results
    print_header("Analysis Results")
    print(f"Total Lines Processed: {len(lines)}")
    print(f"Unique IP Addresses Found: {len(set(ips_found))}")
    print(f"Total Errors: {error_count}")
    print(f"Total Warnings: {warning_count}")
    
    if ips_found:
        print("\n[+] Top IP Addresses:")
        counter = Counter(ips_found)
        for ip, count in counter.most_common(3):
            print(f"    {ip}: {count} occurrences")

def print_header(text):
    print(f"\n{'='*30}")
    print(f"  {text}")
    print(f"{'='*30}\n")

def main():
    log_file = "test_system.log"
    
    # Step 1: Create the data
    create_dummy_log(log_file)
    
    # Step 2: Analyze the data
    analyze_log(log_file)
    
    print("\n[✓] Test completed successfully!")
    print("Tip: You can now edit 'test_system.log' and run this again to see different results.")

if __name__ == "__main__":
    main()
