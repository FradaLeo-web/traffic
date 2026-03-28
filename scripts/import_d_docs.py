import os
import re
import shutil
from pypdf import PdfReader

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

def get_category(filename):
    filename_lower = filename.lower()

    if "交通" in filename or "肇事" in filename or "危险驾驶" in filename:
        return "cases_traffic"
    if "劳动" in filename or "工伤" in filename:
        return "cases_labor"
    if "合同" in filename or "纠纷" in filename:
        return "cases_contract"

    if "条例" in filename:
        return "laws"
    if "工作报告" in filename:
        return "laws"
    if "办法" in filename:
        return "laws"
    if "国家赔偿决定书" in filename or "国家赔偿" in filename:
        return "cases"
    if "解释" in filename or "规定" in filename or "意见" in filename or "通知" in filename or "纪要" in filename or "实施细则" in filename:
        return "interpretations"
    if "指引" in filename or "指南" in filename or "操作指引" in filename:
        return "guides"

    if "挪用" in filename or "贪污" in filename or "受贿" in filename or "行贿" in filename or "套取" in filename or "虚报" in filename or "骗取" in filename or "财政补贴" in filename or "补偿款" in filename or "收受" in filename or "国家工作人员" in filename:
        return "cases"

    for cat_name, cat_info in CATEGORIES.items():
        for keyword in cat_info["keywords"]:
            if keyword in filename:
                return cat_name

    return None

def get_subcategory(filename, cat_name):
    if cat_name not in CATEGORIES:
        return None

    cat_info = CATEGORIES[cat_name]
    if not cat_info.get("subcategories"):
        return None

    for sub_name, keywords in cat_info["subcategories"].items():
        for keyword in keywords:
            if keyword in filename:
                return sub_name

    return None

def extract_text_from_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return None

def sanitize_filename(filename):
    filename = re.sub(r'[<>:"/\\|?*]', '', filename)
    filename = filename.replace('.pdf', '')
    if len(filename) > 100:
        filename = filename[:100]
    return filename + ".md"

def convert_pdf_to_md(pdf_path, output_path):
    text = extract_text_from_pdf(pdf_path)
    if text is None:
        return False

    if not text.strip():
        print(f"Warning: No text extracted from {pdf_path}")
        return False

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"# {os.path.basename(pdf_path).replace('.pdf', '')}\n\n")
        f.write(text)

    return True

def main():
    ensure_dir(KB_BASE)

    files = [f for f in os.listdir(SOURCE_DIR) if f.endswith('.pdf')]
    print(f"Found {len(files)} PDF files")

    success_count = 0
    error_count = 0
    skipped_count = 0

    for filename in files:
        pdf_path = os.path.join(SOURCE_DIR, filename)

        cat_name = get_category(filename)
        if cat_name is None:
            print(f"Skipping (no category match): {filename}")
            skipped_count += 1
            continue

        cat_info = CATEGORIES[cat_name]
        target_dir = cat_info["path"]

        sub_cat = get_subcategory(filename, cat_name)
        if sub_cat:
            target_dir = os.path.join(target_dir, sub_cat)

        ensure_dir(target_dir)

        output_filename = sanitize_filename(filename)
        output_path = os.path.join(target_dir, output_filename)

        if os.path.exists(output_path):
            print(f"Skipping (exists): {filename}")
            skipped_count += 1
            continue

        print(f"Processing: {filename} -> {target_dir}")

        if convert_pdf_to_md(pdf_path, output_path):
            success_count += 1
        else:
            error_count += 1

    print(f"\n=== Summary ===")
    print(f"Success: {success_count}")
    print(f"Errors: {error_count}")
    print(f"Skipped: {skipped_count}")

if __name__ == "__main__":
    main()
