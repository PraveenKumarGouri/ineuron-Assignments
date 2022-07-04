#!/usr/bin/env python
# coding: utf-8

# In[1]:


l=[1,2,3,4,5,"sudh", 45.67,True]


# In[2]:


l[0]


# In[3]:


l[-1]


# In[4]:


len(l)


# In[5]:


l[0:5]


# In[6]:


l


# In[7]:


l[::-1]


# In[8]:


l[0:100]


# In[9]:


l[0:100:2]


# In[10]:


l


# In[11]:


l[0:8:-1]


# In[12]:


l[:3]


# In[13]:


l


# In[14]:


l+["sudh"]


# In[15]:


l*2


# In[16]:


l


# In[17]:


60 in l


# In[18]:


2 in l


# In[19]:


max(l)


# In[20]:


l1=[3,4,5,6,6]


# In[21]:


max(l1)


# In[22]:


l2=["sudh","iNeuron","kumar"]


# In[23]:


max(l2)


# In[24]:


min(l1)


# In[25]:


min(l2)


# In[26]:


l


# In[27]:


l.append("kumar")


# In[28]:


l


# In[29]:


l.append([1,2,3,4])


# In[30]:


l


# In[31]:


l.pop(0)


# In[32]:


l


# In[33]:


l.pop()


# In[34]:


l


# In[35]:


l.reverse()


# In[36]:


l


# In[37]:


l[::-1]


# In[38]:


l.reverse()


# In[39]:


l


# In[40]:


l.append([2,3,4,5])


# In[41]:


l


# In[42]:


l1


# In[43]:


l1.sort()


# In[44]:


l1


# In[45]:


l3= [8,98,34,23,1,0]


# In[46]:


l3.sort(reverse = True)


# In[47]:


l3


# In[48]:


l1=[2,3,4]
l2=[6,7,8]
l3=[3,2,4]


# In[49]:


l4 = [l1,l2,l3]


# In[50]:


l4


# In[51]:


l4[2][1]


# In[52]:


l


# In[53]:


l.count(2)


# In[54]:


l5 = [3,4,5,3,3,3]


# In[55]:


l5.count(3)


# In[56]:


l1=[1,2,3]
l2=[4,5,6]
l3=[7,8,9]
l4=[l1,l2,l3]
l4.count(3)


# In[57]:


l4


# In[58]:


l4.count(3)


# In[59]:


l


# In[60]:


l.append("iNeuron")


# In[61]:


l


# In[62]:


l.append([4,56,"sudh"])


# In[63]:


l


# In[64]:


l.extend("sudh")


# In[65]:


l


# In[66]:


l6 =[1,2,3]


# In[67]:


l6.append([4,5,6])


# In[68]:


l6


# In[69]:


l6.append("sudh")


# In[70]:


l6


# In[71]:


l6.extend(45)


# In[72]:


l6.append(45)


# In[73]:


l6


# In[74]:


l6.extend([56,34,21])


# In[75]:


l6


# In[76]:


l6.extend("sudh")


# In[77]:


l6


# In[78]:


l6


# In[79]:


l6.index(1)


# In[80]:


l7 =[1,2,3,4,55,6,6,7]


# In[81]:


l7.index(6)


# In[82]:


l = [1,2,3,4,5]


# In[83]:


l.append(45)


# In[84]:


l


# In[85]:


l.insert(1,[1,2,34])


# In[86]:


l


# In[87]:


l.insert(5,"sudh")


# In[88]:


l


# In[89]:


l.pop()


# In[90]:


l.pop(2)


# In[91]:


l


# In[92]:


l.remove(100)


# In[93]:


l.remove(4)


# In[94]:


l


# In[95]:


l.remove(3)


# In[96]:


l


# In[97]:


l = [1,2,3,4]


# In[98]:


l[2] ="sudh"


# In[99]:


l


# In[100]:


s="iNeuron"


# In[101]:


s[2] = 'z'


# In[102]:


t = (4,5,6,7,"sudh",45.67,True)


# In[103]:


type(t)


# In[104]:


t[0
]


# In[105]:


t[0:4]


# In[106]:


t[-1]


# In[107]:


t


# In[108]:


t[0:6:2]


# In[109]:


t[0:4:-1]


# In[110]:


l = [1,2,3,456,78]


# In[111]:


l[2] = "kumar"


# In[112]:


l


# In[113]:


t


# In[114]:


t[2] = "sudh"


# In[115]:


t1 = (3,4,5,6)


# In[116]:


t


# In[117]:


t+t1


# In[118]:


t.count(3)


# In[119]:


t.count(4)


# In[120]:


t = t+t1


# In[121]:


t


# In[122]:


t.index(5)


# In[123]:


t = (3,4,56,7,"sudh")


# In[124]:


t2 = list(t)


# In[125]:


t2


# In[126]:


tuple(t2)


# In[127]:


str(t2)


# In[128]:


d = {}


# In[129]:


type(d)


# In[130]:


d1 = {1}


# In[131]:


type(d1)


# In[132]:


d2 = {'key1' : "value" , 234 : "xyz" , "name" : "sudh", "no" : 34324345}


# In[133]:


type(d2)


# In[134]:


d2['name']


# In[135]:


d2['no']


# In[136]:


d3 = {'name' : "sudh" , 'tech' : ["python", "ML","DL","NLP","CV","Bigdata","data analytics"] }


# In[137]:


d3


# In[138]:


d3['tech']


# In[139]:


"python" in d3['tech']


# In[140]:


d4 = {"name" : "iNeuron" , "contact_info" : 345345 , "name" : "sudh"}


# In[141]:


d4


# In[142]:


d4["name1"] = "xyz"


# In[143]:


d4


# In[144]:


d4['k2'] = d2


# In[145]:


d2


# In[146]:


d4


# In[147]:


d4['k2']['no']


# In[148]:


d5 = {_: "sdfsd"}


# In[149]:


d5[_]


# In[150]:


d6 = {(1,2,34) : "fsdfs"}


# In[151]:


d6[(1,2,34)]


# In[152]:


d7 = {[1,2,3,4] : "fasdfasfas"}


# In[153]:


d8 = {{3:4} : "fsdfs"}


# In[154]:


d2


# In[155]:


d3


# In[156]:


d2 +d3


# In[159]:


d2


# In[160]:


d2.keys()


# In[161]:


d2.values()


# In[162]:


d2.items()


# In[163]:


s = {3,4,5,6,7,8}


# In[164]:


type(s)


# In[165]:


s1 = {3,4,4,5,6,6,7,7,8,8,9,9,0,0,0}


# In[166]:


s1


# In[167]:


s2 = {3245,4545,6456,5645,675,6234,345}


# In[168]:


s2


# In[169]:


s3 = {"sudh", 324,34,12,645,12,5,'b','sudh'}


# In[170]:


s3


# In[171]:


s3[0]


# In[172]:


list(s3)


# In[173]:


tuple(s3)


# In[174]:


l = [2,3,4,5666,7,6,7,7,7,77,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7]


# In[175]:


l = list(set(l))


# In[176]:


l


# In[177]:


s2.add(34)


# In[178]:


s2


# In[179]:


s2.add([1,2,3,4,5])


# In[180]:


s = {(1,2,3,4,5), 3,4,45,65,6}


# In[181]:


s


# In[182]:


s1 = {[1,2,3,4],345,345}


# In[183]:


s


# In[184]:


s.remove(3)


# In[185]:


s


# In[186]:


s.discard(4)


# In[187]:


s.pop()


# In[188]:


type(s)


# In[190]:


list(s)


# In[191]:


l = list(s)


# In[192]:


l


# In[193]:


set(l)


# In[194]:


d2


# In[197]:


l9 = [3,4,5,6,7]


# In[198]:


l9.reverse()


# In[199]:


l9


# In[208]:


l1 = [23,456,67,8,78,78]
l2 = [345,56,87,8,98,9]
l3 = [234,6657,6]


# In[209]:


l4 = [l1,l2,l3]


# In[210]:


l4


# In[211]:


l4[2][0]


# In[212]:


l4[0][1]


# In[213]:


l = [3,4,5,6,7, [23,456,67,8,78,78],[345,56,87,8,98,9],[234,6657,6],{"key1" : "sudh" , 234:[23,45,656]}]


# In[214]:


l


# In[215]:


l[0:8]


# In[216]:


l = {"key1" : "sudh" , 234:[23,45,656]}


# In[217]:


l["key1"]


# In[218]:


l.keys()


# In[219]:


l.values()


# In[ ]:




