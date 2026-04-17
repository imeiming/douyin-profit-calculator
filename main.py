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
    # 获取技能目录中的成本文件
    skill_dir = os.path.dirname(os.path.abspath(__file__))
    cost_file_in_skill = os.path.join(skill_dir, "cost_data.xlsx")
    
    original_script = "/root/.openclaw/workspace/douyin_profit_calculator.py"
    
    if not os.path.exists(original_script):
        print("Error: Douyin profit calculator script not found")
        print(f"Please ensure script exists at: {original_script}")
        return 1
    
    # 如果用户没有指定成本文件，且技能目录中有成本文件，则使用它
    args = sys.argv[1:]
    has_cost_arg = any(arg.startswith('--cost-file') for arg in args)
    
    if not has_cost_arg and os.path.exists(cost_file_in_skill):
        args.extend(['--cost-file', cost_file_in_skill])
    
    if len(args) > 0:
        cmd = [sys.executable, original_script] + args
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
        print("")
        print("Note: Includes sample cost_data.xlsx for immediate use")
        print("=" * 50)
        return 0

if __name__ == "__main__":
    sys.exit(main())