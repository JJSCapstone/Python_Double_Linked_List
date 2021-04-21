# Python Double Linked List

## The assignment:
In this assignment, students would be tasked with creating a doubly linked list, with the following requirements (note that parameter names are not strict; field and method names are):

#### Class: DoublyLinkedList(object)
     Contains:
        Inner Class: Node(object)
            Contains:
                Field: data                     // data held by the Node
                Field: next                     // next node
                Field: prev                     // previous node
                Method: __init__(self, data, next=None, prev=None)  
                                                // constructor
                Method: __str__(self)           // string representation of Node object
                                                //    requirement: returns string 
                                                //                 representation of data field
                Method: __eq__(self, other)     // checks for equality
                                                //    requirement: compares data field to other
                Method: __ne__(self, other)     //                 checks for inequality
                                                //    requirement: compares data field to other
                Method: update(self, new_data)  // updates data field of this Node
        Field: head                           // leading node
        Field: tail                           // trailing node
        Field: size                           // total count of all nodes
        Method: __init__(self)                // constructor
        Method: __str__(self)                 // string representation of Doubly Linked List
                                              //    requirement: returns string in format
                                              //                 "[a, 2, c]" for a list of
                                              //                 three nodes where 0, 1, 2 have
                                              //                 data values of "a", 2, "c"
        Method: add_head(self, data)          // adds a node containing data to leading end
        Method: add_tail(self, data)          // adds a node containing data to trailing end
        Method: add(self, data)               // adds a node containing data to trailing end
        Method: remove_data(self, data)       // if data is in the list, removes that
                                              //    node and fixes pointers
        Method: remove_position(self, place)  // if the nth node (place) is in this list,
                                              //    removes that node and fixes pointers
                                              //    0-based indexing required.
        Method: query_position(self, place)   // if the nth node (place) is in this list,
                                              //    returns the data in that node
                                              //    0-based indexing required.
        Method: find_data(self, data)         // if the given data is in this list,
                                              //    returns the position in this list.
                                              //    0-based indexing required.
        Method: update_position(self, place, data)
                                              // if the nth node (place) is in this list,
                                              //    updates the data in that node
        Method: len(self)                     // returns thenumber of nodes in this list
                    

## Tests Run:
     test_node_str()
     test_node_equals()
     test_node_update()
     test_dll_add()
     test_dll_add_head()
     test_ddl_add_tail()
     test_dll_string()
     test_remove_data()
     test_remove_position()
     test_query_position()
     test_find_data()
     test_update_position()
     test_len()
  
## Required Command for Autograding:
     pytest [path/to/test]/[test_name].py -k ‘[method_name]’
     e.x.
     pytest ./tests/dll_tests.py -k 'test_node_str'
