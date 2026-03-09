# 知识库使用指南

本文档说明如何使用律师办公助手的知识库系统。

---

## 快速导航

### 按类型查找

```
knowledge-base/
├── laws/              # 法律法规（14个）
├── cases/             # 典型案例（2686个）
├── interpretations/   # 司法解释（71个）
├── templates/         # 文书模板（5个）
├── standards/         # 计算标准（2个）
└── procedures/        # 办案流程（待完善）
```

### 按领域查找

#### 交通事故领域
- **法律**: `laws/中华人民共和国道路交通安全法*.md`
- **案例**: `cases/交通事故/` (1202个案例)
- **标准**: `standards/人体损伤致残程度分级.md`
- **模板**: `templates/sample_accident_report.md`
- **技能**: `skills/traffic-accident/SKILL.md`

#### 劳动争议领域
- **法律**: `laws/劳动合同法*.md`、`工伤保险条例*.md`
- **案例**: `cases/` (各类型案例)
- **技能**: `skills/labor-dispute/SKILL.md`

#### 合同纠纷领域
- **法律**: `laws/中华人民共和国民法典.md`
- **案例**: `cases/合同纠纷/` (705个案例)
- **技能**: `skills/contract-dispute/SKILL.md`

---

## 使用方法

### 1. 法律法规查询

**方法一：直接查找**
```bash
# 查找特定法律
ls knowledge-base/laws/ | grep "道路交通安全法"

# 阅读法律内容
cat knowledge-base/laws/中华人民共和国道路交通安全法*.md
```

**方法二：通过索引**
```bash
# 查看知识库索引
cat knowledge-base/index.md
```

### 2. 案例检索

**按案由检索**
```bash
# 交通事故案例
ls knowledge-base/cases/交通事故/

# 合同纠纷案例
ls knowledge-base/cases/合同纠纷/
```

**关键词搜索**
```bash
# 搜索包含特定关键词的案例
grep -r "危险驾驶" knowledge-base/cases/交通事故/
```

### 3. 模板使用

**查看可用模板**
```bash
ls knowledge-base/templates/
```

**使用模板**
```bash
# 交通事故认定书模板
cat knowledge-base/templates/sample_accident_report.md
```

### 4. 标准查询

**伤残等级标准**
```bash
cat knowledge-base/standards/人体损伤致残程度分级.md
```

**痕迹物证勘验标准**
```bash
cat knowledge-base/standards/GAT1193-2014.md
```

---

## Agent + Skill 调用

### 交通事故处理

1. **调用交通事故技能**
   ```
   使用 skills/traffic-accident/SKILL.md
   ```

2. **参考知识库**
   - 法律：道路交通安全法、实施条例
   - 案例：cases/交通事故/ 中的相关案例
   - 标准：人体损伤致残程度分级
   - 模板：sample_accident_report.md

### 劳动争议处理

1. **调用劳动争议技能**
   ```
   使用 skills/labor-dispute/SKILL.md
   ```

2. **参考知识库**
   - 法律：劳动合同法、工伤保险条例
   - 案例：cases/ 中的相关案例
   - 解释：interpretations/ 中的相关文件

---

## 更新日志

查看最新的知识库更新记录：

```bash
cat docs/KNOWLEDGE_BASE_CHANGELOG.md
```

---

## 维护说明

### 添加新法律
1. 将法律文件放入 `laws/` 目录
2. 更新 `index.md` 中的法律列表
3. 更新 `docs/KNOWLEDGE_BASE_CHANGELOG.md`

### 添加新案例
1. 根据案由创建或选择目录
2. 将案例文件放入对应目录
3. 更新 `index.md` 中的案例统计
4. 更新 `docs/KNOWLEDGE_BASE_CHANGELOG.md`

### 添加新模板
1. 将模板文件放入 `templates/` 目录
2. 更新 `index.md` 中的模板列表
3. 更新 `docs/KNOWLEDGE_BASE_CHANGELOG.md`

---

## 注意事项

1. **文件格式**：知识库文件统一使用Markdown格式
2. **文件命名**：使用中文命名，便于识别
3. **编码格式**：统一使用UTF-8编码
4. **版本控制**：重要更新应在更新日志中记录

---

**最后更新**: 2025-02-23
**知识库版本**: v2.0
