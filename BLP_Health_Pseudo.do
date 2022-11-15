clear all
import delimited "C:\Users\bobme\Desktop\ECON 850\Research Data\sim_data.csv"
sort county_id time_id

by county_id time_id: egen county_time_xall=sum(av_d)
sort county_id time_id insurer_id
by county_id time_id insurer_id: egen county_time_insurer_xown=sum(av_d)
gen county_time_insurer_xother = county_time_xall-county_time_insurer_xown
egen county_index=group(county_id time_id)
blp share av_d hmo,endog(premium= w w county_time_insurer_xother) stochastic(premium av_d) markets(county_index) draws(100)
