import pandas as pd
df = pd.read_table('dataset\smsspamcollection\SMSSpamCollection', sep='\t', header=None,names=['Label','sms_messages'])

df.head()