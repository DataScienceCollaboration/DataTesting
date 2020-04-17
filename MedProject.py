import pandas as pd
payment_summary = pd.read_csv('Inpatient_Prospective_Payment_System__IPPS__Provider_Summary_for_the_Top_100_Diagnosis-Related_Groups__DRG__-_FY2011 copy.csv', dtype = str)
print(payment_summary.head())