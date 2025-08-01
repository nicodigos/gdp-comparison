import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt




df_dict = dict()

df_dict['df_per_capita'] = pd.read_csv('notebooks/df_per_capita_result.csv')
df_dict['df_total'] = pd.read_csv('notebooks/df_total_result.csv')
df_dict['df_pc_ppp'] = pd.read_csv('notebooks/df_pc_ppp_result.csv')
df_dict['df_ppp'] = pd.read_csv('notebooks/df_ppp_result.csv')


def chart_creator(country_list, df, title):
    temp_df = df_dict[df][df_dict[df].REF_AREA_NAME.isin(country_list)]\
        .set_index('REF_AREA_NAME')
    plt.clf()
    
    for c in country_list:
        plt.plot(temp_df.columns.to_list()[:], 
                 temp_df.transpose()[c], label=c) 

    # Add title and labels
    
    plt.title(title)
    plt.xlabel('year')
    plt.ylabel('value')
    plt.xticks(rotation=85, fontsize=5)
   

    # Add legend
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    
    return plt

st.title("Global GDP Comparison")
st.markdown('''
This app lets you explore and compare countries based on four key GDP indicators. All values are adjusted to allow fair comparisons across time and between countries:

- **GDP (Constant 2015 Prices):** Total economic output of a country, adjusted for inflation using 2015 prices. This reflects real growth over time by removing the effect of price changes.
- **GDP Per Capita (Constant 2015 Prices):** Average economic output per person, adjusted for inflation. Useful for comparing income levels across populations.
- **GDP (Constant 2017 PPP):** Economic output adjusted for both inflation and Purchasing Power Parity (PPP), which accounts for cost-of-living differences across countries. This helps compare what people can actually buy.
- **GDP Per Capita (Constant 2017 PPP):** Average output per person, adjusted for both inflation and purchasing power. Often used to compare living standards internationally.
''')

country_list = st.multiselect('Countries', df_dict['df_total'].REF_AREA_NAME.unique())

tab_names = ["GDP Per Capita 2015", "GDP Total 2015", 
            "GDP Per Capita PPP 2017", "GDP Total PPP 2017",]

tab1, tab2, tab3, tab4 = st.tabs(tab_names)

with tab1:
    st.pyplot(chart_creator(country_list, 'df_per_capita', tab_names[0]))
with tab2:
    st.pyplot(chart_creator(country_list, 'df_total', tab_names[1]))
with tab3:
    st.pyplot(chart_creator(country_list, 'df_pc_ppp', tab_names[2]))
with tab4:
    st.pyplot(chart_creator(country_list, 'df_ppp', tab_names[3]))


