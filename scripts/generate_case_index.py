#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
案例文件分类索引生成脚本
将PDF案例文件按类型分类并生成Markdown索引
"""

import os
import re
import shutil
import argparse
from pathlib import Path
from datetime import datetime

# 分类规则
CATEGORIES = {
    # 刑事类
    "职务侵占": ["职务侵占"],
    "非法集资": ["非法集资", "非法吸收", "集资诈骗"],
    "挪用资金": ["挪用资金", "挪用公款"],
    "贪污受贿": ["贪污", "受贿", "行贿"],
    "诈骗罪": ["诈骗", "电信诈骗", "合同诈骗"],
    "盗窃罪": ["盗窃", "扒窃", "入室盗窃"],
    "危险驾驶": ["危险驾驶", "醉驾", "飙车"],
    "故意伤害": ["故意伤害", "故意杀人", "过失致人"],
    "其他刑事": ["洗钱", "掩饰隐瞒", "操纵", "内幕交易", "虚假破产", "背信", "黑社会性质", "寻衅滋事", "环境污染", "假冒注册商标"],
    # 民事类
    "交通事故": ["交通事故", "机动车事故", "交通肇事"],
    "劳动争议": ["劳动争议", "工伤", "劳动合同", "经济补偿"],
    "婚姻家庭": ["离婚", "抚养权", "继承", "财产分割", "赡养"],
    "民间借贷": ["民间借贷", "借款", "借条", "欠条", "利息"],
    "合同纠纷": ["合同纠纷", "违约", "合同效力", "违约金"],
    "侵权纠纷": ["侵权", "人身损害", "精神损害", "责任认定"],
    # 行政类
    "行政诉讼": ["行政诉讼", "行政复议", "行政处罚", "行政赔偿"]
}

def classify_case(filename):
    """根据文件名分类案例"""
    for category, keywords in CATEGORIES.items():
        for keyword in keywords:
            if keyword in filename:
                return category
    return "其他刑事"

def extract_case_info(filename):
    """提取案例信息"""
    info = {
        "title": filename.replace(".pdf", ""),
        "case_type": "",
        "source": "",
        "level": ""
    }
    
    # 提取案例类型
    if "刑事判决书" in filename:
        info["case_type"] = "刑事判决书"
    elif "民事判决书" in filename:
        info["case_type"] = "民事判决书"
    elif "典型案例" in filename:
        info["case_type"] = "典型案例"
    elif "指导性案例" in filename:
        info["case_type"] = "指导性案例"
    elif "再审" in filename:
        info["case_type"] = "再审案件"
    else:
        info["case_type"] = "其他"
    
    # 提取来源
    if "最高法" in filename or "最高法院" in filename or "最高人民法院" in filename:
        info["source"] = "最高人民法院"
        info["level"] = "国家级"
    elif "最高检" in filename or "最高人民检察院" in filename:
        info["source"] = "最高人民检察院"
        info["level"] = "国家级"
    elif "高院" in filename or "省法院" in filename:
        info["source"] = "省级法院"
        info["level"] = "省级"
    elif "检察院" in filename:
        info["source"] = "检察机关"
        info["level"] = "检察机关"
    else:
        info["source"] = "地方法院"
        info["level"] = "地方级"
    
    return info

def generate_markdown_index(category, files_info, source_path, category_dir):
    """生成Markdown索引文件"""
    # 计算源目录相对于索引目录的相对路径
    rel_source_path = os.path.relpath(source_path, category_dir).replace('\\', '/')

    content = f"""# {category}案例索引

> 本目录收录{category}相关案例，共计 {len(files_info)} 个文件

生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## 案例列表

| 序号 | 案例名称 | 类型 | 来源 | 级别 |
|------|----------|------|------|------|
"""

    for idx, info in enumerate(files_info, 1):
        content += f"| {idx} | [{info['title']}]({rel_source_path}/{info['filename'].replace(' ', '%20')}) | {info['case_type']} | {info['source']} | {info['level']} |\n"

    content += f"""
---

## 使用说明

1. 本索引文件由系统自动生成
2. 原始PDF文件位于：`{rel_source_path}`
3. 如需查看案例详情，请点击案例名称链接打开PDF文件
4. 案例按文件名关键词自动分类，可能存在分类偏差

---

## 分类说明

"""
    
    if category == "职务侵占":
        content += """
### 职务侵占罪

**法律依据**：《刑法》第271条

**构成要件**：
- 主体：公司、企业或其他单位的工作人员
- 客体：公司、企业或其他单位的财产所有权
- 客观方面：利用职务便利，将本单位财物非法占为己有
- 主观方面：故意，具有非法占有目的

**量刑标准**：
- 数额较大：3年以下有期徒刑或拘役，并处罚金
- 数额巨大：3-10年有期徒刑，并处罚金
- 数额特别巨大：10年以上有期徒刑或无期徒刑，并处罚金
"""
    elif category == "非法集资":
        content += """
### 非法集资类犯罪

**涉及罪名**：
- 非法吸收公众存款罪（《刑法》第176条）
- 集资诈骗罪（《刑法》第192条）

**构成要件**：
- 非法性：未经有关部门依法批准
- 公开性：向社会公开宣传
- 利诱性：承诺还本付息或给付回报
- 社会性：向社会不特定对象吸收资金

**量刑标准**：
- 非法吸收公众存款：3年以下/3-10年/10年以上有期徒刑
- 集资诈骗：3-7年/7年以上有期徒刑或无期徒刑
"""
    elif category == "挪用资金":
        content += """
### 挪用资金罪

**法律依据**：《刑法》第272条

**构成要件**：
- 主体：公司、企业或其他单位的工作人员
- 客体：单位资金的使用权
- 客观方面：利用职务便利，挪用本单位资金
- 主观方面：故意，暂时使用目的

**行为类型**：
1. 挪用资金归个人使用，数额较大，超过3个月未还
2. 挪用资金数额较大，进行营利活动
3. 挪用资金进行非法活动

**量刑标准**：
- 数额较大：3年以下有期徒刑或拘役
- 数额巨大：3-7年有期徒刑
- 数额特别巨大：7年以上有期徒刑
"""
    elif category == "贪污受贿":
        content += """
### 贪污受贿罪

**涉及罪名**：
- 贪污罪（《刑法》第382条）
- 受贿罪（《刑法》第385条）
- 行贿罪（《刑法》第389条）

**构成要件**：
- 主体：国家工作人员
- 客体：职务行为的廉洁性和公共财产所有权
- 客观方面：利用职务便利，侵吞/窃取/骗取公共财物
- 主观方面：故意

**量刑标准**：
- 贪污/受贿数额较大：3年以下有期徒刑或拘役，并处罚金
- 数额巨大：3-10年有期徒刑，并处罚金或没收财产
- 数额特别巨大：10年以上有期徒刑、无期徒刑或死刑，并处罚金或没收财产
"""
    
    return content

def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='案例文件分类索引生成脚本')
    parser.add_argument('--source', '-s', default='../1', help='PDF案例文件所在目录（默认：../1）')
    parser.add_argument('--target', '-t', default='../knowledge-base/cases', help='索引文件输出目录（默认：../knowledge-base/cases）')
    args = parser.parse_args()

    print("开始生成案例索引...")

    try:
        # 获取所有PDF文件
        source_path = Path(args.source).resolve()
        target_base = Path(args.target).resolve()

        if not source_path.exists():
            print(f"❌ 错误：源目录不存在 - {source_path}")
            return

        pdf_files = list(source_path.glob("*.pdf"))

        if not pdf_files:
            print(f"⚠️  警告：源目录中没有找到PDF文件 - {source_path}")
            return

        print(f"找到 {len(pdf_files)} 个PDF文件")
    
    # 按分类存储文件信息
    categorized_files = {cat: [] for cat in CATEGORIES.keys()}
    
    # 分类处理
    for pdf_file in pdf_files:
        filename = pdf_file.name
        category = classify_case(filename)
        info = extract_case_info(filename)
        info["filename"] = filename
        info["original_path"] = str(pdf_file)
        categorized_files[category].append(info)
    
    # 生成索引文件
    for category, files_info in categorized_files.items():
        if not files_info:
            continue

        category_dir = target_base / category
        os.makedirs(category_dir, exist_ok=True)

        # 生成索引文件
        index_content = generate_markdown_index(category, files_info, source_path, category_dir)
        index_path = category_dir / "index.md"

        with open(index_path, "w", encoding="utf-8") as f:
            f.write(index_content)

        print(f"✅ {category}: 生成索引文件，包含 {len(files_info)} 个案例")

    # 生成总索引
    generate_master_index(categorized_files, target_base)

    print("\n索引生成完成！")

    except Exception as e:
        print(f"❌ 生成索引失败：{str(e)}")
        import traceback
        traceback.print_exc()

def generate_master_index(categorized_files, target_base):
    """生成总索引文件"""
    total = sum(len(files) for files in categorized_files.values())

    content = f"""# 法律案例库总索引

> 本知识库收录刑事、民事、行政等各类法律案例，共计 {total} 个文件

生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## 分类统计

| 分类 | 案例数量 | 索引文件 |
|------|----------|----------|
"""

    for category, files_info in categorized_files.items():
        if files_info:
            content += f"| {category} | {len(files_info)} | [查看索引](./{category}/index.md) |\n"

    content += """
---

## 快速导航

"""

    for category in sorted(categorized_files.keys()):
        content += f"- [{category}](./{category}/index.md)\n"

    content += """
---

## 使用说明

1. 本索引文件由系统自动生成
2. 案例按文件名关键词自动分类
3. 如需查看案例详情，请进入对应分类查看索引文件并点击链接打开PDF

---

## 更新日志

"""
    content += f"- {datetime.now().strftime('%Y-%m-%d')}: 导入 {total} 个案例文件，扩展支持民事、行政等多类案例\n"

    index_path = target_base / "README.md"
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ 生成总索引文件: {index_path}")

if __name__ == "__main__":
    main()
