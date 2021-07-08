import argparse
from dateutil.relativedelta import relativedelta
from datetime import datetime
from services.query import get_block_number
from services.main import get_distribution


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', help='end block')
    args = parser.parse_args()
    vesting_end_block = int(args.e)
    vesting_cutoff_block = get_block_number(datetime(year=2021, month=3, day=29))
    vesting_end_block = vesting_cutoff_block if vesting_end_block > vesting_cutoff_block else vesting_end_block
    get_distribution(vesting_end_block)

