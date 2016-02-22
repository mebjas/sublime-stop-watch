import sublime, sublime_plugin

# State variable shows, if the stopwatch is started
# Stopped or Paused
# 0 - stopped
# 1 - running
# 2 - paused

class StopwatchStartCommand(sublime_plugin.TextCommand):
	d = 0;
	h = 0;
	m = 0;
	s = 0;

	# State variable shows, if the stopwatch is started
	# Stopped or Paused
	# 0 - stopped
	# 1 - running
	# 2 - paused
	state = 0;

	def run(self, edit):
		if self.state == 0:
			self.Start();
		else:
			self.Stop();

	def Start(self):
		if (self.state == 1): return;
		self.state = 1;	
		sublime.status_message("Stopwatch Started");
		sublime.set_timeout(self.IncrementAndShow, 2000);

	def Stop(self):
		if (self.state == 0): return;

		self.state = 0;	
		sublime.status_message("Stopwatch stopped");
		self.d = self.h = self.m = self.s = 0;

	def IncrementAndShow(self):
		if (self.state != 1): 
			sublime.status_message("Stopwatch stopped");
			return;

		self.s  = self.s + 1;
		if (self.s == 60):
			self.m = self.m + 1;
			self.s = 0;

		if (self.m == 60):
			self.h = self.h + 1;
			self.m = 0;

		if (self.h == 24):
			self.d = self.d + 1;
			self.h = 0;

		sublime.status_message(
			"You have been working for %sd %sh %sm %ss " % (self.d, self.h, self.m, self.s)
		);
		sublime.set_timeout(self.IncrementAndShow, 1000)

	def Pause(self):
		# TODO: implement this
		print ('Pause Command')

	def on_text_command(self, window, name, args):
		print("The text command name is: " + name)
		print("The args are: " + str(args))

	def on_modified(self, view):
		print("The on_modified event fired!")
