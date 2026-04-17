#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
抖音利润计算器 - 使用配置的成本数据
"""

import sys
import csv
import re
from collections import defaultdict
from .product_cost_config import get_product_cost, get_default_cost

def calculate_profit_from_csv(csv_file_path):
    """
    从CSV文件计算抖音销售利润
    """
    # 读取销售数据
    product_sales = defaultdict(lambda: {'quantity': 0, 'revenue': 0.0})
    
    with open(csv_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        if content.startswith('\ufeff'):
            f.seek(3)
        else:
            f.seek(0)
        
        reader = csv.DictReader(f)
        
        for row in reader:
            try:
                product_name = row.get('选购商品', '').strip()
                if not product_name or '【' not in product_name:
                    continue
                    
                clean_name = re.sub(r'【.*?】', '', product_name).split('-')[0].strip()
                
                order_status = row.get('订单状态', '').strip()
                quantity_str = row.get('商品数量', '').strip().replace('\t', '').replace(' ', '')
                if not quantity_str:
                    continue
                quantity = int(quantity_str)
                
                revenue_str = row.get('订单应付金额', '').strip().replace('\t', '').replace(' ', '')
                if not revenue_str:
                    continue
                revenue = float(revenue_str)
                
                if order_status == '已发货':
                    product_sales[clean_name]['quantity'] += quantity
                    product_sales[clean_name]['revenue'] += revenue
                    
            except (ValueError, KeyError) as e:
                continue
    
    # 计算利润
    total_revenue = 0
    total_costs = 0
    profit_details = []
    
    for product, data in product_sales.items():
        if data['quantity'] == 0:
            continue
            
        avg_price = data['revenue'] / data['quantity']
        cost_config = get_product_cost(product)
        
        if cost_config is None:
            # 使用默认成本计算
            cost_config = get_default_cost(avg_price)
            print(f"警告: {product} 未配置成本，使用默认计算")
        
        # 计算各项成本
        product_total_revenue = data['revenue']
        product_total_quantity = data['quantity']
        
        product_total_cost = product_total_quantity * cost_config['product_cost']
        logistics_total_cost = product_total_quantity * cost_config['logistics_cost']
        packaging_total_cost = product_total_quantity * cost_config['packaging_cost']
        douyin_commission = product_total_revenue * 0.05
        payment_fees = product_total_revenue * 0.01
        marketing_costs = product_total_revenue * 0.03
        
        total_product_costs = (product_total_cost + logistics_total_cost + packaging_total_cost + 
                              douyin_commission + payment_fees + marketing_costs)
        product_profit = product_total_revenue - total_product_costs
        profit_margin = (product_profit / product_total_revenue * 100) if product_total_revenue > 0 else 0
        
        profit_details.append({
            'product': product,
            'quantity': product_total_quantity,
            'revenue': product_total_revenue,
            'profit': product_profit,
            'margin': profit_margin,
            'cost_breakdown': {
                'product_cost': product_total_cost,
                'logistics_cost': logistics_total_cost,
                'packaging_cost': packaging_total_cost,
                'douyin_commission': douyin_commission,
                'payment_fees': payment_fees,
                'marketing_costs': marketing_costs
            }
        })
        
        total_revenue += product_total_revenue
        total_costs += total_product_costs
    
    return {
        'total_revenue': total_revenue,
        'total_costs': total_costs,
        'net_profit': total_revenue - total_costs,
        'profit_margin': (total_revenue - total_costs) / total_revenue * 100 if total_revenue > 0 else 0,
        'details': profit_details
    }

def main():
    if len(sys.argv) != 2:
        print("用法: python calculate_profit.py <销售数据CSV文件>")
        sys.exit(1)
    
    csv_file = sys.argv[1]
    result = calculate_profit_from_csv(csv_file)
    
    print("=== 抖音销售利润分析报告 ===")
    print(f"总销售额: ¥{result['total_revenue']:.2f}")
    print(f"净利润: ¥{result['net_profit']:.2f}")
    print(f"利润率: {result['profit_margin']:.2f}%")
    print()
    
    print("=== 各产品详情 ===")
    for detail in result['details']:
        print(f"{detail['product']}:")
        print(f"  销售额: ¥{detail['revenue']:.2f}")
        print(f"  净利润: ¥{detail['profit']:.2f}")
        print(f"  利润率: {detail['margin']:.2f}%")

if __name__ == "__main__":
    main()