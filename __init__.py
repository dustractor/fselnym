bl_info = {
    "name":"fselnym",
    "blender":(2,80,0),
    "description":"ctrl+L or f6 during save-as dialog for popup. .blend will be appended. yes you have to hit enter three times, but still, no mouse.",
    "category":"System"
}
import bpy
class FSELNYM_OT_fselnym(bpy.types.Operator):
    bl_idname = "fselnym.fselnym"
    bl_label = "fselnym"
    bl_property = "s"
    s: bpy.props.StringProperty()
    def execute(self,context):
        t = self.s
        if not t.endswith(".blend"):
            t += ".blend"
        context.space_data.params.filename = t
        return {"FINISHED"}
    def invoke(self,context,event):
        return context.window_manager.invoke_props_dialog(self)

addon_keymap_data = []

def register():
    addon_keymap_data.clear()
    bpy.utils.register_class(FSELNYM_OT_fselnym)
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name="File Browser", space_type="FILE_BROWSER")
    kmi = km.keymap_items.new("fselnym.fselnym",type="L",value="PRESS",ctrl=True)
    addon_keymap_data.append((km,kmi))
    kmi = km.keymap_items.new("fselnym.fselnym",type="F6",value="PRESS")
    addon_keymap_data.append((km,kmi))
    


def unregister():
    for km,kmi in addon_keymap_data:
        km.keymap_items.remove(kmi)
    addon_keymap_data.clear()
    bpy.utils.unregister_class(FSELNYM_OT_fselnym)
