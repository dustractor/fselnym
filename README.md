# fselnym
[Blender Addon] I was determined to make it so you didn't need to use the mouse during a file save-as dialog.

When you choose file -> 'save' or 'save as' ( or press control+S), the text field where you enter the name is not selected by default.  This bothered me.  For a long time.

Although I was not able to find a way to directly control the system caret in blender or to find a way to make an UI element bring the focus of the caret onto itself, I found, thanks to a comment somewhere out there, (thanks BVL) that if an operator is given a 'bl_property' attribute set to the name of a property, then that property becomes the one that is selected when the operator is displayed, so it is a two-step operation, the hotkey calls an operator set up so a string property is automatically focused, then when that operator executes via the user pressing enter or return, it sets the value of the property we weren't able to directly focus on.

Control-L because that is what browsers use but in this case the mnemonic is L for "Let's have a filename"