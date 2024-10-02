import pandas as pd
from pprint import pprint
def read_excel_to_dataframe(excel_file: str, sheet_name: str) -> pd.DataFrame:
    """
    Reads a matrix from an Excel file and stores it as a Pandas DataFrame.

    Parameters:
    excel_file (str): The path to the Excel file.
    sheet_name (str): The name of the sheet to read from.

    Returns:
    pd.DataFrame: The resulting DataFrame containing the data from the specified sheet.
    """
    try:
        # Read the Excel file
        df = pd.read_excel(excel_file, sheet_name=sheet_name, header=None)
        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def dataframe_to_dict(df: pd.DataFrame) -> dict:
    """
    Converts a DataFrame into a dictionary with keys as tuples of (row_index, col_index)
    and values as the corresponding cell values.

    Parameters:
    df (pd.DataFrame): The DataFrame to convert.

    Returns:
    dict: A dictionary with (row_index, col_index) as keys and cell values as values.
    """
    df_dict = {}
    for row_index in df.index:
        for col_index in df.columns:
            df_dict[(row_index, col_index)] = df.at[row_index, col_index]
    return df_dict


#"@dataclass(Frozen = False)
class Data:
    def __init__(self, coef_matrix : dict[(int,int) : float] = {}, current_state_matrix : dict[(int,int) : float] = {}, component_num = 0 , group_num = 0):
        #initialize an empty data
        self.coef_matrix = coef_matrix
        self.current_state_matrix = current_state_matrix
        self.component_num = component_num
        self.group_num = group_num



    def set_coef_matrix(self, coef_df):
        self.coef_matrix = coef_df

    def set_current_state_matrix(self, current_state_df):
        self.current_state_matrix = current_state_df

    def set_component_number(self, coef_df):
        self.component_num =  coef_df.shape[0]

    def set_group_number(self, coef_df):
        self.group_num = coef_df.shape[1]

    def read_and_load(self, excel_file, coef_sheet_name, cur_state_sheet_name):
        coef_df = read_excel_to_dataframe(excel_file=excel_file, sheet_name= coef_sheet_name)
        current_state_df = read_excel_to_dataframe(excel_file=excel_file, sheet_name=cur_state_sheet_name)

        self.set_coef_matrix(coef_df)
        self.set_current_state_matrix(current_state_df)
        self.set_component_number(coef_df)
        self.set_group_number(coef_df)


    def print_data_matrix(self, matrix_name = 'current_state'):
        if matrix_name == 'coef':
            pprint(self.coef_matrix)

        elif matrix_name == 'current_state':
            pprint(self.current_state_matrix)


    """done"""


    def return_data_matrix(self, matrix_name = 'current_state'):
        data_matrix = []
        if matrix_name == 'coef':
            for i in range(self.component_num):
                current_row = []
                for j in range(self.group_num):
                    current_row.append(self.current_state_matrix[(i, j)])

            data_matrix.append(current_row)

        elif matrix_name == 'current_state':
            for i in range(self.component_num):
                current_row = []
                for j in range(self.group_num):
                    current_row.append(self.current_state_matrix[(i,j)])

                data_matrix.append(current_row)

            return data_matrix

    def calculate_max_possible_improvement_matrix(self, basic:list, intermediate:list, advanced: list, basic_UB, intermediate_UB, advanced_UB):
        max_improvement_matrix = []
        for i in range(self.component_num):
            current_row = []
            for j in range(self.group_num):
                if i in basic:
                    if self.current_state_matrix[(i, j)] <= 2:
                        current_row.append(basic_UB - self.current_state_matrix[(i,j)])
                    else:
                        current_row.append(5 - self.current_state_matrix[(i,j)])
                elif i in intermediate:
                    if self.current_state_matrix[(i, j)] <= 2:
                        current_row.append(intermediate_UB - self.current_state_matrix[(i,j)])
                    else:
                        current_row.append(5 - self.current_state_matrix[(i, j)])
                elif i in advanced:
                    if self.current_state_matrix[(i, j)] <= 1:
                        current_row.append(advanced_UB - self.current_state_matrix[(i,j)])
                    else:
                        current_row.append(5 - self.current_state_matrix[(i,j)])
            max_improvement_matrix.append(current_row)
        return max_improvement_matrix


    def cost_matrix_printer(self):
        cost_matrix = []
        # cost_matrix.append([0,1,2,3,4,5])
        for i in range(6):
            current_row = []
            for j in range(6):
                if j < i:
                    # print(-1, end = ' ')
                    current_row.append(-1)
                else:
                    # print(j**2 - i**2, end = ' ')
                    current_row.append(j**2 - i**2)
            cost_matrix.append(current_row)
            # print()

        # new_column = [0,1,2,3,4,5]
        # for i in [1,2,3,4,5,6]:
        #     cost_matrix[i].insert(0, new_column[i - 1])
        # for row in cost_matrix:
        #     print(row)

        s = [[str(e) for e in row] for row in cost_matrix]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print('\n'.join(table))



