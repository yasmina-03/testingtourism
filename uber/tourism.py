import streamlit as st 
import pandas as pd 
import plotly.express as px

# Load the dataset
file_path = "https://linked.aub.edu.lb/pkgcube/data/551015b5649368dd2612f795c2a9c2d8_20240902_115953.csv"
data = pd.read_csv(file_path)

# Title of the Streamlit app
st.title('Tourism Visuals By Yasmina') 

# Show raw data if the checkbox is checked
if st.checkbox('Show Raw Data'):
    st.subheader('Raw Data')
    st.write(data)

# Section to select which visualizations to display
st.header('Select Visualizations to Display')
show_pie = st.checkbox('Pie Chart: Cafes Existence Across Regions', value=True)
show_scatter = st.checkbox('Scatter Plot: Guest Houses vs Hotels', value=True)

# Select region from dropdown
selected_ref_area = st.selectbox('Select Region', data['Ref-area'].unique())

# Filter the data based on the selected region and cafes existence
filtered_data = data[(data['Existence of cafes - exists'] == 1) & (data['Ref-area'] == selected_ref_area)]

# Pie chart for Cafes Existence
if show_pie:
    st.header('Cafes Existence Across Regions')
    fig_pie = px.pie(filtered_data, names='Ref-area', values='Existence of cafes - exists', title=f'Cafes Existence in {selected_ref_area}')
    st.plotly_chart(fig_pie)

# Scatter plot for Guest Houses vs Hotels
if show_scatter:
    st.header('Preference Between Guest Houses and Hotels Based on Tourism Index')

    # Slider for Tourism Index range selection
    selected_tourism_index = st.slider(
        'Tourism Index Range', 
        min_value=int(data['Tourism Index'].min()), 
        max_value=int(data['Tourism Index'].max()), 
        value=(int(data['Tourism Index'].min()), int(data['Tourism Index'].max())), 
        step=1
    )

    # Filter data based on the selected Tourism Index range
    scatter_data = filtered_data[(filtered_data['Tourism Index'] >= selected_tourism_index[0]) & 
                                 (filtered_data['Tourism Index'] <= selected_tourism_index[1])]

    fig_scatter = px.scatter(scatter_data, 
                             x='Total number of guest houses', 
                             y='Total number of hotels', 
                             color='Tourism Index', 
                             size='Tourism Index',  
                             title=f'Guest Houses vs Hotels in {selected_ref_area} by Tourism Index')
    st.plotly_chart(fig_scatter)

