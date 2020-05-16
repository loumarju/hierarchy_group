import maya.cmds as cmds

# Create a variable that contains a list of selected objects
object_selected = cmds.ls(sl=True)

# for each object selected...
for each in object_selected:
    # create a variable that it gives me the transformation of selected object.
    # query = True it's like setAttr
    # matrix = True --> ask about the object's transformation

    father = cmds.listRelatives(each, parent=True)

    object = cmds.xform(each, query=True, matrix=True, worldSpace=True)

    # Create a null, with the object's name follow of a sufix and store in a variable
    grp_ori = cmds.group(em=True, name='ori_' + each + '_n_00')

    # Put the same object's matrix in the grp_group
    cmds.xform(grp_ori, matrix=object, worldSpace=True)

    grp_off = cmds.group(em=True, name='off_' + each + '_n_00')
    cmds.xform(grp_off, matrix=object, worldSpace=True)

    grp_lvu = cmds.group(em=True, name='lvu_' + each + '_n_00')
    cmds.xform(grp_lvu, matrix=object, worldSpace=True)

    grp_lvd = cmds.group(em=True, name='lvd_' + each + '_n_00')
    cmds.xform(grp_lvd, matrix=object, worldSpace=True)

    cmds.parent(grp_off, grp_ori)
    cmds.parent(grp_lvu, grp_off)
    cmds.parent(each, grp_lvu)
    cmds.parent(grp_lvd, each)

    if father:
        cmds.parent(grp_ori, father)

