# 测试用例索引

本文档列出项目中的所有测试用例。

## 工作流测试 (workflow)

| 文件 | 测试内容 | Skill |
|------|----------|-------|
| `workflow/case-manager-test.md` | 案件信息提取、时限计算、材料清单 | case-manager |
| `workflow/evidence-analyzer-test.md` | 证据三性审查、质证意见 | evidence-analyzer |

## 专业领域测试 (professional)

| 文件 | 测试内容 | Skill |
|------|----------|-------|
| `professional/labor-dispute-test.md` | 工伤赔偿计算、经济补偿金、劳动关系认定 | labor-dispute |
| `professional/traffic-accident-test.md` | 赔偿计算、保险理赔、伤残预估 | traffic-accident |

## 智能分析测试 (intelligence)

| 文件 | 测试内容 | Skill |
|------|----------|-------|
| `intelligence/judgment-prediction-test.md` | 案例规则萃取、判决预测 | judgment-prediction |

---

## 运行测试

### 手动测试流程

1. **选择测试用例**
   - 根据需要测试的 Skill 选择对应的测试文件

2. **准备输入**
   - 读取测试文件中「### 输入」部分的内容

3. **调用 Skill**
   - 使用对应的 Skill 处理输入

4. **验证输出**
   - 对比实际输出与「### 期望输出」部分的预期结果

5. **记录差异**
   - 如有差异，记录并分析原因

---

## 测试覆盖

### 已覆盖的 Skill
- ✅ case-manager
- ✅ evidence-analyzer  
- ✅ judgment-prediction
- ✅ labor-dispute
- ✅ traffic-accident

### 待补充的 Skill
- ⏳ document-writer
- ⏳ legal-researcher
- ⏳ trial-assistant
- ⏳ content-writer
- ⏳ contract-dispute
- ⏳ tort-dispute
- ⏳ civil-procedure

---

## 测试标准

### 质量评估标准

| 等级 | 说明 |
|------|------|
| 优秀 | 输出与期望完全一致 |
| 良好 | 输出与期望基本一致，仅有细微差异 |
| 一般 | 输出与期望有较大差异，但核心内容正确 |
| 失败 | 输出与期望差异较大，需要改进 |

### 测试报告格式

```markdown
## 测试报告：[测试名称]

**测试时间**：2024-XX-XX
**测试Skill**：[Skill名称]
**测试结果**：优秀/良好/一般/失败

**差异分析**：
[如有差异，详细说明]

**改进建议**：
[如有需改进的地方]
```