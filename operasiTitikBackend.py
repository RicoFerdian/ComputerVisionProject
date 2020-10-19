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

def getR(img,height,width,color):
    temp = [[[0 for i in range(color)] for j in range(width)]for k in range(height)]
    for i in range(height):
        for j in range(width):
            for k in range(color):
                if k is 0:
                    temp[i][j][k] = img[i,j,2]
                else:
                    temp[i][j][k]= np.uint8(0)
    result = np.array(temp)
#     print(result)
#     plt.imshow(result)
    return result

def getG(img,height,width,color):
    temp = [[[0 for i in range(color)] for j in range(width)]for k in range(height)]
    for i in range(height):
        for j in range(width):
            for k in range(color):
                if k is 1:
                    temp[i][j][k] = img[i,j,1]
                else:
                    temp[i][j][k]= np.uint8(0)
    result = np.array(temp)
#     plt.imshow(result)
    return result

def getB(img,height,width,color):
    temp = [[[0 for i in range(color)] for j in range(width)]for k in range(height)]
    for i in range(height):
        for j in range(width):
            for k in range(color):
                if k is 2:
                    temp[i][j][k] = img[i,j,0]
                else:
                    temp[i][j][k]= np.uint8(0)
    result = np.array(temp)
#     plt.imshow(result)
    return result

def histo(x):
    hist, bins = np.histogram(x, bins=256)
    return hist, bins

def histogramEqualization(img, height, width, color):
    if color is 3:
        histogram = [[np.uint8(0) for i in range(256)] for j in range(color)]
        r = getR(img, height, width, color)
        g = getG(img, height, width, color)
        b = getB(img, height, width, color)
        histR, binR = histo(r)
        histG, binG = histo(g)
        histB, binB = histo(b)
        hist = [histR, histG, histB]
        bins = [binR, binG, binB]

        minBin = [int(round(min(binR))), int(round(min(binG))), int(round(min(binB)))]
        maxBin = [int(round(max(binR))), int(round(max(binG))), int(round(max(binB)))]
        for i in range(color):
            for j in range(minBin[i], maxBin[i]):
                histogram[i][j] = hist[i][j - minBin[i]]
        return equalizeRGB(height, width, color, histogram)
    else:
        histogram = [np.uint8(0) for i in range(256)]
        hist, bins = histo(img)
        minBin = round(min(bins))
        maxBin = round(max(bins))
        minBin = int(minBin)
        maxBin = int(maxBin)
        for j in range(minBin, maxBin):
            histogram[j] = hist[j - minBin]
        return equalizeGray(height, width, color, histogram)

def equalizeRGB(height,width,color,hist):
    n = [[0 for i in range(256)]for j in range(color)]
    g = 256
    for i in range(color):
        headers = ['g','h(g)','c(g)','n(g)']
#         t = PrettyTable(headers)
        c = 0
        for j in range(g):
            h = hist[i][j]
            c = c + h
            n[i][j] = max(0,round(255*(c/(height*width*3)))-1)
            # row = [j,h,c,n[i][j]]
#             t.add_row(row)
#         print(t)
    return n

def equalizeGray(height,width,color,hist):
    n = [0 for i in range(256)]
    g = 256
    headers = ['g','h(g)','c(g)','n(g)']
    # t = PrettyTable(headers)
    c = 0
    for i in range(g):
        h = hist[i]
        c = c + h
        n[i] = max(0,round(255*(c/(height*width*3)))-1)
        # row = [i,h,c,n[i]]
        # t.add_row(row)
    # print(t)
    return n

#Histogram Equalization, Input : rgb/binary image. Output : rgb/binary image
def equalizeResult(img, height, width, color, n):
    if color is 3:
        temp = [[[0 for i in range(color)] for j in range(width)] for k in range(height)]
    else:
        temp = [[0 for i in range(width)] for j in range(height)]

    for i in range(height):
        for j in range(width):
            if color is 3:
                for k in range(color):
                    temp[i][j][k] = np.uint8(n[k][img[i][j][k]])
            else:
                temp[i][j] = np.uint8(n[img[i][j][0]])
    result = np.array(temp)
    return result