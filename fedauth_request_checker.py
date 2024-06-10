import pandas as pd
from pathlib import Path

new_request_path=Path(r"C:\Users\RUTENB\OneDrive - University of Pittsburgh\fed_auth_docs\requests_docs\fedauth_raw_requests.csv")
master_list_path=Path(r"C:\Users\RUTENB\OneDrive - University of Pittsburgh\fed_auth_docs\requests_docs\fedauth_requests_list.csv")

new_request_df=pd.read_csv(new_request_path,index_col="Approval ID",skiprows=13)

my_requests=new_request_df.groupby("Approval Stage").get_group("Pending Analytics and Data Integration Approval")

master_list_df=pd.read_csv(master_list_path,index_col="Approval ID")
updated_master_list_df=my_requests.join(master_list_df[["Status","Notes"]],how="left")

if "AR-02566" in updated_master_list_df.index:
    updated_master_list_df=updated_master_list_df.drop(index="AR-02566")

print(updated_master_list_df)
updated_master_list_df.to_csv(master_list_path)