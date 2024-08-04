# Import the necessary library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import seaborn as sns
import plotly.express as px
# load the data
df = pd.read_csv("cybersecurity_attacks.csv")
# Calculate the number of missing values for each feature
missing_values = df.isnull().sum()
#Check for NaN values in 'Alerts/Warnings' column and replace it with 'No Alert Triggered'
df['Alerts/Warnings'] = df['Alerts/Warnings'].apply(lambda x: 'No Alert Triggered' if pd.isna(x) else x)
#Check for NaN values in 'Malware Indicators' column and replace it with 'No Detection'
df['Malware Indicators'] = df['Malware Indicators'].apply(lambda x: 'No Detection' if pd.isna(x) else x)
#Check for NaN values in 'Proxy Information' column and replace it with 'No proxy'
df['Proxy Information'] = df['Proxy Information'].apply(lambda x: 'No proxy' if pd.isna(x) else x)
#Check for NaN values in 'Firewall Logs' column and replace it with 'No Data'
df['Firewall Logs'] = df['Firewall Logs'].apply(lambda x: 'No Data' if pd.isna(x) else x)
#Check for NaN values in 'IDS/IPS Alerts' column and replace it with 'No Data'
df['IDS/IPS Alerts'] = df['IDS/IPS Alerts'].apply(lambda x: 'No Data' if pd.isna(x) else x)
# Extract 'Device' and store it in 'Browser' column
df['Browser'] = df['Device Information'].str.split('/').str[0]
# Identify all the different device types found (from 'Browser' column)
df['Browser'].unique()
import re
# Identifing common operating systems and devices with regular expressions.
patterns = [
    r'Windows',
    r'Linux',
    r'Android',
    r'iPad',
    r'iPod',
    r'iPhone',
    r'Macintosh',
]

def extract_device_or_os(user_agent):
    for pattern in patterns:
        match = re.search(pattern, user_agent, re.I)  # re.I makes the search case-insensitive
        if match:
            return match.group()
    return 'Unknown' 

# Extract device or OS
df['Device/OS'] = df['Device Information'].apply(extract_device_or_os)
#Drop column
df = df.drop('Device Information', axis = 1)
# Plotting the top devices/OS 
plt.figure(figsize=(10, 6))
sns.barplot(x='Count of Attacks', y='Device/OS', hue='Device/OS', data=top_devices, palette='magma')
plt.xlabel('Count of Attacks')
plt.ylabel('Device/OS')
plt.title('Attacks distribution based on device platform.')
plt.tight_layout()
#plt.show()
plt.savefig('Figuers/Attacks_on_device.png')
# Calculate attack counts
attack_counts = df['Attack Type'].value_counts().reset_index()
attack_counts.columns = ['Attack Type', 'Count']

# Display the count of the attacks and the attack type
attack_type = attack_counts.head()
plt.figure(figsize=(10, 8))
sns.countplot(data=df, x='Attack Type', hue='Malware Indicators', palette='Blues') 
# Get bar objects 
bars = plt.gca().containers[0] 
# Add numbers to each bar
for p in plt.gca().patches:
    plt.gca().annotate(f"{int(p.get_height())}",
                       (p.get_x() + p.get_width() / 2, p.get_height() / 2),
                       ha='center', va='center', color='black', fontsize=13)
# Loop through bars and add text annotations
for bar, count in zip(bars, df['Attack Type'].value_counts()): 
    yval = bar.get_height()  # Get bar height
    plt.text(bar.get_x() + bar.get_width() / 2, yval + 5, str(count),
             ha='center', va='bottom', fontsize=12, fontweight='bold')
plt.xlabel('Attack Type')
plt.ylabel('Count')
plt.title('Attack Type Distribution with Malware Indicators')
plt.xticks(rotation=45)  
plt.tight_layout()
#plt.show()
plt.savefig('Figuers/Attak_type_with_mal.png')
# Create the grouped bar chart using seaborn
plt.figure(figsize=(10, 8))
sns.countplot(data=df, x='Attack Type', hue='Alerts/Warnings', palette='Purples')
# Get bar objects 
bars = plt.gca().containers[0] 
# Loop through bars and add text annotations
for bar, count in zip(bars, df['Attack Type'].value_counts()): 
    yval = bar.get_height()  
    plt.text(bar.get_x() + bar.get_width() / 2, yval + 5, str(count), 
             ha='center', va='bottom', fontsize=12, fontweight='bold')
# Add numbers to each bar
for p in plt.gca().patches:
    plt.gca().annotate(f"{int(p.get_height())}",
                       (p.get_x() + p.get_width() / 2, p.get_height() / 2),
                       ha='center', va='center', color='black', fontsize=11)
plt.xlabel('Attack Type')
plt.ylabel('Count')
plt.title('Attack Type Distribution with Alerts/Warnings')
plt.xticks(rotation=45)
#plt.show()
plt.savefig('Figuers/Attack_with_alerts.png')
# Create the grouped bar chart using seaborn
plt.figure(figsize=(10, 8))
sns.countplot(data=df, x='Attack Type', hue='Attack Signature', palette='Reds')

# Get bar objects
bars = plt.gca().containers[0]  
# Loop through bars and add text annotations
for bar, count in zip(bars, df['Attack Type'].value_counts()): 
    yval = bar.get_height() 
    plt.text(bar.get_x() + bar.get_width() / 2, yval + 5, str(count),
             ha='center', va='bottom', fontsize=12, fontweight='bold')
# Add numbers to each bar
for p in plt.gca().patches:
    plt.gca().annotate(f"{int(p.get_height())}",
                       (p.get_x() + p.get_width() / 2, p.get_height() / 2),
                       ha='center', va='center', color='black', fontsize=11)
plt.xlabel('Attack Type')
plt.ylabel('Count')
plt.title('Attack Type Distribution with Attack Signature ')
plt.xticks(rotation=45)
#plt.show()
plt.savefig('Figuers/Attack_with_signature.png')
# Create the grouped bar chart using seaborn
plt.figure(figsize=(10, 8))
sns.countplot(data=df, x='Attack Type', hue='Action Taken', palette='PuBuGn_r')
# Get bar objects 
bars = plt.gca().containers[0] 
# Loop through bars and add text annotations
for bar, count in zip(bars, df['Attack Type'].value_counts()):  # Use value counts for text content
    yval = bar.get_height()  # Get bar height
    plt.text(bar.get_x() + bar.get_width() / 2, yval + 5, str(count),
             ha='center', va='bottom', fontsize=12, fontweight='bold')
# Add numbers to each bar
for p in plt.gca().patches:
    plt.gca().annotate(f"{int(p.get_height())}",
                       (p.get_x() + p.get_width() / 2, p.get_height() / 2),
                       ha='center', va='center', color='black', fontsize=11)
plt.xlabel('Attack Type')
plt.ylabel('Count')
plt.title('Attack Type Distribution with Action Taken')
plt.xticks(rotation=45)
#plt.show()
plt.savefig('Figuers/Attack_with_action_taken.png')
# Create the grouped bar chart using seaborn
plt.figure(figsize=(10, 8))
sns.countplot(data=df, x='Attack Type', hue='Severity Level', palette='RdYlGn_r')
# Get bar objects 
bars = plt.gca().containers[0] 
# Loop through bars and add text annotations
for bar, count in zip(bars, df['Attack Type'].value_counts()):  
    yval = bar.get_height()  # Get bar height
    plt.text(bar.get_x() + bar.get_width() / 2, yval + 5, str(count), 
             ha='center', va='bottom', fontsize=12, fontweight='bold')
# Add numbers to each bar
for p in plt.gca().patches:
    plt.gca().annotate(f"{int(p.get_height())}",
                       (p.get_x() + p.get_width() / 2, p.get_height() / 2),
                       ha='center', va='center', color='black', fontsize=11)
plt.xlabel('Attack Type')
plt.ylabel('Count')
plt.title('Attack Type Distribution with Severity Level')
plt.xticks(rotation=45)
#plt.show()
plt.savefig('Figuers/Attack_with_severity_level.png')
# Create the grouped bar chart using seaborn
plt.figure(figsize=(10, 8))
sns.countplot(data=df, x='Network Segment', hue='Log Source', palette='Accent')
# Get bar objects 
bars = plt.gca().containers[0]  
# Loop through bars and add text annotations
for bar, count in zip(bars, df['Network Segment'].value_counts()): 
    yval = bar.get_height() 
    plt.text(bar.get_x() + bar.get_width() / 2, yval + 5, str(count),
             ha='center', va='bottom', fontsize=12, fontweight='bold')
# Add numbers to each bar
for p in plt.gca().patches:
    plt.gca().annotate(f"{int(p.get_height())}",
                       (p.get_x() + p.get_width() / 2, p.get_height() / 2),
                       ha='center', va='center', color='black', fontsize=11)
plt.xlabel('Network Segment')
plt.ylabel('Count')
plt.title('Network Segment Distribution with Log Source')
plt.xticks(rotation=45)
#plt.show()
plt.savefig('Figuers/Net_seg_with_log_sor.png')
# Convert the 'Timestamp' column to datetime format
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
# Extract useful time-based features
df['Year'] = df['Timestamp'].dt.year
df['Month'] = df['Timestamp'].dt.month
df['Day'] = df['Timestamp'].dt.day
df['Hour'] = df['Timestamp'].dt.hour
df['DayOfWeek'] = df['Timestamp'].dt.day_name()
# Plot the number of attacks over time
plt.figure(figsize=(12, 6))
plt.plot(attacks_per_day, label='Number of Attacks')
plt.title('Number of Cyber Attacks Per Day')
plt.xlabel('Date')
plt.ylabel('Number of Attacks')
plt.legend()
#plt.show()
plt.savefig('Figuers/Num_of_attack_per_day.png')
# Analyzing attacks by hour of the day
attacks_per_hour = df['Hour'].value_counts().sort_index()
plt.figure(figsize=(12, 6))
sns.barplot(x=attacks_per_hour.index, y=attacks_per_hour.values)
plt.title('Number of Attacks by Hour of the Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Attacks')
#plt.show()
plt.savefig('Figuers/Num_of_attack_By_hour_of_day.png')
#Heatmap of Attacks by Day of the Week and Hour
pivot_table = df.pivot_table(index='DayOfWeek', columns='Hour', values='Attack Type', aggfunc='count')
plt.figure(figsize=(14, 6))
sns.heatmap(pivot_table, cmap='coolwarm', annot=False, fmt='d')
plt.title('Heatmap of Attacks by Day of the Week and Hour')
plt.xlabel('Hour of the Day')
plt.ylabel('Day of the Week')
plt.yticks(ticks=[0, 1, 2, 3, 4, 5, 6], labels=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], rotation=0)
#plt.show()
plt.savefig('Figuers/Heatmap_of_attack.png')
import calendar
# Pivot table to display year 2020...2023 vs months
# aggfunc is count to show attack count on certain month in each year
all_month_year_df = pd.pivot_table(df, values='Attack Type',
                                   index=["Month"],
                                   columns=["Year"],
                                   fill_value=0,                                   
                                   aggfunc="count"
                                   )
named_index = [[calendar.month_abbr[i] if isinstance(i, int) else i for i in list(all_month_year_df.index)]] # name months
all_month_year_df = all_month_year_df.set_index(named_index)
all_month_year_df = all_month_year_df.astype(float)
# display year vs months of 
ax = sns.heatmap(all_month_year_df, cmap='RdYlGn_r',
                 robust=True,
                 fmt='.1f',
                 annot=False,
                 linewidths=.5,
                 annot_kws={'size':11},
                 cbar_kws={'shrink':.8,
                           'label':'Attack Count'})                       
    
ax.set_yticklabels(ax.get_yticklabels(), rotation=0, fontsize=10)
ax.set_xticklabels(ax.get_xticklabels(), rotation=0, fontsize=10)
plt.title('Monthly Attack from 2020 to 2023 ', fontdict={'fontsize':18},    pad=14)
plt.savefig('Figuers/Monthly_attacks.png')