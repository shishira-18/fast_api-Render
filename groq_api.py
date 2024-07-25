# -*- coding: utf-8 -*-

API_KEY = "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"


from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
import json




def groq_api_response(context):
    
    chat = ChatGroq(
        temperature=0,
        model="llama3-8b-8192",
        api_key= API_KEY,
      
    )

    system = """
    Rules You have to follow during response:-
    1.Always respond in JSON  format.
    2.check the context is related to person business card information or else just return null.
    3.Always identitfy the (human being) person name correctly dont get confused with organization name.
    4.These are the only keys of JSON  - NAME,PHONE,WEB,DESIGNATION,ORGANIZATION_NAME no extra key is not added.
    5.for any key if the value is not available in context just assign that key  with value null.
    
    """
    human = "Context:{text}"
    
    prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])
    
    
    chain = prompt | chat
    response = chain.invoke({"text":context })
    return response.content
    
