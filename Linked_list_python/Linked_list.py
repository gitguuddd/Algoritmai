class Node:
    def __init__(self,data_val=None):
        self.data_val = data_val
        self.next_val = None

class Linked_list:
    def __init__(self):
        self.head_val = None
    def check_empty(self):
        empt = False
        if self.head_val == None :
            empt = True
            print("Sąrašas yra tuščias")
        return empt
    def l_print(self):
        p_val = self.head_val
        while p_val is not None:
            print(p_val.data_val)
            p_val = p_val.next_val
    def i_head(self,newdata):
        new_node = Node(newdata)
        new_node.next_val = self.head_val
        self.head_val = new_node
    def i_end(self,newdata):
        new_node = Node(newdata)
        if self.head_val is None:
            self.head_val = new_node
            return
        last_e = self.head_val
        while(last_e.next_val):
            last_e = last_e.next_val
        last_e.next_val = new_node
    def i_in_pos(self,pos,new_data):
        if pos == 0:
            self.i_head(new_data)
            return
        temp = self.head_val
        for i in range(pos - 1):
            temp = temp.next_val
            if temp is None:
                break
        if temp is None:
            print("Šio mazgo nėra :(")
            return
        new_node = Node(new_data)
        if temp.next_val is not None:
            new_node.next_val = temp.next_val
        temp.next_val = new_node
    def d_in_pos(self,pos):
        if pos < 0:
            print("pozicija turi būti >=0")
            return
        if self.check_empty()==True:
            return
        temp = self.head_val
        if pos == 0:
            self.head_val = temp.next_val
            temp = None
            return
        for i in range(pos - 1):
            temp = temp.next_val
            if temp is None:
                break
        if temp is None:
            return
        if temp.next_val is None:
            return
        next = temp.next_val.next_val
        temp.next_val = None
        temp.next_val = next
    def find(self,key):
        temp=self.head_val
        node_id=1
        results = []
        while temp is not None:
            if temp.data_val == key:
                results.append(node_id)
            temp=temp.next_val
            node_id = node_id + 1
        if results.__len__() == 0:
            print(key,"reikšmė sąraše nerasta")
            return
        print(key,"reikšmė rasta",results,"mazguose")
    def length(self):
        count = 0
        if self.head_val == None :
            return count
        temp=self.head_val
        count = count + 1
        while temp is not None:
            count = count + 1
            temp=temp.next_val
        return count - 1
    def d_list(self):
        temp = self.head_val
        while temp:
            prev = temp.next_val
            del temp.data_val
            temp = prev


list1=Linked_list()
list1.i_end("P")
list1.i_end("I")
list1.i_end("T")
list1.i_end("O")
list1.i_end("N")
list1.i_end("A")
list1.i_end("S")
list1.i_head("$")
list1.i_in_pos(4,"$")
print("Sąraše yra",list1.length(),"mazgai/ų/as")
list1.l_print()
list1.d_in_pos(4)
list1.i_head("S")
print("Sąraše yra",list1.length(),"mazgai/ų/as")
list1.l_print()
list1.find("S")
if list1.check_empty() == True:
    print("Sąrašas yra tusčias")
else:
    print("Sąrašas nėra tusčias")

list1.d_list()

