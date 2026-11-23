amazon-fba-cost-calculator/
│
├── app.py                  # 网页主入口
│
├── pages/
│   ├── 01_费用计算器.py
│   ├── 02_产品管理.py
│   ├── 03_库存仓储分析.py
│   ├── 04_利润分析.py
│   └── 05_费用数据库.py
│
├── core/
│   ├── fulfillment.py      # FBA配送费
│   ├── storage.py          # 仓储费
│   ├── referral.py         # 销售佣金
│   ├── aged_inventory.py   # 库龄费用
│   └── profit.py           # 利润计算
│
├── data/
│   ├── fee_rates.csv       # 费率数据
│   └── products.csv        # 产品数据
│
├── database/
│   └── db.py
│
├── requirements.txt
│
└── .streamlit/
    └── secrets.toml
