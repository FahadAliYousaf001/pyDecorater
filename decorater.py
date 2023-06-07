def h(str):
    def inner(str):
        print("******")
        p(str)
        print("******")
	
    inner()

def p(name):
    nam = name
    print(f"///////// \n hello!! {name}")
    print("/////////")



name = "ammar"

h(name)