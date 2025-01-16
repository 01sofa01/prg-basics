class Contact():
    def __init__(self,name,email,telephone):
        self.name = name
        self.email = email
        self.telephone = telephone
    def disp(self):
        print(f"{self.name}\t{self.email}\t{self.telephone}")


telebook=list[Contact]



class Contact_List():
    def __init__(self,contacts: telebook):
        self.list = contacts
    def add(self, contact: Contact):
        self.list.append(contact)
    def display(self):
        for i in self.list :
           i.disp()
c = Contact("zb","@","+48")
c.disp()
print()
b = Contact("aw","@","+48")
d = Contact("op","@","+48")
e = Contact("fg","@","+48")
książka=Contact_List([b, d, e])
książka.display()
książka.add(c)
książka.display()
książka.add(Contact("sa","@","+48"))
książka.display()