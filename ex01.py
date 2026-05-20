from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker
c = (    
     Bar()    
     .add_xaxis(Faker.choose())    
     .add_yaxis("商家1", Faker.values())    
     .add_yaxis("商家2", Faker.values())   
     .set_global_opts(title_opts=opts.TitleOpts(title="這是假資料", subtitle="全都是假的"),
                      yaxis_opts=opts.AxisOpts(name="這個是 Y 軸"),
                      xaxis_opts=opts.AxisOpts(name="這個是 X 軸"),)    
)
c.render("bar01.html")

