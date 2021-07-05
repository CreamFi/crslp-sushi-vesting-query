import argparse
from dateutil.relativedelta import relativedelta
from datetime import datetime
from services.query import get_block_number
from services.main import get_distribution


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--claim-date', help='yyyy-mm-dd')
    args = parser.parse_args()
    claim_date = datetime.strptime(args.claim_date, '%Y-%m-%d')
    vesting_end_date = claim_date + relativedelta(months=-6)
    sushi_vesting_cutoff_date = datetime(year=2021, month=3, day=29)
    vesting_end_date = sushi_vesting_cutoff_date if vesting_end_date > sushi_vesting_cutoff_date else vesting_end_date
    get_distribution(get_block_number(vesting_end_date))

