from data import *
from model import *

def main():
    datax = Data(None, None)
    datax.read_and_load(excel_file='waterManData.xlsx', coef_sheet_name='Weights', cur_state_sheet_name='GASKI')
    m = create_model(datax)
    print('Done')



if __name__ == '__main__':
    main()
    print('Done')