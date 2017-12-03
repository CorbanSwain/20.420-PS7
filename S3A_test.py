import numpy as np
import matplotlib.pyplot as plt

def test_results(required_list):
    if isinstance(required_list, list):
        if len(required_list)==6084:
            data_mat = convert_list_to_matrix(required_list)
            compare_results(data_mat)
            make_figure(data_mat)
        else:
            print('Incorrect number of entries')
    else:
        print('Please make your entry of type list')


def convert_list_to_matrix(required_list):
    data_mat = np.ones((26*3, 26*3)) * -10
    row_flag = 0
    row_ind = 0
    col_flag = 0
    col_ind = 0
    box_ind = 0

    for val in required_list:
        data_mat[row_ind, col_ind]=val
        col_ind = col_ind+1
        col_flag = col_flag+1
        if col_flag>=3:
            col_flag=0
            col_ind=col_ind-3
            row_ind = row_ind+1
            row_flag = row_flag+1
            if row_flag>=3:
                row_flag=0
                box_ind = box_ind+1
                if box_ind>=26:
                    box_ind=0
                    row_ind=0
                    col_ind = col_ind+3
                    
    return data_mat

def compare_results(data_mat):
    answers = np.loadtxt('answers.txt')
    if np.array_equal(answers, data_mat):
        print('All entries are correct')
    else:
        print('All entries are not correct')

def make_figure(data_mat):
    plt.imshow(data_mat)
    plt.show()
