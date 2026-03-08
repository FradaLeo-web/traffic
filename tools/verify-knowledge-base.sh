#!/bin/bash

# 知识库验证脚本
# 用于验证知识库文件的完整性和可访问性

echo "========================================="
echo "  知识库验证工具"
echo "  Knowledge Base Verification Tool"
echo "========================================="
echo ""

# 定义目录路径
KB_DIR="knowledge-base"
LAW_DIR="$KB_DIR/laws"
CASE_DIR="$KB_DIR/cases"
INTER_DIR="$KB_DIR/interpretations"
TEMPLATE_DIR="$KB_DIR/templates"
STANDARD_DIR="$KB_DIR/standards"
PROC_DIR="$KB_DIR/procedures"

# 颜色定义
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 计数变量
total_files=0
total_dirs=0
error_count=0
warning_count=0

# 函数：检查目录是否存在
check_dir() {
    if [ -d "$1" ]; then
        echo -e "${GREEN}✓${NC} 目录存在: $1"
        total_dirs=$((total_dirs + 1))
        return 0
    else
        echo -e "${RED}✗${NC} 目录不存在: $1"
        error_count=$((error_count + 1))
        return 1
    fi
}

# 函数：检查文件
check_files() {
    local dir="$1"
    local name="$2"
    local expected="$3"
    
    if [ -d "$dir" ]; then
        count=$(find "$dir" -type f | wc -l)
        total_files=$((total_files + count))
        
        if [ ! -z "$expected" ] && [ "$count" -ne "$expected" ]; then
            echo -e "${YELLOW}⚠${NC} $name 文件数: $count (期望: $expected)"
            warning_count=$((warning_count + 1))
        else
            echo -e "${GREEN}✓${NC} $name 文件数: $count"
        fi
    fi
}

echo "1. 检查目录结构"
echo "-----------------------------------------"
check_dir "$KB_DIR"
check_dir "$LAW_DIR"
check_dir "$CASE_DIR"
check_dir "$INTER_DIR"
check_dir "$TEMPLATE_DIR"
check_dir "$STANDARD_DIR"
check_dir "$PROC_DIR"
echo ""

echo "2. 检查文件数量"
echo "-----------------------------------------"
check_files "$LAW_DIR" "法律法规" "14"
check_files "$CASE_DIR" "典型案例" "2686"
check_files "$INTER_DIR" "司法解释" "71"
check_files "$TEMPLATE_DIR" "文书模板" "5"
check_files "$STANDARD_DIR" "计算标准" "2"
echo ""

echo "3. 检查关键文件"
echo "-----------------------------------------"

# 检查索引文件
if [ -f "$KB_DIR/index.md" ]; then
    echo -e "${GREEN}✓${NC} 知识库索引文件存在"
else
    echo -e "${RED}✗${NC} 知识库索引文件缺失"
    error_count=$((error_count + 1))
fi

# 检查README文件
if [ -f "$KB_DIR/README.md" ]; then
    echo -e "${GREEN}✓${NC} 知识库说明文件存在"
else
    echo -e "${RED}✗${NC} 知识库说明文件缺失"
    error_count=$((error_count + 1))
fi
echo ""

echo "4. 检查案例分类"
echo "-----------------------------------------"
if [ -d "$CASE_DIR/交通事故" ]; then
    count=$(find "$CASE_DIR/交通事故" -type f | wc -l)
    echo -e "${GREEN}✓${NC} 交通事故案例: $count 个"
else
    echo -e "${RED}✗${NC} 交通事故案例目录不存在"
    error_count=$((error_count + 1))
fi

if [ -d "$CASE_DIR/合同纠纷" ]; then
    count=$(find "$CASE_DIR/合同纠纷" -type f | wc -l)
    echo -e "${GREEN}✓${NC} 合同纠纷案例: $count 个"
else
    echo -e "${YELLOW}⚠${NC} 合同纠纷案例目录不存在"
fi
echo ""

echo "5. 检查标准文件"
echo "-----------------------------------------"
if [ -f "$STANDARD_DIR/人体损伤致残程度分级.md" ]; then
    echo -e "${GREEN}✓${NC} 人体损伤致残程度分级标准存在"
else
    echo -e "${RED}✗${NC} 人体损伤致残程度分级标准缺失"
    error_count=$((error_count + 1))
fi

if [ -f "$STANDARD_DIR/GAT1193-2014.md" ]; then
    echo -e "${GREEN}✓${NC} GAT1193-2014标准存在"
else
    echo -e "${RED}✗${NC} GAT1193-2014标准缺失"
    error_count=$((error_count + 1))
fi
echo ""

echo "6. 检查模板文件"
echo "-----------------------------------------"
if [ -f "$TEMPLATE_DIR/sample_accidentiteport.md" ]; then
    echo -e "${GREEN}✓${NC} 交通事故认定书模板存在"
else
    echo -e "${YELLOW}⚠${NC} 交通事故认定书模板不存在"
fi
echo ""

echo "========================================="
echo "  验证结果汇总"
echo "========================================="
echo "总文件数: $total_files"
echo "总目录数: $total_dirs"
echo -e "错误数: ${RED}$error_count${NC}"
echo -e "警告数: ${YELLOW}$warning_count${NC}"
echo ""

if [ $error_count -eq 0 ]; then
    echo -e "${GREEN}✓${NC} 知识库验证通过！"
    exit 0
else
    echo -e "${RED}✗${NC} 知识库验证失败，请检查上述错误"
    exit 1
fi
