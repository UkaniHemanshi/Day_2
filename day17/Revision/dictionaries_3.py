dict = {'arham':'blue','lisa':'yellow','vinod':'purple','jenny':'Pink'}

def manuplation(dict):
    print(f"Find total number of count:",len(dict.keys()))

    print(f"Chnage lisa's favourite colour: ")
    dict['lisa'] = "Red"
    print(dict)

    dict.pop('jenny')
    print(f"Remove 'jenny' and her color :",dict)

    sorted_dict = sorted(dict.keys())
    print(f"sorted dictionary:",sorted_dict)


manuplation(dict)