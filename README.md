# 齿轮传动计算器 Gear Calculator

一个使用 HTML、CSS、JavaScript 和 Python 开发的机械工程学习项目。

## 功能
- 输入主动轮、从动轮齿数、模数和转速
- 计算传动比、从动轮转速、分度圆直径和标准中心距
- 计算主动轮和从动轮齿顶圆直径
- 绘制齿轮啮合示意图
- 对无效输入进行基本校验

## 计算公式
- 传动比：i = z₂ / z₁
- 从动轮转速：n₂ = n₁ / i
- 分度圆直径：d = mz
- 齿顶圆直径：da = m(z + 2)
- 标准中心距：a = m(z₁ + z₂) / 2

## 运行方法
在项目目录运行 python3 -m http.server 8000，然后访问 http://127.0.0.1:8000/

## 文件说明
- index.html：网页计算器
- main.py：Python 命令行计算器
- index-v1-backup.html：V1 备份
- index-v2-backup.html：V2 备份

## 注意事项
本项目用于学习和基础参数估算。示意图不是精确加工齿形，实际设计需要进行工程校核。
Git practice: my first update.
