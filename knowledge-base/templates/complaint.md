{{ court_name }}

民事起诉状

原告：
姓名：{{ plaintiff.name }}
性别：{{ plaintiff.gender }}
年龄：{{ plaintiff.age }}岁
身份证号：{{ plaintiff.id_card }}
联系电话：{{ plaintiff.phone }}
住址：{{ plaintiff.address }}
职业：{{ plaintiff.occupation }}
工作单位：{{ plaintiff.work_unit }}

被告：
{% for defendant in defendants %}
姓名：{{ defendant.name }}
类型：{{ defendant.type }}
身份证号/统一社会信用代码：{{ defendant.id_card }}
联系电话：{{ defendant.phone }}
住址：{{ defendant.address }}
车牌号：{{ defendant.vehicle_number }}
{% endfor %}

【诉讼请求】

1. 判令被告赔偿原告各项损失共计人民币 {{ total_compensation:,.2f }} 元；
2. 本案诉讼费用由被告承担。

【事实与理由】

{{ accident.date }} {{ accident.location }}，原告与被告发生交通事故。
事故经过：{{ accident.description }}

原告因此事故受伤，于 {{ plaintiff.injury_date }} 到 {{ plaintiff.hospital }} 就诊。
诊断结果：{{ plaintiff.diagnosis }}
{% if plaintiff.injury_level > 0 %}
伤残等级：{{ plaintiff.injury_level }}级
{% endif %}
住院治疗 {{ plaintiff.hospital_days }} 天。

原告因此事故产生如下损失：

1. 医疗费：{{ compensation.medical:,.2f }} 元
2. 误工费：{{ compensation.work_loss:,.2f }} 元
3. 护理费：{{ compensation.nursing:,.2f }} 元
4. 营养费：{{ compensation.nutrition:,.2f }} 元
5. 住院伙食补助费：{{ compensation.hospital_food:,.2f }} 元
{% if plaintiff.injury_level > 0 %}
6. 残疾赔偿金：{{ compensation.disability:,.2f }} 元
7. 精神损害抚慰金：{{ compensation.mental_damage:,.2f }} 元
{% endif %}
   合计：{{ total_compensation:,.2f }} 元

根据《中华人民共和国民法典》第一千一百六十五条、第一千一百七十九条、
第一千二百零八条以及《中华人民共和国道路交通安全法》第七十六条等
法律法规规定，被告应当对原告的损失承担赔偿责任。

被告驾驶的车辆投保有交强险，根据法律规定，应当先由交强险在责任
限额范围内予以赔偿，不足部分由商业险或侵权人赔偿。

现依法向贵院提起诉讼，望判如所请。

此致
{{ court_name }}

                                                具状人：{{ plaintiff.name }}
                                                {{ current_date }}
