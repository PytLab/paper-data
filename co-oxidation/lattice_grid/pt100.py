
# coding: utf-8

# In[1]:


# # 扩展supercell

# In[2]:

nodes, edges = [], []


# ## 创建nodes 和 edges

# ### top位相关

# In[3]:

from catplot.grid_components.nodes import Node2D
from catplot.grid_components.edges import Edge2D


# In[4]:

top = Node2D([0.0, 0.0], size=1200, color="#2A6A9C")


# In[5]:

t1 = Node2D([0.0, 1.0])
t2 = Node2D([1.0, 0.0])


# In[6]:

nodes.append(top)


# In[7]:

e1 = Edge2D(top, t1, width=8, zorder=10)
e2 = Edge2D(top, t2, width=8, zorder=10)


# In[8]:

edges.extend([e1, e2])


# ### bridge相关

# In[9]:

bridge1 = Node2D([0.0, 0.5], style="s", size=400, color="#5A5A5A", alpha=0.6, line_width=2)
bridge2 = Node2D([0.5, 0.0], style="s", size=400, color="#5A5A5A", alpha=0.6, line_width=2)


# In[10]:

b1 = bridge1.clone([0.5, 0.5])
b2 = bridge2.clone([0.5, 0.5])


# In[11]:

nodes.extend([bridge1, bridge2])


# In[12]:

e1 = Edge2D(bridge1, b1, width=2)
e2 = Edge2D(bridge1, bridge2, width=2)
e3 = Edge2D(bridge2, b2, width=2)
e4 = Edge2D(b1, b2, width=2)


# In[13]:

edges.extend([e1, e2, e3, e4])


# ### hollow位

# In[14]:

h = Node2D([0.5, 0.5], style="h", size=500, color="#5A5A5A", alpha=0.3, line_width=2)


# In[15]:

nodes.append(h)


# ## 绘制

# In[16]:

from catplot.grid_components.grid_canvas import Grid2DCanvas


# In[17]:

canvas = Grid2DCanvas()


# In[18]:

from catplot.grid_components.supercell import SuperCell2D


# In[19]:

supercell = SuperCell2D(nodes, edges)


# ## 将此supercell进行扩展

# In[22]:

expanded_supercell = supercell.expand(4, 4)


# ## 绘制

# In[23]:

canvas_big = Grid2DCanvas(figsize=(30, 20), dpi=60)


# In[24]:

canvas_big.add_supercell(expanded_supercell)


# In[25]:

canvas_big.draw()

