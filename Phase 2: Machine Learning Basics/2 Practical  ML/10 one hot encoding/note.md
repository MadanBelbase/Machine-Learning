one hot encoding 
it is use for nominal categorical data
for example: color = red, blue, green
we can represent it as:
red = [1,0,0]
blue = [0,1,0]
green = [0,0,1]
this is called one hot encoding because only one value is hot (1) and the rest are cold (0)

when we have multiple categorical variables we can use one hot encoding for each variable
for example: color = red, blue, green
size = small, medium, large
we can represent it as:
red, small = [1,0,0, 1,0,0]
blue, medium = [0,1,0, 0,1,0]
green, large = [0,0,1, 0,0,1]
this way we can represent multiple categorical variables using one hot encoding

when we are performing one hot encoding we need to be careful about the dummy variable trap
the dummy variable trap occurs when we have multicollinearity in our data
for example: color = red, blue, green
we can represent it as:
red = [1,0,0]
blue = [0,1,0]
green = [0,0,1]
but we can also represent green as:
green = [0,0,1] = 1 - (red + blue)
this means that green is dependent on red and blue
to avoid the dummy variable trap we can drop one of the variables
for example: color = red, blue
we can represent it as:
red = [1,0]
blue = [0,1]
this way we avoid the dummy variable trap
