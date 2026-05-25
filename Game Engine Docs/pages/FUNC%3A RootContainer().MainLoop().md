- The function that contains the whole mainloop.
-
- NOTE: This should NOT be used by the user. To start mainloop, use [[FUNC: RootContainer().StartMainLoop()]]
-
- **The game loop is in the order:**
  1. Perform actions (e.g. [[FUNC: Component().Start()]], [[FUNC: Component().Stop()]], [[FUNC: Component().Update()]], [[FUNC: Component().Tick()]], [[FUNC: Component().Awake()]] ) on all components.
- 2. After sending each action type to all children, perform the same action on RootContainer