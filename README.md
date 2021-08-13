
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-Python 3.7-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/scrapy/scrapy">
    <img alt="scrapy" src="https://img.shields.io/badge/scrapy-success.svg" target="_blank" />
  </a>
  <a href="https://github.com/GuoGuang0536/python_spider/master/LICENSE">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" target="_blank" />
  </a>
  <a href="https://twitter.com/GuoGuang">
    <img alt="Twitter: GuoGuang0536" src="https://img.shields.io/twitter/follow/GuoGuang.svg?style=social" target="_blank" />
  </a>
</p>

## Flask isomerism
提供基础爬虫接口、爬虫脚本，集成到Eureka，主要实现异构系统使用。
如果需要添加新的脚本的在jobs\tasks下添加


### 🏠 [Homepage](codeway.fun)

## Prerequisites

- python3
- Flask


## Install

```sh
git clone https://github.com/GuoGuang/spider.git
```

## Table structure
``` 
CREATE TABLE `movie`  (
  `id` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '电影名称',
  `desc` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '电影描述',
  `classify` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '类别',
  `actor` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '主演',
  `director` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '导演',
  `cover_pic` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '封面图',
  `pics` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '图片地址',
  `magnet_url` varchar(5000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '磁力下载地址',
  `online _url` varchar(5000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '在线播放地址',
  `pub_date` bigint(20) NOT NULL COMMENT '发布日期',
  `rating` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '评分',
  `source` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '来源',
  `visits` int(11) NOT NULL DEFAULT 0 COMMENT '阅读数',
  `is_recommend` int(11) NOT NULL DEFAULT 0 COMMENT '是否推荐，0不推荐，1推荐',
  `update_at` bigint(20) NOT NULL,
  `create_at` bigint(20) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `idx_pu_date`(`pub_date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

// If you create a new entity use auto generate model
flask-sqlacodegen "mysql://root:123456@127.0.0.1/movie_cat" --tables user --outfile "common/models/user.py"  --flask
```

## Usage

```bash

 Run with "python3 manager.py runjob -m movie" start the crawler
 Run with "python3 manager.py runserver" start the web
```


## Job task
Use Linux Crontab implementation
```bash
// 编辑文件
crontab -e 

# 编写脚本 自动执行爬虫
* */1 * * * { export ops_config=local && python3 /Yourdirectory/manager.py runjob -m movie }

```




```bash
# 使用以下命令启动爬虫
 python manager.py runjob -m movie 
 
# 使用以下命令启动Flask web
python manager.py runserver
```

## Author

👤 **GuoGuang**

* Twitter: [@GuoGuang0536](https://twitter.com/GuoGuang0536)
* Github: [@GuoGuang0536](https://github.com/GuoGuang)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/GuoGuang0536/python_spider/issues).

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2019 [GuoGuang](https://github.com/GuoGuang).<br />
This project is [GuoGuang](mit) licensed.
