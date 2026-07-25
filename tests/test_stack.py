from src import stack as st
import pytest

class TestStack:

    def test_stack_push(self):
        s1 = st.Stack()
        assert s1.is_empty() == True
        s1.push(1)
        s1.push(2)
        s1.push(3)
        s1.push(1000)
        assert s1.get_stack_size() == 4
        assert s1.get_stack_peek() == 1000
        assert s1.get_all_stack_items() == [1, 2, 3, 1000]

    
    def test_stack_pop(self):
        s2 = st.Stack()
        assert s2.is_empty() == True
        assert s2.pop() == None
        s2.push(10)
        s2.push(20)
        s2.push(30)
        s2.push(40)
        s2.push(50)
    
        assert s2.get_stack_size() == 5
        assert s2.get_stack_peek() == 50
        assert s2.get_all_stack_items() == [10, 20, 30, 40, 50]        
        
        popped_item = s2.pop()
        assert popped_item == 50
        assert s2.get_stack_size() == 4
        assert s2.get_stack_peek() == 40
        assert s2.get_all_stack_items() == [10, 20, 30, 40]

        popped_item = s2.pop()
        assert popped_item == 40
        assert s2.get_stack_size() == 3
        assert s2.get_stack_peek() == 30
        assert s2.get_all_stack_items() == [10, 20, 30]
        

        


