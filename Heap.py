class PriorityQNode:
    def __init__(self,value,priority):
        self.value=value
        self.priority=priority



class PriorityQ:
    def __init__(self):
        self.pq=[]

    def getsize(self):

        return len(self.pq)

    def getmin(self):
        return self.pq[0].value

    def isEmpty(self):
        return not(bool(self.getsize()))


    def __upheapify(self):
        childindex=self.getsize()-1

        while(childindex >0):
            parentindex = (childindex - 1) // 2
            if self.pq[childindex].priority<self.pq[parentindex].priority:
                self.pq[childindex],self.pq[parentindex]=self.pq[parentindex],self.pq[childindex]
                childindex=parentindex
            else:
                break




    def insert(self ,value,priority):
        pqNode = PriorityQNode(value,priority)
        self.pq.append(pqNode)
        self.__upheapify()

#imp
    def __downheapify(self):

        parentIndex=0
        leftindex=2*parentIndex+1
        rightindex = 2 * parentIndex +2
        # corner case 1. leftindex<self.getsize()
        while(leftindex<self.getsize()):
            #from 51 line to 56 we are trying to get minmum priority value among parent and their child
            minIndex = parentIndex
            if self.pq[minIndex].priority>self.pq[leftindex].priority:
                minIndex=leftindex
            #corner case 2. rightindex<self.getsize()
            if rightindex<self.getsize() and self.pq[minIndex].priority>self.pq[rightindex].priority:
                minIndex=rightindex
            # corner case 3. minIndex==parentIndex:
            if minIndex==parentIndex:
                break

            self.pq[parentIndex],self.pq[minIndex]=self.pq[minIndex] ,self.pq[parentIndex]

            parentIndex=minIndex
            leftindex = 2 * parentIndex + 1
            rightindex = 2 * parentIndex + 2





    def removemin(self):
        if self.isEmpty():
            print('heap is empty')
            return

        min=self.pq[0]
        self.pq[0]=self.pq[self.getsize()-1]

        self.pq.pop()

        self.__downheapify()


        return min.value

heap=PriorityQ()
heap.insert(200,3)
heap.insert(500,2)
heap.insert(600,1)
heap.insert(223,4)
heap.insert(405,5)
heap.insert(220,7)
for i in range(7):
    print("size",heap.getsize())
    print("is empty",heap.isEmpty())
    print("removed",heap.removemin())


