import viz
import vizfx
import vizconnect

vizconnect.go('vizconnect_config.py')

env = vizfx.addChild('basketball_vr.osgb')

basketball = env.getChild('basketball')
shoe = env.getChild('shoe')
grabbable_objects = [basketball, shoe]

grabber = vizconnect.getRawTool('grabber')
grabber.setItems(grabbable_objects)