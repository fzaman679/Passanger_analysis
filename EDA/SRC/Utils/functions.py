import pandas as pd 
import numpy as np
import matplotlib.pylab as plt 
import seaborn as sns 

# cleaning dataframe
def load_clean_dataframe(df):
    df_updated = df.drop(['origin_state_abr', 'dest_state_abr'], axis=1)
    return df_updated


def load_clean_dom_flights(df):
    domestic_flights_df = df[(df['origin_country_name'] == 'United States') & (df['dest_country_name'] == 'United States')]
    domestic_flights_df = domestic_flights_df.drop(['origin_state_nm', 'origin_country_name','dest_state_nm', 'origin_country', 'dest_country_name', 'dest_country'], axis=1)
    domestic_flights_df['yearmonth'] = pd.to_datetime(domestic_flights_df['yearmonth']).dt.strftime('%Y-%m')

    domestic_flights_df['origin_state_name'] = domestic_flights_df['origin_city_name'].str.split(',',expand=True)[1]
    domestic_flights_df['dest_state_name'] = domestic_flights_df['dest_city_name'].str.split(',',expand=True)[1]

    domestic_flights_df = domestic_flights_df[['passengers', 'airline_id','carrier_name', 'origin', 'origin_city_name', 'origin_state_name', 'dest', 'dest_city_name', 'dest_state_name', 'year','month','yearmonth']]
    return domestic_flights_df


def get_flights_with_most_passagers(df):
    grouped_multiple = df.groupby(['origin_city_name', 'dest_city_name']).agg({'passengers': ['sum']})
    grouped_multiple = grouped_multiple.sort_values(by=('passengers', 'sum'), ascending=False).head(100)
    return grouped_multiple

def get_number_passan_per_year(df):
    n_of_passengers_per_year = df.groupby('year')['passengers'].sum().to_frame()
    n_of_passengers_per_year = n_of_passengers_per_year.reset_index()
    n_of_passengers_per_year
    return n_of_passengers_per_year

def load_clean_employment(df):
    df['DATE'] = pd.to_datetime(df['DATE']).dt.strftime('%Y')
    employment_df_year = df.rename(columns={'DATE' : 'YEAR', 'UNRATE': 'UNEMPLOYMENT_RATE'})
    employment_df_year['UNEMPLOYMENT_RATE'] = employment_df_year['UNEMPLOYMENT_RATE'].round(2)
    employment_df_year = employment_df_year[employment_df_year['YEAR'] < '2021']
    employment_df_year['YEAR'] = employment_df_year['YEAR'].astype(int)
    return employment_df_year


def load_clean_income(df):
    df['DATE'] = pd.to_datetime(df['DATE']).dt.strftime('%Y')
    income_df = df.rename(columns={ 'DATE': 'YEAR','MEHOINUSA646N':'Median_Income'})
    income_df['YEAR'] = income_df['YEAR'].astype(int)

    return income_df

def graph_number_of_passangers_vs_unemployment_rate(df1, df2):
    
    #the first few lines for creating x and y axis 

    #for the number of passengers per year
    y_passengers = df1['passengers']
    x_year = df1['year']

    # for the unemployment rate graph
    y_UNEMPLOYMENT_RATE = df2['UNEMPLOYMENT_RATE']
    x_employment_year = df2['YEAR']
    

    # first graph 
    graph_n_pass_and_unem_rate = plt.figure(figsize=(6,8), dpi=100)
    graph_n_pass_and_unem_rate = plt.subplot(2, 1, 1)
    graph_n_pass_and_unem_rate = plt.plot(x_year, y_passengers, 'o-', color='blue', markersize=8)
    graph_n_pass_and_unem_rate = plt.ylabel('Number of Passengers', size=12)
    graph_n_pass_and_unem_rate = plt.xticks(x_year)
    graph_n_pass_and_unem_rate = plt.gca().set_ylim(ymin=0)
    #plt.gca().set_title('Number of Passangers over three years')

    # Second graph 
    graph_n_pass_and_unem_rate = plt.subplot(2, 1, 2)
    graph_n_pass_and_unem_rate = plt.plot(x_employment_year, y_UNEMPLOYMENT_RATE, '*-' , color='#248f24', markersize=8)
    graph_n_pass_and_unem_rate = plt.ylabel('Unemployment Rate', size=12)
    graph_n_pass_and_unem_rate = plt.xticks(x_employment_year)
    graph_n_pass_and_unem_rate = plt.xlabel('Year', size=12)
    graph_n_pass_and_unem_rate = plt.gca().set_ylim(ymin=0)
    #plt.gca().set_title('Unemployment Rate over three years')

    # creating a title for both graphs 
    graph_n_pass_and_unem_rate =  plt.suptitle('Number of Passengers vs Unemployment rate', fontsize=14)
    return graph_n_pass_and_unem_rate



def get_domestic_flights_2020(df):
    domestic_flights_2020 = df[df['year'] == 2020]
    return domestic_flights_2020


def get_n_passanger_by_month_in_2020(df):
    n_of_passengers_2020_by_month = df.groupby('yearmonth')['passengers'].sum().to_frame()
    n_of_passengers_2020_by_month = n_of_passengers_2020_by_month.reset_index()
    n_of_passengers_2020_by_month
    return n_of_passengers_2020_by_month


def load_clean_2020_employment(df):
    employment_df_2020 = df[(df['LOCATION'] == 'USA') & (df['SUBJECT'] == 'TOT')]
    employment_df_2020= employment_df_2020.drop(['LOCATION', 'INDICATOR', 'SUBJECT', 'MEASURE', 'FREQUENCY', 'Flag Codes'], axis=1)
    employment_df_2020.rename(columns={'TIME':'DATE', 'Value':'UNEMPLOYMENT_RATE'}, inplace=True)
    return employment_df_2020


def graph_n_passang_and_unemp_rate_2020(df1, df2):

    # for the number of passangers graph
    y_passengers_2020 = df1['passengers']
    x_year_2020 = df1['yearmonth']

    # for the unemployment rate graph
    y_UNEMPLOYMENT_RATE_2020 = df2['UNEMPLOYMENT_RATE']
    x_employment_year_2020 = df2['DATE']

    # graph Number of Passengers 
    n_passang_and_unemp_rate_2020_graph = plt.figure(figsize=(9,8), dpi=100)
    n_passang_and_unemp_rate_2020_graph = plt.subplot(2, 1, 1)
    n_passang_and_unemp_rate_2020_graph = plt.plot(x_year_2020, y_passengers_2020, 'o-', color='blue', markersize=8)
    n_passang_and_unemp_rate_2020_graph = plt.ylabel('Number of Passengers', size=12)
    n_passang_and_unemp_rate_2020_graph = plt.xticks(x_year_2020)
    n_passang_and_unemp_rate_2020_graph = plt.gca().set_ylim(ymin=0)
    #plt.gca().set_title('Number of Passangers in 2020')

    # graph Unemployment Rate in 2020
    n_passang_and_unemp_rate_2020_graph = plt.subplot(2, 1, 2)
    n_passang_and_unemp_rate_2020_graph = plt.plot(x_employment_year_2020, y_UNEMPLOYMENT_RATE_2020, '*-' , color='#248f24', markersize=8)
    n_passang_and_unemp_rate_2020_graph = plt.ylabel('Unemployment Rate',  size=12)
    n_passang_and_unemp_rate_2020_graph = plt.xticks(x_employment_year_2020)
    n_passang_and_unemp_rate_2020_graph = plt.xlabel('Year',  size=14)
    n_passang_and_unemp_rate_2020_graph = plt.gca().set_ylim(ymin=0)
    
    #plt.gca().set_title('Unemployment Rate in 2020')


    # creating a title for both graphs 
    n_passang_and_unemp_rate_2020_graph = plt.suptitle('Number of Passengers vs Unemployment rate in 2020 ',fontsize=12)
    return n_passang_and_unemp_rate_2020_graph


################################################################ INTERNATIONAL FLIGHTS #######################################################################################
def load_clean_int_flights_dataframe(df):
    int_inbound_flights = df[(df['origin_country_name'] != 'United States') & (df['dest_country_name'] == 'United States')]
    int_inbound_flights = int_inbound_flights.drop(['origin_state_nm', 'origin_country' , 'dest_state_nm', 'dest_country'], axis=1)
    int_inbound_flights['origin_country_name'] = int_inbound_flights['origin_country_name'].replace(['United Kingdom', 'Dominican Republic'], ['UK','D.R.'])
    return int_inbound_flights

def get_n_passanger_int_fligts(df):
    int_inbound_flights_grouped = df.groupby('year')['passengers'].sum().to_frame()
    int_inbound_flights_grouped.reset_index()
    return int_inbound_flights_grouped 

def load_n_pass_int_flights_18_19(df):
    int_inbound_flights_18_19 = df[(df['year'] == 2018) | (df['year'] == 2019)]
    
    int_inbound_flights_18_19_grouped = int_inbound_flights_18_19.groupby('origin_country_name')['passengers'].sum().to_frame()
    int_inbound_flights_18_19_grouped = int_inbound_flights_18_19_grouped.reset_index()
    int_inbound_flights_18_19_grouped = int_inbound_flights_18_19_grouped.sort_values(by='passengers', ascending=True).tail(10)

    return int_inbound_flights_18_19_grouped


def load_clean_asylum_seekers_df(df):
    df['Country of origin'] = df['Country of origin'].replace(['Venezuela (Bolivarian Republic of)', 'Dem. Rep. of the Congo', 'Syrian Arab Rep.'],['Venezuela','Congo', 'Syria'])
    asylum_seekers = df[(df['Year'] == 2018) | (df['Year'] == 2019) & (df['Country of asylum'] == 'United States of America')]
    return asylum_seekers

def n_asylum_seekers(df):
    grouped_asylum_seekers = df.groupby('Country of origin')['applied'].sum().to_frame()
    grouped_asylum_seekers = grouped_asylum_seekers.reset_index()
    grouped_asylum_seekers__top10 = grouped_asylum_seekers.sort_values(by='applied', ascending=True).tail(10)

    return grouped_asylum_seekers__top10

def graph_load_n_pass_and_n_asylum_seekers(df1, df2):
    #Top 10 countries arriving from abroad 
    x_origin_country_name = df1['origin_country_name']
    y_passangers_int_flights = df1['passengers']

    #asylum seekers 
    x_country_of_origin = df2['Country of origin']
    y_number_of_applications = df2['applied']

    # number of passengers Arriving from countries 
    load_n_pass_and_n_asylum_seekers_graph = plt.figure(figsize=(24,6), dpi=80)
    load_n_pass_and_n_asylum_seekers_graph = plt.subplot(1, 2, 1) # row 1, col 2 index 1
    load_n_pass_and_n_asylum_seekers_graph = plt.barh(x_origin_country_name, y_passangers_int_flights)
    load_n_pass_and_n_asylum_seekers_graph = plt.xlabel('Number of Passangers', fontsize=16)
    #plt.xlabel('Outbound countries', fontsize=16)
    load_n_pass_and_n_asylum_seekers_graph = plt.xticks(fontsize=14)
    load_n_pass_and_n_asylum_seekers_graph = plt.yticks(fontsize=14)
    #plt.title('Total # of Passangers arriving from Top 10 countries in 2018' , fontsize=18)

    # median income for 3 years
    load_n_pass_and_n_asylum_seekers_graph = plt.subplot(1, 2, 2) # index 2
    load_n_pass_and_n_asylum_seekers_graph = plt.barh(x_country_of_origin, y_number_of_applications)
    load_n_pass_and_n_asylum_seekers_graph = plt.xlabel('Number of Applications', fontsize=16)
    #plt.xlabel('Outbound Country', fontsize=16)
    load_n_pass_and_n_asylum_seekers_graph = plt.xticks(fontsize=14)
    load_n_pass_and_n_asylum_seekers_graph = plt.yticks(fontsize=14)

    # creating a title for both graphs 
    load_n_pass_and_n_asylum_seekers_graph = plt.suptitle('Number of passangers From Foreign countries Vs Number of Asylum applications',fontsize=16)
    return load_n_pass_and_n_asylum_seekers_graph




def load_clean_non_immigrant_df(df):
    non_immigrant_visas_df_18_19 = df.replace(['X', 'D', '-'],0)
    cols_to_replace = ['Visa_Waiver', 'Other', 'Student_exchange_visitors', 'Temporary workers and families', 'Diplomats and other representatives', 'All other classes', 'Unknown']
    non_immigrant_visas_df_18_19[cols_to_replace] = non_immigrant_visas_df_18_19[cols_to_replace].replace({',':''}, regex=True)
    non_immigrant_visas_df_18_19[['Visa_Waiver', 'Other', 'Student_exchange_visitors', 'Temporary workers and families', 'Diplomats and other representatives', 'All other classes', 'Unknown']] =  non_immigrant_visas_df_18_19[['Visa_Waiver', 'Other', 'Student_exchange_visitors', 'Temporary workers and families', 'Diplomats and other representatives', 'All other classes', 'Unknown']].apply(pd.to_numeric)
    non_immigrant_visas_df_18_19['Total_Applications'] = non_immigrant_visas_df_18_19.sum(axis=1)
    non_immigrant_visas_df_18_19['Country'] = non_immigrant_visas_df_18_19['Country'].replace(['Netherlands12', 'Australia6', 'Korea, South', 'United Kingdom14', 'France10', "China, People's Republic7,8" ],['Netherlands', 'Australia', 'South Korea', 'UK', 'France', 'China' ])
    return non_immigrant_visas_df_18_19

def load_visa_weiver(df):
    visa_waiver_18_19 = df.iloc[:, 0:2]
    return visa_waiver_18_19

def load_top_10_visa_weiver_applications(df):
    grouped_visa_waiver_18_19 = df.groupby('Country')['Visa_Waiver'].sum().to_frame().reset_index()
    grouped_visa_waiver_18_19 = grouped_visa_waiver_18_19.sort_values(by='Visa_Waiver', ascending=True).tail(10)
    return grouped_visa_waiver_18_19

def load_top_10_non_immig_visa_applications(df):
    grouped_visa_total_applications = df.groupby('Country')['Total_Applications'].sum().to_frame().reset_index()
    grouped_visa_total_applications = grouped_visa_total_applications.sort_values(by='Total_Applications', ascending=True).tail(10)
    return grouped_visa_total_applications

def graph_n_passangers_and_visa_weiver_application(df1, df2):
    #Top 10 countries arriving from abroad 
    x_origin_country_name = df1['origin_country_name']
    y_passangers_int_flights = df1['passengers']

    #total visa applications 

    x_country_of_visa_weiver = df2['Country']
    y_number_of_visa_weiver = df2['Visa_Waiver']

    # number of passengers Arriving from countries 
    n_passangers_and_total_visa_waiver_graph = plt.figure(figsize=(24,6), dpi=80)
    n_passangers_and_total_visa_waiver_graph = plt.subplot(1, 2, 1) # row 1, col 2 index 1
    n_passangers_and_total_visa_waiver_graph = plt.barh(x_origin_country_name, y_passangers_int_flights)
    n_passangers_and_total_visa_waiver_graph = plt.xlabel('Number of Passangers', fontsize=16)
    #plt.xlabel('Outbound countries', fontsize=16)
    n_passangers_and_total_visa_waiver_graph = plt.xticks(fontsize=14)
    n_passangers_and_total_visa_waiver_graph = plt.yticks(fontsize=14)
    #plt.title('Total # of Passangers arriving from Top 10 countries in 2018' , fontsize=18)

    # Country of issuance visa 
    n_passangers_and_total_visa_waiver_graph = plt.subplot(1, 2, 2) # index 2
    n_passangers_and_total_visa_waiver_graph = plt.barh(x_country_of_visa_weiver, y_number_of_visa_weiver)
    n_passangers_and_total_visa_waiver_graph = plt.xlabel('Number of Visa Waiver applications', fontsize=16)
    #plt.xlabel('Outbound Country', fontsize=16)
    n_passangers_and_total_visa_waiver_graph = plt.xticks(fontsize=14)
    n_passangers_and_total_visa_waiver_graph = plt.yticks(fontsize=14)

    # creating a title for both graphs 
    n_passangers_and_total_visa_waiver_graph = plt.suptitle('Number of passangers From Foreign countries VS Visa Weiver applications',fontsize=16)
    return n_passangers_and_total_visa_waiver_graph

