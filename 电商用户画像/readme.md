## 某电商app用户画像分析

#### 项目背景

电商行业快速发展的今天，电商数据急剧增加，可以利用一些数仓工具及数据处理软件提取有效数据，分析高潜用户，并进行针对性的营销策略。本项目的分析数据来源为16年真实电商数据，数据源过大，不上传到github上了

项目操作；

- 利用数据库工具mysql获取电商数据。
- 通过python进行探索性数据分析，根据高潜用户的特征：必须有购买行为；对一个商品购买和其他交互行为（浏览，点击，收藏等）的时间差应该多于1天提取高潜用户。
- 利用数据透视表查看
  - 高潜客户的客户等级分布
  - 高潜客户的年龄段对比
  - 购买数据维度：不同量段的对比
- 最后，对高潜用户的行为数据提供针对性的营销建议