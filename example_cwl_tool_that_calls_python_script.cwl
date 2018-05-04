cwlVersion: v1.0

class: CommandLineTool # (or Workflow, or ExpressionTool)

#baseCommand: example_workflow_python_step
baseCommand: /Users/.../path_to/example_workflow_python_step.py
# ^reference the file directly might be easier than running setup.py
# every time you make a change, for development

inputs:

  first_input_file:
    type: File # (string, int, Directory)
    inputBinding:

  another_input:
    type: File?

outputs:
  some_output:
    type: File?
    outputBinding:
      glob: '*'
#      Or, how to find a specific file:
#      glob: ${ return 'output_dir/example_results.pdf' }
    valueFrom: | # Note the pipe
      ${ return inputs.first_input_file.basename }
#       or try:
#      ${ return inputs.first_input_file.basename.replace('-IGO.*', '') }
#      $( inputs.first_input_file.basename.replace('-IGO.*', '') )
