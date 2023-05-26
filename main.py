from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
import subprocess

class NS2TRAnalyzer(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
                # Create a file chooser
        self.file_chooser = FileChooserListView()
        layout.add_widget(self.file_chooser)

        
        # Create a label to display the output
        self.output_label = Label(text='Output will be displayed here')
        layout.add_widget(self.output_label)
        
        # Create a button to run the AWK scripts
        button = Button(text='Run AWK Scripts', on_press=self.run_scripts)
        layout.add_widget(button)
        
        return layout
    
    def run_scripts(self, instance):
        # Replace 'script1.awk', 'script2.awk', 'script3.awk' with the actual paths to your AWK scripts
        selected_file = self.file_chooser.selection and self.file_chooser.selection[0]
        if selected_file:     
            # script1 = 'e2edelay.awk'
            script2 = 'tp.awk'
            script3 = 'pdr.awk'

            try:
                # Run the AWK scripts with the selected file and capture the output
                # output1 = subprocess.check_output(['awk', '-f', script1, selected_file]).decode('utf-8')
                output2 = subprocess.check_output(['awk', '-f', script2, selected_file]).decode('utf-8')
                output3 = subprocess.check_output(['awk', '-f', script3, selected_file]).decode('utf-8')

                # Update the label with the output
                output_text = f'\n\nScript 2 Output:\n{output2}\n\nScript 3 Output:\n{output3}'
                self.output_label.text = output_text
            except subprocess.CalledProcessError as e:
                error_message = f'Error occurred while running AWK scripts:\n{e.output.decode("utf-8")}'
                self.output_label.text = error_message
        else:
            self.output_label.text = 'Please select a TR file.'

if __name__ == '__main__':
    NS2TRAnalyzer().run()
