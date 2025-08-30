#the matrix's get pulled from a file because modularity is good
from vector_matrixies import *

#set the matrix the system processes Here!!!!!!!!
matrix_in_question = vector_matrix1

"""
imageine 2 bookshelves
one on the left 
one on the right
in terms of processing the one on the left is the major bookshelf (temp_matrix1)
you'll take book contents and compare them with the top of the right bookshelf and then go down
once you exists the books on the right bookshelf you put your contents back and move one down on the left bookshelf
    it's hard to visualize. it's ok. 
"""
temp_matrix1 = matrix_in_question

#these are the 2 output vars the system spits out at the end
matching_vectors = []
matching_vectors_k_values = []

print("program begin <3")


def add_equaled_vector(combo_number):
    global temp_matrix2
    # temp_matrix2 is used just so it works like a 2d matrix in the resultaiton variables
    temp_matrix2 = [matrix_a, matrix_b]
    matching_vectors.append(temp_matrix2)
    matching_vectors_k_values.append(combo_list[ combo_number ])


for matrix_a in matrix_in_question:
    print(f"matrix_a = {matrix_a}")

    """
    this is hard to explain 
    ------- -       xxxxxxxx
    -------  ---->  --------
    -------         --------
        exhuasted
    xxxxxx          xxxxxxxx
    ------          --------
    ------          --------
        there's no reason for us to do this
    xxxxxxx       - --------
    -------  <----  --------
    -------         --------
        we already compared them so it's a wasted run 
        so we do this
    xxxxxxx         xxxxxxxx
    -------         --------
    -------         --------
    """
    if len( temp_matrix1 ) == 1:
        print(f"\t\tmatrix is 1 element. nothing to compare")
        break
    else:
        print(f"\t\t{len( temp_matrix1 )} elements")

    """
    metaphorically - compareing the left & right bookshelf
                        compareing the matrixes
    """
    for matrix_b in temp_matrix1[1:]:
        print(f"\tmatrix_b = {matrix_b}")

        #the values extrated from the matrixes just to make my life easier
        #they are called the Vs
        v2x = matrix_b[0]
        v2y = matrix_b[1]
        v2z = matrix_b[2]

        v1x = matrix_a[0]
        v1y = matrix_a[1]
        v1z = matrix_a[2]

        #the combos were made so i could make the console log better.
        #they hold the fraction the Vs make
        x_combo = None
        y_combo = None
        z_combo = None

        #the purpose of the V matrix is for loop optimization
        Vs_matrix = \
            [
                [v2x, v1x],
                [v2y, v1y],
                [v2z, v1z]
            ]

        #for ease of acess inside the loop
        combo_list = [x_combo, y_combo, z_combo]

        #a Bad zero division is when you have a #/0. this corrupts the rest of the decadency of the comparison
        bad_zero_divizion_bool = False
        #a Good zero divizion is when you have a 0/0. this co-exists with the rest of the fractions of the comparison
        good_zero_divizion_bool = False

        #v_couple_counter is used to keep track of which combo it's editing
        v_couple_counter = 0

        for v_couple in Vs_matrix:
            print(f"\t\t\t\tv_couple[0] = {v_couple[0]}")
            print(f"\t\t\t\tv_couple[1] = {v_couple[1]}")

            if v_couple[0] == 0 and v_couple[1] == 0:
                print(f'\t\t\t\t\tgood 0 division!')
                print(f"\t\t\t\t\tcombo_list[v_couple_counter] = {combo_list[v_couple_counter]}")
                combo_list[ v_couple_counter ] = "!good 0 division!"
                good_zero_divizion_bool = True

            elif ((v_couple[0] == 0 and v_couple[1] != 0)
                  or
                  (v_couple[0] != 0 and v_couple[1] == 0)):
                print(f'\t\t\t\t\tbad 0 division!')
                print(f"\t\t\t\t\tcombo_list[v_couple_counter] = {combo_list[v_couple_counter]}")
                combo_list[v_couple_counter] = "!bad 0 division!"
                bad_zero_divizion_bool = True

            else:
                print(f"\t\t\t\t\tall non-zero numbers")
                combo_list[v_couple_counter] = abs( v_couple[0] / v_couple[1] )
            v_couple_counter += 1


        print(f"\t\t{v1x} == {v1y} == {v1z}")
        print(f"\t\t/ == / == /")
        print(f"\t\t{v2x} == {v2y} == {v2z}")
        print(f"\t\t{combo_list[0]} == {combo_list[1]} == {combo_list[2]}")

        if bad_zero_divizion_bool:
            print(f"\t\t\tnot this one. Division by 0")

        elif combo_list[0] == combo_list[1] == combo_list[2]:
            print(f"\t\t\tgot one!")
            print(f"\t\t\t\tAdding it to the matching vectors.")

            add_equaled_vector(0)

        elif good_zero_divizion_bool:
            if (combo_list[0] == "!good 0 division!") and combo_list[1] == combo_list[2]:
                add_equaled_vector(1)

            elif (combo_list[1] == "!good 0 division!") and combo_list[0] == combo_list[2]:
                add_equaled_vector(0)

            elif (combo_list[2] == "!good 0 division!") and combo_list[0] == combo_list[1]:
                add_equaled_vector(0)

        else:
            print(f"\t\t\tnot this one. Values not equal")

    temp_matrix1 = temp_matrix1[1:]

print("\ndone scanning master UwU")
print("the matching vectors are:")
for i in range( len( matching_vectors ) ):
    print(f"\t{matching_vectors[i]}")
    print(f"\t{matching_vectors_k_values[i]}")


