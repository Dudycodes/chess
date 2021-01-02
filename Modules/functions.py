#je nějaký lepší způsob jak si posílat potřebné údaje? tohle je asi docela bastl se obává, ale doopravdy netuším, jak bych to udělal jinak - leda si místo několika neznýmých posílat nějaký tuple?

def mid_char(char_initial_x_coor, char_end_x_coor, char_initial_y_coor, char_end_y_coor, letters, char_set):
#kontrola - kámen mezi?

    x = int((char_initial_x_coor + char_end_x_coor)/2)
    y = int((char_initial_y_coor + char_end_y_coor)/2)


    x = letters[x]

    mid_char = x + str(y)
    mid_char = str(mid_char)
    square_mid = char_set.get(mid_char,"not_in_this_dict")

    return(square_mid, mid_char)

def input_line_data_check(char_initial_x_coor, char_end_x_coor, index, square_initial, square_end):

    if ((char_initial_x_coor or char_end_x_coor) < 0): # test správně zadaných souřadnic pokud se rovná '-1' písmeno není v letters, jinak jsou možné pouze kladné hodnoty
        print('chybně zadaná souřadnice v tahu', index ,'v pismenu')
        print()
        return True
    
    elif (square_initial == 'None') or (square_initial == None): #square_initial je prázdná = True
        print('Tah', index ,' nemohl být proveden - není kámen k posunutí')
        print()
        return True

    elif ((square_end != 'None') and (square_end != None)): #square_end není prázná = True
        print('v tahu', index,'posun na již zabrané pole')
        print()
        return True

def forward_move_check(square_initial, char_move_x, char_move_y):
    if ( ((square_initial[1] == 'w') and (char_move_y < 0)) or ((square_initial[1] == 'b') and (char_move_y > 0)) ): #neposunuje se vpřed
        if (square_initial[3] != 'king'):
            print('postup kamenem zpět - to ne toto...')
            return False
        else:
            return True
    else:
        return True

def move_len_check(char_move_x, char_move_y):
    if ((abs(char_move_x) == 1) and (abs(char_move_y) == 1)): 
        return True
    else:
        return False

def check_if_king(square_initial):
    if ((square_initial[3] != 'king') or (square_initial[3] == 'stone')): #nejsi dáma
        return True
    else:
        return False

def move_is_jump_check(char_move_x, char_move_y):
    if ((abs(char_move_x) == 2) and (abs(char_move_y) == 2)):
        return True
    else:
        return False 

def mid_square_occupied(char_initial_x_coor, char_end_x_coor, char_initial_y_coor, char_end_y_coor, letters, char_set):
    square_mid = (mid_char(char_initial_x_coor, char_end_x_coor, char_initial_y_coor, char_end_y_coor, letters, char_set))[0]

    if ( (square_mid != "not_in_this_dict") and (square_mid != None) and (square_mid != 'None')):
        return True
    else:
        return False 

def color_initial_mid_check(char_initial_x_coor, char_end_x_coor, char_initial_y_coor, char_end_y_coor, letters, char_set, square_initial):
    square_mid = (mid_char(char_initial_x_coor, char_end_x_coor, char_initial_y_coor, char_end_y_coor, letters, char_set))[0]

    if (square_mid[1] != square_initial[1]):
        return True
    else:
        print('Přeskok kamene stejné barvy není možný')
        return False 


            #def produktů:

def char_move(char_set, move_lst, canvas, char_move_x, char_move_y, size):
    square_initial = (char_set.get( move_lst[0] , "not_in_dict"))

    char_intitial_id = square_initial[2]
    canvas.move(char_intitial_id, (char_move_x * size), (char_move_y * size) )


    #oprava zápisu v charsetu
    square_end_key = move_lst[2]
    char_final_coor = {square_end_key: square_initial}  #nový dict_val s opravou pro koncovou coord v char_setu
    #char_set values:   {aktuální pole: (výchozí pole kamene, barva kamene, id kamene)}   None = prázdné pole
    square_initial_key = move_lst[0]
    char_init_coor_setNone = {square_initial_key: None}

    #print('char_init_coor_setNone:', char_init_coor_setNone)
    
    char_set.update(char_final_coor) #přepis koncové coord
    char_set.update(char_init_coor_setNone) #initial coord = None


def declare_king(move_lst, square_initial, char_set, canvas):
    square_end_key = move_lst[2]        

    if (((str(square_initial[1]) == 'w') and ((int(square_end_key[1]) == 8))) or ((str(square_initial[1]) == 'b') and (int(square_end_key[1]) == 1)) ):
        if (square_initial[3] != 'king'):
            square_to_declare = {move_lst[0]: (square_initial[0],square_initial[1],square_initial[2], 'king')} #šlo by to napsat efektněji? Tuple asi jinak nezměním se obávám...
            char_set.update(square_to_declare)


            canvas.itemconfig(square_initial[2],outline='red')
            
            print('dáma žije!')


        
    #napřed vždy deklarovat, pak až char_move!!!


def jump(char_initial_x_coor, char_end_x_coor, char_initial_y_coor, char_end_y_coor, letters, char_set, move_lst, square_initial, canvas, char_move_x, char_move_y, size):

    mid_char_fce_val = mid_char(char_initial_x_coor, char_end_x_coor, char_initial_y_coor, char_end_y_coor, letters, char_set)

    square_mid = mid_char_fce_val[0]
    mid_char_val = mid_char_fce_val[1]

    declare_king(move_lst, square_initial, char_set, canvas)

    #animace exterminatu
    char_mid_id = square_mid[2] 
    char_move(char_set, move_lst, canvas, char_move_x, char_move_y, size)
    canvas.after(200)
    canvas.delete(char_mid_id)

    #anulace dat
    char_mid_coor_setNone = {str(mid_char_val): None}
    print('char_mid_coor_setNone', char_mid_coor_setNone)
    char_set.update(char_mid_coor_setNone)

def king_jump(cell_to_exterminate, char_set, move_lst, canvas, char_move_x, char_move_y, size):

    #animace exterminatu a posunu
    char_ext_id = char_set.get(cell_to_exterminate)[2] 
    char_move(char_set, move_lst, canvas, char_move_x, char_move_y, size)
    canvas.after(200)
    canvas.delete(char_ext_id)
        
    char_ext_coor_setNone = {str(char_ext_id): None}
    char_set.update(char_ext_coor_setNone)



def king_jump_check(char_move_x, char_move_y, char_initial_y_coor, char_end_y_coor, char_initial_x_coor, letters, char_set, square_initial, move_lst, canvas, size):
    #pohyb po diagonále
    if (abs(char_move_x) != abs(char_move_y)):
        return True

    #obsazenost mezi
    if (char_initial_y_coor < char_end_y_coor):
        a = 1
    else:
        a = -1

    c = char_initial_x_coor + a
    cell_to_exterminate = []

    for u in range((char_initial_y_coor+a), char_end_y_coor, a): #projdi všechny pole mezi
        cell = str(letters[c] + str(u))
        

        if ((char_set.get(cell, "not_in_this_dict") == None) or (char_set.get(cell, "not_in_this_dict") == 'None') ):
            c = c + a
            
        else:
            if (char_set.get(cell, "not_in_this_dict") == "not_in_this_dict"): #čtverc není definován
                print('fatal Error!')
                return True

            # => něco tam je
            if (char_set.get(cell)[1] == square_initial[1]): # shodná barva?
                print('dáma přeskakuje vlastní kámen')
                return True

            else:
                cell_to_exterminate.append(cell)
                c = c + a

    if (len(cell_to_exterminate) > 1):
        print('lze přeskočit jen jeden kámen')
        return True
    else:
        cell_to_exterminate = str(cell_to_exterminate[0])
        king_jump(cell_to_exterminate, char_set, move_lst, canvas, char_move_x, char_move_y, size)
