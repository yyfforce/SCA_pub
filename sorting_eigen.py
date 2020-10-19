def sorting_eigen(matrix):
    matrix_size = len(matrix)

    #eigenv and eigenvector
    v,w = scipy.linalg.eig(matrix)
    idx = np.argsort(v)
    v_sort = v[idx]
    w_sort = w[:,idx]
    
    return v_sort,w_sort,idx