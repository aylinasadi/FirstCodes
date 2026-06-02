print("This program will determine your place in the universe.")

weight = float(input("Enter your weight in pounds: "))
weight_kg = weight * 2.2

contain_atoms = (weight_kg / 70) * 7e27
comprise = (contain_atoms / 10e80) * 100

print(f"You contain approximately {contain_atoms: .2e} atoms")
print(f"Therefore, you comprise {comprise: .2e} % of the universe")