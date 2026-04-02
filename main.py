#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Douyin Profit Calculator Skill Main File
"""

import os
import sys
import subprocess

def main():
    """Skill main entry point"""
    original_script = "/root/.openclaw/workspace/douyin_profit_calculator.py"
    
    if not os.path.exists(original_script):
        print("Error: Douyin profit calculator script not found")
        print(f"Please ensure script exists at: {original_script}")
        return 1
    
    if len(sys.argv) > 1:
        cmd = [sys.executable, original_script] + sys.argv[1:]
        result = subprocess.run(cmd)
        return result.returncode
    else:
        print("🎯 Douyin Profit Calculator Skill")
        print("=" * 50)
        print("Usage:")
        print("  douyin-profit-calculator /path/to/order_file.xlsx")
        print("  douyin-profit-calculator --help")
        print("")
        print("Features:")
        print("  • Automatic Douyin order profit calculation")
        print("  • Intelligent specification matching")
        print("  • Detailed profit report generation")
        print("=" * 50)
        return 0

if __name__ == "__main__":
    sys.exit(main())