import os

SOURCE_DIR = r"D:\1"
KB_BASE = r"D:\AILaw\法律Agents\lawyer-office-assistant\knowledge-base"

CATEGORIES = {
    "laws": {
        "path": os.path.join(KB_BASE, "laws"),
        "keywords": ["中华人民共和国", "刑法", "民法典", "刑事诉讼法", "民事诉讼法",
                    "会计法", "监察法", "企业国有资产法", "合伙企业法", "公司法",
                    "劳动合同法", "保险法", "证券法", "信托法", "票据法", "条例"],
        "subcategories": {
            "刑法": ["刑法", "犯罪", "刑罚", "量刑"],
            "民法": ["民法典", "合同", "侵权", "物权", "人格权"],
            "诉讼法": ["诉讼法", "仲裁", "执行", "管辖"],
            "行政法": ["行政", "处罚", "许可", "强制"],
            "经济法": ["金融", "证券", "保险", "税收", "会计"]
        }
    },
    "interpretations": {
        "path": os.path.join(KB_BASE, "interpretations"),
        "keywords": ["解释", "规定", "意见", "批复", "通知", "纪要", "实施细则"],
        "subcategories": {
            "立案追诉标准": ["立案追诉", "追诉标准"],
            "量刑规范": ["量刑", "量刑规范", "实施细则"],
            "司法解释": ["最高人民法院", "最高人民检察院", "解释"]
        }
    },
    "cases": {
        "path": os.path.join(KB_BASE, "cases"),
        "keywords": ["案", "判决", "裁定", "案例", "典型案例", "指导性案例"],
        "subcategories": {
            "职务侵占": ["职务侵占", "侵占股权", "侵占股东", "股东签名"],
            "挪用资金": ["挪用资金", "挪用公款"],
            "贪污受贿": ["贪污", "受贿", "行贿", "套取", "虚报", "骗取补偿", "财政补贴", "挪用公款", "收受他人", "补偿款"],
            "非法集资": ["非法吸收", "集资诈骗", "P2P", "贷款诈骗"],
            "其他刑事": ["刑事", "国家工作人员"]
        }
    },
    "cases_traffic": {
        "path": os.path.join(KB_BASE, "cases", "交通事故"),
        "keywords": ["交通", "肇事", "危险驾驶", "事故"],
        "subcategories": {}
    },
    "cases_labor": {
        "path": os.path.join(KB_BASE, "cases", "劳动纠纷"),
        "keywords": ["劳动", "工伤", "劳动合同", "劳务派遣"],
        "subcategories": {}
    },
    "cases_contract": {
        "path": os.path.join(KB_BASE, "cases", "合同纠纷"),
        "keywords": ["合同", "纠纷", "民事", "判决书"],
        "subcategories": {}
    },
    "standards": {
        "path": os.path.join(KB_BASE, "standards"),
        "keywords": ["标准", "规范", "规程", "规则"],
        "subcategories": {}
    },
    "guides": {
        "path": os.path.join(KB_BASE, "guides"),
        "keywords": ["指引", "指南", "操作指引", "业务指引"],
        "subcategories": {}
    },
    "corporate": {
        "path": os.path.join(KB_BASE, "cases", "刑事案例", "其他刑事"),
        "keywords": ["股东", "股权", "公司", "知情权", "代持股"],
        "subcategories": {}
    }
}

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def get_category_debug(filename):
    print(f"\n=== Debugging: {filename} ===")

    if "交通" in filename or "肇事" in filename or "危险驾驶" in filename:
        print("  Match: cases_traffic")
        return "cases_traffic"
    if "劳动" in filename or "工伤" in filename:
        print("  Match: cases_labor")
        return "cases_labor"
    if "合同" in filename or "纠纷" in filename:
        print("  Match: cases_contract")
        return "cases_contract"

    if "条例" in filename:
        print("  Match: laws (条例)")
        return "laws"
    if "工作报告" in filename:
        print("  Match: laws (工作报告)")
        return "laws"
    if "办法" in filename:
        print("  Match: laws (办法)")
        return "laws"
    if "国家赔偿决定书" in filename or "国家赔偿" in filename:
        print("  Match: cases (国家赔偿)")
        return "cases"
    if "解释" in filename or "规定" in filename or "意见" in filename or "通知" in filename or "纪要" in filename or "实施细则" in filename:
        print("  Match: interpretations")
        return "interpretations"
    if "指引" in filename or "指南" in filename or "操作指引" in filename:
        print("  Match: guides")
        return "guides"

    print("  Checking CATEGORIES loop:")
    for cat_name, cat_info in CATEGORIES.items():
        print(f"    Checking category '{cat_name}' with keywords: {cat_info['keywords']}")
        for keyword in cat_info["keywords"]:
            if keyword in filename:
                print(f"      MATCH: keyword '{keyword}' found in filename!")
                return cat_name

    print("  No match found!")
    return None

test_files = [
    "个人买理财 校长挪用公款数千万——江苏高院通报涉民生领域职务犯罪审判之一.pdf",
    "以扶贫救灾为名  村支书虚报拆迁补偿款——江苏高院通报涉民生领域职务犯罪审判之七.pdf",
]

for f in test_files:
    result = get_category_debug(f)
    print(f"  Final result: {result}")
