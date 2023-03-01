#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Create a function that returns with a subsest of a list.
#The subset's starting and ending indexes should be set as input parameters (the list aswell).
#return type: list
#function name must be: subset
#input parameters: input_list,start_index,end_index


# In[3]:


def subset(input_list, start_index, end_index) -> list:
    return input_list[start_index:end_index]


# In[ ]:


#Create a function that returns every nth element of a list.
#return type: list
#function name must be: every_nth
#input parameters: input_list,step_size


# In[4]:


def every_nth(input_list, step_size) -> list:
    return [input_list[i] for i in range(0, len(input_list), step_size)]


# In[ ]:


#Create a function that can decide whether a list contains unique values or not
#return type: bool
#function name must be: unique
#input parameters: input_list


# In[8]:


def unique(input_list) -> bool:
    for item in input_list:
        if input_list.count(item) > 1:
            return False
    return True


# In[ ]:


#Create a function that can flatten a nested list ([[..],[..],..])
#return type: list
#fucntion name must be: flatten
#input parameters: input_list


# In[15]:


def flatten(input_list) -> list:
    output_list = []
    for sublist in input_list:
        output_list.extend(sublist)
    return output_list


# In[ ]:


#Create a function that concatenates n lists
#return type: list
#function name must be: merge_lists
#input parameters: *args


# In[17]:


def merge_lists(*args) -> list:
    output_list = []
    for item in args:
        output_list.extend(item)
    return output_list


# In[ ]:


#Create a function that can reverse a list of tuples
#example [(1,2),...] => [(2,1),...]
#return type: list
#fucntion name must be: reverse_tuples
#input parameters: input_list


# In[23]:


def reverse_tuples(input_list) -> list:
    output_list = []
    for item in input_list:
        output_list.append(item[::-1])
    return output_list


# In[ ]:


#Create a function that removes duplicates from a list
#return type: list
#fucntion name must be: remove_tuplicates
#input parameters: input_list


# In[31]:


def remove_tuplicates(input_list) -> list:
    return list(set(input_list))


# In[ ]:


#Create a function that transposes a nested list (matrix)
#return type: list
#function name must be: transpose
#input parameters: input_list


# In[43]:


def transpose(input_list) -> list:
    output_list = [[0 for i in range(len(input_list))] for j in range(len(input_list[0]))]
    for i in range(len(input_list)):
        for j in range(len(input_list[0])):
            output_list[j][i] = input_list[i][j]
    return output_list


# In[ ]:


#Create a function that can split a nested list into chunks
#chunk size is given by parameter
#return type: list
#function name must be: split_into_chunks
#input parameters: input_list,chunk_size


# In[51]:


def split_into_chunks(input_list, chunk_size) -> list:
    output_list = flatten(input_list)
    return [output_list[i:i+chunk_size] for i in range(0, len(output_list), chunk_size)]


# In[ ]:


#Create a function that can merge n dictionaries
#return type: dictionary
#function name must be: merge_dicts
#input parameters: *dict


# In[53]:


def merge_dicts(*dicts) -> dict:
    output_dict = {}
    for item in dicts:
        output_dict.update(item)
    return output_dict


# In[ ]:


#Create a function that receives a list of integers and sort them by parity
#and returns with a dictionary like this: {"even":[...],"odd":[...]}
#return type: dict
#function name must be: by_parity
#input parameters: input_list


# In[55]:


def by_parity(input_list) -> dict:
    evens = [num for num in input_list if num % 2 == 0]
    odds = [num for num in input_list if num % 2 != 0]
    return {"even": evens, "odd": odds}


# In[ ]:


#Create a function that receives a dictionary like this: {"some_key":[1,2,3,4],"another_key":[1,2,3,4],....}
#and return a dictionary like this : {"some_key":mean_of_values,"another_key":mean_of_values,....}
#in short calculates the mean of the values key wise
#return type: dict
#function name must be: mean_key_value
#input parameters: input_dict


# In[68]:


def mean_key_value(input_dict: dict) -> dict:
    output_dict = {}
    for pair in input_dict.items():
        output_dict[pair[0]] = sum(pair[1]) / len(pair[1])
    return output_dict


# In[ ]:


#If all the functions are created convert this notebook into a .py file and push to your repo

