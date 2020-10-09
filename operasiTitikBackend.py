import numpy as np

#INPUT : 3 DIMENSI RGB, OUTPUT : 3 DIMENSI GRAYSCALE
def rgb2Gray(img, height, width, color):
    temp = [[[0 for i in range(color)] for j in range(width)] for k in range(height)]
    for i in range(height):
        for j in range(width):
            temp[i][j][0] = np.uint8((img[i, j, 0] / 3) + (img[i, j, 1] / 3) + (img[i, j, 2] / 3))
            temp[i][j][1] = temp[i][j][0]
            temp[i][j][2] = temp[i][j][0]
            print('PIXEL ROW ',i,'COL ',j,' | RED:',img[i, j, 0],'GREEN:',img[i, j, 1],'BLUE:',img[i, j, 2])
    return np.array(temp)

#INPUT : 3 DIMENSI RGB, OUTPUT : 2 DIMENSI GRAYSCALE
def rgb2Gray2d(img, height, width, color):
    temp = [[0 for j in range(width)] for k in range(height)]
    for i in range(height):
        for j in range(width):
            temp[i][j] = np.uint8((img[i, j, 0] / 3) + (img[i, j, 1] / 3) + (img[i, j, 2] / 3))
    return np.array(temp)

#INPUT : 3 DIMENSI RGB, OUTPUT : 3 DIMENSI BINER
def gray2Bin(img, height, width, color, value):
    temp = [[[0 for i in range(color)] for j in range(width)] for k in range(height)]
    for i in range(height):
        for j in range(width):
            if((img[i, j, 0])>=value):
                temp[i][j][0] = np.uint8(255)
                temp[i][j][1] = temp[i][j][0]
                temp[i][j][2] = temp[i][j][0]
            else:
                temp[i][j][0] = np.uint8(0)
                temp[i][j][1] = temp[i][j][0]
                temp[i][j][2] = temp[i][j][0]
    return np.array(temp)

#INPUT : 3 DIMENSI RGB, OUTPUT : 2 DIMENSI BINER
def gray2Bin2d(img, height, width, color, value):
    temp = [[0 for j in range(width)] for k in range(height)]
    for i in range(height):
        for j in range(width):
            if((img[i, j, 0])>=value):
                temp[i][j] = np.uint8(255)
            else:
                temp[i][j] = np.uint8(0)
    return np.array(temp)

#INPUT : 3 DIMENSI RGB, OUTPUT : 3 DIMENSI RGB
def brighten(img, height, width, color, value):
    temp = [[[0 for i in range(color)] for j in range(width)] for k in range(height)]
    for i in range(height):
        for j in range(width):
            for k in range(color):
                if (255 - img[i, j, k] <= value):
                    temp[i][j][k] = np.uint8(255)
                else:
                    temp[i][j][k] = img[i, j, k] + np.uint8(value)
    print('temp',temp)
    return np.array(temp)

#INPUT : 3 DIMENSI RGB, OUTPUT : 3 DIMENSI RGB
def negative(img, height, width, color):
    temp = [[[0 for i in range(color)] for j in range(width)] for k in range(height)]
    for i in range(height):
        for j in range(width):
            for k in range(color):
                temp[i][j][k] = np.uint8(255) - img[i, j, k]
    return np.array(temp)

#INPUT : 3 DIMENSI RGB, OUTPUT : 3 DIMENSI RGB
def contrast(img, height, width, color, minA, maxA):
    if color is 3:
        temp = [[[0 for i in range(color)] for j in range(width)] for k in range(height)]
    else:
        temp = [[0 for i in range(width)] for j in range(height)]
    if(minA>maxA):
        return None
    for i in range(height):
        for j in range(width):
            if color is 3:
                for k in range(color):
                    constrech = ((img[i, j, k] - np.uint8(minA)) / np.uint8(maxA - minA)) * (255)
                    if (constrech < 0):
                        constrech = 0
                    temp[i][j][k] = np.uint8(constrech)
            else:
                constrech = ((img[i, j] - np.uint8(minA)) / np.uint8(maxA - minA)) * (255)
                if (constrech[0] < 0):
                    constrech = 0
                temp[i][j] = np.uint8(constrech)
    return np.array(temp)

def getMinPixel(img,height,width,color):
    if color is 3:
        minR = img[..., 2].min()
        minG = img[..., 1].min()
        minB = img[..., 0].min()
        minA = [minR,minG,minB]
        minA = min(minA)
        minA = [minA,minA,minA]
        return minA
    else:
        minA = img[..., 0].min()
        minA = [minA]
        return minA

def getMaxPixel(img,height,width,color):
    if color is 3:
        maxR = img[..., 2].max()
        maxG = img[..., 1].max()
        maxB = img[..., 0].max()
        maxA = [maxR,maxG,maxB]
        maxA = max(maxA)
        maxA = [maxA,maxA,maxA]
        return maxA
    else:
        maxA = img[..., 0].max()
        maxA = [maxA]
        return maxA

def conStrech(img,height,width,color):
    if color is 3:
        temp = [[[0 for i in range(color)] for j in range(width)]for k in range(height)]
    else:
        temp = [[0 for i in range(width)] for j in range(height)]
    minA = getMinPixel(img,height,width,color)
    maxA = getMaxPixel(img,height,width,color)
    print(min,max)
    for i in range(height):
        for j in range(width):
            if color is 3:
                for k in range(color):
                    constrech = ((img[i,j,k]-np.uint8(minA[k]))/np.uint8(maxA[k]-minA[k]))*(255)
                    if(constrech<0):
                        constrech = 0
                    temp[i][j][k] = np.uint8(constrech)
            else:
                constrech = ((img[i,j]-np.uint8(minA[0]))/np.uint8(maxA[0]-minA[0]))*(255)
                if(constrech[0]<0):
                    constrech = 0
                temp[i][j] = np.uint8(constrech)
    result = np.array(temp)
#     plt.imshow(result,cmap='gray')
    return result