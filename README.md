# 律师办公助手 - Lawyer Lawyer Assistant

> 基于AI Agent的法律实务辅助工具，助力律师高效处理日常法律事务

## 📋 项目简介

本项目是一套完整的法律实务辅助Agent系统，包含：
- **6个通用能力Agent**：案件管理、证据分析、文书写作、法律检索、庭审辅助、内容创作
- **5个专业技能Agent**：劳动争议、交通事故、合同纠纷、侵权纠纷、民事诉讼
- **完整的知识库系统**：结构化存储法律法规、典型案例、文书模板、计算标准、办案流程

## 🏗️ 项目架构

```
lawyer-office-assistant/
├── agents/                    # 通用能力Agent（6个）
│   ├── case-manager.md        # 案件管理助手
│   ├── evidence-analyzer.md   # 证据分析专家
│   ├── document-writer.md     # 法律文书专家
│   ├── legal-researcher.md    # 法律检索专家
│   ├── trial-assistant.md     # 庭审策略专家
│   └── content-writer.md      # 内容创作专家
├── skills/                    # 专业技能Agent（5个领域）
│   ├── labor-dispute/         # 劳动争议
│   ├── traffic-accident/      # 交通事故
│   ├── contract-dispute/      # 合同纠纷
│   ├── tort-dispute/          # 侵权纠纷
│   └── civil-procedure/       # 民事诉讼
├── knowledge-base/            # 知识库（1571个文件）
│   ├── index.md               # 知识库索引
│   ├── laws/                  # 法律法规（14个）
│   ├── cases/                 # 典型案例（1484个）
│   ├── interpretations/       # 司法解释（71个）
│   ├── templates/             # 文书模板
│   ├── standards/             # 计算标准
│   └── procedures/            # 办案流程
├── config/                    # 配置文件
│   └── output-config.json     # 输出配置
├── tools/                     # 工具脚本
├── docs/                      # 项目文档
├── tests/                     # 测试用例
└── README.md                  # 项目说明

../outputs/                    # 输出目录（Agent生成文件）
├── README.md                  # 输出目录说明
├── 2025-02-23/                # 按日期分类的输出
├── 2025-02-24/
└── ...
```
lawyer-office-assistant/
├── agents/                    # 通用能力Agent（6个）
│   ├── case-manager.md        # 案件管理助手
│   ├── evidence-analyzer.md   # 证据分析专家
│   ├── document-writer.md     # 法律文书专家
│   ├── legal-researcher.md    # 法律检索专家
│   ├── trial-assistant.md     # 庭审策略专家
│   └── content-writer.md      # 内容创作专家
├── skills/                    # 专业技能Agent（5个领域）
│   ├── labor-dispute/         # 劳动争议
│   ├── traffic-accident/      # 交通事故
│   ├── contract-dispute/      # 合同纠纷
│   ├── tort-dispute/          # 侵权纠纷
│   └── civil-procedure/       # 民事诉讼
├── knowledge-base/            # 知识库
│   ├── laws/                  # 法律法规
│   ├── cases/                 # 典型案例
│   ├── templates/             # 文书模板
│   ├── standards/             # 计算标准
│   └── procedures/            # 办案流程
├── tools/                     # 工具脚本
├── docs/                      # 项目文档
├── config/                    # 配置文件
├── tests/                     # 测试用例
└── README.md                  # 项目说明
```

## 🚀 快速开始

### 1. 通用能力Agent使用

所有通用Agent都位于 `agents/` 目录，可直接调用：

```markdown
# 案件管理
- 文件: agents/case-manager.md
- 功能: 案件信息管理、办案节点追踪、材料清单生成

# 证据分析
- 文件: agents/evidence-analyzer.md
- 功能: 证据三性审查、证据目录生成、质证意见起草

# 文书写作
- 文件: agents/document-writer.md
- 功能: 起诉状、答辩状、代理词等法律文书生成

# 法律检索
- 文件: agents/legal-researcher.md
- 功能: 法条检索、类案检索、裁判规则总结

# 庭审辅助
- 文件: agents/trial-assistant.md
- 功能: 庭审话术、发问提纲、应答策略

# 内容创作
- 文件: agents/content-writer.md
- 功能: 小红书图文、短视频口播等法律内容创作
```

### 2. 专业技能Agent使用

专业技能按领域组织在 `skills/` 目录：

```markdown
# 1. 劳动争议
- 文件: skills/labor-dispute/SKILL.md
- 覆盖: 劳动关系认定、工资报酬、工伤赔偿、社保纠纷
- 代码量: 711行

# 2. 交通事故
- 文件: skills/traffic-accident/SKILL.md
- 覆盖: 责任认定、伤残鉴定、保险理赔、刑事评估
- 代码量: 686行

# 3. 合同纠纷
- 文件: skills/contract-dispute/SKILL.md
- 覆盖: 合同效力、违约责任、损失计算
- 代码量: 152行

# 4. 侵权纠纷
- 文件: skills/tort-dispute/SKILL.md
- 覆盖: 人身损害、财产损害、精神损害
- 代码量: 181行

# 5. 民事诉讼
- 文件: skills/civil-procedure/SKILL.md
- 覆盖: 管辖、立案、证据、庭审、执行
- 代码量: 245行
```

### 3. 知识库使用

知识库位于 `knowledge-base/` 目录，包含2792个法律文件，支持检索和引用：

```markdown
# 法律法规 (knowledge-base/laws/) - 14个文件
- 中华人民共和国民法典、民事诉讼法、刑法
- 劳动合同法、劳动法、工伤保险条例
- 道路交通安全法、公司法等

# 典型案例 (knowledge-base/cases/) - 2686个文件
- 交通事故案例（1202个）
- 合同纠纷案例（705个）
- 民间借贷案例（11个）
- 破产案例（768个）

# 司法解释 (knowledge-base/interpretations/) - 71个文件
- 最高司法解释
- 司法指导意见
- 地性规范
- 其他规范性文件

# 其他分类（已完成）
- 文书模板 (templates/) - 5个文件
- 计算标准 (standards/) - 2个文件
- 办案流程 (procedures/) - 待完善
```

### 4. 输出文件管理

所有Agent生成的文件统一存放在 `../outputs/` 目录：

```markdown
# 输出目录结构
../outputs/
├── 2025-02-23/              # 按日期分类
│   ├── case-report_2025-02-23_001.md
│   ├── legal-doc_2025-02-23_001.md
│   └── ...
└── 2025-02-24/

# 输出文件类型
- case-report: 案件分析报告
- legal-doc: 法律文书
- evidence: 证据分析
- research: 法律检索结果
- trial: 庭审策略
- content-img: 图文内容
- content-video: 视频口播文稿
```

详见 `../outputs/README.md`

## 📊 项目统计

| 项目 | 数量 |
|------|------|
| **总文件数** | 2,809个 |
| **代码/文档行数** | 约 2,691行 |
| **通用Agent** | 6个 |
| **专业Skill** | 5个 |
| **知识库文件** | 2,792个 |
| **配置文件** | 1个 |

### Agent+Skill统计
| Agent名称 | 文件路径 | 行数 |
|-----------|----------|------|
| 案件管理助手 | agents/case-manager.md | 31 |
| 证据分析专家 | agents/evidence-analyzer.md | 36 |
| 法律文书专家 | agents/document-writer.md | 125 |
| 法律检索专家 | agents/legal-researcher.md | 36 |
| 庭审策略专家 | agents/trial-assistant.md | 53 |
| 内容创作专家 | agents/content-writer.md | 435 |
| 劳动争议 | skills/labor-dispute/SKILL.md | 711 |
| 交通事故 | skills/traffic-accident/SKILL.md | 686 |
| 合同纠纷 | skills/contract-dispute/SKILL.md | 152 |
| 侵权纠纷 | skills/tort-dispute/SKILL.md | 181 |
| 民事诉讼 | skills/civil-procedure/SKILL.md | 245 |

## 🎯 使用场景

1. **案件管理**: 跟踪案件进度，管理办案节点
2. **证据分析**: 审查证据三性，生成证据目录
3. **文书写作**: 快速生成各类法律文书
4. **法律检索**: 检索法条、类案、裁判规则
5. **庭审辅助**: 准备庭审话术，制定应答策略
6. **内容创作**: 生成普法内容，运营自媒体

## 🔄 后续计划

### 短期（1-2周）
- [x] 填充知识库基础内容（已导入1571个文件）
- [x] 更新交通领域知识库（新增1209个文件）
- [x] 创建常用计算标准
- [ ] 编写办案流程文档
- [ ] 创建输出文件管理工具

### 中期（1个月）
- [x] 完善Agent功能示例
- [ ] 建立知识库检索系统
- [ ] 创建自动化工具脚本
- [x] 建立输出文件管理机制

### 长期（持续）
- [ ] 持续更新法律知识
- [ ] 扩展更多专业领域
- [ ] 建立社区协作机制

## 📄 许可证

本项目采用 MIT 许可证

---

**注意**: 本工具仅供法律专业人士辅助使用，不构成正式法律意见。重要法律决策请咨询执业律师。
