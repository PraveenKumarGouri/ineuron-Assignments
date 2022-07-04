#!/usr/bin/env python
# coding: utf-8

# In[20]:


l=[1,2,3,4,5,"sudh", 45.67,True]


# In[21]:


l[0]


# In[22]:


l[-1]


# In[23]:


len(l)


# In[24]:


l[0:5]


# In[25]:


l


# In[26]:


l[::-1]


# In[27]:


l[0:100]


# In[28]:


l[0:100:2]


# In[29]:


l


# In[30]:


l[0:8:-1]


# In[31]:


l[:3]


# In[32]:


l


# In[33]:


l+["sudh"]


# In[34]:


l*2


# In[35]:


l


# In[36]:


60 in l


# In[37]:


2 in l


# In[38]:


max(l)


# In[ ]:


l1=[3,4,5,6,6]


# In[ ]:


max(l1)


# In[ ]:


l2=["sudh","iNeuron","kumar"]


# In[ ]:


max(l2)


# In[ ]:


min(l1)


# In[ ]:


min(l2)


# In[ ]:


l


# In[ ]:


l.append("kumar")


# In[ ]:


l


# In[ ]:


l.append([1,2,3,4])


# In[ ]:


l


# In[ ]:


l.pop(0)


# In[ ]:


l


# In[ ]:


l.pop()


# In[ ]:


l


# In[ ]:


l.reverse()


# In[ ]:


l


# In[ ]:


l[::-1]


# In[ ]:


l.reverse()


# In[39]:


l


# In[40]:


l.append([2,3,4,5])


# In[41]:


l


# In[42]:


l1


# In[ ]:


l1.sort()


# In[ ]:


l1


# In[ ]:


l3= [8,98,34,23,1,0]


# In[ ]:


l3.sort(reverse = True)


# In[ ]:


l3


# In[ ]:


l1=[2,3,4]
l2=[6,7,8]
l3=[3,2,4]


# In[ ]:


l4 = [l1,l2,l3]


# In[ ]:


l4


# In[43]:


l4[2][1]


# In[ ]:


l


# In[ ]:


l.count(2)


# In[44]:


l5 = [3,4,5,3,3,3]


# In[45]:


l5.count(3)


# In[46]:


l1=[1,2,3]
l2=[4,5,6]
l3=[7,8,9]
l4=[l1,l2,l3]
l4.count(3)


# In[47]:


l4


# In[48]:


l4.count(3)


# In[49]:


l


# In[50]:


l.append("iNeuron")


# In[51]:


l


# In[52]:


l.append([4,56,"sudh"])


# In[53]:


l


# In[54]:


l.extend("sudh")


# In[55]:


l


# In[56]:


l6 =[1,2,3]


# In[57]:


l6.append([4,5,6])


# In[58]:


l6


# In[59]:


l6.append("sudh")


# In[60]:


l6


# In[61]:


l6.extend(45)


# In[ ]:


l6.append(45)


# In[ ]:


l6


# In[ ]:


l6.extend([56,34,21])


# In[ ]:


l6


# In[ ]:


l6.extend("sudh")


# In[ ]:


l6


# In[ ]:


l6


# In[ ]:


l6.index(1)


# In[ ]:


l7 =[1,2,3,4,55,6,6,7]


# In[ ]:


l7.index(6)


# In[ ]:


l = [1,2,3,4,5]


# In[ ]:


l.append(45)


# In[ ]:


l


# In[ ]:


l.insert(1,[1,2,34])


# In[ ]:


l


# In[ ]:


l.insert(5,"sudh")


# In[ ]:


l


# In[ ]:


l.pop()


# In[ ]:


l.pop(2)


# In[ ]:


l


# In[ ]:


l.remove(100)


# In[ ]:


l.remove(4)


# In[ ]:


l


# In[ ]:


l.remove(3)


# In[ ]:


l


# In[ ]:


l = [1,2,3,4]


# In[62]:


l[2] ="sudh"


# In[63]:


l


# In[64]:


s="iNeuron"


# In[65]:


s[2] = 'z'


# In[ ]:


t = (4,5,6,7,"sudh",45.67,True)


# In[ ]:


type(t)


# In[ ]:


t[0
]


# In[ ]:


t[0:4]


# In[66]:


t[-1]


# In[ ]:


t


# In[ ]:


t[0:6:2]


# In[67]:


t[0:4:-1]


# In[ ]:


l = [1,2,3,456,78]


# In[ ]:


l[2] = "kumar"


# In[68]:


l


# In[69]:


t


# In[ ]:


t[2] = "sudh"


# In[ ]:


t1 = (3,4,5,6)


# In[70]:


t


# In[ ]:


t+t1


# In[ ]:


t.count(3)


# In[ ]:


t.count(4)


# In[71]:


t = t+t1


# In[ ]:


t


# In[ ]:


t.index(5)


# In[72]:


t = (3,4,56,7,"sudh")


# In[73]:


t2 = list(t)


# In[74]:


t2


# In[75]:


tuple(t2)


# In[76]:


str(t2)


# In[77]:


d = {}


# In[78]:


type(d)


# In[79]:


d1 = {1}


# In[80]:


type(d1)


# In[81]:


d2 = {'key1' : "value" , 234 : "xyz" , "name" : "sudh", "no" : 34324345}


# In[82]:


type(d2)


# In[83]:


d2['name']


# In[84]:


d2['no']


# In[85]:


d3 = {'name' : "sudh" , 'tech' : ["python", "ML","DL","NLP","CV","Bigdata","data analytics"] }


# In[86]:


d3


# In[87]:


d3['tech']


# In[88]:


"python" in d3['tech']


# In[89]:


d4 = {"name" : "iNeuron" , "contact_info" : 345345 , "name" : "sudh"}


# In[90]:


d4


# In[91]:


d4["name1"] = "xyz"


# In[92]:


d4


# In[93]:


d4['k2'] = d2


# In[94]:


d2


# In[95]:


d4


# In[96]:


d4['k2']['no']


# In[97]:


d5 = {_: "sdfsd"}


# In[98]:


d5[_]


# In[99]:


d6 = {(1,2,34) : "fsdfs"}


# In[100]:


d6[(1,2,34)]


# In[101]:


d7 = {[1,2,3,4] : "fasdfasfas"}


# In[ ]:


d8 = {{3:4} : "fsdfs"}


# In[ ]:


d2


# In[ ]:


d3


# In[ ]:


d2 +d3


# In[ ]:


d2


# In[ ]:


d2.keys()


# In[ ]:


d2.values()


# In[ ]:


d2.items()


# In[ ]:


s = {3,4,5,6,7,8}


# In[ ]:


type(s)


# In[ ]:


s1 = {3,4,4,5,6,6,7,7,8,8,9,9,0,0,0}


# In[ ]:


s1


# In[ ]:


s2 = {3245,4545,6456,5645,675,6234,345}


# In[ ]:


s2


# In[ ]:


s3 = {"sudh", 324,34,12,645,12,5,'b','sudh'}


# In[ ]:


s3


# In[ ]:


s3[0]


# In[ ]:


list(s3)


# In[ ]:


tuple(s3)


# In[ ]:


l = [2,3,4,5666,7,6,7,7,7,77,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7]


# In[ ]:


l = list(set(l))


# In[ ]:


l


# In[ ]:


s2.add(34)


# In[ ]:


s2


# In[ ]:


s2.add([1,2,3,4,5])


# In[ ]:


s = {(1,2,3,4,5), 3,4,45,65,6}


# In[ ]:


s


# In[ ]:


s1 = {[1,2,3,4],345,345}


# In[ ]:


s


# In[ ]:


s.remove(3)


# In[ ]:


s


# In[ ]:


s.discard(4)


# In[ ]:


s.pop()


# In[ ]:


type(s)


# In[102]:


list(s)


# In[103]:


l = list(s)


# In[104]:


l


# In[105]:


set(l)


# In[106]:


d2


# In[107]:


l9 = [3,4,5,6,7]


# In[108]:


l9.reverse()


# In[109]:


l9


# In[110]:


l1 = [23,456,67,8,78,78]
l2 = [345,56,87,8,98,9]
l3 = [234,6657,6]


# In[111]:


l4 = [l1,l2,l3]


# In[112]:


l4


# In[113]:


l4[2][0]


# In[114]:


l4[0][1]


# In[115]:


l = [3,4,5,6,7, [23,456,67,8,78,78],[345,56,87,8,98,9],[234,6657,6],{"key1" : "sudh" , 234:[23,45,656]}]


# In[116]:


l


# In[117]:


l[0:8]


# In[118]:


l = {"key1" : "sudh" , 234:[23,45,656]}


# In[119]:


l["key1"]


# In[120]:


l.keys()


# In[121]:


l.values()

