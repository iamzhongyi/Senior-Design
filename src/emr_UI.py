import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class EMRWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="Electronic Medical Record")
#		self.set_default_size(400,200)
		grid = Gtk.Grid()
		self.add(grid)
		name = Gtk.Label()
		name.set_markup("<big><b>Jane Doe</b></big>")
		age = Gtk.Label()
		age.set_text("27 years old")
		gender = Gtk.Label()
		gender.set_text("Female")
		box = Gtk.Box(spacing=10)
		box.pack_start(name, False, False, 10)
		box.pack_start(age, False, False, 10)
		box.pack_start(gender, False, False, 10)
		grid.attach(box,0,0,4,1)
		color = Gdk.color_parse("gray")
		rgba = Gdk.RGBA.from_color(color)
        
        # Medications
		meds_store = Gtk.ListStore(str)
		meds_store.append(["Advil"])
		meds_store.append(["Antibiotics"])
		meds_store.append(["Benedryl"])
		meds = Gtk.TreeView(meds_store)
		meds_renderer = Gtk.CellRendererText()
		meds_renderer.set_property("editable", True)
		meds_renderer.connect("edited", self.text_edited,meds_store)
		column = Gtk.TreeViewColumn("Medications", meds_renderer, text=0)
		meds.append_column(column)
		select = meds.get_selection()
		select.connect("changed", self.on_tree_selection_changed)
		grid.attach(meds, 0, 1, 1, 3)

		# Allergies
		allergies_store = Gtk.ListStore(str)
		allergies_store.append(["Penicillin"])
		allergies = Gtk.TreeView(allergies_store)
		allergy_renderer = Gtk.CellRendererText()
		allergy_renderer.set_property("editable", True)
		allergy_renderer.connect("edited", self.text_edited, allergies_store)
		column = Gtk.TreeViewColumn("Allergies", allergy_renderer, text=0)
		allergies.append_column(column)
		select = allergies.get_selection()
		select.connect("changed", self.on_tree_selection_changed)
		grid.attach(allergies, 1, 1, 1, 3)
#		allergies.override_background_color(Gtk.StateFlags.NORMAL,rgba);
        
        # Family History
		familyHistory_store = Gtk.ListStore(str)
		familyHistory_store.append(["Father - heart condition"])
		familyHistory_store.append(["Mother - diabetes"])
		familyHistory = Gtk.TreeView(familyHistory_store)
		fh_renderer = Gtk.CellRendererText()
		fh_renderer.set_property("editable", True)
		fh_renderer.connect("edited", self.text_edited, familyHistory_store)
		column = Gtk.TreeViewColumn("Family History", fh_renderer, text=0)
		familyHistory.append_column(column)
		select = familyHistory.get_selection()
		select.connect("changed", self.on_tree_selection_changed)
		grid.attach(familyHistory, 2, 1, 1, 3)
		
		# Medical History
		medicalHistory_store = Gtk.ListStore(str)
		medicalHistory_store.append(["List Medical History Here"])
		medicalHistory_store.append(["Past Medical Conditions"])
		medicalHistory = Gtk.TreeView(medicalHistory_store)
		mh_renderer = Gtk.CellRendererText()
		mh_renderer.set_property("editable", True)
		mh_renderer.connect("edited", self.text_edited,medicalHistory_store)
		column = Gtk.TreeViewColumn("Medical History", mh_renderer, text=0)
		medicalHistory.append_column(column)
		select = medicalHistory.get_selection()
		select.connect("changed", self.on_tree_selection_changed)
		grid.attach(medicalHistory,3,1,1,3)
		
		# History of Present Illness (HPI)
		hpiLabel = Gtk.Label()
		hpiLabel.set_text("History of Present Illness (HPI)")
		hpiView = Gtk.TextView()
		hpiView.set_wrap_mode(Gtk.WrapMode.WORD)
		hpiBuffer = hpiView.get_buffer()
		hpiBuffer.set_text("History of present illness goes here. "
		+ "History of present illness goes here. History of present illness goes here. "
		+ "History of present illness goes here.")
		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		vbox.pack_start(hpiLabel,True,True,0)
		vbox.pack_start(hpiView,True,True,0)
		grid.attach(vbox,0,5,2,4)
		
		# Review of Systems (ROS)
		rosLabel = Gtk.Label()
		rosLabel.set_text("Reviw of Systems (ROS)")
		rosView = Gtk.TextView()
		rosView.set_wrap_mode(Gtk.WrapMode.WORD)
		rosBuffer = rosView.get_buffer()
		rosBuffer.set_text("Review of Systems goes here. "
		+ "Review of Systems goes here. Review of Systems goes here. "
		+ "Review of Systems goes here. Review of Systems goes here.")
		rosBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		rosBox.pack_start(rosLabel,False,False,0)
		rosBox.pack_start(rosView,False,False,0)
		grid.attach(rosBox,2,5,2,4)
		
		# Physical Exam
		peLabel = Gtk.Label()
		peLabel.set_text("Physical Exam")
		peView = Gtk.TextView()
		peView.set_wrap_mode(Gtk.WrapMode.WORD)
		peBuffer = peView.get_buffer()
		peBuffer.set_text("Physical Exam results go here. "
		+ "Physical Exam results go here. Physical Exam results go here. "
		+ "Physical Exam results go here. Physical Exam results go here.")
		peBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		peBox.pack_start(peLabel,False,False,0)
		peBox.pack_start(peView,False,False,0)
		grid.attach(peBox,0,9,2,4)
		
		# Assessment
		aLabel = Gtk.Label()
		aLabel.set_text("Assessment")
		aView = Gtk.TextView()
		aView.set_wrap_mode(Gtk.WrapMode.WORD)
		aBuffer = aView.get_buffer()
		aBuffer.set_text("Assessment goes here. "
		+ "Assessment goes here. Assessment goes here. "
		+ "Assessment goes here. Assessment goes here.")
		aBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		aBox.pack_start(aLabel,False,False,0)
		aBox.pack_start(aView,False,False,0)
		grid.attach(aBox,2,9,2,4)
		
		# Plan
		planLabel = Gtk.Label()
		planLabel.set_text("Plan")
		planView = Gtk.TextView()
		planView.set_wrap_mode(Gtk.WrapMode.WORD)
		planBuffer = planView.get_buffer()
		planBuffer.set_text("Plan information goes here. "
		+ "Plan information goes here. Plan information goes here. "
		+ "Plan information goes here. Plan information goes here.")
		planBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		planBox.pack_start(planLabel,False,False,0)
		planBox.pack_start(planView,False,False,0)
		grid.attach(planBox,0,13,2,4)
		
		# Patient Instructions
		piLabel = Gtk.Label()
		piLabel.set_text("Patient Instructions")
		piView = Gtk.TextView()
		piView.set_wrap_mode(Gtk.WrapMode.WORD)
		piBuffer = piView.get_buffer()
		piBuffer.set_text("Patient instructions go here. "
		+ "Patient instructions go here. Patient instructions go here. "
		+ "Patient instructions go here. Patient instructions go here.")
		piBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		piBox.pack_start(piLabel,False,False,0)
		piBox.pack_start(piView,False,False,0)
		grid.attach(piBox,2,13,2,4)
		
	def text_edited(self, widget, path, text, liststore):
		liststore[path][0] = text
		
	def on_tree_selection_changed(self,selection):
		model, treeiter = selection.get_selected()
		if treeiter is not None:
			print("You selected", model[treeiter][0]) 
       
win = EMRWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
