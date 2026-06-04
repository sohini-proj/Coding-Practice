# NESTING in Dictionaries
'''
# d is a dict with key-dict pairs and the sub-dictionaries have key-list pairs
d={
    "India":{
        "Delhi":["Red Fort","India Gate"],
        "Mumbai":["Marine Drive","Gateway of India"]
    },
    "China":{
        "Beijing":["Forbidden Palace","Tiannmen Square"],
        "Chongqing":["Train station"]
    }    
}
print(d.keys())
print(d["India"])
print(d["China"])
print(d["India"]["Delhi"])
print(d["India"]["Delhi"][1])
'''

# functions with return type

fn=input("Enter First Name: ")
ln=input("Enter Last Name: ")
def fullname(fn,ln):
    fn=fn.title()
    ln=ln.title()
    return f" {fn} {ln}"
print(fullname())
