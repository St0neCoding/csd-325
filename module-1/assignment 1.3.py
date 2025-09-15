# Stone Nettles, 9/14/25, Assignment 1.3
# This program plays the "100 bottles of beer" song starting with a number from the user.
def bottle_subtract(bottles):
    if bottles > 1:
        print(f"\n{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        bottles = bottles - 1
        print(f"Take one down, pass it around, {bottles} bottles of beer on the wall.")
        bottle_subtract(bottles)
    else:
        print("\n1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take one down, pass it around, 0 bottles of beer on the wall.")


def main():
    bottles = int(input("How many bottles of beer on the wall?: "))
    if bottles <= 0:  # ensures there's a valid starting number
            print("There's no beer!")
    else:
            bottle_subtract(bottles)
            print("\nTime to buy more beer.")

main()