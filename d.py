#!/usr/bin/env python
# coding: utf-8

# ## library data

# In[42]:


library_data={1000:{'book_name':'dystopian',
                   'quantity':10,
                   'genre':'sci-fi',
                   'author':'alan',
                   'price':3000},
             1001:{'book_name':'the dairy of anne frank',
                  'quantity':14,
                  'genre':'journal',
                  'autor':'turing',
                  'price':1500},
             1002:{'book_name':'lord of the flies',
                  'quantity':7,
                  'genre':'classic',
                  'author':'jane austen',
                  'price':1200}}


# ## student data

# In[36]:


student_data={4011:{'name':'alan',
                   'graduation':2024,
                   'graduation_dregree':'B.E',
                   'book_issued':{'book_id':1000,
                                 'issue_date':'19-03-2023',
                                 'expire_date':'29-03-2023'}},
             4013:{'name':'anderson',
                   'graduation':2024,
                   'graduation_dregree':'B.E',
                   'book_issued':{'book_id':1001,
                                 'issue_date':'22-03-2023',
                                 'expire_date':'02-04-2023'}},
             4015:{'name':'amrutha',
                   'graduation':2025,
                   'graduation_dregree':'B.E',
                   'book_issued':{'book_id':1002,
                                 'issue_date':'25-03-2023',
                                 'expire_date':'05-04-2023'}}}
                    
                    
                    


# ## displaying the details
# 

# In[37]:


def display_data():
    n=int(input('enter the option "0"for library , "1 for student"'))
    if n==0:
        print('-'*20)
        for i in library_data.keys():
            print(library_data[i])
            print('-'*20)
        
    else:
        print('-'*20)
        for i in student_data.keys():
            print(student_data[i])
            print('-'*20)


# In[25]:


display_data()


# ## adding item

# In[38]:



def adding_item():
    n=int(input('enter the value : '))
    if (n == 0):
        book_name=str(input('enter the book name : '))
        book_id=int(input('enter the book id : '))
        quantity=int(input('enter the quanity : '))
        genre=str(input('enter the genre: '))
        price=int(input('enter the price : '))
        author=str(input('enter the author name : '))
        
        temp={}
        temp['book_name']=book_name
        temp['quantity']=quantity
        temp['genre']=genre
        temp['author']=author
        temp['price']=price
                     
        library_data[book_id] = temp  
        
    else:
        student_name=str(input('enter the student name : '))
        student_id=int(input('enter the student id : '))
        graduation_year=int(input('enter the graduation year : '))
        graduation_degree=str(input('enter the graduation degree :'))
        books_id=int(input('enter  the book id : '))
        issue_date=str(input('enter the issue date : '))
        expiry_date=str(input('enter the expiry date : '))
        
        book_issued={}
        book_issued['book_id'] = book_id
        book_issued['issue_date'] = issue_date
        book_issued['expiry date'] = expiry_date
        
        temp={}
        temp['student_name'] = student_name
        temp['graduation_year'] = graduation_year
        temp['graduation_degree'] = graduation_degree
        
        temp['book_issued']=book_issued
        
        student_data[student_id] = temp
        


# In[28]:


adding_item()


# ## update of data
# 

# In[41]:


def update_data():
    
    n=int(input('enter the type ISSUES | or | SUBMISSION : '))
    if (n == 0 ):
        book_id=int(input('enter the book id number : '))
          
          
        if (book_id in library_data.keys()):
            library_data['book_id']['quantity']=library_data['book_id']['quantity'] - 1
          

    else:
        book_id=int(input('enter the book id number : '))
        if (book_id in library_data.keys()):
            library_data['book_id']['quantity']=library_data['book_id']['quantity'] + 1
            
     
          


# In[22]:


update_data()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




