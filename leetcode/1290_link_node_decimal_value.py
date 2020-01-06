
class ListNode:

    def __init__(self, value):
        self.val = value
        self.next = None


class Solution:

    def getDecimalValueBestAnswer(self, head: ListNode) -> int:
        re = 0
        tmp = head
        while tmp is not None:
            re = (re << 1) | tmp.val  # 这里res << 1,虽然res是十进制数，但是<<运算符是将该数的二进制全部左移一位，末尾补零。这样整个数就往前挪了一位，也就正好符号链表的存储位置。最后与值进行或运算，用于确定末尾的值 是零还是一
            tmp = tmp.next
        return re



    def getDecimalValue(self, head: ListNode) -> int:
        # 遍历相加
        decimal_values = []
        next_node = head
        while next_node:

            decimal_values.append(next_node.val)
            next_node = next_node.next

        decimal_value, decimal_value_index = 0, 0
        decimal_values_length = len(decimal_values)
        for i in decimal_values:
            decimal_value_index += 1
            decimal_value += i * (2 ** (decimal_values_length - decimal_value_index))
        return decimal_value


class TestCase:

    def test(self):

        values = [1, 1, 0]
        first_node = ListNode(values[0])
        n = first_node
        for v in values[1:]:
            n.next = ListNode(v)
            n = n.next

        print(Solution().getDecimalValue(first_node))

# 链表的遍历和头部插入。
# 插入的形式可以 1.作为头部节点插入 2.作为尾部节点插入 3.在指定位置后插入节点 4.在指定位置前插入节点
# 为了新增节点方便 将头部节点的位置 和 尾部节点的位置记录下来，这样在新增节点的时候，可以直接用记录的位置变量进行对应的操作。
# 链表是动态的存储结构，所以在链表操作的时候，比如说 新增或者删除某个节点，只需要对于其前后的节点进行操作就可以了，比之静态存储(都存在同一块内存)的数据结构
# 其增删的成本会更低。但是但是修改、查询 某个节点的时候，必须遍历到对应的节点（一个个指针指过去），才能找到对应的节点。这部分成本较之静态存储会更高

"""
时间和空间复杂度都很高。
先用列表存储数据，在进行累加。

node 自己提前进行header标记，然后 n.next= next_node, 进行列表组装。



"""

TestCase().test()