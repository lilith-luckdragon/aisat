import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
#import ed_dse_shef_v2 as ed
import random
import math


#Title

st.title("DEMONSTRATION Cost-effectiveness of Air filters")

#generate sample data

np.random.seed(42)

#data = {
#	"Month": ["January", "February", "March", "April", "May", "June"],
#	"Sales": np.random.randint(200, 500, 6),
#	"Cost": np.random.randint(100, 300, 6)
#}

#df = pd.DataFrame(data)

st.sidebar.subheader("Select variables")
#st.dataframe(df)

cost_ai = st.sidebar.number_input("Total cost of AI per year", 0, 1000, value = 500)

cost_hepa = st.sidebar.number_input(
    label = "Cost per hour of HEPA",
    min_value=0.01,
    max_value=1.00,
    step=1e-2,
    format="%.2f")

n= st.sidebar.slider(
    label= "Total number of patients per year",
    min_value=1000,
    max_value=100000,
    value=10000,  # Default value
)

#cost_ai =

#proportion of people with an infection

sick = st.sidebar.slider(
    label="Percentage of people with an infection",
    min_value=0,
    max_value=100,
    value=4,  # Default value
    format="%d%%",  # Displays as integer with a % symbol
)

sick = sick/100


#sick = 0.04


# number of patients in clinical area on average

pa = st.sidebar.number_input("Number of people in a clinical area at any time", 0, 100, value = 10)

# chance of passing the infection on 

infect = st.sidebar.slider(
    label="Probability of infection transmission",
    min_value=0,
    max_value=100,
    value=15,  # Default value
    format="%d%%",  # Displays as integer with a % symbol
)

infect = infect/100
#reduction in risk HEPA AI

reduce = st.sidebar.slider(
    label="Effectiveness of AI placement of HEPA filters in reducing infection transmission",
    min_value=0,
    max_value=100,
    value=20,  # Default value
    format="%d%%",  # Displays as integer with a % symbol
)


reduce = reduce/100


#chance of hospital admission if sick

admit = st.sidebar.slider(
    label="Proportion of sick people who are admitted to hospital",
    min_value=0,
    max_value=100,
    value=5,  # Default value
    format = "%d%%"
)

admit = admit/100

# cost of hospital admission if sick

cost = 500


# disutility of illness

dis = 0.05


# disutility of admission

dis_admi = 0.1

# probability of death

death = 0.01


#sample size from trial



data = {
    "id": [],
    "sick": [],
    "infected": [],
    "admit": [],
    "cost": [],
    "disutility": [],
    "disutility_admi": [],
    "death": []
    
        }





for i in range(0, n):
    
    # chance of already being sick
    x = sick > random.random()
    
    # chance of getting infected
    if x == False:
        y = 1-(1-infect)**(pa*sick) > random.random()
        
    else:
        y = True
        
    #chance of being admitted and disutility
    if y == True:
        d = dis
        z = admit >random.random()
        dead = death > random.random()
        
    else:
        d = 0
        z = False
        dead = False
    #cost and disutility from admission
    if z == True:
        c = cost
        d_a = dis_admi
        
    else:
        c = 0 
        d_a = 0
        
        
        

        
   
    
    data['id'].append(i)
    data['sick'].append(x)
    data['infected'].append(y)
    data['admit'].append(z)
    data["cost"].append(c)
    data["disutility"].append(d)
    data["disutility_admi"].append(d_a)
    data["death"].append(dead)
    
    

df = pd.DataFrame(data)
       
            

data_ai = {
    "id": [],
    "sick": [],
    "infected": [],
    "admit": [],
    "cost": [],
    "disutility": [],
    "disutility_admi": [],
    "death": []
    
        }





for i in range(0, n):
    
    # chance of already being sick
    x = sick > random.random()
    
    # chance of getting infected
    if x == False:
        y = 1-(1-infect*reduce)**(pa*sick) > random.random()
              
    else:
        y = True
        
    #chance of being admitted and disutility
    if y == True:
        d = dis
        z = admit >random.random()
        dead = death > random.random()
        
    else:
        d = 0
        z = False
        dead = False
    #cost and disutility from admission
    if z == True:
        c = cost
        d_a = dis_admi
        
    else:
        c = 0 
        d_a = 0
        
    
    data_ai['id'].append(i)
    data_ai['sick'].append(x)
    data_ai['infected'].append(y)
    data_ai['admit'].append(z)
    data_ai["cost"].append(c)
    data_ai["disutility"].append(d)
    data_ai["disutility_admi"].append(d_a)
    data_ai["death"].append(dead)
    
    

df_ai = pd.DataFrame(data_ai)
       

#cost per minute of HEPA filters

t_hepa = cost_hepa * 8 * 5 *52

t_cost_ai = cost_ai

tot_admi = df['cost'].sum()

tot_admi_ai = df_ai['cost'].sum()

st.write(f"Total number of patients per year = {n}")

st.write(f"Proportion of people admitted to hospital - no HEPA: {df.admit.sum()/n*100:.2f}%")

st.write(f"Proportion of people admitted to hospital - AI HEPA: {df_ai.admit.sum()/n*100:.2f}%")

st.write(f"Total cost of AI and HEPA: £{(t_cost_ai + t_hepa):.0f}")

st.write(f"Total cost of admissions control: £{df['cost'].sum()}")

st.write(f"Total cost of admissions AI HEPA: £{df_ai['cost'].sum()}")

st.write(f"Difference in cost of admissions: £{tot_admi_ai-tot_admi}")

st.write(f"Total cost of admissions + AI cost: £{df_ai['cost'].sum() + t_cost_ai}")

st.write(f"Total cost savings AI: £{df_ai['cost'].sum() + t_cost_ai + t_hepa - tot_admi}")












'''
#Bar Chart

st.subheader("Sales vs. Cost")
fig, ax= plt.subplots()
ax.bar(df["Month"], df["Sales"], label="Sales", color="skyblue")
ax.bar(df["Month"], df["Cost"], label="Cost", color="salmon", alpha=0.7)
ax.legend()

st.pyplot(fig)

#Filter option

st.subheader("Monthly Sales Analysis")
selected_month = st.selectbox("Select a month:", df['Month'])
selected_data = df[df["Month"] == selected_month]

st.write(f"**Sales in {selected_month}:** {selected_data['Sales'].values[0]}")
st.write(f"**Costs in {selected_month}:** {selected_data['Cost'].values[0]}")
'''