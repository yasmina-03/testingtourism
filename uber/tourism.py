import streamlit as st 
import pandas as pd 
import plotly.express as px


file_path = "https://linked.aub.edu.lb/pkgcube/data/551015b5649368dd2612f795c2a9c2d8_20240902_115953.csv"
data = pd.read_csv(file_path)

st.title('Tourism Visuals By Yasmina') 

if st.checkbox('Show Raw Data'):
    st.subheader('Raw Data')
    st.write(data)


st.header('Select Visualizations to Display')
show_scatter = st.checkbox('Scatter Plot: Guest Houses vs Hotels', value=True)
show_heatmap = st.checkbox('Heatmap: Initiatives and Attractions Co-occurrence', value=True)


if show_scatter:
    st.header('Preference Between Number of Guest Houses and Hotels Based on Tourism Index')
    
  
    selected_tourism_index = st.slider(
        'Tourism Index Range', 
        min_value=int(data['Tourism Index'].min()), 
        max_value=int(data['Tourism Index'].max()), 
        value=(int(data['Tourism Index'].min()), int(data['Tourism Index'].max())), 
        step=1
    )
    
    filtered_data = data[(data['Tourism Index'] >= selected_tourism_index[0]) & 
                         (data['Tourism Index'] <= selected_tourism_index[1])]
    
    fig = px.scatter(filtered_data, 
                     x='Total number of guest houses', 
                     y='Total number of hotels', 
                     color='Tourism Index', 
                     size='Tourism Index',  
                     title='Preference Between Guest Houses and Hotels in Ref-areas Based on Tourism Index')
    st.plotly_chart(fig)
    
    st.write("""
    **Imbalance in Accommodation:** Outliers with many hotels but few guest houses (or vice versa) indicate a potential focus on one type of accommodation with respect to specific tourism index. Also, it is recommended that regions with fewer accommodations, but a decent Tourism Index could benefit from increased investment in guest houses or hotels.
    """)

if show_heatmap:
    st.header('Heatmap of Initiatives and Attractions Co-occurrence')
    fig_heatmap = px.density_heatmap(
        data,
        x='Existence of initiatives and projects in the past five years to improve the tourism sector - exists',
        y='Existence of touristic attractions prone to be exploited and developed - exists',
        title='Heatmap of Initiatives and Attractions Co-occurrence',
        labels={
            'Existence of initiatives and projects in the past five years to improve the tourism sector - exists': 'Initiatives Exists',
            'Existence of touristic attractions prone to be exploited and developed - exists': 'Attractions Prone to Development'
        }
    )
    st.plotly_chart(fig_heatmap)

    st.write("""
    **Investment Focus:** Darker areas on the heatmap indicate regions where tourism initiatives and attractions needing development overlap. Thus, it is recommended to focus investment on regions with both initiatives and underdeveloped attractions to maximize tourism potential.
    """)

