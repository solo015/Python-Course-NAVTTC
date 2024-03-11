# class start
class saif:
    
    my_list=[1,2,3]
    print(my_list[1])

    # 6. code
    my_list=[1,2,3]
    my_list.insert(1,10)
    # my_list.pop()
    my_list.append(15)
    # loop start
    def lmethod(value )->int:
        value.append(35)
        new_value=[2*i for i in value]
        new_value.sort()
        return new_value
    def lmethod2(value2,my_list):
        value2=[i for i in my_list if i%2==0]
        return value2
    max_value=max(lmethod2(lmethod(my_list),my_list))
    print(max_value)
    # loop end

# class end

# class start
class dictionary_class:
    # initial dictionary
    new_dictionary={"name":"Saifullah","age":21}
    duplicate_dictionary={"name":"Saifullah","age":21,"department":"Computer Science","city":"Pano Aqil"}
    print("Initial Dictionary")
    print(new_dictionary)
    # method start
    def new_dic(values):
        values["department"]="Computer Science"
        values["city"]="Pano Aqil"
        return values
    # method end
    dictionary_value=new_dic(new_dictionary)
    # method start
    def change_values(new_values):
        new_values["age"]=20
        return new_values
    # method end
    # insert into the Dictionary
    print("\ninsert into the Dictionary")
    print(dictionary_value)
    # update values into the Dictionary
    print("\nupdate values into the Dictionary")
    dictionary_value2=change_values(dictionary_value)
    
    print(dictionary_value2)

    # method start
    def del_dictionary(del_dic):
        del del_dic["department"]
        return del_dic
    # method end

    # Deleting values from the dictionary
    dictionary_value3=del_dictionary(dictionary_value2)
    print("\n Delecting values from the dictionay")
    print(dictionary_value3)

    # find if key exist in dictionary
    # method start
    def find_key(dictionary_value3):
        value="city" in dictionary_value3
        return value
    # method end
    dictionary_value4=find_key(dictionary_value3)
    print("\nFind the key exist in the dictionary")
    print(dictionary_value4)
    # Get number of key-value pairs
    # method start
    def length_method(value):
        value2=len(value)
        return value2
    # method end
    dictionary_value5=length_method(dictionary_value)
    print("\nGet number of key-value pair ")
    print(dictionary_value5)
    # Get list of All Keys
    # method start
    def list_dictionary(value):
        keys_list=list(value.keys())
        return keys_list
    # method end
    dictionary_value6=list_dictionary(dictionary_value)
    print("\nGet list of All keys")
    print(dictionary_value6)
    # Get list of All values
    # method start
    def list_dictionary_values(value):
        keys_list=list(value.values())
        return keys_list
    # method end
    dictionary_value7=list_dictionary_values(dictionary_value)
    print("\nGet list of All values")
    print(dictionary_value7)
    # Get list of All key values pairs
    # method start
    def list_dictionary_values_pairs(value):
        keys_list=list(value.items())
        return keys_list
    # method end
    dictionary_value8=list_dictionary_values_pairs(dictionary_value)
    print("\nGet list of All key values pairs")
    print(dictionary_value8)
    # Clear of All values pairs
    # method start
    def list_dictionary_value_pairs_clear(value):
        keys_list=value.clear()
        return keys_list
    # method end
    dictionary_value9=list_dictionary_value_pairs_clear(dictionary_value2)
    print("\nClear of All values pairs")
    print(dictionary_value9)
    # Get Value of Specific Key
    # method start
    def get_value_of_specific_key(value):
        keys_list=value.get("name")
        return keys_list
    # method end
    dictionary_value10=get_value_of_specific_key(duplicate_dictionary)
    print("\nGet value of Specific Key")
    print(dictionary_value10)
    # Return and remove values for a key
    # method start
    def remove_value_of_specific_key(value):
        keys_list=value.pop("age")
        return keys_list
    # method end
    dictionary_value11=remove_value_of_specific_key(duplicate_dictionary)
    print("\nReturn and remove values for a key")
    print(dictionary_value11)
    # Merge Dictionaries
    def merge_dictionaries():
        dic1={"name":"Saifullah","age":21}
        dic2={"city":"Pano Aqil","department":"Computer Science"}
        merge_dic={**dic1,**dic2}
        return merge_dic
    print(merge_dictionaries())
# class end