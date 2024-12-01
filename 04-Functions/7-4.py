
def lll (tekst):
    litera_e = tekst.count('e')
    print(f"The number of letters e:{litera_e}")
    return litera_e
def main():
    txt= 'You never get a second chance to make a first impression'
    lll(txt)
if __name__ == "__main__":
    main()