import numpy as np
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
val=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
def ceasor_conversion(text,key):
    new_text=""
    steps=[]
    for char in text:
        if(char in alphabet):
            pos=alphabet.index(char)
            new_pos = (pos + key) %26
            new_text += alphabet[new_pos]
            steps.append(f"{char} → {alphabet[new_pos]}")
        else:
            new_text += char
            steps.append(f"{char} → {char}")
    return new_text,steps

def railfence_encrypt(text,key):
    text = text.replace(" ","")
    fence=[['*' for i in range(len(text))]
           for j in range(key)]
    row, step=0, 1
    for i in range(len(text)):
        fence[row][i] = text[i]
        
        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1
        
        row += step
        
    new_text = ""
    for i in range(key):
        for j in range(len(text)):
            if(fence[i][j] != '*'):
                new_text += fence[i][j]
    matrix_output=[]

    for i in range(key):
        row=""
        for j in range(len(text)):
            row+=fence[i][j]+"\t\t\t\t\t\t\t\t\t\t"
        matrix_output.append(row)
    return new_text,matrix_output

def railfence_decrypt(text,key):
    fence = [['#' for i in range(len(text))]
             for j in range(key)]
    row, step=0,1
    for i in range(len(text)):
        fence[row][i] = '*'
        if row==0:
            step=1
        elif row == key-1:
            step=-1
        row += step
    ind=0
    for i in range(key):
        for j in range(len(text)):
            if fence[i][j]=='*' and ind<len(text):
                fence[i][j]=text[ind]
                ind += 1
    row, step=0,1
    new_text=""
    for i in range(len(text)):
        new_text += fence[row][i]
        if row==0:
            step=1
        elif row==key-1:
            step=-1
        row += step
    matrix_output=[]

    for i in range(key):
        row=""
        for j in range(len(text)):
            row+=fence[i][j]+"\t\t\t\t\t\t\t\t\t\t"
        matrix_output.append(row)
    return new_text,matrix_output

def vigenere_conversion(text,key,type):
    #making key and text length equal
    if(len(text)!=len(key)):
        for i in range(len(key),len(text)):
            key += key[i%len(key)]
    newtext=""
    i=0
    steps=[]
    j=0
    if(type=='e'):# for encryption
        for char in text:
            new_pos=((alphabet.index(text[i]))+(alphabet.index(key[i])))%26
            newtext += alphabet[new_pos]
            i += 1
            #method of algorithm
            row=""
            row += ("\t\t(\t\t" + text[j] + "\t+\t" + key[j] + "\t\t)\t\t" + "\t%26\t" + "\t\t=\t\t" + alphabet[new_pos])
            steps.append(row)
            j += 1
    else:
        for char in text:# for decryption
            new_pos=((alphabet.index(text[i]))-(alphabet.index(key[i])))%26
            newtext += alphabet[new_pos]
            i += 1
            #method
            row=""
            row += ("\t\t(\t\t" + text[j] + "\t-\t" + key[j] + "\t\t)\t\t" + "\t%26\t" + "\t\t=\t\t" + alphabet[new_pos])
            steps.append(row)
            j += 1
    
    return newtext, steps

def playfair_conversion(text,key,type):
    #Removing Duplicates
    final_key=""
    for i in key:    
        if i not in final_key:
            if(i=='j'):
                continue
            else:
                final_key += i
    #Creating Matrix 
    matrix= [i for i in final_key]
    for i in alphabet:
        if i=='j':
            continue
        elif i not in matrix:
            matrix.append(i)
    matrix=np.array(matrix).reshape(5,5)
    text = text.replace(" ","")
    text= text.replace("j","i")
    #organizing text in pair form
    text_pairs=[]
    i=0
    while i < len(text)-1:
        if(text[i]==text[i+1]):#condition 1(same letter)
            text_pairs.append(text[i]+'x')
            i += 1
        else:#condition 2
            text_pairs.append(text[i]+text[i+1])
            i += 2
    if(len(text_pairs)*2<len(text)):#condition 3(odd no. of letters)
        text_pairs.append(text[-1]+'x')
    
    matrix_output=[]
    for i in range(5):
        row=""
        for j in range(5):
            row+=matrix[i][j]+"\t\t\t\t\t\t\t\t\t\t"
        matrix_output.append(row)

    newtext=""
    for pair in text_pairs:
        p_h=False
        for row in range(0,5):# for same row 
            if type=='e':
                curr_row=matrix[row,:]
                if pair[0] in curr_row and pair[1] in curr_row:
                    first_ind=list(curr_row).index(pair[0])
                    second_ind=list(curr_row).index(pair[1])
                    newtext += matrix[row , (first_ind +1)%5]
                    newtext += matrix[row , (second_ind +1)%5]
                    p_h=True
                    break
            else:
                curr_row=matrix[row,:]
                if pair[0] in curr_row and pair[1] in curr_row:
                    first_ind=list(curr_row).index(pair[0])
                    second_ind=list(curr_row).index(pair[1])
                    newtext += matrix[row , (first_ind -1)%5]
                    newtext += matrix[row , (second_ind -1)%5]
                    p_h=True
                    break
        if p_h:
            continue

        for col in range(0,5):# for same column
            if type=='e':
                curr_col=matrix[:,col]
                if pair[0] in curr_col and pair[1] in curr_col:
                    first_ind=list(curr_col).index(pair[0])
                    second_ind=list(curr_col).index(pair[1])
                    newtext += matrix[(first_ind +1)%5 , col]
                    newtext += matrix[(second_ind +1)%5 , col]
                    p_h=True
                    break
            else:
                curr_col=matrix[:,col]
                if pair[0] in curr_col and pair[1] in curr_col:
                    first_ind=list(curr_col).index(pair[0])
                    second_ind=list(curr_col).index(pair[1])
                    newtext += matrix[(first_ind -1)%5 , col]
                    newtext += matrix[(second_ind -1)%5 , col]
                    p_h=True
                    break
        if p_h:
            continue    
        #for different row & column
        first_coord=np.where(matrix == pair[0])
        second_coord=np.where(matrix == pair[1])
        newtext += matrix[first_coord[0][0],second_coord[1][0]]
        newtext += matrix[second_coord[0][0],first_coord[1][0]]
    return newtext,matrix_output

def chr_to_num(c):
    return ord(c) - ord('A')

def num_to_chr(n):
    return chr(n % 26 + ord('A'))

def make_key_matrix(key):
    matrix=[[chr_to_num(key[0]),chr_to_num(key[1])],
            [chr_to_num(key[2]),chr_to_num(key[3])]]
    return np.array(matrix)

def hill_encrypt(text,key):
    text=text.upper().replace(" ","")
    if(len(text)%2 != 0):
        text += 'X'
    key_matrix= make_key_matrix(key)
    new_text=""
    for i in range(0,len(text),2):
        pair= np.array([[chr_to_num(text[i])],
                       [chr_to_num(text[i+1])]])
        res = np.dot(key_matrix,pair)%26
        new_text += num_to_chr(res[0][0])
        new_text += num_to_chr(res[1][0])
    return new_text

def hill_decrypt(text,key):
    key_matrix = make_key_matrix(key)
    det = int(np.linalg.det(key_matrix))
    det_inv = pow(det % 26, -1, 26)
    adj = np.array([[key_matrix[1][1], -key_matrix[0][1]],
                    [-key_matrix[1][0], key_matrix[0][0]]])
    inv_matrix = (det_inv * adj) % 26
    text = ""
    for i in range(0, len(text), 2):
        pair = np.array([[chr_to_num(text[i])],
                         [chr_to_num(text[i+1])]])
        result = np.dot(inv_matrix, pair) % 26
        new_text += num_to_chr(result[0][0])
        new_text += num_to_chr(result[1][0])
    return new_text