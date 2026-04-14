#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
法律条文版本校验脚本
用于校验使用的法律条文版本是否为最新版本
"""

import json
import os
from datetime import datetime

CONFIG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'law-version.json')

def load_config():
    """加载版本配置文件"""
    try:
        with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"加载版本配置文件失败: {e}")
        return None

def check_law_version(law_name, used_version):
    """
    校验法律条文版本是否为最新
    :param law_name: 法律条文名称
    :param used_version: 当前使用的版本
    :return: 校验结果字典
    """
    config = load_config()
    if not config:
        return {"status": "error", "message": "版本配置文件加载失败"}

    for law in config.get('laws', []):
        if law.get('name') == law_name or law_name in law.get('name'):
            current_version = law.get('current_version')
            effective_date = law.get('effective_date')
            previous_version = law.get('previous_version')

            if used_version == current_version:
                return {
                    "status": "success",
                    "message": f"您使用的《{law_name}》{used_version}为最新版本，生效日期：{effective_date}",
                    "is_latest": True
                }
            elif used_version == previous_version:
                return {
                    "status": "warning",
                    "message": f"注意：您使用的《{law_name}》{used_version}已失效，最新版本为{current_version}，生效日期：{effective_date}",
                    "is_latest": False,
                    "latest_version": current_version,
                    "effective_date": effective_date
                }
            else:
                return {
                    "status": "warning",
                    "message": f"注意：您使用的《{law_name}》{used_version}不是最新版本，最新版本为{current_version}，生效日期：{effective_date}",
                    "is_latest": False,
                    "latest_version": current_version,
                    "effective_date": effective_date
                }

    return {
        "status": "not_found",
        "message": f"未找到《{law_name}》的版本信息，请确认名称是否正确",
        "is_latest": None
    }

def get_latest_version(law_name):
    """获取指定法律的最新版本"""
    config = load_config()
    if not config:
        return None

    for law in config.get('laws', []):
        if law.get('name') == law_name or law_name in law.get('name'):
            return {
                "name": law.get('name'),
                "latest_version": law.get('current_version'),
                "effective_date": law.get('effective_date'),
                "description": law.get('description')
            }

    return None

def get_all_latest_versions():
    """获取所有法律的最新版本信息"""
    config = load_config()
    if not config:
        return []

    return [
        {
            "name": law.get('name'),
            "latest_version": law.get('current_version'),
            "effective_date": law.get('effective_date')
        }
        for law in config.get('laws', [])
    ]

if __name__ == "__main__":
    # 测试
    print("版本校验测试：")
    result = check_law_version("中华人民共和国民事诉讼法", "2024修正")
    print(result['message'])

    result = check_law_version("中华人民共和国刑法", "刑法修正案（十一）")
    print(result['message'])

    result = check_law_version("工伤保险条例", "2010修订")
    print(result['message'])
