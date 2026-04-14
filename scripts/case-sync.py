#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
案件数据同步脚本
实现跨技能案件数据的统一存储、读取、更新、同步
"""

import json
import os
import uuid
from datetime import datetime
from typing import Dict, List, Optional

SCHEMA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'case-schema.json')
STORAGE_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'workspace', 'cases')

# 确保存储目录存在
os.makedirs(STORAGE_ROOT, exist_ok=True)

def load_schema() -> Dict:
    """加载案件数据结构"""
    try:
        with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"加载案件数据结构失败: {e}")
        return {}

def generate_case_id() -> str:
    """生成案件唯一ID"""
    return f"CASE_{datetime.now().strftime('%Y%m%d')}_{str(uuid.uuid4())[:8].upper()}"

def get_case_path(case_id: str) -> str:
    """获取案件文件路径"""
    return os.path.join(STORAGE_ROOT, f"{case_id}.json")

def create_case(case_data: Dict) -> Dict:
    """
    创建新案件
    :param case_data: 案件数据
    :return: 创建结果
    """
    schema = load_schema()
    if not schema:
        return {"status": "error", "message": "案件数据结构加载失败"}

    # 生成案件ID
    case_id = generate_case_id()
    case_data['case_id'] = case_id
    case_data['create_time'] = datetime.now().isoformat()
    case_data['update_time'] = datetime.now().isoformat()

    # 保存案件数据
    try:
        with open(get_case_path(case_id), 'w', encoding='utf-8') as f:
            json.dump(case_data, f, ensure_ascii=False, indent=2)
        return {
            "status": "success",
            "message": "案件创建成功",
            "case_id": case_id,
            "case_data": case_data
        }
    except Exception as e:
        return {"status": "error", "message": f"保存案件数据失败: {e}"}

def get_case(case_id: str) -> Dict:
    """
    获取案件数据
    :param case_id: 案件ID
    :return: 案件数据
    """
    case_path = get_case_path(case_id)
    if not os.path.exists(case_path):
        return {"status": "error", "message": "案件不存在"}

    try:
        with open(case_path, 'r', encoding='utf-8') as f:
            case_data = json.load(f)
        return {
            "status": "success",
            "message": "案件获取成功",
            "case_data": case_data
        }
    except Exception as e:
        return {"status": "error", "message": f"读取案件数据失败: {e}"}

def update_case(case_id: str, update_data: Dict, operation: Optional[str] = None) -> Dict:
    """
    更新案件数据
    :param case_id: 案件ID
    :param update_data: 需要更新的数据
    :param operation: 操作描述，用于记录操作日志
    :return: 更新结果
    """
    case_result = get_case(case_id)
    if case_result['status'] != 'success':
        return case_result

    case_data = case_result['case_data']

    # 合并更新数据
    case_data.update(update_data)
    case_data['update_time'] = datetime.now().isoformat()

    # 记录操作日志
    if operation:
        if 'operation_records' not in case_data:
            case_data['operation_records'] = []
        case_data['operation_records'].append({
            "time": datetime.now().isoformat(),
            "skill": operation.get('skill', 'unknown'),
            "content": operation.get('content', ''),
            "result": operation.get('result', 'success')
        })

    # 保存更新后的数据
    try:
        with open(get_case_path(case_id), 'w', encoding='utf-8') as f:
            json.dump(case_data, f, ensure_ascii=False, indent=2)
        return {
            "status": "success",
            "message": "案件更新成功",
            "case_data": case_data
        }
    except Exception as e:
        return {"status": "error", "message": f"更新案件数据失败: {e}"}

def list_cases(page: int = 1, page_size: int = 20) -> Dict:
    """
    获取案件列表
    :param page: 页码
    :param page_size: 每页数量
    :return: 案件列表
    """
    case_files = [f for f in os.listdir(STORAGE_ROOT) if f.endswith('.json') and f.startswith('CASE_')]
    case_files.sort(reverse=True)  # 按创建时间倒序

    total = len(case_files)
    start = (page - 1) * page_size
    end = start + page_size
    current_page_files = case_files[start:end]

    case_list = []
    for file in current_page_files:
        case_id = file.replace('.json', '')
        case_result = get_case(case_id)
        if case_result['status'] == 'success':
            case_data = case_result['case_data']
            case_list.append({
                "case_id": case_id,
                "case_name": case_data.get('case_name', ''),
                "case_type": case_data.get('case_type', ''),
                "case_cause": case_data.get('case_cause', ''),
                "case_stage": case_data.get('case_stage', ''),
                "create_time": case_data.get('create_time', ''),
                "update_time": case_data.get('update_time', '')
            })

    return {
        "status": "success",
        "message": "案件列表获取成功",
        "data": {
            "total": total,
            "page": page,
            "page_size": page_size,
            "total_pages": (total + page_size - 1) // page_size,
            "list": case_list
        }
    }

def delete_case(case_id: str) -> Dict:
    """
    删除案件
    :param case_id: 案件ID
    :return: 删除结果
    """
    case_path = get_case_path(case_id)
    if not os.path.exists(case_path):
        return {"status": "error", "message": "案件不存在"}

    try:
        os.remove(case_path)
        return {"status": "success", "message": "案件删除成功"}
    except Exception as e:
        return {"status": "error", "message": f"删除案件失败: {e}"}

def sync_case_data(source_case_id: str, target_skill: str) -> Dict:
    """
    同步案件数据到其他技能
    :param source_case_id: 源案件ID
    :param target_skill: 目标技能
    :return: 同步结果
    """
    case_result = get_case(source_case_id)
    if case_result['status'] != 'success':
        return case_result

    case_data = case_result['case_data']

    # 记录同步操作
    update_case(source_case_id, {}, {
        "skill": "case-sync",
        "content": f"同步案件数据到{target_skill}技能",
        "result": "success"
    })

    return {
        "status": "success",
        "message": "案件数据同步成功",
        "case_data": case_data
    }

if __name__ == "__main__":
    # 测试功能
    print("测试案件创建：")
    test_case = {
        "case_name": "张三与李四民间借贷纠纷案",
        "case_type": "民事",
        "case_cause": "民间借贷纠纷",
        "parties": [
            {"name": "张三", "role": "原告", "type": "自然人"},
            {"name": "李四", "role": "被告", "type": "自然人"}
        ],
        "lawyer_role": "原告代理律师",
        "case_stage": "一审",
        "claim_amount": 100000,
        "core_controversy": "借款是否实际支付，利息约定是否合法"
    }
    create_result = create_case(test_case)
    print(create_result['message'])
    if create_result['status'] == 'success':
        case_id = create_result['case_id']
        print(f"生成的案件ID: {case_id}")

        print("\n测试案件获取：")
        get_result = get_case(case_id)
        print(get_result['message'])
        if get_result['status'] == 'success':
            print(f"案件名称: {get_result['case_data']['case_name']}")

        print("\n测试案件更新：")
        update_result = update_case(case_id, {"case_stage": "开庭前准备"}, {
            "skill": "案件管理助手",
            "content": "更新案件阶段为开庭前准备"
        })
        print(update_result['message'])

        print("\n测试案件列表：")
        list_result = list_cases()
        print(list_result['message'])
        print(f"案件总数: {list_result['data']['total']}")
