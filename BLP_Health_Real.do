clear all

import delimited "C:\Users\bobme\Desktop\ECON 850\Research Data\Real_BLP.csv"
drop if share==1
drop if share==0
*replace share=0.99999 if share==1
*replace share=0.00001 if share==0
sort mkt time
by mkt time: egen mkt_time_xall=sum(issueractuarialvalue)
sort mkt time issuer
by mkt time issuer: egen mkt_time_issuer_xown=sum(issueractuarialvalue)
gen mkt_time_issuer_xother = mkt_time_xall-mkt_time_issuer_xown
egen mkt_index=group(mkt time)
blp share issueractuarialvalue plantypedum,endog(premium=w x mkt_time_issuer_xother) stochastic(issueractuarialvalue) markets(mkt_index) draws(10)
