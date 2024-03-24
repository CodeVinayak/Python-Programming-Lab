print("Name : Vinayak Kumar Singh \nRegister No : 23MCA1030")
state_capitals={"Andhra Pradesh":"Amaravati","Bihar":"Patna","Chhattisgarh":"Raipur","Maharashtra"
:"Mumbai","Tamil Nadu":"Chennai"}

print("\n1.Printing Dictionary of State and Capitals")
print(state_capitals)

print("\n2.Using keys to Accessing a Value in a Dictionary")
print(state_capitals ["Bihar"])

print("\n3.Using get method to Accessing a Value in a Dictionary")
print (state_capitals.get("Tamil Nadu"))

print("\n4.Modifying the values:")
state_capitals["Andhra Pradesh"] = "Visakhapatnam"
print("Updated capital of Andhra Pradesh:", state_capitals["Andhra Pradesh"])

print("\n5.Using update method in a Dictionary")
emptydictionary = {}
dictionarywithdata = {"India": "New Delhi", "England": "London"}
emptydictionary.update(dictionarywithdata)
print (emptydictionary)

print("\n6.Using copy in a Dictionary")
original_data = {'Python':95, 'Java':82,'DSA':75,'DBMS':78}
copied_data = original_data.copy()
print('original data:', original_data)
print('copied data', copied_data)

print("\n7.Using fromkeys in a Dictionary")
keys = {'Liberty City','Vice City','San Andreas','Grand Theft Auto V'}
value = 'RockstarGames'
RockstarGames = dict.fromkeys(keys, value)
print(RockstarGames)

print("\n9.Using items in a Dictionary")
Birthdate = { 'A':'10','B':'August','C':2002}
print(Birthdate.items())

print("\n10.Using keys and values Functions in Dictionary Methods:")
print("States are key:", state_capitals.keys())
print("Capitals are value:", state_capitals.values())

print("\n11.Using Pop method in a Dictionary")
dict2= {"India": "New Delhi", "England": "London"}
print('All vaue in dic2 is:',dict2)
element = dict2.pop('India')
print('Popping value of India:', element)

print("\n12.Clearing the dictionary:")
state_capitals.clear()
print("Cleared dictionary:", state_capitals)

print("\n13. Using setdefault() in a Dictionary:")
my_dict = {'State': 'Karnataka', 'City': 'Bangalore'}
print("Value for 'State':", my_dict.setdefault('State', None))
print("Value for 'Country':", my_dict.setdefault('Country', None))