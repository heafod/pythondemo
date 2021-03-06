# 笔记

## 树
树是 n(n>=0) 个节点的有限集。 当n=0时，称为空树。在任意一个非空树中，有如下特点:
1. 有且仅有一个特定的称为根的节点
2. 当 n>1 时，其余节点可分为 m(m>0) 个互不相交的有限集，每一个集合本身又时一个树，并称为根的子树。
- 根节点： root
- 叶子节点：leaf。 树的末端，没有"孩子"
- 子树：
- 父节点： parent
- 孩子节点： child
- 兄弟节点： sibling


### 二叉树：binary tree
这种树的每个节点最多有2个孩子节点。

满二叉树
一个二叉树的所有非叶子节点都存在左孩子和右孩子，并且所有叶子节点都在同一个层级上。

完全二叉树
对一个有 n个节点的二叉树，按层级顺序编号，则所有节点的编号为从1到n，如果这个树所有节点和 同样深度的满二叉树的编号为从
1到n 的节点位置相同。

存储结构
- 链式存储结构
- 数组

二叉查找树 = 二叉排序树


### 二叉树的遍历

从位置：
- 前序遍历
- 中序遍历
- 后序遍历
- 层序遍历

更宏观：
- 深度优先遍历（前序遍历、中序遍历、后序遍历）
- 广度优先遍历（层序遍历）

前序遍历：输出顺序是根节点、左子树、右子树
中序遍历：输出顺序是左子树、根节点、右子树
后序遍历：输出顺序是左子树、右子树、根节点


