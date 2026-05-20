import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar

df = pd.read_excel("data.xlsx")
c = (
    Bar()
    .add_xaxis(df["品項"].tolist())
    .add_yaxis("商家 A", df["商家A"].tolist())
    .add_yaxis("商家 B", df["商家B"].tolist())
    .set_global_opts(title_opts=opts.TitleOpts(title="這是data.xlsx裡的資料", subtitle="商家A與商家B的資料"))
)
c.render("bar03.html")

