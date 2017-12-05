import numpy as np
import matplotlib.pyplot as plt
import matplotlib as m

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
        data_mat[row_ind, col_ind] = val
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


def unwrap(data_mat):
    out_list = []
    if np.size(data_mat) != 6084 and np.size(data_mat, 1) != np.size(data_mat, 2):
        print("The passed array is of the wrong size!  Must be 78 X 78.")
    for i_ko_1 in range(26):
        row = 3 * i_ko_1
        for i_ko_2 in range(26):
            col = 3 * i_ko_2
            d_row, d_col = (0, 0)
            for i_source in range(9):
                if d_row == 3:
                    d_row = 0
                    d_col = d_col + 1
                val = data_mat[int(row + d_row), int(col + d_col)]
                out_list.append(val)
                d_row += 1
    return out_list


def trial_descriptor(index, remove_duplicates=False):
    sources = ["glu","fru","gnt","rib","pyr","xyl","2pg","ace","gly"]
    reactions = ["PTS","PGI","PFK","FBP","FBA","TPI","GAPD","GPM","ENO","PYK","PPS", "PDH","PFL","ZWF",
                 "GND","EDA","RPE","RPI","TKT","TAL","PPC","PPCK","CS","ACONT","ALCD2x","ACALD"]
    si = int(index % 9)
    src = sources[si]
    ri1 = int((index // 9) % 26)
    ri2 = int((index // (9 * 26)) % 26)
    if remove_duplicates and (ri1 > ri2):
        return ""
    rxn1 = reactions[ri1]
    rxn2 = reactions[ri2]
    return "** Double KO: {:6s}-{:6s} with SOURCE: {:4s} **".format(rxn1, rxn2, src)


def compare_results(data_mat, verbose=True, remove_duplicates=False):
    answers = np.loadtxt('answers.txt')
    if np.array_equal(answers, data_mat):
        print('All entries are correct')
    else:
        print('All entries are not correct ...')
        uw_ans = unwrap(answers)
        uw_sumbit = unwrap(data_mat)
        tol = 0.01
        count = 0
        for i in range(len(uw_ans)):
            if abs(uw_ans[i] - uw_sumbit[i]) > tol:
                count += 1
                description = trial_descriptor(i, remove_duplicates)
                print("#{:4.0f} --> ans:{:2.0f}, you:{:2.0f} for {}".format(count,
                    uw_ans[i], uw_sumbit[i], description))




def make_figure(data_mat):
    plt.imshow(data_mat)
    plt.show()

