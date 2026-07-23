def information(**kwargs):                        # **kwargs is used to pass any number of keyword arguments to the function
    print("The details are:")
    for key, value in kwargs.items():              # for loop is used to iterate over the keyword arguments
        print(f"{key}: {value}")                  # key and value are printed

print(information(name="Sydney Sweeney", age=25, city="Los Angeles", country="USA", profession="Actress"))