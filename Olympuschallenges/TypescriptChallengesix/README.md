Repository
https://github.com/TianyiDataScience/openclaw-control-center
Commit: 5d1e3245d9540b676aca7069c3f900bb36d8d44f

Title
Hall task card dependency graph with cascading state resolution

Task cards in the collaboration hall need dependency tracking. A card should be able to declare that it depends on other cards, and the system should prevent cycles, self-references, and references to cards that don't exist -- all as validation errors with a 400 status. Adding a dependency that already exists should be a no-op, and cycle detection should only consider active (non-archived) cards.
When a card gets blocked, that state should cascade transitively downstream through its dependents, tagging each with a "blocked-by:<rootCardId>" blocker string. Cards that are already completed or archived should be left alone, and the same blocker tag shouldn't be added twice. When a blocked card's dependencies all complete, it should revert to discussion and shed its blocked-by entries.
There should also be a way to get a topological ordering of active cards (excluding archived and completed), breaking ties by creation time then card ID, and a way to find all cards transitively downstream of a given card.
A new module at src/runtime/hall-task-dependency should export:
  addHallTaskDependency({ taskCardId, dependsOnTaskCardId }) -> { path, taskCard }
  removeHallTaskDependency({ taskCardId, dependsOnTaskCardId }) -> { path, taskCard }
    Both return the updated dependent card (the one identified by taskCardId).
  cascadeBlockedState(rootCardId) -> string[]
  cascadeUnblockState(resolvedCardId) -> string[]
    Both return the taskCardIds of cards whose state was actually changed.
  topologicalOrder(store: CollaborationTaskCardStoreSnapshot) -> string[]
  impactAnalysis(store: CollaborationTaskCardStoreSnapshot, taskCardId) -> Set<string>
Task cards gain a dependsOn: string[] field. Validation errors use CollaborationHallStoreValidationError with status 400.
