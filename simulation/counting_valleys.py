def countingValleys(steps, path):
    # Write your code here
    movement=0
    isMovedDown = False
    valleyCount = 0
    for val in path:
        if val == "U":
            movement+=1
        else:
            movement-=1
        if movement==-1:
            isMovedDown = True
        if isMovedDown and movement==0:
            valleyCount+=1
            isMovedDown = False
    return valleyCount
