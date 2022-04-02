#!/usr/bin/env python
# coding: utf-8

# In[1]:


# pip install flask


# In[2]:


from flask import Flask #, request, render_template


# In[3]:


from textblob import TextBlob


# In[4]:


app = Flask(__name__) #__name__ => to make sure it is yourself


# In[5]:


#import joblib


# In[6]:


from flask import request, render_template

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST": #this happens after pressing button submit
        text = request.form.get("text") #add after testing
        print(text) #add after testing
        s = TextBlob(text).sentiment #add after testing
        return(render_template("index.html", result=s)) #change from "1" to pred1, pred2, pred3
    else:
        return(render_template("index.html", result="2")) #this happens before pressing button submit


# In[ ]:


if __name__=="__main__":
    app.run() #change from app.run() to app.run(host='0.0.0.0',port=80) if 5000 cannot work


# In[ ]:


#Step 1:

#from flask import request, render_template

#@app.route("/", methods=["GET","POST"])
#def index():
#    if request.method == "POST": #this happens after pressing button submit
#        return(render_template("index.html", result="1")) #change from "1" to pred1, pred2, pred3
#    else:
#        return(render_template("index.html", result="2")) #this happens before pressing button submit


# In[ ]:


#Step 1:

#from flask import request, render_template

#@app.route("/", methods=["GET","POST"])
#def index():
#    if request.method == "POST": #this happens after pressing button submit
#        return(render_template("index.html", result="1")) #change from "1" to pred1, pred2, pred3
#    else:
#        return(render_template("index.html", result="2")) #this happens before pressing button submit


# In[ ]:


#Step 2

#from flask import request, render_template

#@app.route("/", methods=["GET","POST"])
#def index():
#    if request.method == "POST": #this happens after pressing button submit
#        text = request.form.get("text") #add after testing
#        print(text) #add after testing
#        s = TextBlob(text).sentiment #add after testing
#        return(render_template("index.html", result=s)) #change from "1" to pred1, pred2, pred3
#    else:
#        return(render_template("index.html", result="2")) #this happens before pressing button submit


# In[ ]:


#index.html
#<form action="http://127.0.0.1:5000/" method="post"> 
#<form action="/" method="post"> 

#if 5000 cannot work
#if __name__=="__main__":
#    app.run(host='0.0.0.0',port=80)

