import pandas as pd
import matplotlib.pyplot as plt 

import streamlit as st

# Point to your Django project so Python can find it
#sys.path.append('/home/lilithluckdragon/conference')  # path to folder containing manage.py

# Tell Django which settings module to use
# Initialize Django (loads settings, sets up app registry)


# Now you can import and query your models like normal Django code


st.title("Questionnaire Responses to NIHR Economics mental health sub-group")


df = pd.read_csv('Question-2026-09-29.csv')

uni = df["institution"]

york = uni.str.contains("York", regex=False, na=False)

uoy = uni.str.contains("UoY", regex=False, na=False)

swansea = uni.str.contains("Swansea", regex=False, na=False)

manchester = uni.str.contains("Manchester", regex=False, na=False)

belfast = uni.str.contains("Belfast", regex=False, na=False)

oxford = uni.str.contains("Oxford", regex=False, na=False)

edin = uni.str.contains("Edinburgh", regex=False, na=False)

exeter = uni.str.contains("Exeter", regex=False, na=False)

lse = uni.str.contains("LSE", regex=False, na=False)

imperial = uni.str.contains("Imperial", regex=False, na=False)

bangor = uni.str.contains("Bangor", regex=False, na=False)

glasgow = uni.str.contains("Glasgow", regex=False, na=False)

liver = uni.str.contains("Liverpool", regex=False, na=False)

lancs = uni.str.contains("Lancashire", regex=False, na=False)

ucl = uni.str.contains("UCL", regex=False, na=False)

ucl_long = uni.str.contains("University College", regex=False, na=False)

sheffield = uni.str.contains("Sheffield", regex=False, na=False)

kcl = uni.str.contains("King", regex=False, na=False)

greenwich = uni.str.contains("Greenwich", regex=False, na=False)

newcastle = uni.str.contains("Newcastle", regex=False, na=False)

st.subheader("Institutions")

st.write(f"Responses from 18 different universities") 

york = york.sum() + uoy.sum()

swansea = swansea.sum()

manchester = manchester.sum()

belfast = belfast.sum()

oxford = oxford.sum()

edin = edin.sum()

exeter = exeter.sum()

lse = lse.sum()

imperial = imperial.sum()

bangor = bangor.sum()

glasgow = glasgow.sum()

liver = liver.sum()

lancs = lancs.sum()

ucl = ucl.sum() + ucl_long.sum()

sheffield = sheffield.sum()

kcl = kcl.sum()

greenwich = greenwich.sum()

newcastle = newcastle.sum()


uni_n = [york, swansea, manchester, belfast, oxford, edin, exeter, lse, imperial, bangor, glasgow, liver, lancs,
		ucl, sheffield, kcl, greenwich, newcastle]


uni_l = ["York", "Swansea", "Manchester", "Queen's, Belfast", "Oxford", "Edininburgh", "Exeter", "LSE", "Imperial", 
		"Bangor", "Glasgow", "Liverpool", "Lancashire", "UCL", "Sheffield", "KCL", "Greenwich", "Newcastle"]

fig, ax = plt.subplots()

ax.pie(uni_n, labels = uni_l)



st.pyplot(fig)



st.subheader("Career Stage")

total_ecr = (df['career_stage'] == 'ECR').sum()

total_mcr = (df['career_stage'] == 'MCR').sum()

total_sar = (df['career_stage'] == 'SAR').sum()

total = [total_ecr, total_mcr, total_sar]

labels = "ECR", "MCR", "SAR"


fig, ax = plt.subplots()

pie = ax.pie(total, labels=labels)
ax.pie_label(pie, '{absval:d}\n{frac:.1%}')


st.pyplot(fig)


#funders

st.subheader("Funding source")

tot_nihr = (df['funder'] == 'NIHR').sum()

tot_ukri = (df['funder'] == 'UKRI').sum()

tot_oth = (df['funder'] == 'Other').sum()

tot_na = (df['funder'] == 'N_A').sum()


tot_fund = [tot_nihr, tot_ukri, tot_oth, tot_na]

tot_lab = "NIHR", "UKRI", "Other", "N/A"

fig, ax = plt.subplots()

pie = ax.pie(tot_fund, labels=tot_lab)
ax.pie_label(pie, '{absval:d}\n{frac:.1%}')


st.pyplot(fig)

st.subheader("Representation from the global south")


st.write(f"{((df['lmic'] == 'LMIC').sum() + (df['lmic'] == 'COMB').sum())/len(df.index)*100:.0f} % of reseachers that responded to the questionnaire are from the global south ")


st.subheader("Challenges")



ch = df["challenges"].str.lower()


ch_data = ch.str.contains("data", regex=False, na=False)

ch_res = ch.str.contains("resource", regex=False, na=False)


st.write(f"{(ch_data.sum()+ ch_res.sum())/len(df.index)*100:.0f}% of reseachers identified data as a challenge in mental health research. This included access to the right data at the right time to inform policy choices as well the burden on patients for self-reported data and data quality.")



ch_meas = ch.str.contains("measure", regex=False, na=False)

ch_meas2 = ch.str.contains("qaly", regex=False, na=False)

ch_meas3 = ch.str.contains("questionnaire", regex=False, na=False)

ch_meas4 = ch.str.contains("PROM", regex=False, na=False)

st.write(f"{(ch_meas.sum() + ch_meas2.sum() + ch_meas3.sum() + ch_meas4.sum())/len(df.index)*100:.0f}% of reseachers identified suitability of adequate questionnaires to measure quality of life and impact on care givers.")


ch_costs = ch.str.contains("costs", regex=False, na=False)

st.write(f"{ch_costs.sum()/len(df.index)*100:.0f}% of reseachers had challenges in identifing suitable sources for unit costs")


ch_fund = ch.str.contains("funding", regex=False, na=False)


st.write(f"{ch_fund.sum()/len(df.index)*100:.0f}% of reseachers identified funding as a challenge in mental health research.")



ch_policy = ch.str.contains("policy", regex=False, na=False)

st.write(f"{ch_policy.sum()/len(df.index)*100:.0f}% of reseachers raised issues with how we inform policy, particularly if we aren't measuring the right things")



st.subheader("Value of NIHR Economics Mental Health Sub-group")

grp = df["interest"].str.lower()


grp_meet = grp.str.contains("meet", regex=False, na=False)

grp_dis = grp.str.contains("discuss", regex=False, na=False)

grp_meth = grp.str.contains("method", regex=False, na=False)

grp_kn = grp.str.contains("knowledge", regex=False, na=False)

grp_dev = grp.str.contains("develop", regex=False, na=False)

grp_sup = grp.str.contains("support", regex=False, na=False)

grp_net = grp.str.contains("network", regex=False, na=False)

ass = df["assist"].str.lower()


ass_net = ass.str.contains("network", regex=False, na=False)





st.write(f"Researchers identified that they would like a group where they could meet ({grp_meet.sum()/len(df.index)*100:.0f}%), discuss methodology ({(grp_dis.sum() + grp_meth.sum())/len(df.index)*100:.0f}%) and share knowledge ({grp_kn.sum()/len(df.index)*100:.0f}%)")

st.write (f"Development ({grp_dev.sum()/len(df.index)*100:.0f}%) and support ({grp_meet.sum()/len(df.index)*100:.0f}%) were also idenfitied as important")

st.write (f"({(grp_net.sum() + ass_net.sum())/len(df.index)*100:.0f}% of researchers were interested in networking opportunities")


st.subheader("Issues with data access")

st.dataframe(df["access"])

use = df["use"].str.lower()

use_mis = use.str.contains("miss", regex=False, na=False)

use_qal = use.str.contains("quality", regex=False, na=False)

st.write(f"Missing data ({use_mis.sum()/len(df.index)*100:.0f}%) and data quality ({use_qal.sum()/len(df.index)*100:.0f}%)were both identified as key issues in improving data analysis in mental health economics")

