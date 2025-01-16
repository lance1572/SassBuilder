import sublime
import sublime_plugin
import subprocess
import os

class SassBuilderCommand(sublime_plugin.WindowCommand):
    def run(self):
        # Get settings from file.
        settings = sublime.load_settings("SassBuilder.sublime-settings")
        dart_executable = settings.get("dart_sass_path")
        input_dir = settings.get("input", {}).get("dir")
        output_dir = settings.get("output", {}).get("dir")

        project_path = self.window.folders()[0]
        sass_input = os.path.join(project_path, input_dir)
        css_output = os.path.join(project_path, output_dir)

        compile_command = [dart_executable, sass_input + ":" + css_output]

        try:
            output = subprocess.check_output(
                compile_command,
                universal_newlines=False,
                stderr=subprocess.STDOUT,
                shell=False
            )
            # Weird encdoding thing. Let decode.
            decoded_output = output.decode("utf-8")
            sublime.status_message("Sass compiled successfully!")
        except subprocess.CalledProcessError as e:
            # Check for encoding
            error_output = e.output.decode("utf-8")
            sublime.error_message("Sass Builder: " + str(e.output))
        except Exception as e:
            sublime.error_message("Sass Builder: " + error_output)
            sublime.error_message("Sass Builder: " + str(e))
