print("class in pythond")

class studend:
    name = "emmanuel"
    last = "saleem"
    study = "bs/cs"

    def fullName(self):
        return f"name {self.name} last name {self.last}"

emmanuel = studend()
print(emmanuel.name,emmanuel.fullName(),end="\n")

moon = studend()
moon.name =  "moon"
print(moon.name,moon.fullName(),end="\n")