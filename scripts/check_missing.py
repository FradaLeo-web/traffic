import os

SOURCE_DIR = r"D:\1"
KB_DIR = r"D:\AILaw\法律Agents\lawyer-office-assistant\knowledge-base"

def get_md_filenames():
    md_files = set()
    for root, dirs, files in os.walk(KB_DIR):
        for f in files:
            if f.endswith('.md'):
                md_name = f.replace('.md', '')
                md_files.add(md_name)
    return md_files

def check_source_files():
    source_files = os.listdir(SOURCE_DIR)

    md_files = get_md_filenames()

    print(f"Source files in D:\\1: {len(source_files)}")
    print(f"MD files in knowledge-base: {len(md_files)}")

    print("\n=== Checking which files were skipped or failed ===")

    skipped = []
    converted = []

    for f in source_files:
        if f.endswith('.pdf'):
            md_name = f.replace('.pdf', '')
            if md_name in md_files:
                converted.append(f)
            else:
                skipped.append(f)

    print(f"\n=== Converted: {len(converted)} files ===")
    for f in converted[:10]:
        print(f"  {f}")
    if len(converted) > 10:
        print(f"  ... and {len(converted) - 10} more")

    print(f"\n=== Skipped or not converted: {len(skipped)} files ===")
    for f in skipped:
        print(f"  '{f}'")

    print(f"\n=== DEBUG: Checking specific keywords ===")
    test_files = [
        "个人买理财 校长挪用公款数千万——江苏高院通报涉民生领域职务犯罪审判之一.pdf",
        "以扶贫救灾为名 村支书虚报拆迁补偿款——江苏高院通报涉民生领域职务犯罪审判之七.pdf",
        "骗取补偿款  村主任发“死人”财——江苏高院通报涉民生领域职务犯罪审判之六.pdf",
        "受聘于国有出资企业的工作人员，不以国家工作人员论.pdf",
    ]
    for f in test_files:
        print(f"\n'{f}':")
        print(f"  '挪用公款' in f: {'挪用公款' in f}")
        print(f"  '虚报' in f: {'虚报' in f}")
        print(f"  '骗取' in f: {'骗取' in f}")
        print(f"  '国家工作人员' in f: {'国家工作人员' in f}")

if __name__ == "__main__":
    check_source_files()
