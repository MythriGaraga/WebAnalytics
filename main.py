"""
start
"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import util
import datetime
from dateutil.relativedelta import relativedelta


#businesses, business_id_set = util.load_business_data('data/yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_business.json')

#reviews = util.load_reviews_data('data/yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_review.json', business_id_set)

file_name_lst = ['clean_reviews_csv.csv', 'clean_reviews_csv_200001.csv', 'clean_reviews_csv_400001.csv',
                 'clean_reviews_csv_600001.csv', 'clean_reviews_csv_800001.csv', 'clean_reviews_csv_1000001.csv']
# Start Date: 2004-10-12
# End Date: 2016-07-19
buckets = util.generate_buckets(datetime.date(2004, 10, 12), datetime.date(2016, 7, 19), relativedelta(years=1))
bucket_counter_lst = util.gen_counter_per_bucket_business('4bEjOyTaDG24SY5TxsaUNQ', buckets, file_name_lst)
bucket_counter_lst_diff = util.get_bucket_counter_lst_diff(bucket_counter_lst)

print(bucket_counter_lst_diff)
