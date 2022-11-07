import streamlit as st
#Must do this first in Streamlit
st.set_page_config(page_title='Global Sales Data',
page_icon='Romolo.png',layout='wide',
initial_sidebar_state='expanded') #initial_sidebar_state='collapsed 'expanded or auto
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime



# df = pd.read_csv('5000 Sales Records.csv')
# Central=df[(df['Region']=='Central America and the Caribbean') & (df['Sales Channel']=='Online')]
# cent_fruits=Central[Central['Item Type']=='Fruits']


sales_df = pd.read_csv("5000 Sales Records.csv",parse_dates =['Ship Date', 'Order Date']).iloc[1:,:]
# europe_sales_df = sales_df[sales_df['Region']=='Europe'].set_index(["Region","Country"])
sales_df['Order Priority'] =sales_df['Order Priority'].map({"L":"Low", "M":"Medium", "H":"High", "C":"Critical"})
europe_sales_df = sales_df[sales_df['Region']=='Europe']

asia_sales_df = sales_df[sales_df['Region']=='Asia']
Africa_sales_df = sales_df[sales_df['Region']=='Sub-Saharan Africa']
Middle_East_sales_df = sales_df[sales_df['Region']=='Middle East and North Africa']
Central_America_sales_df = sales_df[sales_df['Region']=='Central America and the Caribbean']
Aussie_sales_df = sales_df[sales_df['Region']=='Australia and Oceania']
NorthAmerica_sales_df = sales_df[sales_df['Region']=='North America']
stat_list = ['mean','median','std','sum','cov','corr','var']
def main():
# """put all your streamlit code here first """
    st.title('Global Sales Data')
    menu = ['Home','North America','Central America','Europe','Asia','Africa','Middle East','Australia']
    sales_df['Net Profit Margin'] = (sales_df['Total Profit']/sales_df['Total Revenue'])*100
    # sales_df['Order Date'] = pd.to_datetime(sales_df['Order Date'],format='%Y-%m-%d')
    # sales_df['Ship Date'] = pd.to_datetime(sales_df['Ship Date'],format='%Y-%m-%d')
    sales_df['Duration'] = (sales_df['Ship Date'] - sales_df['Order Date'])/  np.timedelta64(1, 'D')
    choice=st.sidebar.selectbox("Region Menu",menu)

    if choice == 'Home':
        st.subheader('Home')
        # st.table(sales_df.head())
        st.write('')
        Sales_prof_marg = sales_df.loc[:,['Country','Ship Date','Units Sold','Total Revenue','Total Profit','Net Profit Margin']]

        left_column, right_column,far_right = st.columns(3)
        # You can use a column just like st.sidebar:
        # left_column.button('Press me!')
        # begin = left_column.date_input("Begin")
        # end = left_column.date_input('End')
        begin = st.date_input("Begin")
        end = st.date_input('End')
        st.dataframe(Sales_prof_marg.loc[(Sales_prof_marg['Ship Date'] >= str(begin))&(Sales_prof_marg['Ship Date'] <= str(end))])
        # left_column.dataframe(Sales_prof_marg.loc[(Sales_prof_marg['Ship Date'] >= str(begin))&(Sales_prof_marg['Ship Date'] <= str(end))])
        # left_column.dataframe(Sales_prof_marg.loc[Sales_prof_marg['Ship Date'] =="2017-3"])
        # sales_column_list = ['Units Sold','Total Revenue','Total Profit','Net Profit Margin']
        # sales_choice = st.multiselect('Select a Column',sales_column_list)
        # new_df = Sales_prof_marg.groupby([sales_choice]).median()
        # st.dataframe(new_df)
        # # st.bar_chart(new_df)
        st.subheader('Units Grouped By Item and Order Priority')
        item_df = sales_df.groupby(['Item Type','Order Priority']).sum()
        item_list = ['Baby Food', 'Beverages', 'Cereal', 'Clothes', 'Cosmetics', 'Fruits', 'Household', 'Meat', 'Office Supplies', 'Personal Care', 'Snacks', 'Vegetables']
        item_column_list = ['Total Profit','Units Sold','Total Revenue','Net Profit Margin','Total Cost']
        # item_selected=st.sidebar.selectbox("Items",item_list)
        # item_column_selected = st.sidebar.selectbox("Column",item_column_list)
        item_selected=st.selectbox("Items",item_list)
        item_column_selected = st.selectbox("Column",item_column_list)
        st.dataframe(item_df.loc[item_selected][item_column_selected])
        st.bar_chart(item_df.loc[item_selected][item_column_selected])
        st.header('using cross section')
        order_priority_list = ['Critical','High','Low','Medium']
        # PriorityL = st.sidebar.radio('Priority Level',order_priority_list)
        PriorityL = st.radio('Priority Level',order_priority_list)
        st.dataframe(item_df.xs(key=PriorityL,level='Order Priority'))
        # st.write(item_df.columns)
        # st.subheader('Units Grouped By Item and Order Priority transpose')
        # st.dataframe(sales_df.groupby(['Item Type','Order Priority']).describe().transpose())
        # st.write(new_df.shape)
        # st.dataframe(new_df.value_counts())

        # Or even better, call Streamlit functions inside a "with" block:
        # with right_column:
        #     chosen = st.radio(
        #         'Sorting hat',
        #         ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
        #     st.write(f"You are in {chosen} house!")
        # far_right.button('No Wait Press Me')









        # col1, col2, col3 = st.columns(3)
        #
        # with col1:
        #     st.header("A cat")
        #     st.image("https://static.streamlit.io/examples/cat.jpg")
        #
        # with col2:
        #     st.header("A dog")
        #     st.image("https://static.streamlit.io/examples/dog.jpg")
        #
        # with col3:
        #     st.header("An owl")
        #     st.image("https://static.streamlit.io/examples/owl.jpg")

        # Sales_prof = px.pie(Sales_prof_marg,names='Country', values='Total Revenue')
        # st.plotly_chart(Sales_prof,use_container_width=True)
        # st.bar_chart(Sales_prof_marg['Total Revenue'])

    if choice == 'North America':
        st.subheader('North America')
        st.write('')
        st.write('')
        NorthAmerica_sales_df['Net Profit Margin'] = (NorthAmerica_sales_df['Total Profit']/NorthAmerica_sales_df['Total Revenue'])*100
        st.dataframe(NorthAmerica_sales_df)
        st.write(NorthAmerica_sales_df.shape)
        # avg_NorthAmerica_sales = NorthAmerica_sales_df.groupby("Country")["Units Sold","Total Profit"].sum()
        NorthAmerica_sales2 = NorthAmerica_sales_df[["Country","Units Sold","Net Profit Margin"]]
        NorthAmerica_sales3 = NorthAmerica_sales_df[["Item Type","Units Sold","Net Profit Margin"]]
        NorthAmerica_sales_channelgroup = NorthAmerica_sales_df.groupby(["Sales Channel"])["Units Sold","Total Profit"].sum()
        NorthAmerica_sales2group = NorthAmerica_sales_df.groupby(["Country"])["Units Sold","Total Profit"].sum()
        NorthAmerica_sales3group = NorthAmerica_sales_df.groupby(["Item Type"])["Units Sold","Total Profit"].sum()
        with st.expander('Country Units Sold Total Profit'):
            st.dataframe(NorthAmerica_sales2group)
            st.bar_chart(NorthAmerica_sales2group)

        with st.expander('Item Type Units Sold Net Profit Margin'):
            st.dataframe(NorthAmerica_sales3group)
            st.bar_chart(NorthAmerica_sales3group)

        with st.expander('Sales Channel'):
            st.dataframe(NorthAmerica_sales_channelgroup)
            st.bar_chart(NorthAmerica_sales_channelgroup)
        # st.bar_chart(avg_NorthAmerica_sales)
        # NorthAmerica_item_sales = NorthAmerica_sales_df.groupby("Item Type")["Total Profit"].mean()
        # st.dataframe(NorthAmerica_item_sales)
        # st.bar_chart(NorthAmerica_item_sales)
        na = px.pie(NorthAmerica_sales_df,names='Country', values='Total Profit')
        # st.plotly_chart(na,use_container_width=True)
        na_channel = px.pie(NorthAmerica_sales_df,names='Sales Channel', values='Total Profit')
        # st.plotly_chart(na_channel,use_container_width=True)

        col1, col2 = st.columns(2)

        with col1:
            st.header("Sales Channel Profit")
            # st.image("https://static.streamlit.io/examples/cat.jpg")
            st.plotly_chart(na_channel,use_container_width=True)

        with col2:
            st.header("Profit By Country")
            # st.image("https://static.streamlit.io/examples/dog.jpg")
            st.plotly_chart(na,use_container_width=True)

        # with col3:
        #     st.header("An owl")
        #     st.image("https://static.streamlit.io/examples/owl.jpg")
        na_fig = px.scatter(NorthAmerica_sales_df, x="Units Sold", y="Total Profit",
	         size="Net Profit Margin", color="Country",
                 hover_name="Country", log_x=True, size_max=60)
        st.plotly_chart(na_fig)


        na_fig2 = px.sunburst(NorthAmerica_sales_df, path=['Sales Channel', 'Country', 'Item Type'], values='Total Profit', color='Country')
        st.plotly_chart(na_fig2)



    if choice == 'Central America':
        st.subheader('Central America')
        st.write('')
        st.write('')
        Central_America_sales_df['Net Profit Margin'] = (Central_America_sales_df['Total Profit']/Central_America_sales_df['Total Revenue'])*100
        st.dataframe(Central_America_sales_df)
        st.subheader('Item Count')
        st.dataframe(Central_America_sales_df['Item Type'].value_counts())
        st.subheader('Order Priority')
        st.dataframe(Central_America_sales_df['Order Priority'].value_counts())
        st.subheader('Item Type Count')
        st.bar_chart(Central_America_sales_df['Item Type'].value_counts())
        st.write(Central_America_sales_df.shape)
        avg_Central_America_sales = Central_America_sales_df.groupby("Country")["Total Profit"].mean()
        Central_America_item_sales = Central_America_sales_df.groupby("Item Type")["Total Profit"].mean()
        st.subheader('avg_Central_America_sales')

        st.bar_chart(avg_Central_America_sales)
        st.subheader('avg_Central_America_ item sales')
        st.bar_chart(Central_America_item_sales)
        st.subheader('Profit By Country')
        cent = px.pie(Central_America_sales_df,names='Country', values='Total Profit')
        st.plotly_chart(cent,use_container_width=True)
        st.subheader('Profit By Sales Channel')
        cent_channel = px.pie(Central_America_sales_df,names='Sales Channel', values='Total Profit')
        st.plotly_chart(cent_channel,use_container_width=True)
        st.subheader('Units Sold By Item')
        cent_items = px.pie(Central_America_sales_df,names='Item Type', values='Units Sold')
        st.plotly_chart(cent_items,use_container_width=True)


        cent_fig = px.scatter(Central_America_sales_df, x="Units Sold", y="Total Profit",
	         size="Net Profit Margin", color="Country",
                 hover_name="Country", log_x=True, size_max=60)
        st.plotly_chart(cent_fig)


        cent_fig2 = px.sunburst(Central_America_sales_df, path=['Sales Channel', 'Country', 'Item Type'], values='Total Profit', color='Country')
        st.plotly_chart(cent_fig2)




    if choice == 'Europe':
        st.subheader('Europe')
        st.write('')
        st.write('')
        europe_sales_df['Net Profit Margin'] = (europe_sales_df['Total Profit']/europe_sales_df['Total Revenue'])*100
        st.dataframe(europe_sales_df)
        st.write(europe_sales_df.shape)
        avg_europe_sales = europe_sales_df.groupby("Country")["Total Profit"].mean()
        st.bar_chart(avg_europe_sales)
        eu = px.pie(europe_sales_df,names='Country', values='Total Profit')
        st.plotly_chart(eu,use_container_width=True)
        eu_channel = px.pie(europe_sales_df,names='Sales Channel', values='Total Profit')
        st.plotly_chart(eu_channel,use_container_width=True)

        st.subheader('Totatl Item Profit By Type')
        eu_item = px.pie(europe_sales_df,names='Item Type', values='Total Profit')
        st.plotly_chart(eu_item,use_container_width=True)
        st.subheader('Units Sold By Item')
        eu_units = px.pie(europe_sales_df,names='Item Type', values='Units Sold')
        st.plotly_chart(eu_units,use_container_width=True)


        eu_fig = px.scatter(europe_sales_df, x="Units Sold", y="Total Profit",
	         size="Net Profit Margin", color="Country",
                 hover_name="Country", log_x=True, size_max=60)
        st.plotly_chart(eu_fig)


        eu_fig2 = px.sunburst(europe_sales_df, path=['Sales Channel', 'Country', 'Item Type'], values='Total Profit', color='Country')
        st.plotly_chart(eu_fig2)
        stat_line = st.selectbox('Stat Line',stat_list)
        st.dataframe(europe_sales_df.agg(stat_line))
        # --------------------------ADVANCED METHOD USED PASS IN A DICTIONARY-----------------------------------------
        # europe_sales_df.agg({'Total Profit':['max','mean'],'Units Sold':['mean','std']})

    if choice == 'Asia':
            st.subheader('Asia')
            st.write('')
            st.write('')
            asia_sales_df['Net Profit Margin'] = (asia_sales_df['Total Profit']/asia_sales_df['Total Revenue'])*100
            st.write(asia_sales_df.shape)
            st.dataframe(asia_sales_df)
            avg_asia_sales = asia_sales_df.groupby("Country")["Total Profit"].mean()
            st.bar_chart(avg_asia_sales)
            asia = px.pie(asia_sales_df,names='Country', values='Total Profit')
            st.plotly_chart(asia,use_container_width=True)
            asia_channel = px.pie(asia_sales_df,names='Sales Channel', values='Total Profit')
            st.plotly_chart(asia_channel,use_container_width=True)


            st.subheader('Totatl Item Profit By Type')
            asia_item = px.pie(asia_sales_df,names='Item Type', values='Total Profit')
            st.plotly_chart(asia_item,use_container_width=True)
            st.subheader('Units Sold By Item')
            asia_units = px.pie(asia_sales_df,names='Item Type', values='Units Sold')
            st.plotly_chart(asia_units,use_container_width=True)

            asia_fig = px.scatter(asia_sales_df, x="Units Sold", y="Total Profit",
	         size="Net Profit Margin", color="Country",
                 hover_name="Country", log_x=True, size_max=60)
            st.plotly_chart(asia_fig)


            asia_fig2 = px.sunburst(asia_sales_df, path=['Sales Channel', 'Country', 'Item Type'], values='Total Profit', color='Country')
            st.plotly_chart(asia_fig2)





    if choice == 'Africa':
            st.subheader('Africa')
            st.write('')
            st.write('')
            Africa_sales_df['Net Profit Margin'] = (Africa_sales_df['Total Profit']/Africa_sales_df['Total Revenue'])*100

            st.write(Africa_sales_df.shape)
            st.dataframe(Africa_sales_df)
            avg_Africa_sales = Africa_sales_df.groupby("Country")["Total Profit"].mean()
            st.bar_chart(avg_Africa_sales)
            afr = px.pie(Africa_sales_df,names='Country', values='Total Profit')
            st.plotly_chart(afr,use_container_width=True)
            afr_channel = px.pie(Africa_sales_df,names='Sales Channel', values='Total Profit')
            st.plotly_chart(afr_channel,use_container_width=True)

            st.subheader('Totatl Item Profit By Type')
            afr_item = px.pie(Africa_sales_df,names='Item Type', values='Total Profit')
            st.plotly_chart(afr_item,use_container_width=True)
            st.subheader('Units Sold By Item')
            afr_units = px.pie(Africa_sales_df,names='Item Type', values='Units Sold')
            st.plotly_chart(afr_units,use_container_width=True)

            afr_fig = px.scatter(Africa_sales_df, x="Units Sold", y="Total Profit",
	         size="Net Profit Margin", color="Country",
                 hover_name="Country", log_x=True, size_max=60)
            st.plotly_chart(afr_fig)


            afr_fig2 = px.sunburst(Africa_sales_df, path=['Sales Channel', 'Country', 'Item Type'], values='Total Profit', color='Country')
            st.plotly_chart(afr_fig2)

    if choice == 'Australia':
            st.subheader('Australia')
            st.write('')
            st.write('')
            Aussie_sales_df['Net Profit Margin'] = (Aussie_sales_df['Total Profit']/Aussie_sales_df['Total Revenue'])*100

            st.write(Aussie_sales_df.shape)
            st.dataframe(Aussie_sales_df)
            avg_Aussie_sales = Aussie_sales_df.groupby("Country")["Total Profit"].mean()
            st.bar_chart(avg_Aussie_sales)
            aus = px.pie(Aussie_sales_df,names='Country', values='Total Profit')
            st.plotly_chart(aus,use_container_width=True)
            aus_channel = px.pie(Aussie_sales_df,names='Sales Channel', values='Total Profit')
            st.plotly_chart(aus_channel,use_container_width=True)
            st.subheader('Totatl Item Profit By Type')
            aus_item = px.pie(Aussie_sales_df,names='Item Type', values='Total Profit')
            st.plotly_chart(aus_item,use_container_width=True)
            st.subheader('Units Sold By Item')
            aus_units = px.pie(Aussie_sales_df,names='Item Type', values='Units Sold')
            st.plotly_chart(aus_units,use_container_width=True)
            fig = px.area(Aussie_sales_df, x="Total Profit", y="Units Sold", color="Item Type", line_group="Country")
            st.plotly_chart(fig,use_container_width=True)

            Aussie_fig = px.scatter(Aussie_sales_df, x="Units Sold", y="Total Profit",
	         size="Net Profit Margin", color="Country",
                 hover_name="Country", log_x=True, size_max=60)
            st.plotly_chart(Aussie_fig)


            Aussie_fig2 = px.sunburst(Aussie_sales_df, path=['Sales Channel', 'Country', 'Item Type'], values='Total Profit', color='Country')
            st.plotly_chart(Aussie_fig2)






    if choice == 'Middle East':
            st.subheader('Middle East')
            st.write('')
            st.write('')
            Middle_East_sales_df['Net Profit Margin'] = (Middle_East_sales_df['Total Profit']/Middle_East_sales_df['Total Revenue'])*100
            st.dataframe(Middle_East_sales_df)
            st.write(Middle_East_sales_df.shape)
            avg_Middle_East_sales = Middle_East_sales_df.groupby("Country")["Total Profit"].mean()
            st.subheader('Average Mean Sales')
            st.bar_chart(avg_Middle_East_sales)
            st.subheader('Total Profit By Country')
            me = px.pie(Middle_East_sales_df,names='Country', values='Total Profit')
            st.plotly_chart(me,use_container_width=True)
            st.subheader('Profit By Sales Channel')
            me_channel = px.pie(Middle_East_sales_df,names='Sales Channel', values='Total Profit')
            st.plotly_chart(me_channel,use_container_width=True)
            st.subheader('Totatl Item Profit By Type')
            me_item = px.pie(Middle_East_sales_df,names='Item Type', values='Total Profit')
            st.plotly_chart(me_item,use_container_width=True)
            st.subheader('Units Sold By Item')
            me_units = px.pie(Middle_East_sales_df,names='Item Type', values='Units Sold')
            st.plotly_chart(me_units,use_container_width=True)
            # st.bar_chart(Middle_East_sales_df['Item Type'])
            # me_profit_m = px.pie(Middle_East_sales_df,names='Country', values='Net Profit Margin')
            # st.plotly_chart(me_profit_m,use_container_width=True)
            fig = px.scatter(Middle_East_sales_df, x="Units Sold", y="Total Profit",
	         size="Net Profit Margin", color="Country",
                 hover_name="Country", log_x=True, size_max=60)
            st.plotly_chart(fig)


            fig2 = px.sunburst(Middle_East_sales_df, path=['Sales Channel', 'Country', 'Item Type'], values='Total Profit', color='Country')
            st.plotly_chart(fig2)





if __name__ == '__main__':
    main()
