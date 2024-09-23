import streamlit as st 
import pandas as pd 
import plotly.express as px

file_path = r"C:\Users\yasmi\OneDrive\Desktop\msba325-assignment2\tourism.csv"
data = pd.read_csv(file_path)

st.title('Tourism Visuals By Yasmina') 

file_path = r"C:\Users\yasmi\OneDrive\Desktop\msba325-assignment2\tourism.csv"
data = pd.read_csv(file_path)


if st.checkbox('Show Raw Data'):
    st.subheader('Raw Data')
    st.write(data)

st.header('Select Visualizations to Display')
show_pie = st.checkbox('Pie Chart: Cafes Existence Across Regions', value=True)
show_scatter = st.checkbox('Scatter Plot: Guest Houses vs Hotels', value=True)

selected_ref_area = st.selectbox('Select Region', data['Ref-area'].unique())
filtered_data = data[data['Existence of cafes - exists'] == 1]

if show_pie:
    st.header('Cafes Existence Across Regions')
    fig_pie = px.pie(filtered_data, names='Ref-area', values='Existence of cafes - exists', title='Cafes Existence')
    st.plotly_chart(fig_pie)



if show_scatter:
    st.header('Preference Between Guest Houses and Hotels Based on Tourism Index')
    fig_scatter = px.scatter(filtered_data, 
                             x='Total number of guest houses', 
                             y='Total number of hotels', 
                             color='Tourism Index', 
                             size='Tourism Index',  
                             title='Guest Houses vs Hotels by Tourism Index')
    st.plotly_chart(fig_scatter)
    
    selected_tourism_index = st.slider(
    'Tourism Index Range', 
    min_value=int(data['Tourism Index'].min()), 
    max_value=int(data['Tourism Index'].max()), 
    value=(int(data['Tourism Index'].min()), int(data['Tourism Index'].max())), 
    step=1 )
    