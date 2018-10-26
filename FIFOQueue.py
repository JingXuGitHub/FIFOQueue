# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 15:16:14 2018

@author: Jing
"""

import DoubleLinkedList as DLL

class FIFOQue(object):
    
    def __init__(self):
        self.FIFO = DLL.DoubleLinkedList()
        
    def Enqueue(self, newCar):
        self.FIFO.AppendToTail(newCar)
        
    def Dequeue(self):
        return self.FIFO.RemoveFromHead()
        
    def Print(self):
        self.FIFO.PrintCars()