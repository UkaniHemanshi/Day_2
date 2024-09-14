import  plotly.graph_objects as go
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales_data = np.random.randint(50, 500, size=12)
print(sales_data)

# line plot
line_fig = go.Figure()
line_fig.add_trace(go.Scatter(x=months,y=sales_data,mode="lines+markers",name='Sales'))
line_fig.update_layout(title="Monthly sales data",xaxis_title="months",yaxis_title="Sales_data")
line_fig.write_image('line_plot.png')

# bar plot
bar_fig = go.Figure()
bar_fig.add_trace(go.Bar(x=months,y=sales_data,name='Sales'))
bar_fig.update_layout(title="Monthly sales data-Bar chart",xaxis_title="months",yaxis_title="Sales_data")
bar_fig.write_image('bar_plot.png')
