
# coding: utf-8

# In[2]:



# # 绘制3D supercell

# ## 创建nodes

# In[3]:

from catplot.grid_components.nodes import Node3D


# In[4]:

n1 = Node3D([0.0, 0.0, 0.0], color="#0F387A", size=150, alpha=0.6)
n2 = Node3D([0.0, 0.5, 0.0], color="#5A5A5A", size=50, alpha=0.6)
n3 = Node3D([0.5, 0.0, 0.0], color="#5A5A5A", size=50, alpha=0.6)
n4 = Node3D([0.3, 0.3, 0.3], color="#5A5A5A", size=50, alpha=0.3)


# ### 创建辅助nodes

# In[5]:

an1 = Node3D([1.0, 0.0, 0.0], color="#0F387A")
an2 = Node3D([0.0, 1.0, 0.0], color="#0F387A")
an3 = Node3D([0.0, 0.0, 1.0], color="#0F387A")


# ## 创建edges

# In[6]:

from catplot.grid_components.edges import Edge3D


# In[7]:

ex = Edge3D(n1, an1, width=1.5, alpha=0.7)
ey = Edge3D(n1, an2, width=1.5, alpha=0.7)
ez = Edge3D(n1, an3, width=1.5, alpha=0.7)


# In[8]:

#e1 = Edge3D(n1, n2, color="#5A5A5A", alpha=0.5)
#e2 = Edge3D(n1, n3, color="#5A5A5A", alpha=0.5)
e3 = Edge3D(n1, n4, color="#5A5A5A", alpha=0.5)


# ## 创建 supercell

# In[9]:

from catplot.grid_components.supercell import SuperCell3D


# In[10]:

supercell = SuperCell3D([n1, n4], [ex, ey, ez, e3])


# ## 创建3D画布

# In[11]:

from catplot.grid_components.grid_canvas import Grid3DCanvas


# In[12]:

canvas = Grid3DCanvas(figsize=(30, 20), dpi=100)


# ## 扩展supercell

# In[13]:

expanded_supercell = supercell.expand(4, 4, 4)


# ## 绘制

# In[14]:

canvas.add_supercell(expanded_supercell)


# In[15]:

canvas.draw()

