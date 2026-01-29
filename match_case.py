movie_name = input ("Enter a movie name: ").lower()

if movie_name == "star wars":
    print ("Incredible Movie")
    print ("Check it out!")
elif movie_name == "star trek":
    print ("Great Movie")
elif movie_name == "maze runner":
    print ("Cool!")
else:
    print ("Unknown Movie")
    
#Match Case version

match movie_name:
    case "star wars":
        print ("Incredible Movie")
        print ("Check it out!")
    case "star trek":
        print ("Great Movie")
    case "maze runner":
        print("Cool!")
    case _:
        print("Unknown Movie")
