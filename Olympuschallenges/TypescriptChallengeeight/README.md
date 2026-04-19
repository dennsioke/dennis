Repository
https://github.com/inikulin/parse5
Commit: e402276597de95b3ce5372a62559d19ff2c7b052

Title
Tree traversal, cloning, and structural comparison utilities

Add tree walking, node cloning, and structural equality to parse5, working generically through the TreeAdapter interface rather than against the default adapter's concrete types. The new module lives at packages/parse5/lib/tree-utils/index.ts and exports walk, cloneNode, isEqualNode, findNode, findAllNodes, and a WalkerAction enum with SKIP and STOP members. These should also be re-exported from the main parse5 entry point.

walk(root, adapter, visitor) performs a depth-first traversal. The visitor object has optional enter(node) and leave(node) callbacks. enter is called pre-order and may return WalkerAction.SKIP to bypass the current node's descendants while still invoking leave for that node, or WalkerAction.STOP to halt traversal immediately with no further enter or leave calls. leave is called post-order after all children have been visited. Template elements are a special case -- their children live in a content document fragment, not in childNodes, and the walker needs to follow that indirection.

findNode(root, adapter, predicate) returns the first node matching predicate using the walker, or null. findAllNodes(root, adapter, predicate) collects all matching nodes including inside template content.

cloneNode(node, adapter, deep) produces a fully detached copy. When deep is true the entire subtree is recursively cloned; when false only the node itself is copied with no children. A deep clone of a template must independently clone the content fragment rather than sharing it with the original.

isEqualNode(nodeA, nodeB, adapter) returns true when both subtrees are structurally identical -- same node types, tag names, namespaces, text content, and attributes. Attribute order shouldn't matter, and source code locations should be ignored. Template content fragments must be compared recursively.
