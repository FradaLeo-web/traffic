import os
import shutil

KB_BASE = r"D:\AILaw\法律Agents\lawyer-office-assistant\knowledge-base"
CASES_DIR = os.path.join(KB_BASE, "cases")

CASE_CATEGORIES = {
    "职务侵占": ["职务侵占", "侵占股权", "侵占股东", "股东签名", "职务便利", "工作便利", "员工舞弊"],
    "挪用资金": ["挪用资金", "挪用公款"],
    "贪污受贿": ["贪污", "受贿", "行贿", "套取", "虚报", "骗取补偿", "财政补贴", "收受", "补偿款"],
    "非法集资": ["非法吸收", "集资诈骗", "P2P", "贷款诈骗"],
    "其他刑事": ["诈骗", "盗窃", "抢劫", "杀人", "黑社会", "组织、领导", "走私", "毒品", "卖淫", "赌博", "虚报注册资本", "假冒注册商标", "洗钱", "掩饰、隐瞒", "诬告陷害", "妨碍公务", "非法拘禁", "敲诈勒索", "寻衅滋事", "故意杀人", "故意伤害", "侵犯公民个人信息", "帮助信息网络犯罪", "开设赌场", "组织卖淫", "运输毒品"],
    "国家赔偿": ["国家赔偿"],
    "破产清算": ["破产", "清算"],
    "知识产权": ["知识产权", "专利", "商标", "商业秘密", "假冒注册商标"],
    "行政诉讼": ["行政判决", "行政赔偿", "行政复议", "行政协议"],
    "证券期货": ["证券", "期货", "操纵市场"],
}

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def get_category(filename):
    for cat_name, keywords in CASE_CATEGORIES.items():
        for keyword in keywords:
            if keyword in filename:
                return cat_name
    return None

def main():
    files = [f for f in os.listdir(CASES_DIR) if f.endswith('.md')]

    categorized = {}
    uncategorized = []

    for filename in files:
        cat_name = get_category(filename)
        if cat_name:
            if cat_name not in categorized:
                categorized[cat_name] = []
            categorized[cat_name].append(filename)
        else:
            uncategorized.append(filename)

    total_moved = 0

    for cat_name, files_list in categorized.items():
        target_dir = os.path.join(CASES_DIR, "刑事案例", cat_name)
        ensure_dir(target_dir)

        print(f"\n=== {cat_name}: {len(files_list)} files ===")

        for filename in files_list:
            src_path = os.path.join(CASES_DIR, filename)
            dest_path = os.path.join(target_dir, filename)

            if os.path.exists(dest_path):
                print(f"  Skip (exists): {filename}")
                continue

            shutil.move(src_path, dest_path)
            print(f"  Moved: {filename}")
            total_moved += 1

    print(f"\n=== Uncategorized: {len(uncategorized)} files ===")
    for f in uncategorized[:20]:
        print(f"  {f}")
    if len(uncategorized) > 20:
        print(f"  ... and {len(uncategorized) - 20} more")

    print(f"\n=== Total: {total_moved} files moved ===")

if __name__ == "__main__":
    main()
