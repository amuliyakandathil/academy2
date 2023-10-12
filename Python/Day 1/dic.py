thisdict = {
    "Book": "A set of printed pages bound together, containing written or printed material.",

     "Dog": "A domesticated mammal commonly kept as a pet, known for its loyalty and companionship.",

     "Sun": "The star at the center of our solar system that provides light and heat to Earth.",

     "Run": "To move rapidly on foot, covering a distance by moving quickly with both legs.",

     "Food": "Any substance consumed to provide nutritional support for the body; sustenance.",

     "Jump": "To propel oneself into the air by using one's leg muscles and then descend back to the ground.",

     "Water": "A transparent, odorless, tasteless liquid essential for the survival of all living organisms.",

     "Tree": "A large plant with a woody trunk, branches, and leaves, typically providing shade and oxygen.",

     "Blue": "A color that is the hue of the clear sky or the deep sea, often associated with calmness.",

     "Happy": "Feeling or showing joy, contentment, or satisfaction."
    }
print(thisdict)
x = input("Enter the string to be searched: ")
if x in thisdict.keys():
    print("The meaning is: " + thisdict[x])
else:
    print("Sory!!! word is not present....")
    s = input("Pls Enert ur suggestion: ")
    thisdict[x] = s
    


