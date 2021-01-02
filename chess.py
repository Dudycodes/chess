from tkinter import *
from Modules.board import *
from Modules.functions import *

root = Tk()


canvas = Canvas(bg='lightblue', width='500', height='500') 
canvas.pack()             

canvas_width = int(canvas['width'])
canvas_height = int(canvas['height'])
print(canvas_width)
print(canvas_height)


size = 50
margin = 50

chess_board(size,margin, canvas)
board_notation(size, margin, canvas)
char_set = characters(size, margin, canvas)

canvas.update()
canvas.after(10)

#hra
with open("moves.txt", "r") as moves:

    print('Pohyby:')

    index = 0
    Error = False
    last_move_color = 'b'

    for lines in moves:

        if Error == True:
            break
        index += 1
        lines = lines.rstrip('\n')
        print('Tah', index,'. :', lines)

        #rozbor tahu

        letters = "abcdefgh"
        move_lst = lines.partition(' -> ')
        print('move_lst:', move_lst)
        move_lst_2 = ""

        c = 1
        moves = {}
        moves_update = {c: move_lst}
        moves.update(moves_update)


        #test barvy kamene pohybu
        move_color = (char_set.get( move_lst[0])[1])

        if (move_color != last_move_color):
            last_move_color = move_color
        else:
            print('Dva tahy entitou stejné barvy za sebou!')
            break

        #bude určovat počet opakování cyklu - počet tahů v 1 řádku
        while (len(move_lst[2])>2): #test - existuje další tah v řádku
            move_lst_2 = move_lst[2].partition(' -> ')
            move_lst_convert = list(move_lst) #prasárna s alokací paměti? Šlo by to jinak? Tuple je jinak neměnný...
            move_lst_convert[2] = move_lst_2[0]
            move_lst = move_lst_convert
            move_lst = tuple(move_lst)
            print('move_lst_2:', move_lst_2)


            if ( (len(str(move_lst_2[2])) == 2) and (char_set.get(move_lst_2[2], "not_in_this_dict") != 'None') and (char_set.get(move_lst_2[2], "not_in_this_dict") != None)):
                print('Chyba: formát vstupních dat')
                break
            
            moves_update = {c: move_lst}
            moves.update(moves_update)
        
            move_lst = move_lst_2
            c += 1

            moves_update = {c: move_lst}
            moves.update(moves_update)


        print(moves)


        for h in moves:
            move_lst = moves.get(h)
            
            square_initial = (char_set.get( move_lst[0] , "not_in_dict")) 
            square_end = (char_set.get( move_lst[2] , "not_in_dict"))

            char_initial_x_coor = letters.find(str(move_lst[0])[0])
            char_end_x_coor = letters.find(str(move_lst[2])[0])
            char_initial_y_coor = int(str(move_lst[0])[1])
            char_end_y_coor = int(str(move_lst[2])[1])

            char_move_x = (char_end_x_coor - char_initial_x_coor)
            char_move_y = (char_end_y_coor - char_initial_y_coor)


            #test - dvojtah = přeskok
            if (len(moves) > 1):
                if (abs(char_move_x) and abs(char_move_y) != 2):#pokud více tahů -> vzdálenost posunu v tahu == 2 -> ok
                    print(char_move_x)
                    print(char_move_y)
                    if (((square_initial[3] != 'king') and (abs(char_move_x) and abs(char_move_y) != 1)) or ((square_initial[3] == 'king') and (abs(char_move_x) and abs(char_move_y) == 1))):
                        print(square_initial[3])
                        print('Vícenásobný pohyb nesprávné velikosti')
                        Error = True
                        break
                

                #pokud více tahů -> vzdálenost = 2, pokud není dáma

            #test area
            print('rozebraný tah:', move_lst)
            print('char_vals_initial:', square_initial)
            print('char_vals_end:', square_end)
            #



            #hra!

            #kontrola dat:
            if input_line_data_check(char_initial_x_coor, char_end_x_coor, index, square_initial, square_end):
                Error = True
                break
            
            #kontrola pohybu vpřed -
            if forward_move_check(square_initial, char_move_x, char_move_y):
                #kontrola dékly posunu
                if move_len_check(char_move_x, char_move_y): #posun o 1 - v pořádku za již deklarovaných podmínek
                    # == 1 po obou osách
                    declare_king(move_lst, square_initial, char_set, canvas)
                    char_move(char_set, move_lst, canvas, char_move_x, char_move_y, size)
                    print('posun o 1')

                else: #posun o >1
                    if check_if_king(square_initial): #True = posunovaný kámen není dáma
                        if move_is_jump_check(char_move_x, char_move_y): # posun o 2 je přeskok, tedy jediný povolený pohyb větší jedné pro kameny, ne-dámy.
                            if mid_square_occupied: #pole mezi existuje a není prázdné
                                if color_initial_mid_check(char_initial_x_coor, char_end_x_coor, char_initial_y_coor, char_end_y_coor, letters, char_set, square_initial): #přeskakovaný kámen není stejné barvy
                                    jump(char_initial_x_coor, char_end_x_coor, char_initial_y_coor, char_end_y_coor, letters, char_set, move_lst, square_initial, canvas, char_move_x, char_move_y, size)
                                else:
                                    Error = True
                                    break
                            else:
                                Error = True
                                break


                        else:
                            Error = True
                            print('nepovolený pohyb kamenem - moc velký pohyb')
                            break
                    else:
                        if king_jump_check(char_move_x, char_move_y, char_initial_y_coor, char_end_y_coor, char_initial_x_coor, letters, char_set, square_initial, move_lst, canvas, size): #jsem dáma a posouvám se 
                            Error = True
                            break
            else:
                print('Forward_move_check: False')
                if not check_if_king(square_initial): #True = posunovaný kámen není dáma
                    if king_jump_check(char_move_x, char_move_y, char_initial_y_coor, char_end_y_coor, char_initial_x_coor, letters, char_set, square_initial, move_lst, canvas, size):
                        Error = True
                        break

            
            print('char_set_update_last')
            print(char_set)
            print()
            
            canvas.after(500)
            canvas.update()



root.mainloop()