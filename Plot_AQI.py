import pandas as pd
import matplotlib.pyplot as plt

##in this file we gettionh the daily avg  of pm2.5 for the dependent data 
def avg_data_2013():
    #Creating temp_i varibale With 0 Value
    temp_i=0
    #creating average varibale with empty list 
    average=[]
    #Iterating 24 data Values from the 2013 data set that store in rows
    for rows in pd.read_csv('Data/AQI/aqi2013.csv',chunksize=24):
        #creating Varibales with Empty Value and empty list
        add_var=0
        avg=0.0
        data=[]
        #Covertinng Rows values into dataframe
        df=pd.DataFrame(data=rows)
        #Accesing 
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var=add_var+temp
                    
        #adding Average to value of daily to avg            
        avg=add_var/24
        #temp is increasing
        temp_i=temp_i+1
        
        average.append(avg)
    return average

def avg_data_2014():
    #Creating temp_i varibale With 0 Value
    temp_i=0
    #creating average varibale with empty list 
    average=[]
    #Iterating 24 data Values from the 2013 data set that store in rows
    for rows in pd.read_csv('Data/AQI/aqi2014.csv',chunksize=24):
        #creating Varibales with Empty Value and empty list
        add_var=0
        avg=0.0
        data=[]
        #Covertinng Rows values into dataframe
        df=pd.DataFrame(data=rows)
        #Accesing 
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/24
        temp_i=temp_i+1
        
        average.append(avg)
    return average

def avg_data_2015():
    #Creating temp_i varibale With 0 Value
    temp_i=0
    #creating average varibale with empty list 
    average=[]
    #Iterating 24 data Values from the 2013 data set that store in rows
    for rows in pd.read_csv('Data/AQI/aqi2015.csv',chunksize=24):
        #creating Varibales with Empty Value and empty list
        add_var=0
        avg=0.0
        data=[]
        #Covertinng Rows values into dataframe
        df=pd.DataFrame(data=rows)
        #Accesing 
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/24
        temp_i=temp_i+1
        
        average.append(avg)
    return average

def avg_data_2016():
    #Creating temp_i varibale With 0 Value
    temp_i=0
    #creating average varibale with empty list 
    average=[]
    #Iterating 24 data Values from the 2013 data set that store in rows
    for rows in pd.read_csv('Data/AQI/aqi2016.csv',chunksize=24):
        #creating Varibales with Empty Value and empty list
        add_var=0
        avg=0.0
        data=[]
        #Covertinng Rows values into dataframe
        df=pd.DataFrame(data=rows)
        #Accesing 
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/24
        temp_i=temp_i+1
        
        average.append(avg)
    return average


if __name__=="__main__":
    lst2013=avg_data_2013()
    lst2014=avg_data_2014()
    lst2015=avg_data_2015()
    lst2016=avg_data_2016()
    #lst2017=avg_data_2017()
    #lst2018=avg_data_2018()
    plt.plot(range(0,365),lst2013,label="2013 data")
    plt.plot(range(0,364),lst2014,label="2014 data")
    plt.plot(range(0,365),lst2015,label="2015 data")
    plt.plot(range(0,365),lst2016,label="2016 data")
    plt.xlabel('Day')
    plt.ylabel('PM 2.5')
    plt.legend(loc='upper right')
    plt.show()