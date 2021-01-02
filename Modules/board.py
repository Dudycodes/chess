def chess_board(size, margin, canvas):
    for r in range(0,8,2): #liché řady
        for s in range(0,8,2): #černá pole
            canvas.create_rectangle(margin + s*size, # x levý-vrchní vrchol
                                     margin + r*size, # y levý-vrchní vrchol
                                      margin + (s+1)*size, # x pravý-dolní vrchol
                                       margin + (r+1)*size, # y levý-dolní vrchol
                                        fill='black', outline='')

        for s in range(1,8,2): #bílá pole
            canvas.create_rectangle(margin + s*size,
                                     margin + r*size,
                                      margin + (s+1)*size,
                                       margin + (r+1)*size,
                                        fill='white', outline='')

    for r in range(1,8,2): #sudé řady
        for s in range(0,8,2): #bílá pole
            canvas.create_rectangle(margin + s*size, # x levý-vrchní vrchol
                                     margin + r*size, # y levý-vrchní vrchol
                                      margin + (s+1)*size, # x pravý-dolní vrchol
                                       margin + (r+1)*size, # y levý-dolní vrchol
                                        fill='white', outline='')
        for s in range(1,8,2): #černá pole
            canvas.create_rectangle(margin + s*size,
                                     margin + r*size,
                                      margin + (s+1)*size,
                                       margin + (r+1)*size,
                                        fill='black', outline='')

# popisky
def board_notation(size, margin, canvas):
    letters = "abcdefgh"
    for position in range(8):
        canvas.create_text(margin + position*size + size // 2, margin // 2, 
                           text=letters[position], 
                           font='Arial 20', 
                           fill='black')
        canvas.update()
        canvas.after(50)

    num = "12345678"
    for position in range(8):
        canvas.create_text(margin // 2, margin + position*size + size // 2, 
                           text=num[position], 
                           font='Arial 20', 
                           fill='black')
        canvas.update()
        canvas.after(50)

def characters(size, margin, canvas):
    result = {}
    for r in range(1,9): #množina 64 prvků, každý = None
        for s in "abcdefgh":
            result[s+str(r)] = None
    letters = "abcdefgh"


    # bile figurky
    radius_padding = size // 8 
    for r in range(0, 3, 2):#řádky
        for s in range(0, 8, 2): #sloupce
            square = letters[s] + str(r+1)
            result[square] = (square, 
                                'w', #popiska bílých
                                canvas.create_oval(margin + s*size + radius_padding,
                                                    margin  + r*size + radius_padding, 
                                                    margin + (s+1) *size - radius_padding, 
                                                    margin + (r+1) *size - radius_padding, 
                                                    fill='white', outline=''
                                                    ),
                                'stone'
                                )


    for r in range(1, 3, 2):
        for s in range(1, 8, 2):
            square = letters[s] + str(r+1)
            result[square] =  (square, 
                                'w',
                                canvas.create_oval(margin  + s*size + radius_padding, 
                                                    margin  + r*size + radius_padding,
                                                    margin + (s+1) *size - radius_padding, 
                                                    margin + (r+1) *size - radius_padding, 
                                                    fill='white', outline=''
                                                    ),
                                'stone'
                                )

    # cerne figurky
    radius_padding = size // 8
    for r in range(6, 8, 2):
        for s in range(-1, 7, 2):
            square = letters[s+1] + str(r+1)
            result[square] = (square, 
                            'b',
                            canvas.create_oval(margin + (s+1)*size + radius_padding, 
                                                margin  + r*size + radius_padding,
                                                margin + (s+2) *size - radius_padding, 
                                                margin + (r+1) *size - radius_padding, 
                                                fill='black', outline='white'
                                                ),
                            'stone'
                            )

    for r in range(5, 8, 2):
        for s in range(0, 8, 2):
            square = letters[s+1] + str(r+1)
            result[square] = (square, 
                            'b',
                            canvas.create_oval(margin + (s+1)*size + radius_padding, 
                                                margin  + r*size + radius_padding,
                                                margin + (s+2) *size - radius_padding, 
                                                margin + (r+1) *size - radius_padding, 
                                                fill='black', outline='white'
                                                ),
                            'stone'
                            )


    print(result)
    return result
