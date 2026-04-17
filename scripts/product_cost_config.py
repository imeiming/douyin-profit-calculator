#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
产品成本配置文件
根据最新成本Excel文件逐行提取，不进行任何合并或总结
"""

# 产品成本配置字典（严格按照原始表格的每一行）
# 格式: {'完整产品名称': {'product_cost': 商品成本, 'logistics_cost': 物流成本, 'packaging_cost': 包装成本}}
PRODUCT_COST_CONFIG = {
    # 百家布床盖系列（已修正）
    '【百家布】双人四季加厚防滑柔软亲肤透气床盖-百家布/200cm*230cm': {
        'product_cost': 34.0,
        'logistics_cost': 3.6,
        'packaging_cost': 0.5
    },
    '【百家布】双人四季加厚防滑柔软亲肤透气床盖-百家布三件套(枕套+床盖)/200cm*230cm': {
        'product_cost': 47.0,
        'logistics_cost': 3.6,
        'packaging_cost': 0.5
    },
    '【百家布】加大四季加厚防滑柔软亲肤透气床盖-百家布/230cm*250cm': {
        'product_cost': 43.0,
        'logistics_cost': 4.5,
        'packaging_cost': 0.5
    },
    '【百家布】加大四季加厚防滑柔软亲肤透气床盖-百家布三件套(枕套+床盖)/230cm*250cm': {
        'product_cost': 56.0,
        'logistics_cost': 4.5,
        'packaging_cost': 0.5
    },
    '【百家布】四季通用柔顺亲肤碎花风信封式枕套-百家布枕套/48*74': {
        'product_cost': 11.8,
        'logistics_cost': 1.7,
        'packaging_cost': 0.5
    },
    '【百家布垫】单人四季加厚防滑柔软亲肤透气多功能垫-百家布垫子/90cm*220cm': {
        'product_cost': 13.5,
        'logistics_cost': 2.5,
        'packaging_cost': 0.5
    },
    '【百家布夏凉被】美式复古 单双人百福拼块 夏凉被 两用 空调被-200cm*230cm': {
        'product_cost': 39.0,
        'logistics_cost': 4.5,
        'packaging_cost': 0.5
    },
    '【百家布夏凉被】美式复古 单双人百福拼块 夏凉被 两用 空调被-150cm*200cm': {
        'product_cost': 32.0,
        'logistics_cost': 4.5,
        'packaging_cost': 0.5
    },
    
    # 沙发巾系列（正确配置）
    # 90.180±5cm 规格
    '【繁花】沙发巾四季通用北欧简约现代沙发毯坐垫90.180±5cm-默认': {
        'product_cost': 6.5,
        'logistics_cost': 1.7,
        'packaging_cost': 0.25
    },
    '【多彩南瓜】升级版加厚加密艺术品沙发巾刺绣编织提花90.180±5cm-默认': {
        'product_cost': 6.5,
        'logistics_cost': 1.7,
        'packaging_cost': 0.25
    },
    '【福气】沙发巾四季通用棉麻沙发巾浴巾可铺可盖90.180±5cm-默认': {
        'product_cost': 6.5,
        'logistics_cost': 1.7,
        'packaging_cost': 0.25
    },
    '【花园】沙发巾高级提花工艺防滑纱布浴巾可铺可盖沙发垫90.180±5cm-默认': {
        'product_cost': 6.5,
        'logistics_cost': 1.7,
        'packaging_cost': 0.25
    },
    '【蓝色油画】新款沙发巾棉麻四季通用高档百搭盖巾90.180±5cm-默认': {
        'product_cost': 6.5,
        'logistics_cost': 1.7,
        'packaging_cost': 0.25
    },
    '【年年有余】沙发巾棉麻沙发垫四季通用90.180±5cm-默认': {
        'product_cost': 6.5,
        'logistics_cost': 1.7,
        'packaging_cost': 0.25
    },
    '【圣诞老人】新款圣诞高颜值盖毯个性时尚四季通用90.180±5cm-默认': {
        'product_cost': 6.5,
        'logistics_cost': 1.7,
        'packaging_cost': 0.25
    },
    '【熊猫】卡通沙发巾加厚加密防滑坐垫四季通用90.180±5cm-默认': {
        'product_cost': 6.5,
        'logistics_cost': 1.7,
        'packaging_cost': 0.25
    },
    '【捡漏】孤品棉麻沙发巾不挑不选现代防滑坐垫沙发巾盖毯90.180±5cm-默认': {
        'product_cost': 6.5,
        'logistics_cost': 1.7,
        'packaging_cost': 0.25
    },
    '[朵颜】沙发巾四季通用北欧简约现代沙发毯坐垫80.180±5cm-默认': {
        'product_cost': 6.5,
        'logistics_cost': 1.7,
        'packaging_cost': 0.25
    },
    '【吉祥大象】升级版加厚加密艺术品沙发巾刺绣编织提花90.180±5cm-默认': {
        'product_cost': 6.5,
        'logistics_cost': 1.7,
        'packaging_cost': 0.25
    },
    '（孤品沙发巾）艺术品沙发巾刺绣编织提花90.180±5cm-默认': {
        'product_cost': 6.5,
        'logistics_cost': 1.7,
        'packaging_cost': 0.25
    },
    '【繁花1】沙发巾四季通用北欧简约现代沙发毯坐垫90.180±5cm-默认': {
        'product_cost': 6.5,
        'logistics_cost': 1.7,
        'packaging_cost': 0.25
    },
    '【多彩南瓜1】升级版加厚加密艺术品沙发巾刺绣编织提花90.180±5cm-默认': {
        'product_cost': 6.5,
        'logistics_cost': 1.7,
        'packaging_cost': 0.25
    },
    '【繁花2】90.180±5cm沙发巾四季通用北欧简约现代沙发毯坐垫-默认': {
        'product_cost': 6.5,
        'logistics_cost': 1.7,
        'packaging_cost': 0.25
    },
    
    # 90.240±5cm 规格
    '【繁花】沙发巾四季通用北欧简约现代沙发毯坐垫90.240±5cm-默认': {
        'product_cost': 10.5,
        'logistics_cost': 2.5,
        'packaging_cost': 0.25
    },
    '【多彩南瓜】升级版加厚加密艺术品沙发巾刺绣编织提花90.240±5cm-默认': {
        'product_cost': 10.5,
        'logistics_cost': 2.5,
        'packaging_cost': 0.25
    },
    '【花园】沙发巾高级提花工艺防滑纱布浴巾可盖可盖沙发垫90.240±5cm-默认': {
        'product_cost': 10.5,
        'logistics_cost': 2.5,
        'packaging_cost': 0.25
    },
    '【蓝色油画】新款沙发巾四季通用高档百搭盖巾90.240±5cm-默认': {
        'product_cost': 10.5,
        'logistics_cost': 2.5,
        'packaging_cost': 0.25
    },
    '【吉祥大象】升级版加厚加密艺术品沙发巾刺绣编织提花90.240±5cm-默认': {
        'product_cost': 10.5,
        'logistics_cost': 2.5,
        'packaging_cost': 0.25
    },
    '【繁花1】沙发巾四季通用北欧简约现代沙发毯坐垫90.240±5cm-默认': {
        'product_cost': 10.5,
        'logistics_cost': 2.5,
        'packaging_cost': 0.25
    },
    '【繁花2】90.240±5cm沙发巾四季通用北欧简约现代沙发毯坐垫-默认': {
        'product_cost': 10.5,
        'logistics_cost': 2.5,
        'packaging_cost': 0.25
    },
    
    # 90.330±5cm 规格  
    '【繁花】沙发巾四季通用北欧简约现代沙发毯坐垫90.330±5cm-默认': {
        'product_cost': 17.5,
        'logistics_cost': 2.5,
        'packaging_cost': 0.25
    },
    '【多彩南瓜】升级版加厚加密艺术品沙发巾刺绣编织提花90.330±5cm-默认': {
        'product_cost': 17.5,
        'logistics_cost': 2.5,
        'packaging_cost': 0.25
    },
    '【繁花1】沙发巾四季通用北欧简约现代沙发毯坐垫90.330±5cm-默认': {
        'product_cost': 17.5,
        'logistics_cost': 2.5,
        'packaging_cost': 0.25
    },
    '【多彩南瓜1】升级版加厚加密艺术品沙发巾刺绣编织提花90.330±5cm-默认': {
        'product_cost': 17.5,
        'logistics_cost': 2.5,
        'packaging_cost': 0.25
    },
    '【牡丹蝴蝶】升级版加厚加密艺术品沙发巾刺绣编织提花90.330±5cm-默认': {
        'product_cost': 17.5,
        'logistics_cost': 2.5,
        'packaging_cost': 0.25
    },
    '【繁花2】90.330±5cm沙发巾四季通用北欧简约现代沙发毯坐垫-默认': {
        'product_cost': 17.5,
        'logistics_cost': 2.5,
        'packaging_cost': 0.25
    },
    
    # 90.90±5cm 规格
    '【繁花】沙发巾四季通用北欧简约现代沙发毯坐垫90.90±5cm-默认': {
        'product_cost': 4.5,
        'logistics_cost': 1.7,
        'packaging_cost': 0.25
    },
    '【多彩南瓜】升级版加厚加密艺术品沙发巾刺绣编织提花90.90±5cm-默认': {
        'product_cost': 4.5,
        'logistics_cost': 1.7,
        'packaging_cost': 0.25
    },
    '【繁花1】沙发巾四季通用北欧简约现代沙发毯坐垫90.90±5cm-默认': {
        'product_cost': 4.5,
        'logistics_cost': 1.7,
        'packaging_cost': 0.25
    },
    '【繁花2】90.90±5cm沙发巾四季通用北欧简约现代沙发毯坐垫-默认': {
        'product_cost': 4.5,
        'logistics_cost': 1.7,
        'packaging_cost': 0.25
    }
}

# 默认成本（用于未匹配的产品）
DEFAULT_COST_CONFIG = {
    'product_cost_rate': 0.40,  # 商品成本占售价的40%
    'logistics_cost': 8.0,      # 默认物流成本
    'packaging_cost': 0.5       # 默认包装成本
}

def get_product_cost(product_name):
    """
    根据完整产品名称获取成本配置
    严格匹配，不进行模糊匹配
    """
    # 直接查找完整匹配
    if product_name in PRODUCT_COST_CONFIG:
        return PRODUCT_COST_CONFIG[product_name]
    
    # 如果没有完全匹配，返回None表示使用默认计算方式
    return None

def get_default_cost(sale_price):
    """
    根据售价计算默认成本
    """
    return {
        'product_cost': sale_price * DEFAULT_COST_CONFIG['product_cost_rate'],
        'logistics_cost': DEFAULT_COST_CONFIG['logistics_cost'],
        'packaging_cost': DEFAULT_COST_CONFIG['packaging_cost']
    }

if __name__ == "__main__":
    # 测试配置
    test_products = [
        '【百家布】双人四季加厚防滑柔软亲肤透气床盖-百家布/200cm*230cm',
        '【百家布】双人四季加厚防滑柔软亲肤透气床盖-百家布三件套(枕套+床盖)/200cm*230cm', 
        '【繁花】沙发巾四季通用北欧简约现代沙发毯坐垫90.180±5cm-默认',
        '【繁花】沙发巾四季通用北欧简约现代沙发毯坐垫90.240±5cm-默认',
        '【繁花】沙发巾四季通用北欧简约现代沙发毯坐垫90.330±5cm-默认',
        '【繁花】沙发巾四季通用北欧简约现代沙发毯坐垫90.90±5cm-默认'
    ]
    
    for product in test_products:
        cost = get_product_cost(product)
        if cost:
            total_cost = cost['product_cost'] + cost['logistics_cost'] + cost['packaging_cost']
            print(f"{product}:")
            print(f"  商品成本: ¥{cost['product_cost']}")
            print(f"  物流成本: ¥{cost['logistics_cost']}")  
            print(f"  包装成本: ¥{cost['packaging_cost']}")
            print(f"  总成本: ¥{total_cost}")
            print()
        else:
            print(f"{product}: 未找到成本配置")