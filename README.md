# Area-Of-Overlapping-Rectangles-


This function allows the calculation of the sum of the area of overlapping rectangles.

The function requires 8 variables, where 4 of them are the horizontal and vertical coordinates of one of the rectangles, and the other 4 of them are the horizontal and vertical coordinates of the other rectangle. 

1) We have to define the function using 'def', followed by the function name, in this case 'solution' is used. The names of the variables are then placed in parenthesis as follows:

        def solution(S, T, U, V, W, X, Y, Z):
        
 2) We then move on to define the other variables that we need, in this case I chose to make them as lists to contain all the coordinates of the breadth and length of each squares. 
 
        breadth_A = []
        length_A = []
        breadth_B = []
        length_B = []
    where breadth_A, length_A and breadth_B, length_B are the lists of coordinates of the length and breadth of squares A and     B respectively. 

3) The list created above are empty, so we need to fill them up with the coordinates of the breadth and length of each rectangle. 

Rectangle A:
(S,V) - top left coordinate of rectangle A. (U,V) - top right coordinate of rectangle A. (S,T) - bottom left coordinates of rectangle A. (U,T) - bottom right coordinate of rectangle A.

Rectangle B:
(W,Z - top left coordinate of rectangle B. (Y,Z) - top right coordinate of rectangle B. (W,X) - bottom left coordinates of rectangle B. (Y,X) - bottom right coordinate of rectangle B.

With these defined, we can now fill those lists that represents the length and breadth of the squares as follows:
      
      #rectangle A
     for i in range (T, (V + 1) ):
        breadth_A.append(i)
        
    sbreadth_A = set()
    for item in breadth_A:
        sbreadth_A.add(item)
    
    
    for j in range (S, (U + 1)):
        length_A.append (j)
        
    slength_A = set()
    for item in length_A:
        slength_A.add(item)
        
    #rectangle B
    breadth_B = []
    length_B = []
    
    for i in range (X, (Z + 1) ):
        breadth_B.append(i)
        
    sbreadth_B = set()
    for item in breadth_B:
        sbreadth_B.add(item)
    
    
    for j in range (W, (Y + 1)):
        length_B.append (j)
        
    slength_B = set()
    for item in length_B:
        slength_B.add(item)

What is being done from the above set of statements is that for loops will run through the numbers in-between and including the end points of each squares and append them to the lists created. Sets such as slength and sbreadth are created from the lists so that it would be easier for the intersection to be found later on. 

4) Next, we have to find the intersection between 2 squares: 

        over_len = slength_A.intersection (slength_B)

        over_breadth = sbreadth_A.intersection (sbreadth_B)


        lover_len = list(over_len)
        lover_breadth = list(over_breadth)

        l = lover_len[len(lover_len) - 1] - lover_len[0]

        b = lover_breadth[len(lover_breadth) - 1] - lover_breadth[0]

Here, we make use of the properties of sets with the sets created and use the '.intersection' tool to find out if the 2 squares share common coordinates, i.e, overlapping one another. Once the intersections have been found, we assign it to 'over_len' and 'over_breadth'.

We then proceeed to make the lists version of the over_len and the over_breadth so that we can find the actual length and breadth and the intersection. Once the list versions are created, we can now find the actual length and breadth of the overlap by taking the difference between the element of the last position and and the element at the first position of the horizontal and vertical coordinates.

5) We can finally find the area of rectangle A, rectangle B and the area of the overlap as follows, and sum up the area of the overlapping rectangles and the function returns the sum.
            
            
            Area_A = (V - T) * (U - S)
            Area_B = (Y -W) * (Z-X)
            Area_O = (l * b)

            summ = Area_A + Area_B - Area_O

            print ("A" ,Area_A) 
            print ("B" , Area_B) 
            print ("O" , Area_O)


            return (summ)
                
                
                




 


