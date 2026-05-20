from pyecharts import options as opts
from pyecharts.charts import Bar

c = (    
     Bar()    
     .add_xaxis(["襯衫", "羊毛衫", "雪紡衫", "褲子", "高跟鞋", "襪子", "T恤"])   
     .add_yaxis("商家 A", [5, 20, 36, 10, 75, 90, 40], stack="stack1")    
     .add_yaxis("商家 B", [15, 25, 16, 55, 48, 8, 30], stack="stack1")   
     .set_global_opts(title_opts=opts.TitleOpts(title="這是一個堆疊圖", subtitle="商家A與商家B的資料"))    
)
c.render("bar04.html")