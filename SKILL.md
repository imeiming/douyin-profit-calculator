---
name: douyin-profit-calculator
description: Calculate profit margins for Douyin (TikTok) orders based on cost data files with automatic specification matching.
metadata:
  {
    "openclaw":
      {
        "emoji": "💰",
        "requires": { "bins": ["python3"], "env": [] }
      },
  }
---
# Douyin Profit Calculator

Calculate profit margins for Douyin (TikTok) orders based on cost data files with automatic specification matching.

## Trigger Conditions

Activate this skill when the user mentions:
- douyin profit calculation
- calculate douyin order profit
- douyin cost analysis
- 抖音利润计算
- 计算抖音订单利润

## Features

- Automatic order file recognition (Excel format)
- Intelligent specification matching (90/180/240/330cm, etc.)
- Invalid order filtering (pending payment, closed status)
- Accurate profit formula: (Order Amount × 0.95) + Platform Subsidy - Product Cost - Shipping Cost - Packaging Cost
- Batch processing of multiple order files
- Detailed profit reports generation

## Usage

### Basic Usage
```bash
# Calculate profit for single order file
douyin-profit-calculator /path/to/order_file.xlsx

# Batch process all order files in directory
douyin-profit-calculator /path/to/orders/
```

### Parameters
- `--cost-file`: Specify cost data file path (default: cost_data.xlsx)
- `--output-dir`: Specify output directory (default: current directory)
- `--verbose`: Show detailed calculation process

## Dependencies

- `cost_data.xlsx`: Cost data file containing product specifications, costs, shipping fees
- Python 3.6+
- pandas, openpyxl libraries

## Notes

- Order files must contain required columns: order status, product quantity, order amount, product specifications
- Cost data file should be updated regularly to reflect current costs
- Profit calculations are for reference only; actual profits may vary due to other factors