import pandas as pd
from pathlib import Path

#hard paths to raw source csv and output csv
new_request_path=Path(r"C:\Users\RUTENB\OneDrive - University of Pittsburgh\fed_auth_docs\requests_docs\fedauth_raw_requests.csv")
master_list_path=Path(r"C:\Users\RUTENB\OneDrive - University of Pittsburgh\fed_auth_docs\requests_docs\fedauth_requests_list.csv")

#read in raw source
new_request_df=pd.read_csv(new_request_path,index_col="Approval ID",skiprows=13)

#Filter to analytics only
my_requests=new_request_df.groupby("Approval Stage").get_group("Pending Analytics and Data Integration Approval")

#read in existing master sheet. Used to get status and notes columns
#joined to my_requests so only outstanding requests are in the df
master_list_df=pd.read_csv(master_list_path,index_col="Approval ID")
updated_master_list_df=my_requests.join(master_list_df[["Status","Notes"]],how="left")

#weird bug from peoplesoft: old request AR-02566 keeps showing up. If present remove.
if "AR-02566" in updated_master_list_df.index:
    updated_master_list_df=updated_master_list_df.drop(index="AR-02566")

#sort df by Status, record type, and created date
updated_sorted_master_list_df=updated_master_list_df.sort_values(by=['Status','Record Type','Created Date'])
#print to check, also shows up in the bat file output
print(updated_sorted_master_list_df)
#save to csv, overwites existing master sheet
updated_sorted_master_list_df.to_csv(master_list_path)