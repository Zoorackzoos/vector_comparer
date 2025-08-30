test_vector_matrix_true = \
    [
        [1,1,1],
        [1,1,1]
    ]

vector_matrix1 = \
    [
        [4,-2,10],
        [-12,9,6],
        [5,15,5],
        [-20,10,50],
        [0,20,-5],
        [0,0,25]
    ]

matrix_in_question = vector_matrix1
temp_matrix1 = matrix_in_question

matching_vectors = []
matching_vectors_k_values = []

print("program begin <3")
for matrix_a in matrix_in_question:
    print(f"matrix_a = {matrix_a}")

    if len( temp_matrix1 ) == 1:
        print(f"\t\tmatrix is 1 element. nothing to compare")
        break
    else:
        print(f"\t\t{len( temp_matrix1 )} elements")

    for matrix_b in temp_matrix1[1:]:
        print(f"\tmatrix_b = {matrix_b}")
        v2x = matrix_b[0]
        v2y = matrix_b[1]
        v2z = matrix_b[2]

        v1x = matrix_a[0]
        v1y = matrix_a[1]
        v1z = matrix_a[2]

        all_Vs = [v2x, v2y, v2z, v1x, v1y, v1z]
        divizion_by_zero_killswitch = False
        for v in all_Vs:
            if v == 0:
                divizion_by_zero_killswitch = True

        print(f"\t\t{v1x} == {v1y} == {v1z}")
        print(f"\t\t/ == / == /")
        print(f"\t\t{v2x} == {v2y} == {v2z}")
        if divizion_by_zero_killswitch:
            print(f"\t\tcan't show divizion for this one")
        else:
            print(f"\t\t{abs(v1x / v2x)} == {abs(v1y / v2y)} == {abs(v1z / v2z)}")

        if divizion_by_zero_killswitch:
            print(f"\t\t\tnot this one. Division by 0")
        elif (abs(v1x / v2x)) == (abs(v1y / v2y)) == (abs(v1z / v2z)):
            print(f"\t\t\tgot one!")

            temp_matrix2 = [matrix_a, matrix_b]
            if temp_matrix2.reverse() in matching_vectors:
                print(f"\t\t\t\tThis is already in matching vectors. not adding it.")
            else:
                print(f"\t\t\t\tAdding it to the matching vectors.")
                matching_vectors.append( temp_matrix2 )
                matching_vectors_k_values.append( v1x / v2x )
        else:
            print(f"\t\t\tnot this one. Values not equal")

    temp_matrix1 = temp_matrix1[1:]

print("\ndone scanning master UwU")
print("the matching vectors are:")
for i in range( len( matching_vectors ) ):
    print(f"\t{matching_vectors[i]}")
    print(f"\t{matching_vectors_k_values[i]}")
