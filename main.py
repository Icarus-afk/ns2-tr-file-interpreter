from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.core.window import Window
from kivy.uix.checkbox import CheckBox
import subprocess

class NS2TRAnalyzer(App):
    def build(self):
        Window.clearcolor = (0.3, 0.3, 0.3, 1)  # Set window background color to gray
        Window.minimum_width = 800  # Set minimum window width
        Window.minimum_height = 800  # Set minimum window height
        layout = BoxLayout(orientation='vertical', spacing=30, padding=30)

        # Create a label for the app title
        # title_label = Label(text='NS2 TR File Analyzer', font_size=24, color=(1, 1, 1, 1),
        #                     font_name='roboto.ttf')
        # layout.add_widget(title_label)

        # Create a file chooser
        self.file_chooser = FileChooserListView(size_hint=(1, 2.0))  # Increase the height of the file chooser
        layout.add_widget(self.file_chooser)

        # Create checkboxes for script selection
        script_selection_layout = BoxLayout(orientation='horizontal', spacing=10)
        self.script_selection = []
        script1_checkbox = CheckBox(active=False)
        script1_checkbox.text = 'e2edelay.awk'
        script1_checkbox.bind(active=self.update_script_selection)
        script1_label = Label(text='End to End Delay', color=(1, 1, 1, 1))
        script_selection_layout.add_widget(script1_checkbox)
        script_selection_layout.add_widget(script1_label)
        
        script2_checkbox = CheckBox(active=False)
        script2_checkbox.text = 'pdr.awk'
        script2_checkbox.bind(active=self.update_script_selection)
        script2_label = Label(text='packet delivery ratio', color=(1, 1, 1, 1))
        script_selection_layout.add_widget(script2_checkbox)
        script_selection_layout.add_widget(script2_label)    
            
        script3_checkbox = CheckBox(active=False)
        script3_checkbox.text = 'tp.awk'
        script3_checkbox.bind(active=self.update_script_selection)
        script3_label = Label(text='Average Throughput', color=(1, 1, 1, 1))
        script_selection_layout.add_widget(script3_checkbox)
        script_selection_layout.add_widget(script3_label)
        
        layout.add_widget(script_selection_layout)


        # Create a label to display the output
        self.output_label = Label(text='Output will be displayed here', color=(1, 1, 1, 1))
        layout.add_widget(self.output_label)

        # Create a button to run the AWK scripts
        button_layout = BoxLayout(size_hint=(1, None), height=40, spacing=10)
        button_layout.add_widget(Label())  # Add an empty widget for spacing
        button_layout.add_widget(Button(text='Analyze', size_hint=(None, None),
                                        size=(120, 40),
                                        background_color=(0.2, 0.7, 0.3, 1),
                                        color=(1, 1, 1, 1),
                                        on_press=self.run_scripts))
        button_layout.add_widget(Label())  # Add an empty widget for spacing
        layout.add_widget(button_layout)
        
        return layout

    def update_script_selection(self, instance, value):
        checkbox_value = value
        checkbox_label = instance.text
        if checkbox_value and checkbox_label not in self.script_selection:
            self.script_selection.append(checkbox_label)
        elif not checkbox_value and checkbox_label in self.script_selection:
            self.script_selection.remove(checkbox_label)

    def run_scripts(self, instance):
        selected_file = self.file_chooser.selection and self.file_chooser.selection[0]
        if selected_file and self.script_selection:
            try:
                output = ''
                for script in self.script_selection:
                    # Run each selected script with the selected file and capture the output
                    script_output = subprocess.check_output(['awk', '-f', script, selected_file]).decode('utf-8')
                    output += f'{script} Output:\n{script_output}\n'
                self.output_label.text = output
            except subprocess.CalledProcessError as e:
                error_message = f'Error occurred while running the script:\n{e.output.decode("utf-8")}'
                self.output_label.text = error_message
        else:
            self.output_label.text = 'Please select a TR file and at least one script.'

if __name__ == '__main__':
    NS2TRAnalyzer().run()
