
# coding: utf-8

# In[1]:


# # 绘制3D supercell

# ## 创建nodes

# In[2]:

from catplot.grid_components.nodes import Node3D


# In[3]:

n1 = Node3D([0.0, 0.0, 0.0], color="#0F387A")
n2 = Node3D([0.0, 0.5, 0.5], color="#5A5A5A", size=200, alpha=0.6)
n3 = Node3D([0.5, 0.0, 0.5], color="#5A5A5A", size=200, alpha=0.6)
n4 = Node3D([0.5, 0.5, 0.5], color="#5A5A5A", size=200, alpha=0.3)


# ### 创建辅助nodes

# In[4]:

an1 = Node3D([1.0, 0.0, 0.0], color="#0F387A")
an2 = Node3D([0.0, 1.0, 0.0], color="#0F387A")
an3 = Node3D([0.0, 0.0, 1.0], color="#0F387A")


# ## 创建edges

# In[5]:

from catplot.grid_components.edges import Edge3D


# In[6]:

ex = Edge3D(n1, an1, width=6)
ey = Edge3D(n1, an2, width=6)
ez = Edge3D(n1, an3, width=6)


# In[7]:

e1 = Edge3D(n1, n2, color="#5A5A5A")
e2 = Edge3D(n1, n3, color="#5A5A5A")
e3 = Edge3D(n1, n4, color="#5A5A5A")


# ## 创建 supercell

# In[8]:

from catplot.grid_components.supercell import SuperCell3D


# In[9]:

supercell = SuperCell3D([n1, n2, n3, n4], [ex, ey, ez, e1, e2, e3])


# ## 创建3D画布

# In[10]:

from catplot.grid_components.grid_canvas import Grid3DCanvas


# In[11]:

canvas = Grid3DCanvas()


# ## 绘制

# In[12]:

canvas.add_supercell(supercell)


# In[13]:

canvas.draw()

